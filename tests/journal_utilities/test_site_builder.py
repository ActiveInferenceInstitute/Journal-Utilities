"""Tests for static site builder (GitHub Pages generation)."""

import json
from pathlib import Path

from journal_utilities.site.builder import build_item_payload, build_site, parse_srt


def test_parse_srt() -> None:
    srt_text = (
        "1\n00:00:01,000 --> 00:00:04,500\nHello and welcome!\n\n"
        "2\n00:00:05,000 --> 00:00:08,200\nToday we talk about Active Inference.\n"
    )
    cues = parse_srt(srt_text)
    assert len(cues) == 2
    assert cues[0]["start"] == 1.0
    assert cues[0]["end"] == 4.5
    assert cues[0]["text"] == "Hello and welcome!"
    assert cues[1]["start"] == 5.0
    assert cues[1]["end"] == 8.2


def test_build_item_payload_and_site(tmp_path: Path) -> None:
    journal_dir = tmp_path / "journal"
    item_dir = journal_dir / "data/video/activeinferenceinstitute/Livestream/LiveStream_001"
    item_dir.mkdir(parents=True)

    meta = {
        "series": "Livestream",
        "item": "LiveStream_001",
        "title": "Introduction to Active Inference",
        "category": "Livestream",
        "episode": "1",
        "parts": [{"video_id": "test_vid_123", "title": "Part 1", "speakers": {"SPEAKER_00": "Daniel"}}],
    }
    (item_dir / "metadata.json").write_text(json.dumps(meta), encoding="utf-8")
    (item_dir / "transcript.txt").write_text("Hello world transcript", encoding="utf-8")

    # Add translations
    tr_dir = item_dir / "translations"
    tr_dir.mkdir()
    (tr_dir / "LiveStream_001.es.srt").write_text("1\n00:00:01,000 --> 00:00:03,000\nHola mundo\n", encoding="utf-8")

    # Add INDEX.json
    index_data = {
        "count": 1,
        "items": [
            {
                "path": "data/video/activeinferenceinstitute/Livestream/LiveStream_001",
                "series": "Livestream",
                "item": "LiveStream_001",
                "has_transcript": True,
            }
        ],
    }
    (journal_dir / "INDEX.json").write_text(json.dumps(index_data), encoding="utf-8")

    payload = build_item_payload(item_dir, meta)
    assert payload["id"] == "Livestream/LiveStream_001"
    assert "es" in payload["translations"]
    assert len(payload["translations"]["es"][0]["cues"]) == 1

    out_dir = tmp_path / "site_out"
    res = build_site(journal_dir=journal_dir, output_dir=out_dir)
    assert res["items_processed"] == 1
    assert (out_dir / "index.html").exists()
    assert (out_dir / "styles.css").exists()
    assert (out_dir / "app.js").exists()
    assert (out_dir / "manifest.json").exists()

    manifest = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["total_items"] == 1
    assert manifest["items"][0]["languages"] == ["es"]
