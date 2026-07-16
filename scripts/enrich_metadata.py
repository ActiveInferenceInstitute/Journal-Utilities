#!/usr/bin/env python3
"""
Enrich ActiveInferenceJournal metadata.json files (v2.1 schema) from:

  1. the Coda (Superhuman Docs) livestream table — full API fetch with
     fallback to the checked-in snapshot,
  2. data/input/*_split.txt session split-files (multi-talk videos),
  3. data/output/channel_videos.json (fills empty parts[] on split items).

Dry-run by default; pass --apply to write. Never creates journal items —
unmatched Coda rows are reported only. Idempotent: re-running --apply on an
enriched tree changes nothing.

Usage:
    python scripts/enrich_metadata.py                # dry run, API fetch
    python scripts/enrich_metadata.py --snapshot-only
    python scripts/enrich_metadata.py --apply --report report.json
"""

import argparse
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from dotenv import load_dotenv  # noqa: E402

from journal_utilities.data.coda_client import load_rows  # noqa: E402
from journal_utilities.data.enrichment import (  # noqa: E402
    PER_PART_KEYS,
    map_coda_row,
    merge_enrichment,
    parse_split_file,
)
from journal_utilities.youtube.categorizer import categorize_name  # noqa: E402
from journal_utilities.youtube.youtube import extract_youtube_id  # noqa: E402

logger = logging.getLogger("enrich_metadata")

SRC_PREFIX = "data/video/activeinferenceinstitute"  # matches refactor_journal.py


def load_journal_index(journal: Path) -> dict[str, dict]:
    """item_rel_path -> {path, meta}; item_rel_path is relative to SRC_PREFIX."""
    root = journal / SRC_PREFIX
    items = {}
    for meta_path in sorted(root.rglob("metadata.json")):
        rel = str(meta_path.parent.relative_to(root))
        items[rel] = {"path": meta_path, "meta": json.loads(meta_path.read_text(encoding="utf-8"))}
    return items


def video_index(items: dict[str, dict]) -> dict[str, str]:
    """video_id -> item_rel_path (first claim wins; collisions logged)."""
    index: dict[str, str] = {}
    for rel, entry in items.items():
        for part in entry["meta"].get("parts", []):
            vid = part.get("video_id", "")
            if vid and vid not in index:
                index[vid] = rel
            elif vid:
                logger.debug("video id %s in both %s and %s", vid, index[vid], rel)
    return index


def load_manifest(path: Path) -> dict[str, dict]:
    videos = json.loads(path.read_text(encoding="utf-8")).get("videos", [])
    return {v["id"]: v for v in videos if v.get("id")}


def manifest_part(video: dict) -> dict:
    part = {
        "video_id": video["id"],
        "url": video.get("url", f"https://www.youtube.com/watch?v={video['id']}"),
        "title": video.get("title", ""),
    }
    if video.get("duration"):
        part["duration"] = video["duration"]
    if video.get("upload_date"):
        part["upload_date"] = video["upload_date"]
    return part


def process_split_files(split_dir: Path, items: dict, manifest: dict, report: dict) -> dict[str, dict]:
    """Parse *_split.txt files -> {item_rel: {enrichment, fill_parts}}; mark Other/ duplicates."""
    pending: dict[str, dict] = {}
    for split_path in sorted(split_dir.glob("*_split.txt")):
        result = parse_split_file(split_path.read_text(encoding="utf-8"))
        target = f"{result.category}/{result.series}"
        if target not in items:
            report["errors"].append(f"{split_path.name}: target item {target!r} not found in journal")
            continue
        enrichment = {
            "sessions": result.sessions,
            "enriched_from": ["split_file"],
        }
        if result.description:
            enrichment["description"] = result.description
        fill = [manifest_part(manifest[result.video_id])] if result.video_id in manifest else None
        pending[target] = {"enrichment": enrichment, "fill_parts": fill}
        report["split_files"].append(
            {"file": split_path.name, "item": target, "sessions": len(result.sessions),
             "parts_filled": bool(fill)}
        )

        duplicate = f"Other/{result.video_id}"
        if duplicate in items:
            pending[duplicate] = {
                "enrichment": {"duplicate_of": target, "enriched_from": ["split_file"]},
                "fill_parts": None,
            }
            report["duplicates_marked"].append(duplicate)
    return pending


