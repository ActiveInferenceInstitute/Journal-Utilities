#!/usr/bin/env python3
"""Validate an ActiveInferenceJournal checkout without modifying it.

This is the read-only release gate for the journal/utility boundary.  It checks
the canonical metadata, derived indexes, transcript JSON, duplicate semantics,
manifest coverage, URL fields, and the ``main``-branch security boundary in a
single command.

Usage::

    python scripts/validate_journal.py \
        --journal ../ActiveInferenceJournal \
        --manifest data/output/channel_videos.json
    python scripts/validate_journal.py \
        --journal ../ActiveInferenceJournal \
        --manifest data/output/channel_videos.json \
        --strict-manifest

The manifest is optional for isolated fixture validation, but a production
run should always provide it so coverage can be reconciled to the channel
source of truth.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import parse_qs, urlparse

try:  # Works both as ``python scripts/...`` and as an imported module.
    from scripts.generate_journal_indexes import (
        SRC_PREFIX,
        build_index,
        render_index_markdown,
    )
except ModuleNotFoundError:  # pragma: no cover - exercised by direct CLI use
    from generate_journal_indexes import SRC_PREFIX, build_index, render_index_markdown


URL_FIELDS = ("github", "slides_url", "paper_link", "zenodo")
PLACEHOLDERS = {"", "n/a", "na", "none", "null", "tbd", "unknown"}


@dataclass
class ValidationReport:
    """Collected validation findings and corpus counts."""

    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def _display(path: Path, root: Path) -> str:
    """Return a stable path for human-readable findings."""
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _is_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _youtube_id(value: object) -> str | None:
    """Extract a video ID from common YouTube URL forms."""
    if not isinstance(value, str):
        return None
    parsed = urlparse(value.strip())
    host = parsed.netloc.lower().split(":", 1)[0]
    if host == "youtu.be":
        return parsed.path.strip("/").split("/", 1)[0] or None
    if host.endswith("youtube.com"):
        query_id = parse_qs(parsed.query).get("v", [""])[0].strip()
        return query_id or None
    return None


def _validate_url_fields(obj: dict[str, object], location: str, report: ValidationReport) -> None:
    for field_name in URL_FIELDS:
        if field_name not in obj:
            continue
        value = obj[field_name]
        if isinstance(value, str) and value.strip().lower() in PLACEHOLDERS:
            report.error(f"{location}.{field_name}: placeholder value is not allowed")
        elif not _is_http_url(value):
            report.error(f"{location}.{field_name}: expected an absolute http(s) URL")


def _parts(metadata: dict[str, object]) -> list[object]:
    """Return metadata parts without allowing malformed input to crash validation."""
    value = metadata.get("parts")
    return value if isinstance(value, list) else []


def _load_manifest(path: Path, report: ValidationReport) -> set[str] | None:
    if not path.is_file():
        report.error(f"manifest not found: {path}")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        report.error(f"manifest cannot be read as JSON: {path}: {exc}")
        return None
    videos = data.get("videos") if isinstance(data, dict) else None
    if not isinstance(videos, list):
        report.error(f"manifest has no videos list: {path}")
        return None
    ids: set[str] = set()
    for index, video in enumerate(videos):
        if not isinstance(video, dict) or not isinstance(video.get("id"), str):
            report.error(f"manifest.videos[{index}]: missing string id")
            continue
        video_id = video["id"].strip()
        if not video_id:
            report.error(f"manifest.videos[{index}]: blank id")
        elif video_id in ids:
            report.error(f"manifest: duplicate video id {video_id!r}")
        ids.add(video_id)
    report.counts["manifest_videos"] = len(ids)
    return ids


def _validate_metadata(journal: Path, report: ValidationReport) -> list[tuple[Path, dict]]:
    root = journal / SRC_PREFIX
    records: list[tuple[Path, dict]] = []
    for metadata_path in sorted(root.rglob("metadata.json")):
        location = _display(metadata_path, journal)
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            report.error(f"{location}: invalid JSON: {exc}")
            continue
        if not isinstance(metadata, dict):
            report.error(f"{location}: top-level value must be an object")
            continue
        records.append((metadata_path, metadata))

        relative_item = metadata_path.parent.relative_to(root)
        series = metadata.get("series")
        item = metadata.get("item")
        if not isinstance(series, str) or not series.strip():
            report.error(f"{location}: missing non-empty series")
        elif relative_item.parts and series != relative_item.parts[0]:
            report.error(f"{location}: series does not match source path")
        if not isinstance(item, str) or not item.strip():
            report.error(f"{location}: missing non-empty item")
        elif relative_item.parts and item != relative_item.parts[-1]:
            report.error(f"{location}: item does not match source path")

        parts = metadata.get("parts")
        if not isinstance(parts, list):
            report.error(f"{location}: parts must be a list")
            parts = []
        _validate_url_fields(metadata, location, report)
        for part_index, part in enumerate(parts):
            part_location = f"{location}.parts[{part_index}]"
            if not isinstance(part, dict):
                report.error(f"{part_location}: expected an object")
                continue
            video_id = part.get("video_id")
            if not isinstance(video_id, str) or not video_id.strip():
                report.error(f"{part_location}: missing non-empty video_id")
            url = part.get("url")
            if not _is_http_url(url):
                report.error(f"{part_location}.url: expected an absolute http(s) URL")
            elif video_id and (url_id := _youtube_id(url)) and url_id != video_id:
                report.error(
                    f"{part_location}.url: video ID {url_id!r} does not match {video_id!r}"
                )
            _validate_url_fields(part, part_location, report)
    report.counts["metadata_items"] = len(records)
    report.counts["metadata_parts"] = sum(
        len(metadata.get("parts", []))
        for _, metadata in records
        if isinstance(metadata.get("parts"), list)
    )
    return records


def _validate_indexes(journal: Path, report: ValidationReport) -> None:
    try:
        expected = build_index(journal)
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        report.error(f"cannot derive indexes from metadata: {exc}")
        return
    json_path = journal / "INDEX.json"
    markdown_path = journal / "INDEX.md"
    try:
        actual_json = json.loads(json_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        report.error(f"missing derived index: {json_path}")
        actual_json = None
    except (OSError, json.JSONDecodeError) as exc:
        report.error(f"invalid derived index {json_path}: {exc}")
        actual_json = None
    if actual_json is not None and actual_json != expected:
        report.error(f"stale derived index: {json_path}")
    expected_markdown = render_index_markdown(expected)
    try:
        actual_markdown = markdown_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        report.error(f"missing derived index: {markdown_path}")
    except OSError as exc:
        report.error(f"cannot read derived index {markdown_path}: {exc}")
    else:
        if actual_markdown != expected_markdown:
            report.error(f"stale derived index: {markdown_path}")


def _validate_index_alignment(
    journal: Path, records: list[tuple[Path, dict]], report: ValidationReport
) -> None:
    """Check that every canonical metadata record has the matching index row."""
    index_path = journal / "INDEX.json"
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return
    items = index.get("items") if isinstance(index, dict) else None
    if not isinstance(items, list):
        return
    by_path = {entry.get("path"): entry for entry in items if isinstance(entry, dict)}
    for metadata_path, metadata in records:
        relative = metadata_path.parent.relative_to(journal).as_posix()
        entry = by_path.get(relative)
        if entry is None:
            report.error(f"INDEX.json: missing item record for {relative}")
            continue
        expected_parts = [
            part.get("video_id")
            for part in _parts(metadata)
            if isinstance(part, dict) and part.get("video_id")
        ]
        if entry.get("parts") != expected_parts:
            report.error(f"INDEX.json: parts differ from metadata for {relative}")
        expected_transcript = (metadata_path.parent / "transcript.txt").is_file()
        if entry.get("has_transcript") is not expected_transcript:
            report.error(f"INDEX.json: transcript flag differs from files for {relative}")


def _validate_duplicates(
    journal: Path, records: list[tuple[Path, dict]], report: ValidationReport
) -> None:
    root = journal / SRC_PREFIX
    paths = {metadata_path.parent.relative_to(root).as_posix() for metadata_path, _ in records}
    seen: dict[str, str] = {}
    for metadata_path, metadata in records:
        location = _display(metadata_path, journal)
        item_path = metadata_path.parent.relative_to(root).as_posix()
        duplicate_of = metadata.get("duplicate_of")
        if duplicate_of is not None:
            if not isinstance(duplicate_of, str) or not duplicate_of.strip():
                report.error(f"{location}.duplicate_of: expected a non-empty item path")
            elif duplicate_of not in paths:
                report.error(f"{location}.duplicate_of: target does not exist: {duplicate_of}")
        for part in _parts(metadata):
            if not isinstance(part, dict):
                continue
            video_id = part.get("video_id")
            if not isinstance(video_id, str) or not video_id:
                continue
            if duplicate_of:
                continue
            previous = seen.get(video_id)
            if previous:
                report.error(
                    f"duplicate canonical video ID {video_id!r}: {previous} and {item_path}"
                )
            else:
                seen[video_id] = item_path
    report.counts["canonical_video_ids"] = len(seen)


def _validate_transcripts(journal: Path, report: ValidationReport) -> None:
    root = journal / SRC_PREFIX
    transcript_count = 0
    for transcript_path in sorted(root.rglob("transcript.json")):
        transcript_count += 1
        location = _display(transcript_path, journal)
        try:
            data = json.loads(transcript_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            report.error(f"{location}: invalid JSON: {exc}")
            continue
        if not isinstance(data, list):
            report.error(f"{location}: top-level value must be a list")
            continue
        for index, record in enumerate(data):
            if not isinstance(record, dict):
                report.error(f"{location}[{index}]: expected an object")
                continue
            # AssemblyAI exports use a single raw ``segments`` object and may
            # intentionally have no video ID. Split transcript records use a
            # segment list and must carry their stable session identity.
            if (
                isinstance(record.get("segments"), list)
                and not str(record.get("video_id") or "").strip()
            ):
                report.error(f"{location}[{index}]: split record has blank video_id")
    report.counts["transcript_json_files"] = transcript_count


def _validate_main_branch_boundary(journal: Path, report: ValidationReport) -> None:
    forbidden: list[Path] = []
    for path in journal.rglob("*"):
        if ".git" in path.parts:
            continue
        if not path.is_file():
            continue
        if path.name == "cookies.txt" or path.suffix.lower() in {".m4a", ".mp3", ".wav"}:
            forbidden.append(path)
    for path in forbidden:
        report.error(f"main-branch forbidden file: {_display(path, journal)}")
    report.counts["forbidden_main_files"] = len(forbidden)


def validate_journal(
    journal: Path,
    manifest: Path | None = None,
    strict_manifest: bool = False,
) -> ValidationReport:
    """Validate a journal checkout and return a structured report."""
    journal = journal.resolve()
    report = ValidationReport()
    root = journal / SRC_PREFIX
    if not root.is_dir():
        report.error(f"journal source root not found: {root}")
        return report

    records = _validate_metadata(journal, report)
    _validate_indexes(journal, report)
    _validate_index_alignment(journal, records, report)
    _validate_duplicates(journal, records, report)
    _validate_transcripts(journal, report)
    _validate_main_branch_boundary(journal, report)

    if manifest is not None:
        manifest_ids = _load_manifest(manifest.resolve(), report)
        if manifest_ids is not None:
            canonical_ids = {
                part.get("video_id")
                for _, metadata in records
                if not metadata.get("duplicate_of")
                for part in _parts(metadata)
                if isinstance(part, dict) and isinstance(part.get("video_id"), str)
            }
            # Per-talk uploads are canonical via the linking session entry
            # (sessions[].video_id); their own items carry duplicate_of.
            session_ids = {
                session.get("video_id")
                for _, metadata in records
                if not metadata.get("duplicate_of")
                for session in (metadata.get("sessions") or [])
                if isinstance(session, dict) and isinstance(session.get("video_id"), str)
            }
            missing = sorted(manifest_ids - canonical_ids - session_ids)
            extras = sorted(canonical_ids - manifest_ids)
            report.counts["missing_manifest_videos"] = len(missing)
            report.counts["manifest_extras"] = len(extras)
            if missing:
                report.error(
                    f"manifest coverage missing {len(missing)} video(s): {', '.join(missing[:20])}"
                )
            if extras:
                message = f"journal has {len(extras)} canonical video ID(s) absent from manifest"
                if strict_manifest:
                    report.error(message + f": {', '.join(extras[:20])}")
                else:
                    report.warning(message + "; re-enumerate the channel before classifying them")
    return report


def print_report(report: ValidationReport) -> None:
    """Print a stable human-readable report."""
    for key in sorted(report.counts):
        print(f"{key}: {report.counts[key]}")
    for warning in report.warnings:
        print(f"warning: {warning}")
    for error in report.errors:
        print(f"error: {error}", file=sys.stderr)
    if report.ok:
        print("journal validation: PASS")
    else:
        print(f"journal validation: FAIL ({len(report.errors)} error(s))", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument(
        "--manifest",
        type=Path,
        help="channel_videos.json used for canonical coverage reconciliation",
    )
    parser.add_argument(
        "--strict-manifest",
        action="store_true",
        help="treat canonical journal IDs absent from the manifest as errors",
    )
    args = parser.parse_args(argv)
    report = validate_journal(args.journal, args.manifest, args.strict_manifest)
    print_report(report)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
