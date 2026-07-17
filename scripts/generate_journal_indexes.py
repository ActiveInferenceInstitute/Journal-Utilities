#!/usr/bin/env python3
"""Regenerate ActiveInferenceJournal's machine and human indexes.

The journal's ``metadata.json`` files are canonical.  This script derives
``INDEX.json`` and ``INDEX.md`` from those records so corrected part IDs,
duplicate markers, and transcript flags cannot leave stale indexes behind.

Usage:
    python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal
    python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal --check
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

SRC_PREFIX = Path("data/video/activeinferenceinstitute")


def _item_records(journal: Path) -> list[dict]:
    root = journal / SRC_PREFIX
    records: list[dict] = []
    for metadata_path in sorted(root.rglob("metadata.json")):
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        parts = [
            part["video_id"]
            for part in metadata.get("parts", [])
            if isinstance(part, dict) and part.get("video_id")
        ]
        record = {
            "path": metadata_path.parent.relative_to(journal).as_posix(),
            "series": metadata.get("series", ""),
            "item": metadata.get("item", metadata_path.parent.name),
            "parts": parts,
            "has_transcript": (metadata_path.parent / "transcript.txt").is_file(),
        }
        if metadata.get("duplicate_of"):
            record["duplicate_of"] = metadata["duplicate_of"]
        records.append(record)
    return records


def build_index(journal: Path) -> dict:
    """Build the JSON index from canonical metadata records."""
    items = _item_records(journal)
    video_ids = [video_id for item in items for video_id in item["parts"]]
    return {
        "count": len(items),
        # ``videos`` counts indexed part records, including deliberate duplicate
        # copies. ``unique_videos`` makes coverage checks unambiguous.
        "videos": len(video_ids),
        "unique_videos": len(set(video_ids)),
        "items": items,
    }


def _markdown_path(path: str) -> str:
    return "/".join(quote(part, safe="") for part in path.split("/")) + "/"


def render_index_markdown(index: dict) -> str:
    """Render the human index from a machine index."""
    groups: defaultdict[str, list[dict]] = defaultdict(list)
    for item in index["items"]:
        groups[item["series"]].append(item)

    lines = [
        "# ActiveInferenceJournal — Index",
        "",
        f"{index['count']} items · {index['videos']} video records · "
        f"{len(groups)} series · {index['unique_videos']} unique video IDs. "
        "Root: `data/video/activeinferenceinstitute/`. Machine index: `INDEX.json`.",
        "",
    ]
    for series in sorted(groups):
        entries = sorted(groups[series], key=lambda item: item["path"])
        lines.append(f"## {series} ({len(entries)})")
        for item in entries:
            status = "✓" if item["has_transcript"] else "·"
            duplicate = (
                f" — duplicate of `{item['duplicate_of']}`" if item.get("duplicate_of") else ""
            )
            lines.append(
                f"- {status} [`{item['item']}`]({_markdown_path(item['path'])}) — "
                f"{len(item['parts'])} video record(s){duplicate}"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _rendered_files(journal: Path) -> tuple[str, str]:
    index = build_index(journal)
    return (
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        render_index_markdown(index),
    )


def update_indexes(journal: Path, check: bool = False) -> bool:
    """Write indexes, or report whether they are current when ``check`` is set."""
    json_text, markdown_text = _rendered_files(journal)
    targets = ((journal / "INDEX.json", json_text), (journal / "INDEX.md", markdown_text))
    stale = [
        path
        for path, expected in targets
        if not path.exists() or path.read_text(encoding="utf-8") != expected
    ]
    if check:
        for path in stale:
            print(f"stale: {path}")
        return not stale
    for path, expected in targets:
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            path.write_text(expected, encoding="utf-8")
            print(f"updated: {path}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="fail if either index is stale")
    args = parser.parse_args()
    journal = args.journal.resolve()
    if not (journal / SRC_PREFIX).is_dir():
        print(f"journal source root not found: {journal / SRC_PREFIX}", file=sys.stderr)
        return 1
    return 0 if update_indexes(journal, check=args.check) else 1


if __name__ == "__main__":
    raise SystemExit(main())