def match_coda_rows(rows: list[dict], vid_index: dict, items: dict, report: dict) -> dict[str, list]:
    """Return item_rel -> [(video_id_or_None, mapped_fields), ...]."""
    matched: dict[str, list] = defaultdict(list)
    claimed_fallback: set[str] = set()
    for row in rows:
        values = row.get("values", {})
        name = row.get("name", "") or values.get("Unique event name", "")
        vid = extract_youtube_id(values.get("YouTube", "") or "")
        fields = map_coda_row(values)
        if not fields:
            continue
        if vid and vid in vid_index:
            matched[vid_index[vid]].append((vid, fields))
            report["matched_by_id"] += 1
            continue
        # Fallback: reconstruct the item path from the Unique event name.
        category, series, _ = categorize_name(values.get("Unique event name", "") or "", True)
        rel = f"{category}/{series}" if category and series else None
        if rel and rel in items and rel not in claimed_fallback and rel not in matched:
            claimed_fallback.add(rel)
            matched[rel].append((vid, fields))
            report["matched_by_fallback"].append({"row": name, "item": rel})
        else:
            report["unmatched"].append({"row": name, "video_id": vid or None})
    return matched


# List-valued fields whose cross-row differences merge by order-preserving union.
UNION_KEYS = ("guests", "other_participants", "keywords")


