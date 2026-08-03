#!/usr/bin/env python3
"""Translate ActiveInferenceJournal caption SRTs into target languages via local Ollama.

Reproducible, idempotent, resumable offline translator for the journal's
``captions/*.srt`` (English source) into the target-language set, writing
``translations/<translation-title>.<lang>.srt`` beside each item so the
generated journal schema (docs/JOURNAL_SCHEMA.md) is satisfied.

Design (matches the repo's established translation conventions):
  - Provider is a single function (Ollama by default; swap for a hosted
    OpenAI-compatible endpoint in one spot). No API key needed offline.
  - Each caption cue's text is translated while its index and timing are
    preserved verbatim, so the translated SRT stays frame-accurate.
  - Idempotent / resumable: an existing ``<lang>.srt`` for an item is
    skipped unless ``--force``. Progress checkpoints every N items.
  - Deterministic ordering and stable filenames for reproducible runs.

Usage:
  python scripts/translate_subtitles.py --journal ../ActiveInferenceJournal
  python scripts/translate_subtitles.py --journal ../ActiveInferenceJournal --series GuestStream
  python scripts/translate_subtitles.py --journal ../ActiveInferenceJournal --lang es
  python scripts/translate_subtitles.py --journal ../ActiveInferenceJournal --limit 10
  # --force to re-translate existing languages; --model / --lang to override.

Environment:
  OLLAMA_URL   (default http://localhost:11434)
  OLLAMA_MODEL (default selected per-language: qwen2.5:3b for CJK else gemma3:4b)
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit

# ── Target languages (ISO-639 codes, matching the ActiveInferenceJournal
# ── convention). zh-Hans / zh-Hant use the qwen2.5 CJK model; the rest gemma3.
TARGET_LANGS = [
    "es",
    "fr",
    "de",
    "pt",
    "it",
    "nl",
    "ru",
    "ja",
    "ko",
    "zh-Hans",
    "zh-Hant",
]
LANGUAGE_NAMES = {
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "pt": "Portuguese",
    "it": "Italian",
    "nl": "Dutch",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-Hans": "Simplified Chinese",
    "zh-Hant": "Traditional Chinese",
}
CJK = {"ja", "ko", "zh-Hans", "zh-Hant"}

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
DEFAULT_MODEL = os.environ.get("OLLAMA_MODEL", "")
MODEL = {"default": "gemma3:4b", "cjk": "qwen2.5:3b"}

# Proper nouns / brand terms that must survive translation verbatim.
KEEP_VERBATIM = [
    "Active Inference Institute",
    "Active Inference",
    "pymdp",
    "Youtube",
    "YouTube",
    "Discord",
    "GitHub",
    "ActiveInferenceInstitute",
    "ActiveInference",
]

CUES_SRT_SPLIT_RE = re.compile(r"\n{2,}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--journal",
        type=Path,
        default=Path(__file__).resolve().parent.parent.parent / "ActiveInferenceJournal",
    )
    ap.add_argument(
        "--series",
        default="",
        help="limit to one series dir under data/video/activeinferenceinstitute/",
    )
    ap.add_argument(
        "--lang",
        action="append",
        default=[],
        help="one or more target language codes (repeatable); default all",
    )
    ap.add_argument(
        "--limit", type=int, default=0, help="max number of caption files to translate (0 = all)"
    )
    ap.add_argument(
        "--force", action="store_true", help="re-translate languages that already exist"
    )
    ap.add_argument(
        "--skip-to",
        type=int,
        default=0,
        help="resume at the Nth caption file (1-based), for restart",
    )
    return ap.parse_args(argv)


def ollama_translate(text: str, lang: str, model: str) -> str:
    """Translate a single caption text line via a local model. Returns cleaned text."""
    languages_name = LANGUAGE_NAMES[lang]
    keep = ", ".join(f'"{k}"' for k in KEEP_VERBATIM)
    system = (
        "You are a translation engine. The user message contains one short English "
        f"subtitle line wrapped in «guillemets». Translate ONLY that text into {languages_name}.\n"
        "Output just the translation on a single line. Do NOT answer, explain, expand, "
        "summarize, or continue the text; do NOT add markdown, bold, quotes, guillemets, or commentary.\n"
        "Keep these terms exactly as written (do not translate): " + keep + ".\n"
        "Keep placeholder tokens like {n}, {title}, {count} unchanged.\n"
        "Match the length and register of the source — a short subtitle stays short."
    )
    body = json.dumps(
        {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": f"«{text}»"},
            ],
            "stream": False,
            "options": {"temperature": 0, "top_p": 0.9, "num_predict": 512},
        }
    ).encode("utf-8")
    # Use http.client (stdlib) so this script has zero external deps and works in
    # a bare venv — no requests/httpx needed.
    parsed = urlsplit(OLLAMA_URL if "://" in OLLAMA_URL else f"http://{OLLAMA_URL}")
    host = parsed.hostname or "localhost"
    port = parsed.port or 11434
    # Retry transient failures (Ollama queuing under concurrent load / timeouts)
    # so a single slow response doesn't silently fall back to English source text.
    attempts = int(os.environ.get("OLLAMA_RETRIES", "4"))
    timeout = int(os.environ.get("OLLAMA_TIMEOUT", "180"))
    last_exc: Exception | None = None
    result = ""
    for attempt in range(attempts):
        conn = http.client.HTTPConnection(host, port, timeout=timeout)
        try:
            conn.request(
                "POST", "/api/chat", body=body, headers={"Content-Type": "application/json"}
            )
            resp = conn.getresponse()
            if resp.status != 200:
                raise RuntimeError(f"Ollama HTTP {resp.status}: {resp.read().decode()[:200]}")
            data = json.loads(resp.read().decode("utf-8"))
            raw = data.get("message", {}).get("content", "")
            candidate = clean_translation(raw, languages_name)
            # Detect an English echo (degraded response under load): if the model
            # returned the source line (or nearly all of it) unchanged, treat it as
            # a failed translation and retry rather than silently writing English.
            if candidate and _is_english_echo(candidate, text):
                last_exc = RuntimeError("Ollama returned English echo (degraded response)")
                if attempt < attempts - 1:
                    time.sleep(1.5 * (attempt + 1))
                continue
            result = candidate
            break
        except Exception as exc:  # noqa: BLE001 — retry then fall back in caller
            last_exc = exc
            if attempt < attempts - 1:
                time.sleep(1.5 * (attempt + 1))
        finally:
            conn.close()
    if not result and last_exc is not None:
        raise last_exc
    return result


def _is_english_echo(candidate: str, source: str) -> bool:
    """True if a translation candidate looks like an untranslated English echo.

    Under heavy Ollama load, requests can return the source line unchanged with an
    HTTP 200 status. Detect this so the caller retries instead of writing English.
    """
    def _words(s: str) -> set[str]:
        return set(re.findall(r"[A-Za-z']+", s.lower()))
    cw = _words(candidate)
    sw = _words(source)
    if not cw or not sw:
        return False
    # Long runs of words already entirely English strongly imply an untranslated echo.
    shared = len(cw & sw) / len(sw)
    if shared >= 0.7 and len(sw) >= 3:
        return True
    # Exact (post-clean) equality is an obvious echo even for short lines.
    return candidate.strip().lower() == source.strip().lower()


def clean_translation(raw: str, language_name: str) -> str:
    text = str(raw or "")
    brk = text.find("\n")
    if brk != -1:
        text = text[:brk]
    for marker in ("English:", f"{language_name}:", "Translation:"):
        if text.startswith(marker):
            text = text[len(marker) :]
    edge_chars = "\\s«»‹›「」『』“”‘’\\\"'*_`#"
    edge_re = re.compile(f"^[{edge_chars}]+|[{edge_chars}]+$", re.UNICODE)
    return edge_re.sub("", text).strip()


def model_for(lang: str, override: str) -> str:
    if override:
        return override
    return MODEL["cjk"] if lang in CJK else MODEL["default"]


def translate_srt(srt_text: str, lang: str, model: str) -> str:
    """Translate the text lines of an SRT, preserving indices and timing."""
    # Normalise to \n line endings first; SRT files may use \r\n.
    norm = srt_text.replace("\r\n", "\n").replace("\r", "\n")
    # SRT blocks are separated by a blank line. Rebuild each block.
    blocks = re.split(r"\n\s*\n", norm.strip())
    out_blocks = []
    for block in blocks:
        lines = [ln for ln in block.split("\n")]
        if not lines:
            continue
        cue_text = "\n".join(
            ln.strip()
            for ln in lines
            if ln.strip() and "-->" not in ln and not ln.strip().isdigit()
        )
        if not cue_text.strip():
            out_blocks.append(block)
            continue
        try:
            translated = ollama_translate(cue_text, lang, model)
        except Exception:  # noqa: BLE001 — fall back to source text per-cue
            translated = cue_text
        # Rebuild the block: index line, timing line(s), then the translated text.
        index_lines = [ln for ln in lines if ln.strip().isdigit()]
        timing_lines = [ln for ln in lines if "-->" in ln]
        rebuilt = index_lines + timing_lines
        if translated:
            rebuilt.append(translated)
        out_blocks.append("\n".join(rebuilt))
    result = "\n\n".join(out_blocks) + "\n"
    # Restore CRLF line endings to match the repo's existing translation files.
    return result.replace("\n", "\r\n")


def translation_filename(source_srt: Path, lang: str) -> str:
    """Reconstruct a translation filename from the source caption filename.

    Journal caption files carry a noisy per-video suffix token (``.en``,
    ``.en(ca)``, ``.en(ie)``, ``.m4a``, ``.caption40D`` …) that must be stripped so
    the translation filename is the clean English title plus ``.<lang>.srt``,
    matching the repo's dominant ``translations/<title>.<lang>.srt`` convention.
    """
    name = source_srt.name
    if name.endswith(".srt"):
        name = name[: -len(".srt")]
    name = re.sub(r"\.(en(\([a-z]{2}\))?|m4a|caption40?d?)\s*$", "", name, flags=re.IGNORECASE)
    return f"{name}.{lang}.srt"


def iter_caption_files(journal: Path, series: str) -> list[Path]:
    base = journal / "data" / "video" / "activeinferenceinstitute"
    if series:
        base = base / series
    return sorted(base.rglob("captions/*.srt"))


def build_placeholder_hashes(journal: Path, use_cache: bool = True) -> dict[str, int]:
    """Map content-md5 -> count of distinct item dirs holding that exact caption.

    A caption file whose exact bytes appear under several different item folders
    is a copied placeholder (the ActiveInferenceJournal has a known case: the
    "ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1)" transcript
    is duplicated across 63 items in ~10 series). Translating it would attribute
    Textbook Group content to unrelated videos, so the driver skips those files
    and reports them instead.

    The scan walks the whole journal and is md5-dominated, so results are cached
    to a sidecar keyed on the journal's caption-directory mtime signature. Agents
    call this on every run; the cache makes repeat invocations fast.
    """
    import hashlib
    import tempfile
    from collections import defaultdict

    cache_dir = Path(tempfile.gettempdir()) / "transl_subtitles_cache"
    cache_path = cache_dir / (
        hashlib.sha1(str(journal.resolve()).encode("utf-8")).hexdigest() + ".json"
    )
    if use_cache and cache_path.exists():
        try:
            cached = json.loads(cache_path.read_text(encoding="utf-8"))
            counts = cached.get("counts", {})
            if isinstance(counts, dict) and cached.get("signature") == _caption_signature(journal):
                return counts
        except Exception:  # noqa: BLE001 — rebuild on any cache error
            pass

    by_hash = defaultdict(set)
    for srt in journal.rglob("captions/*.srt"):
        parent_item = srt.parent.parent
        by_hash[md5_file(srt)].add(parent_item)
    counts = {h: len(items) for h, items in by_hash.items() if len(items) > 1}

    if use_cache:
        try:
            cache_path.write_text(
                json.dumps({"signature": _caption_signature(journal), "counts": counts}),
                encoding="utf-8",
            )
        except Exception:  # noqa: BLE001 — cache is best-effort
            pass
    return counts


def _caption_signature(journal: Path) -> str:
    """Cheap manifest of caption files → mtime, to invalidate the placeholder cache."""
    import hashlib

    entries = [
        (str(p.relative_to(journal)), int(p.stat().st_mtime))
        for p in journal.rglob("captions/*.srt")
    ]
    entries.sort()
    h = hashlib.sha1()
    h.update(repr(entries).encode("utf-8"))
    return h.hexdigest()


def md5_file(path: Path) -> str:
    import hashlib

    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    args = parse_args(sys.argv[1:])
    langs = args.lang or TARGET_LANGS

    caption_files = list(iter_caption_files(args.journal, args.series))
    if args.skip_to:
        caption_files = caption_files[args.skip_to - 1 :]
    if args.limit:
        caption_files = caption_files[: args.limit]

    # Skip caption files whose exact bytes are duplicated across multiple items —
    # these are copied placeholders, not real per-video source.
    placeholder_counts = build_placeholder_hashes(args.journal)
    real_files, placeholders = [], []
    if placeholder_counts:
        for srt in caption_files:
            h = md5_file(srt)
            if h in placeholder_counts:
                placeholders.append(srt)
            else:
                real_files.append(srt)
    else:
        real_files = caption_files

    print(f"journal={args.journal}")
    print(
        f"series={args.series or '(all)'}  langs={langs}  "
        f"caption_files={len(caption_files)}  force={args.force}"
    )
    if placeholder_counts:
        print(
            f"  skipped {len(placeholders)} duplicate/placeholder caption files "
            f"(content shared across >1 item); {len(real_files)} real files to translate"
        )
    if not real_files:
        print("No real (non-placeholder) caption files matched.")
        return 0 if placeholders else 1

    produced = 0
    skipped = 0
    started = time.time()
    for idx, srt in enumerate(real_files, 1):
        item_dir = srt.parent.parent
        trans_dir = item_dir / "translations"
        for lang in langs:
            model = model_for(lang, os.environ.get("OLLAMA_MODEL", DEFAULT_MODEL))
            dest = trans_dir / translation_filename(srt, lang)
            if dest.exists() and not args.force:
                skipped += 1
                continue
            src_text = srt.read_text(encoding="utf-8-sig", errors="replace")
            translated = translate_srt(src_text, lang, model)
            trans_dir.mkdir(parents=True, exist_ok=True)
            # write with UTF-8 (BOM-free, matching existing translation files)
            dest.write_text(translated, encoding="utf-8")
            produced += 1
        if idx % 5 == 0:
            elapsed = time.time() - started
            print(
                f"  …{idx}/{len(caption_files)} files  "
                f"(+{produced} translated, {skipped} skipped)  {elapsed:.0f}s"
            )
    elapsed = time.time() - started
    print(
        f"\nDone. Produced {produced} translation files, skipped {skipped} "
        f"existing, in {elapsed:.0f}s."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
