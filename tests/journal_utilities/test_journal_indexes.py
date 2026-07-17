"""Tests for the derived ActiveInferenceJournal indexes."""

import json

from scripts.generate_journal_indexes import build_index, render_index_markdown


def test_index_counts_parts_and_unique_ids(tmp_path):
    root = tmp_path / "data" / "video" / "activeinferenceinstitute" / "Series"
    canonical = root / "Item"
    duplicate = tmp_path / "data" / "video" / "activeinferenceinstitute" / "Other" / "vid-a"
    canonical.mkdir(parents=True)
    duplicate.mkdir(parents=True)
    (canonical / "transcript.txt").write_text("text", encoding="utf-8")
    (canonical / "metadata.json").write_text(
        json.dumps(
            {
                "series": "Series",
                "item": "Item",
                "parts": [{"video_id": "vid-a"}, {"video_id": "vid-b"}],
            }
        ),
        encoding="utf-8",
    )
    (duplicate / "metadata.json").write_text(
        json.dumps(
            {
                "series": "Other",
                "item": "vid-a",
                "parts": [{"video_id": "vid-a"}],
                "duplicate_of": "Series/Item",
            }
        ),
        encoding="utf-8",
    )

    index = build_index(tmp_path)

    assert index["count"] == 2
    assert index["videos"] == 3
    assert index["unique_videos"] == 2
    by_path = {item["path"]: item for item in index["items"]}
    assert by_path["data/video/activeinferenceinstitute/Series/Item"]["has_transcript"] is True
    assert (
        by_path["data/video/activeinferenceinstitute/Other/vid-a"]["duplicate_of"] == "Series/Item"
    )


def test_markdown_surfaces_duplicate_semantics():
    text = render_index_markdown(
        {
            "count": 1,
            "videos": 1,
            "unique_videos": 1,
            "items": [
                {
                    "path": "data/video/activeinferenceinstitute/Other/vid-a",
                    "series": "Other",
                    "item": "vid-a",
                    "parts": ["vid-a"],
                    "has_transcript": False,
                    "duplicate_of": "Series/Item",
                }
            ],
        }
    )

    assert "1 video records · 1 series · 1 unique video IDs" in text
    assert "duplicate of `Series/Item`" in text
