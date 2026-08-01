"""
Metadata enrichment: map Coda rows and session split-files onto the
ActiveInferenceJournal v2.1 ``metadata.json`` schema.

Pure functions only — no I/O beyond what callers pass in. See
ActiveInferenceJournal ``docs/SCHEMA.md`` (Enrichment fields v2.1).
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import cast

# Keys this module owns in metadata.json. Merging only ever sets these;
# foreign keys are never touched or removed.
ENRICH_KEYS = (
    "title",
    "date",
    "guests",
    "other_participants",
    "description",
    "github",
    "slides_url",
    "slides_label",
    "paper_link",
    "paper_title",
    "doi",
    "zenodo",
    "keywords",
    "thumbnails",
    "summaries",
    "enriched_from",
    "sessions",
    "duplicate_of",
)

# Serialization order for known keys; foreign keys keep their original
# relative order and are appended after these.
CANONICAL_ORDER = (
    "series",
    "item",
    "source",
    "channel",
    "category",
    "episode",
    "title",
    "date",
    "guests",
    "other_participants",
    "description",
    "github",
    "slides_url",
    "slides_label",
    "paper_link",
    "paper_title",
    "doi",
    "zenodo",
    "keywords",
    "thumbnails",
    "summaries",
    "enriched_from",
    "parts",
    "sessions",
    "duplicate_of",
)

# Fields that may attach per-part when multiple Coda rows map to one item.
PER_PART_KEYS = (
    "title",
    "date",
    "slides_url",
    "slides_label",
    "paper_link",
    "paper_title",
    "doi",
    "zenodo",
)

# Journal-owned fields: enrichment seeds them when absent but NEVER overwrites —
# the journal repo is their source of truth and hand-edits there must stick.
SEED_ONLY_KEYS = ("sessions",)

# Name suffixes/credentials that a naive comma-split would sever.
_NAME_SUFFIX = re.compile(
    r"^(?:Psy\.?\s?D\.?|Ph\.?\s?D\.?|M\.?\s?D\.?|Jr\.?|Sr\.?|Esq\.?|[IVX]{2,3})$", re.I
)

# Canonical spellings for people who appear under multiple names across sources.
NAME_ALIASES = {
    "Sasha Mikhailova": "Alexandra Mikhailova",
    "JF Cloutier": "Jean-François Cloutier",
}

_CURLY = str.maketrans({"“": '"', "”": '"', "„": '"', "‘": "'", "’": "'"})


def _clean(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""


_PLACEHOLDERS = {"", "n/a", "na", "none", "null", "-"}


def _is_url(value: str) -> bool:
    return value.startswith(("http://", "https://"))


def _is_placeholder(value: str) -> bool:
    return value.casefold() in _PLACEHOLDERS


def _link_and_label(primary: object, fallback: object = "") -> tuple[str, str]:
    """Split a source cell into a real URL and an optional display label."""
    primary, fallback = _clean(primary), _clean(fallback)
    url = primary if _is_url(primary) else fallback if _is_url(fallback) else ""
    label = primary if primary and not _is_url(primary) and not _is_placeholder(primary) else ""
    if not label and fallback and not _is_url(fallback) and not _is_placeholder(fallback):
        label = fallback
    return url, label


def split_names(raw: object) -> list[str]:
    """Split a comma-separated name list, re-joining credential suffixes."""
    names: list[str] = []
    for token in _clean(raw).split(","):
        token = token.strip()
        if not token:
            continue
        if names and _NAME_SUFFIX.match(token):
            names[-1] = f"{names[-1]}, {token}"
        else:
            names.append(token)
    return [NAME_ALIASES.get(name, name) for name in names]


def _iso_date(raw: object) -> str:
    text = _clean(raw)
    if not text:
        return ""
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return ""


def map_coda_row(values: dict[str, object]) -> dict[str, object]:
    """Extract the curated enrichment fields from one Coda row's ``values``."""
    out: dict = {}

    def put(key: str, value: object) -> None:
        if value:
            out[key] = value

    # Title follows the channel convention: "<Unique event name> ~ <stream title>".
    unique = _clean(values.get("Unique event name"))
    stream = _clean(values.get("Title or name of stream"))
    put("title", f"{unique} ~ {stream}" if unique and stream else stream or unique)
    put("date", _iso_date(values.get("Date")))
    put("guests", split_names(values.get("Guests")))
    put("other_participants", split_names(values.get("Other Participants")))
    put("github", _clean(values.get("Github")))

    slides_url, slides_label = _link_and_label(values.get("Slides"), values.get("Slides URL"))
    put("slides_url", slides_url)
    put("slides_label", slides_label)

    paper = _clean(values.get("Paper link"))
    paper_url = _clean(values.get("Paper URL"))
    if _is_url(paper):
        put("paper_link", paper)
    elif _is_url(paper_url):
        put("paper_link", paper_url)
        if paper and not _is_placeholder(paper):
            put("paper_title", paper)
    elif paper and not _is_placeholder(paper):
        put("paper_title", paper)
    put("doi", _clean(values.get("DOI")))
    put("zenodo", _clean(values.get("Zenodo Link")))
    put("keywords", [k.strip() for k in _clean(values.get("Keywords")).split(",") if k.strip()])

    thumbnails = {}
    if _clean(values.get("Thumbnail Image")):
        thumbnails["thumbnail"] = _clean(values.get("Thumbnail Image"))
    if _clean(values.get("Cover image")):
        thumbnails["cover"] = _clean(values.get("Cover image"))
    put("thumbnails", thumbnails)

    summaries = {}
    for key, column in (
        ("human", "Human Summary"),
        ("ai", "AI Summary Text"),
        ("word_300", "300 word summary"),
        ("abstract", "Abstract"),
    ):
        if _clean(values.get(column)):
            summaries[key] = _clean(values.get(column))
    put("summaries", summaries)

    return out


