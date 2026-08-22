"""Unit tests for YouTube metadata and description formatter."""

from journal_utilities.youtube.metadata_formatter import (
    ChapterEntry,
    split_base_description,
    assemble_video_description,
    format_chapters_block,
    format_seconds_to_timestamp,
)


def test_format_seconds_to_timestamp():
    assert format_seconds_to_timestamp(0) == "00:00"
    assert format_seconds_to_timestamp(65) == "01:05"
    assert format_seconds_to_timestamp(3665) == "01:01:05"


def test_format_chapters_block():
    chapters = [
        {"start": 120.0, "title": "Main Presentation"},
        {"start": 600.0, "title": "Q&A Session"},
    ]
    formatted = format_chapters_block(chapters)
    # Checks that 00:00 Introduction is prepended automatically
    assert "00:00 Introduction" in formatted
    assert "02:00 Main Presentation" in formatted
    assert "10:00 Q&A Session" in formatted


def test_assemble_video_description():
    chapters = [
        ChapterEntry(start=0.0, title="Intro"),
        ChapterEntry(start=180.0, title="Discussion"),
    ]
    desc = assemble_video_description(
        base_description="A deep dive into Active Inference.",
        chapters=chapters,
        video_id="test_vid_123",
        slides_url="https://slides.example.com",
    )
    assert "A deep dive into Active Inference." in desc
    assert "--- TIMESTAMPS & CHAPTERS ---" in desc
    assert "00:00 Intro" in desc
    assert "03:00 Discussion" in desc
    assert "--- RESOURCES & TRANSCRIPT ---" in desc
    assert "https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal/blob/main/transcripts/test_vid_123.md" in desc
    assert "https://slides.example.com" in desc
    assert "Active Inference Institute information:" in desc
    assert "https://video.activeinference.institute/" in desc


def test_split_base_description_strips_legacy_timestamp_runs():
    """Regression: legacy embedded chapter lists must not duplicate on re-assembly."""
    base = (
        "Paper abstract text.\n"
        "\n"
        "------\n"
        "\n"
        "CHAPTERS\n"
        "00:00 Introduction\n"
        "00:02 Introduction\n"
        "00:34 Chapter 1\n"
        "\n"
        "Follow us:\n"
        "https://example.com"
    )
    paper_info, link_block = split_base_description(base)
    assert "00:00 Introduction" not in paper_info
    assert "Paper abstract text." in paper_info
    assert "Follow us:" in link_block

    chapters = [
        ChapterEntry(start=0.0, title="Introduction"),
        ChapterEntry(start=34.0, title="Chapter 1"),
    ]
    once = assemble_video_description(base_description=base, chapters=chapters, video_id="vid_regtest")
    twice = assemble_video_description(base_description=once, chapters=chapters, video_id="vid_regtest")
    assert once == twice  # idempotent
    assert once.count("00:00 Introduction") == 1
    assert once.count("--- TIMESTAMPS & CHAPTERS ---") == 1
    assert "--- RESOURCES & TRANSCRIPT ---" in once
    assert "Active Inference Institute information:" in once
    # Short (<3 line) timestamp runs are preserved verbatim.
    short = "Intro text\n00:30 Note\n00:45 Another\n\nFollow us:\nhttps://example.com"
    pi, _ = split_base_description(short)
    assert "00:30 Note" in pi