def combine_rows(entries: list, meta: dict, report: dict, rel: str) -> tuple[dict, dict]:
    """Merge multiple matched rows: shared values -> item level, list fields
    union, per-part fields attach to their part, rest first-row-wins."""
    if len(entries) == 1:
        return entries[0][1], {}
    item_level: dict = {}
    part_updates: dict = defaultdict(dict)
    keys = {key for _, fields in entries for key in fields}
    for key in keys:
        values = [fields.get(key) for _, fields in entries if fields.get(key)]
        unique = {json.dumps(v, sort_keys=True) for v in values}
        if len(unique) == 1:
            item_level[key] = values[0]
        elif key in UNION_KEYS:
            item_level[key] = list(dict.fromkeys(name for value in values for name in value))
        elif key in PER_PART_KEYS:
            for vid, fields in entries:
                if vid and fields.get(key):
                    part_updates[vid][key] = fields[key]
            report["per_part_attachments"].append({"item": rel, "field": key})
        else:
            item_level[key] = values[0]
            report["conflicts"].append({"item": rel, "field": key, "kept": "first row"})
    return item_level, dict(part_updates)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--journal", type=Path, default=REPO.parent / "ActiveInferenceJournal")
    parser.add_argument("--snapshot-only", action="store_true", help="skip the Coda API fetch")
    parser.add_argument("--coda-cache", type=Path, default=REPO / "data/input/livestream_fulldata_full.json")
    parser.add_argument("--split-dir", type=Path, default=REPO / "data/input")
    parser.add_argument("--manifest", type=Path, default=REPO / "data/output/channel_videos.json")
    parser.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    parser.add_argument("--report", type=Path, help="write full JSON report to this path")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    load_dotenv(REPO / ".env")

    report: dict = {
        "source": "", "rows_total": 0, "matched_by_id": 0,
        "matched_by_fallback": [], "unmatched": [], "split_files": [],
        "duplicates_marked": [], "per_part_attachments": [], "conflicts": [],
        "items_enriched": 0, "items_unchanged": 0, "errors": [],
        "per_series": defaultdict(lambda: {"enriched": 0, "total": 0}),
    }

    items = load_journal_index(args.journal)
    if not items:
        logger.error("no journal items under %s/%s", args.journal, SRC_PREFIX)
        return 1
    manifest = load_manifest(args.manifest)

    # Split files first, so symposium parts get filled before id-matching.
    pending = process_split_files(args.split_dir, items, manifest, report)
    vid_index = video_index(items)
    for rel, work in pending.items():
        for part in work.get("fill_parts") or []:
            vid_index[part["video_id"]] = rel  # symposium item wins over Other/ duplicate

    rows, source = load_rows(
        snapshot_path=REPO / "data/input/livestream_fulldata_table.json",
        cache_path=args.coda_cache,
        fetch=not args.snapshot_only,
    )
    report["source"] = source
    report["rows_total"] = len(rows)

    matched = match_coda_rows(rows, vid_index, items, report)

    for rel, entry in items.items():
        series = rel.split("/")[0]
        report["per_series"][series]["total"] += 1
        enrichment: dict = {}
        part_updates: dict = {}
        fill_parts = None

        if rel in matched:
            enrichment, part_updates = combine_rows(matched[rel], entry["meta"], report, rel)
            enrichment.setdefault("enriched_from", [])
            enrichment["enriched_from"] = list(dict.fromkeys(enrichment["enriched_from"] + ["coda"]))
        if rel in pending:
            work = pending[rel]
            for key, value in work["enrichment"].items():
                if key == "enriched_from":
                    enrichment["enriched_from"] = list(
                        dict.fromkeys(enrichment.get("enriched_from", []) + value)
                    )
                else:
                    enrichment.setdefault(key, value)
            fill_parts = work["fill_parts"]
            if fill_parts:
                enrichment["enriched_from"] = list(
                    dict.fromkeys(enrichment.get("enriched_from", []) + ["youtube"])
                )

        if not enrichment and not part_updates and not fill_parts:
            continue

        new_meta, changed = merge_enrichment(entry["meta"], enrichment, part_updates, fill_parts)
        if changed:
            report["items_enriched"] += 1
            report["per_series"][series]["enriched"] += 1
            if args.apply:
                entry["path"].write_text(
                    json.dumps(new_meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
                )
        else:
            report["items_unchanged"] += 1

    report["per_series"] = dict(sorted(report["per_series"].items()))
    _print_summary(report, dry_run=not args.apply)
    if args.report:
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        logger.info("full report -> %s", args.report)
    return 0 if not report["errors"] else 1


def _print_summary(report: dict, dry_run: bool) -> None:
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n=== enrich_metadata {mode} ===")
    print(f"coda source:          {report['source']}")
    print(f"coda rows:            {report['rows_total']}")
    print(f"  matched by id:      {report['matched_by_id']}")
    print(f"  matched by fallback:{len(report['matched_by_fallback']):>4}")
    print(f"  unmatched:          {len(report['unmatched'])}")
    print(f"split files:          {len(report['split_files'])} "
          f"({sum(s['sessions'] for s in report['split_files'])} sessions)")
    print(f"duplicates marked:    {report['duplicates_marked']}")
    print(f"items enriched:       {report['items_enriched']}")
    print(f"items already current:{report['items_unchanged']:>4}")
    print(f"per-part attachments: {len(report['per_part_attachments'])}")
    print(f"conflicts:            {len(report['conflicts'])}")
    if report["errors"]:
        print("ERRORS:")
        for err in report["errors"]:
            print(f"  - {err}")
    print("\nper-series coverage:")
    for series, counts in report["per_series"].items():
        print(f"  {series:<45} {counts['enriched']}/{counts['total']}")
    if report["unmatched"]:
        print("\nunmatched coda rows:")
        for row in report["unmatched"][:25]:
            print(f"  - {row['row']!r} (video_id={row['video_id']})")
        if len(report["unmatched"]) > 25:
            print(f"  … and {len(report['unmatched']) - 25} more (see --report)")


if __name__ == "__main__":
    sys.exit(main())