def prefer_url(primary: object, fallback: object) -> str:
    """Return primary if it's an http(s) URL, else fallback if it is, else primary."""
    primary, fallback = _clean(primary), _clean(fallback)
    if primary.startswith(("http://", "https://")):
        return primary
    if fallback.startswith(("http://", "https://")):
        return fallback
    return primary


def _normalize_owned_links(meta: dict) -> None:
    """Keep URL fields URL-only while preserving old labels/titles."""
    for link_key, label_key in (
        ("slides_url", "slides_label"),
        ("paper_link", "paper_title"),
    ):
        value = _clean(meta.get(link_key))
        if not value or _is_url(value):
            continue
        if not meta.get(label_key) and not _is_placeholder(value):
            meta[label_key] = value
        meta.pop(link_key, None)


@dataclass
class SplitResult:
    """Parsed session split-file for one multi-talk video."""

    category: str
    series: str
    video_id: str
    description: str = ""
    sessions: list[dict] = field(default_factory=list)


_CHAPTER = re.compile(r'^\s*(\d{1,2}(?::\d{2}){1,2})\s+(.+?)\s*:\s*"(.*)"\s*$')
# key = 'value' pairs; single-quoted strings honor \' escapes and may span lines.
_KV = re.compile(r"(\w+)\s*=\s*(d?'(?:[^'\\]|\\.)*'|\d+|true|false)", re.S)


def _unquote(raw: str) -> str:
    if raw.startswith("d'"):
        raw = raw[1:]
    if raw.startswith("'") and raw.endswith("'"):
        raw = raw[1:-1]
    return raw.replace("\\'", "'").replace("\\\\", "\\")


def _normalize_start(stamp: str) -> str:
    parts = [int(p) for p in stamp.split(":")]
    if len(parts) == 2:  # MM:SS
        parts = [0] + parts
    h, m, s = parts
    return f"{h}:{m:02d}:{s:02d}"


