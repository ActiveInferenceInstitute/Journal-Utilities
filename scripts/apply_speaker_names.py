#!/usr/bin/env python3
"""
Apply human speaker identifications to journal transcripts.

The mapping lives in the journal item's metadata.json — journal-owned, so it
survives regeneration and records provenance:

    "parts": [{"video_id": "vjtYYbO9jCY", ...,
               "speakers": {"SPEAKER_03": "Daniel Friedman",
                            "SPEAKER_05": "Omar Hashash"}}]

This script replaces the diarization labels in transcript.txt (and the
"speaker" fields in transcript.json) with the mapped names. Idempotent:
already-replaced names are untouched; unmapped labels remain SPEAKER_NN and
are reported as to-dos.

Usage:
    python scripts/apply_speaker_names.py               # all items with mappings
    python scripts/apply_speaker_names.py --item GuestStream/GuestStream_128
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC_PREFIX = "data/video/activeinferenceinstitute"


def apply_to_item(item_dir: Path, meta: dict) -> dict:
    mapping: dict[str, str] = {}
    for part in meta.get("parts", []):
        mapping.update(part.get("speakers") or {})
    if not mapping:
        return {}

    replaced = 0
    tx_path = item_dir / "transcript.txt"
    if tx_path.exists():
        text = tx_path.read_text(encoding="utf-8")
        for label, name in mapping.items():
            text, n = re.subn(rf"^{re.escape(label)}:", f"{name}:", text, flags=re.M)
            replaced += n
        if replaced:
            tx_path.write_text(text, encoding="utf-8")

    tj_path = item_dir / "transcript.json"
    if tj_path.exists():
        blocks = json.loads(tj_path.read_text(encoding="utf-8"))
        changed = False
        for block in blocks if isinstance(blocks, list) else []:
            for seg in block.get("segments", []) if isinstance(block, dict) else []:
                if seg.get("speaker") in mapping:
                    seg["speaker"] = mapping[seg["speaker"]]
                    changed = True
        if changed:
            tj_path.write_text(json.dumps(blocks, ensure_ascii=False), encoding="utf-8")

    unmapped = sorted(set(re.findall(r"^(SPEAKER_\d+):", tx_path.read_text(encoding="utf-8"), re.M))) \
        if tx_path.exists() else []
    return {"replaced": replaced, "unmapped": unmapped}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--journal", type=Path, default=REPO.parent / "ActiveInferenceJournal")
    parser.add_argument("--item", help="single item (path relative to the source root)")
    args = parser.parse_args()

    root = args.journal / SRC_PREFIX
    targets = [root / args.item / "metadata.json"] if args.item \
        else sorted(root.rglob("metadata.json"))

    any_applied = False
    for meta_path in targets:
        if not meta_path.exists():
            print(f"no such item: {meta_path.parent}")
            return 1
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        result = apply_to_item(meta_path.parent, meta)
        if result:
            any_applied = True
            rel = meta_path.parent.relative_to(root)
            todo = f", unmapped: {', '.join(result['unmapped'])}" if result["unmapped"] else ""
            print(f"{rel}: {result['replaced']} label(s) replaced{todo}")
    if not any_applied:
        print("no items with parts[].speakers mappings found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
