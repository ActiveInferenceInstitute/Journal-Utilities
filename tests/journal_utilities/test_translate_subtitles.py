"""Tests for scripts/translate_subtitles.py (pure logic, no model/network)."""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from translate_subtitles import (  # noqa: E402
    clean_translation,
    translate_srt,
    translation_filename,
)


def test_clean_translation_strips_label_and_echo():
    assert clean_translation("Spanish: hola", "Spanish") == "hola"
    assert clean_translation("«buenos días»\n", "Spanish") == "buenos días"


def test_clean_translation_strips_capitalized_label():
    # The prompt's marker is capitalized ("Translation:"), so the lowercase variant
    # is NOT stripped by design — only the exact echoed label is.
    assert clean_translation("Translation:  vale ", "Spanish") == "vale"
    assert clean_translation("translation:  vale ", "Spanish") == "translation:  vale"


def test_translation_filename_strips_noisy_suffixes(monkeypatch):
    # .en(ca) / .en(ie) / .m4a / .caption40D tokens are dropped to a clean title.
    assert translation_filename(Path("Reward Is Not Necessary.en(ca).srt"), "es") == (
        "Reward Is Not Necessary.es.srt"
    )
    assert translation_filename(Path("ActInfLab ModelStream #001.2.caption40D.srt"), "zh-Hans") == (
        "ActInfLab ModelStream #001.2.zh-Hans.srt"
    )
    assert translation_filename(Path("whatever.m4a.srt"), "fr") == "whatever.fr.srt"


def test_translate_srt_preserves_index_timing_and_replaces_body(monkeypatch):
    from translate_subtitles import ollama_translate  # noqa: E402

    monkeypatch.setattr("translate_subtitles.ollama_translate", lambda t, lang, md: f"TRANS:{t}")
    srt = (
        "1\r\n00:00:02,940 --> 00:00:05,939\r\nhello there,\r\n\r\n"
        "2\r\n00:00:17,359 --> 00:00:20,520\r\ngood morning\r\n"
    )
    got = translate_srt(srt, "es", "gemma")
    assert got.replace("\r\n", "\n") == (
        "1\n00:00:02,940 --> 00:00:05,939\nTRANS:hello there,\n\n"
        "2\n00:00:17,359 --> 00:00:20,520\nTRANS:good morning\n"
    )
    assert ollama_translate  # keep the import referenced / avoid unused warning