def parse_split_file(text: str) -> SplitResult:
    """
    Parse a ``<video_id>_split.txt`` file: a chapter list (timestamps,
    speakers, talk titles) followed by SurQL ``CREATE session`` blocks.
    Chapters and blocks are joined by episode number == chapter order.
    """
    text = text.translate(_CURLY)
    head, *raw_blocks = text.split("CREATE session")
    chapters = [m for line in head.splitlines() if (m := _CHAPTER.match(line))]

    blocks = []
    for raw in raw_blocks:
        body = raw.split(";")[0] if ";" in raw else raw
        fields = {key: _unquote(val) for key, val in _KV.findall(body)}
        blocks.append(fields)
    blocks.sort(key=lambda b: int(b.get("episode", 0)))

    if len(chapters) != len(blocks):
        raise ValueError(
            f"split file mismatch: {len(chapters)} chapters vs {len(blocks)} CREATE blocks"
        )
    if not blocks:
        raise ValueError("split file contains no CREATE session blocks")

    video_id = blocks[0].get("session_name", "").split("_sess")[0]
    sessions = []
    for chapter, block in zip(chapters, blocks, strict=True):
        expected_prefix = f"{video_id}_sess"
        if not block.get("session_name", "").startswith(expected_prefix):
            raise ValueError(
                f"session_name {block.get('session_name')!r} does not match video {video_id!r}"
            )
        session = {
            "index": int(block["episode"]),
            "session_name": block["session_name"],
            "start": _normalize_start(chapter.group(1)),
            "title": chapter.group(3).strip(),
            "guests": split_names(block.get("guests", "")),
        }
        participants = split_names(block.get("other_participants", ""))
        if participants:
            session["other_participants"] = participants
        sessions.append(session)

    description = _common_description(blocks)
    return SplitResult(
        category=blocks[0].get("category", ""),
        series=blocks[0].get("series", ""),
        video_id=video_id,
        description=description,
        sessions=sessions,
    )


_SESSION_LINE = re.compile(r"^\s*Session \d+:.*$", re.M)


def _normalize_ws(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def _common_description(blocks: list[dict]) -> str:
    stripped = {
        _normalize_ws(_SESSION_LINE.sub("", block.get("description", ""))) for block in blocks
    }
    return stripped.pop() if len(stripped) == 1 else ""


def merge_enrichment(
    meta: dict[str, object],
    enrichment: dict[str, object],
    part_updates: dict[str, dict[str, object]] | None = None,
    fill_parts: list[dict[str, object]] | None = None,
    replace_parts: bool = False,
) -> tuple[dict, bool]:
    """
    Merge enrichment into a metadata.json dict.

    - Only ENRICH_KEYS are ever set/overwritten; foreign keys survive.
    - Empty enrichment values are skipped (never written, never deleted).
    - ``part_updates`` maps video_id -> {field: value} for per-part fields.
    - ``fill_parts`` replaces ``parts`` only when the existing list is empty,
      or unconditionally with ``replace_parts`` (curated corrections of
      refactor-derived bogus ids).
    - Returns (new_meta, changed) — changed compares values, so key
      reordering alone never triggers a write.
    """
    new = dict(meta)
    for key in ENRICH_KEYS:
        value = enrichment.get(key)
        if value and not (key in SEED_ONLY_KEYS and meta.get(key)):
            new[key] = value

    if fill_parts and (replace_parts or not new.get("parts")):
        new["parts"] = fill_parts

    parts = [dict(p) for p in cast(list, new.get("parts", []))]
    if part_updates:
        for part in parts:
            for key, value in part_updates.get(part.get("video_id", ""), {}).items():
                if key == "slides_url":
                    # A display label must never replace a real URL.
                    if not _is_url(_clean(value)):
                        if (
                            value
                            and not part.get("slides_label")
                            and not _is_url(_clean(part.get("slides_url", "")))
                        ):
                            part["slides_label"] = value
                        continue
                elif key == "paper_link" and not _is_url(_clean(value)):
                    if value and not part.get("paper_title") and not _is_placeholder(_clean(value)):
                        part["paper_title"] = value
                    continue
                if value:
                    part[key] = value
    for part in parts:
        _normalize_owned_links(part)
    new["parts"] = parts
    _normalize_owned_links(new)

    ordered = {key: new[key] for key in CANONICAL_ORDER if key in new}
    ordered.update({key: value for key, value in new.items() if key not in ordered})
    return ordered, ordered != meta
