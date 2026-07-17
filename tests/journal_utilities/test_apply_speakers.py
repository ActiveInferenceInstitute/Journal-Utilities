"""Tests for scripts/apply_speaker_names.py."""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from apply_speaker_names import apply_to_item


def _item(tmp_path: Path, speakers: dict) -> tuple[Path, dict]:
    item = tmp_path / "item"
    item.mkdir()
    meta = {"parts": [{"video_id": "vid00000001", "speakers": speakers}]}
    (item / "transcript.txt").write_text(
        "SPEAKER_00:\nhello\n\nSPEAKER_01:\nhi SPEAKER_00 there\n")
    (item / "transcript.json").write_text(json.dumps(
        [{"video_id": "vid00000001",
          "segments": [{"speaker": "SPEAKER_00", "text": "hello"},
                       {"speaker": "SPEAKER_01", "text": "hi"}]}]))
    return item, meta


class TestApplySpeakers:
    def test_replaces_only_label_headings(self, tmp_path):
        item, meta = _item(tmp_path, {"SPEAKER_00": "Ada Lovelace"})
        result = apply_to_item(item, meta)
        text = (item / "transcript.txt").read_text()
        assert text.startswith("Ada Lovelace:\n")
        # in-sentence mention is not a heading and stays untouched
        assert "hi SPEAKER_00 there" in text
        assert result["unmapped"] == ["SPEAKER_01"]

    def test_json_speakers_replaced(self, tmp_path):
        item, meta = _item(tmp_path, {"SPEAKER_00": "Ada Lovelace", "SPEAKER_01": "Alan Turing"})
        apply_to_item(item, meta)
        segs = json.loads((item / "transcript.json").read_text())[0]["segments"]
        assert [s["speaker"] for s in segs] == ["Ada Lovelace", "Alan Turing"]

    def test_idempotent(self, tmp_path):
        item, meta = _item(tmp_path, {"SPEAKER_00": "Ada Lovelace", "SPEAKER_01": "Alan Turing"})
        apply_to_item(item, meta)
        first = (item / "transcript.txt").read_text()
        result = apply_to_item(item, meta)
        assert (item / "transcript.txt").read_text() == first
        assert result["unmapped"] == []

    def test_no_mapping_is_noop(self, tmp_path):
        item, meta = _item(tmp_path, {})
        meta["parts"][0].pop("speakers")
        assert apply_to_item(item, meta) == {}
