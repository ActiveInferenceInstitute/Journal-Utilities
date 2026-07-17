import json
from pathlib import Path

from scripts.refactor_journal import _video_id
from scripts.repair_split_transcripts import _session_sources, repair_item


def test_video_id_recognizes_session_split_filename():
    assert _video_id("cIBIecj7UZE_sess01.simple.txt") == "cIBIecj7UZE"


def test_session_sources_preserve_session_identity(tmp_path: Path):
    output = tmp_path / "data/output"
    output.mkdir(parents=True)
    (output / "video123456_sess01.simple.txt").write_text("First", encoding="utf-8")
    (output / "video123456_sess01.json").write_text(
        '[{"start": 0, "text": "First"}]', encoding="utf-8"
    )
    rendered = _session_sources(["video123456_sess01"], tmp_path)
    assert rendered is not None
    text, structured = rendered
    assert text == "## video123456_sess01\n\nFirst\n"
    assert json.loads(structured)[0]["video_id"] == "video123456_sess01"


def test_repair_item_is_idempotent(tmp_path: Path):
    utilities = tmp_path / "utilities"
    output = utilities / "data/output"
    output.mkdir(parents=True)
    session = "video123456_sess01"
    (output / f"{session}.simple.txt").write_text("First", encoding="utf-8")
    (output / f"{session}.json").write_text("[]", encoding="utf-8")

    item = tmp_path / "journal/data/video/activeinferenceinstitute/Series/item"
    item.mkdir(parents=True)
    (item / "metadata.json").write_text(
        json.dumps({"sessions": [{"index": 1, "session_name": session}]}), encoding="utf-8"
    )
    assert repair_item(item, utilities)
    assert not repair_item(item, utilities, check=True)
