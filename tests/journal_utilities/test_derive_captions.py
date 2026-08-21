"""Tests for deriving caption SRTs from transcript.json."""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from derive_captions_from_json import derive_captions, sec_to_srt_time, segments_to_srt


def test_sec_to_srt_time() -> None:
    assert sec_to_srt_time(0.0) == "00:00:00,000"
    assert sec_to_srt_time(5.467) == "00:00:05,467"
    assert sec_to_srt_time(3665.123) == "01:01:05,123"


def test_segments_to_srt() -> None:
    segments = [
        {"start": 1.0, "end": 4.0, "text": "Hello world"},
        {"start": 5.5, "end": 8.0, "text": "Next cue"},
    ]
    srt = segments_to_srt(segments)
    assert "00:00:01,000 --> 00:00:04,000" in srt
    assert "Hello world" in srt
    assert "00:00:05,500 --> 00:00:08,000" in srt
    assert "Next cue" in srt


def test_derive_captions_integration(tmp_path: Path) -> None:
    journal_dir = tmp_path / "journal"
    item_dir = journal_dir / "data/video/activeinferenceinstitute/ModelStream/ModelStream_001"
    item_dir.mkdir(parents=True)

    meta = {
        "series": "ModelStream",
        "item": "ModelStream_001",
        "title": "ModelStream 1",
        "parts": [{"video_id": "vid123", "title": "ModelStream 1 ~ Intro"}],
    }
    (item_dir / "metadata.json").write_text(json.dumps(meta), encoding="utf-8")

    tj_data = [
        {
            "video_id": "vid123",
            "segments": [{"start": 0.0, "end": 2.0, "text": "Welcome to ModelStream 1"}],
        }
    ]
    (item_dir / "transcript.json").write_text(json.dumps(tj_data), encoding="utf-8")

    index_data = {
        "count": 1,
        "items": [
            {
                "path": "data/video/activeinferenceinstitute/ModelStream/ModelStream_001",
                "series": "ModelStream",
                "item": "ModelStream_001",
            }
        ],
    }
    (journal_dir / "INDEX.json").write_text(json.dumps(index_data), encoding="utf-8")

    res = derive_captions(journal_dir, apply=True)
    assert res["created"] == 1

    srt_files = list((item_dir / "captions").glob("*.srt"))
    assert len(srt_files) == 1
    assert "Welcome to ModelStream 1" in srt_files[0].read_text(encoding="utf-8")
