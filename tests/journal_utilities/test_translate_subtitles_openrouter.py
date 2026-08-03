"""Tests for scripts/translate_subtitles_openrouter.py (pure logic, no network)."""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from translate_subtitles_openrouter import (  # noqa: E402
    translate_srt,
    translation_filename,
)

SRT = (
    "1\r\n00:00:02,940 --> 00:00:05,939\r\nhello there,\r\n\r\n"
    "2\r\n00:00:17,359 --> 00:00:20,520\r\ngood morning\r\n"
)


def test_translation_filename_strips_noisy_suffixes():
    assert translation_filename(Path("Reward Is Not Necessary.en(ca).srt"), "es") == (
        "Reward Is Not Necessary.en(ca).es.srt"
    )
    assert translation_filename(Path("Reward Is Not Necessary.en.srt"), "es") == (
        "Reward Is Not Necessary.es.srt"
    )
    assert translation_filename(Path("whatever.m4a.srt"), "fr") == "whatever.fr.srt"


def test_translate_srt_success_path(monkeypatch):
    from translate_subtitles_openrouter import translate_batch  # noqa: E402

    monkeypatch.setattr(
        "translate_subtitles_openrouter.translate_batch",
        lambda texts, lang, model, api_key, base_url, max_tokens=16000: texts,
    )
    out, fallbacks, cues = translate_srt(SRT, "es", "m", "k", "http://x", 60, 2)
    assert fallbacks == 0 and cues == 2
    assert out.replace("\r\n", "\n") == (
        "1\n00:00:02,940 --> 00:00:05,939\nhello there,\n\n"
        "2\n00:00:17,359 --> 00:00:20,520\ngood morning\n"
    )
    assert translate_batch  # keep the import referenced / avoid unused warning


def test_translate_srt_falls_back_to_source_when_api_fails(monkeypatch):
    def boom(*args, **kwargs):
        raise RuntimeError("api down")

    monkeypatch.setattr("translate_subtitles_openrouter.translate_batch", boom)
    out, fallbacks, cues = translate_srt(SRT, "es", "m", "k", "http://x", 60, 2)
    # Both single-cue chunks fell back to the source text; structure preserved.
    assert fallbacks == 2 and cues == 2
    assert out.replace("\r\n", "\n") == (
        "1\n00:00:02,940 --> 00:00:05,939\nhello there,\n\n"
        "2\n00:00:17,359 --> 00:00:20,520\ngood morning\n"
    )


def test_load_api_key_requires_env_or_repo_env(monkeypatch, tmp_path):
    from translate_subtitles_openrouter import load_api_key  # noqa: E402

    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    monkeypatch.setattr("translate_subtitles_openrouter.Path", lambda *a: tmp_path / "nope")
    try:
        load_api_key()
        raise AssertionError("should have exited")
    except SystemExit as e:
        assert "OPENROUTER_API_KEY" in str(e)
