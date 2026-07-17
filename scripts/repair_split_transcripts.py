#!/usr/bin/env python3
"""Repair merged v2 transcripts built from session-split source files.

Some multi-session items were refactored with blank section IDs because source
files named ``<video_id>_sessNN`` were not recognized as belonging to their
parent video.  This command uses the canonical item's ``sessions[]`` records
and Journal-Utilities' split outputs to rebuild only the affected TXT/JSON
artifacts.

Usage:
    python scripts/repair_split_transcripts.py \
        --journal ../ActiveInferenceJournal \
        --utilities .
    python scripts/repair_split_transcripts.py \
        --journal ../ActiveInferenceJournal --utilities . --check
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SRC_PREFIX = Path("data/video/activeinferenceinstitute")


def _session_sources(session_names: list[str], utilities: Path) -> tuple[str, str] | None:
    """Render a merged transcript from complete split-file outputs."""
    text_sections: list[str] = []
    json_records: list[dict] = []
    output = utilities / "data/output"
    for session_name in session_names:
        text_path = output / f"{session_name}.simple.txt"
        json_path = output / f"{session_name}.json"
        if not text_path.is_file() or not json_path.is_file():
            return None
        try:
            segments = json.loads(json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid session JSON: {json_path}: {exc}") from exc
        if not isinstance(segments, list):
            raise ValueError(f"session JSON must contain a segment list: {json_path}")
        text = text_path.read_text(encoding="utf-8", errors="replace").strip()
        if not text:
            raise ValueError(f"session transcript is empty: {text_path}")
        text_sections.append(f"## {session_name}\n\n{text}")
        json_records.append({"video_id": session_name, "segments": segments})
    return "\n\n".join(text_sections) + "\n", json.dumps(json_records, ensure_ascii=False)


def repair_item(item_dir: Path, utilities: Path, check: bool = False) -> bool:
    """Repair one item and return whether its derived files were stale."""
    metadata_path = item_dir / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    session_names = [
        session["session_name"]
        for session in sorted(metadata.get("sessions", []), key=lambda entry: entry.get("index", 0))
        if session.get("session_name")
    ]
    if not session_names:
        return False
    rendered = _session_sources(session_names, utilities)
    if rendered is None:
        return False
    text, structured = rendered
    targets = ((item_dir / "transcript.txt", text), (item_dir / "transcript.json", structured))
    stale = any(
        not path.is_file() or path.read_text(encoding="utf-8") != expected
        for path, expected in targets
    )
    if stale and not check:
        for path, expected in targets:
            path.write_text(expected, encoding="utf-8")
        print(f"updated: {item_dir}")
    elif stale:
        print(f"stale: {item_dir}")
    return stale


def repair_journal(journal: Path, utilities: Path, check: bool = False) -> bool:
    """Repair every v2 item with complete split-file sources."""
    stale = False
    for metadata_path in sorted((journal / SRC_PREFIX).rglob("metadata.json")):
        stale = repair_item(metadata_path.parent, utilities, check) or stale
    return stale


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--utilities", type=Path, required=True)
    parser.add_argument(
        "--check", action="store_true", help="fail when a derived transcript is stale"
    )
    args = parser.parse_args()
    journal = args.journal.resolve()
    utilities = args.utilities.resolve()
    if not (journal / SRC_PREFIX).is_dir():
        print(f"journal source root not found: {journal / SRC_PREFIX}", file=sys.stderr)
        return 1
    return int(repair_journal(journal, utilities, args.check) and args.check)


if __name__ == "__main__":
    raise SystemExit(main())
