#!/usr/bin/env python3
"""Refactor the ActiveInferenceJournal into the v2 schema (see docs/JOURNAL_SCHEMA.md).

DRY-RUN by default: classifies every file in every item folder into its v2 target
(or an intentional placeholder-drop), and reports an audit so we can prove zero
data loss before applying. ``--apply`` performs the moves with ``git mv`` (history
preserved), builds metadata.json / README.md / transcript.txt, and routes audio to
a side list for the ``audio`` branch.

Usage:
    python scripts/refactor_journal.py --journal ../ActiveInferenceJournal            # dry-run
    python scripts/refactor_journal.py --journal ../ActiveInferenceJournal --apply
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

PLACEHOLDERS = {"blank_document.txt", "blank.txt"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
SERIES_DIRS_SKIP = {".git", "Stream Series Template"}

# Item dir name like "GuestStream_094", "Roundtable_2024.2", "LiveStream_008"
ITEM_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*_[0-9].*")


def classify(rel_parts: list[str], name: str) -> str:
    """Return the v2 destination category for a file given its path *inside* an item."""
    lower = name.lower()
    ext = Path(name).suffix.lower()
    pathlow = "/".join(p.lower() for p in rel_parts)

    if name in PLACEHOLDERS or name == ".gitkeep":
        return "DROP"
    if "metadata" in pathlow and ext == ".json" and not lower.endswith(".simple.json"):
        return "metadata"
    if lower.endswith(".simple.txt"):
        return "transcript_txt"
    if lower.endswith(".simple.json"):
        return "transcript_json"
    if ext == ".srt":
        return "translations" if "translation" in pathlow else "captions"
    if ext in {".m4a", ".mp3", ".wav", ".opus", ".webm"}:
        return "AUDIO"
    if ext in IMAGE_EXT:
        return "assets/images"
    if ext in {".html", ".xhtml"}:
        return "assets/html"
    if "prose" in pathlow:
        return "assets/prose"
    if "appendic" in pathlow:
        return "assets/appendices"
    if "bibliograph" in pathlow:
        return "assets/bibliography"
    if ext in {".pdf", ".odt", ".zip", ".csv", ".lua", ".docx"}:
        return f"assets/{ext.lstrip('.')}"
    if ext in {".txt", ".md", ".vtt", ".json"}:
        # leftover transcript/notes text
        return "assets/notes"
    return "UNMAPPED"


def find_items(journal: Path) -> list[Path]:
    items: list[Path] = []
    for series in sorted(journal.iterdir()):
        if not series.is_dir() or series.name in SERIES_DIRS_SKIP:
            continue
        for sub in sorted(series.iterdir()):
            if sub.is_dir() and ITEM_RE.match(sub.name):
                items.append(sub)
            elif sub.is_dir():
                # nested (e.g. TextbookGroup/<cohort>/Meeting_xxx)
                for deep in sorted(sub.iterdir()):
                    if deep.is_dir() and ITEM_RE.match(deep.name):
                        items.append(deep)
    return items


def analyze(journal: Path) -> dict:
    items = find_items(journal)
    cats: collections.Counter = collections.Counter()
    unmapped: list[str] = []
    audio: list[str] = []
    per_item = []
    for item in items:
        files = [f for f in item.rglob("*") if f.is_file()]
        item_cats: collections.Counter = collections.Counter()
        for f in files:
            rel = f.relative_to(item)
            cat = classify(list(rel.parts[:-1]), f.name)
            cats[cat] += 1
            item_cats[cat] += 1
            if cat == "UNMAPPED":
                unmapped.append(str(f.relative_to(journal)))
            elif cat == "AUDIO":
                audio.append(str(f.relative_to(journal)))
        per_item.append({"item": str(item.relative_to(journal)), "files": len(files), "by_cat": dict(item_cats)})
    return {
        "items": len(items),
        "total_files": sum(cats.values()),
        "by_category": dict(cats.most_common()),
        "audio_count": len(audio),
        "unmapped_count": len(unmapped),
        "unmapped_sample": unmapped[:25],
        "per_item": per_item,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--journal", type=Path, default=Path(__file__).resolve().parent.parent.parent / "ActiveInferenceJournal")
    ap.add_argument("--apply", action="store_true", help="(not yet) perform moves; default is dry-run audit")
    ap.add_argument("--report", type=Path, default=None, help="write full JSON plan here")
    args = ap.parse_args()

    journal = args.journal.resolve()
    if not journal.exists():
        print(f"journal not found: {journal}")
        return 1

    plan = analyze(journal)
    print(f"=== ActiveInferenceJournal v2 refactor — DRY RUN ===")
    print(f"journal: {journal}")
    print(f"items: {plan['items']}   total files: {plan['total_files']}")
    print("by category:")
    for cat, n in plan["by_category"].items():
        print(f"  {n:6d}  {cat}")
    print(f"audio files (-> audio branch): {plan['audio_count']}")
    print(f"UNMAPPED (must be 0 before apply): {plan['unmapped_count']}")
    for u in plan["unmapped_sample"]:
        print(f"    ? {u}")
    if args.report:
        args.report.write_text(json.dumps(plan, indent=2), encoding="utf-8")
        print(f"full plan -> {args.report}")
    if args.apply:
        print("\n--apply is gated until UNMAPPED==0 and the plan is reviewed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
