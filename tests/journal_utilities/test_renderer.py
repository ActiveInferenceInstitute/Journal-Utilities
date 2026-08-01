"""
Tests for course scaffolding and rendering (renderer.py).

All tests use real methods and real file I/O — no mocks.
"""

import json
from pathlib import Path

from journal_utilities.render.renderer import (
    format_duration,
    format_upload_date,
    render_module_md,
    scaffold_course,
    slugify,
)

# ---------------------------------------------------------------------------
# slugify
# ---------------------------------------------------------------------------


class TestSlugify:
    """Tests for the slugify helper."""

    def test_basic_title(self) -> None:
        assert slugify("Hello World") == "hello-world"

    def test_special_characters(self) -> None:
        result = slugify("ActInf GuestStream #001: What & Why?")
        assert result == "actinf-gueststream-001-what-why"

    def test_collapses_multiple_hyphens(self) -> None:
        result = slugify("hello   world---test")
        assert "--" not in result

    def test_strips_leading_trailing_hyphens(self) -> None:
        result = slugify("---hello---")
        assert not result.startswith("-")
        assert not result.endswith("-")

    def test_empty_string(self) -> None:
        assert slugify("") == ""

    def test_only_special_chars(self) -> None:
        result = slugify("!@#$%^&*()")
        assert result == ""

    def test_truncation_on_word_boundary(self) -> None:
        long_title = "this is a very long title that should be truncated at a word boundary"
        result = slugify(long_title, max_length=30)
        assert len(result) <= 30

    def test_preserves_numbers(self) -> None:
        assert slugify("Video 123") == "video-123"

    def test_unicode_removed(self) -> None:
        result = slugify("Café Résumé")
        # Non-ASCII chars become hyphens
        assert "é" not in result

    def test_max_length_respected(self) -> None:
        result = slugify("a" * 100, max_length=20)
        assert len(result) <= 20


# ---------------------------------------------------------------------------
# format_duration
# ---------------------------------------------------------------------------


class TestFormatDuration:
    """Tests for format_duration helper."""

    def test_none_returns_unknown(self) -> None:
        assert format_duration(None) == "Unknown"

    def test_zero_seconds(self) -> None:
        assert format_duration(0) == "0:00"

    def test_seconds_only(self) -> None:
        assert format_duration(45) == "0:45"

    def test_minutes_and_seconds(self) -> None:
        assert format_duration(125) == "2:05"

    def test_hours(self) -> None:
        assert format_duration(3661) == "1:01:01"

    def test_exactly_one_hour(self) -> None:
        assert format_duration(3600) == "1:00:00"

    def test_float_input(self) -> None:
        assert format_duration(90.7) == "1:30"


# ---------------------------------------------------------------------------
# format_upload_date
# ---------------------------------------------------------------------------


class TestFormatUploadDate:
    """Tests for format_upload_date helper."""

    def test_none_returns_unknown(self) -> None:
        assert format_upload_date(None) == "Unknown"

    def test_empty_returns_unknown(self) -> None:
        assert format_upload_date("") == "Unknown"

    def test_valid_date(self) -> None:
        assert format_upload_date("20230615") == "2023-06-15"

    def test_short_string(self) -> None:
        assert format_upload_date("2023") == "Unknown"

    def test_long_string(self) -> None:
        assert format_upload_date("202306151234") == "Unknown"


# ---------------------------------------------------------------------------
# render_module_md
# ---------------------------------------------------------------------------


class TestRenderModuleMd:
    """Tests for render_module_md template rendering."""

    def test_basic_rendering(self) -> None:
        content = render_module_md(
            video_title="Test Video",
            video_id="abc123DEF_-",
            transcript_text="This is the transcript content.",
        )
        assert "# Test Video" in content
        assert "abc123DEF_-" in content
        assert "This is the transcript content." in content
        assert "---" in content

    def test_includes_youtube_link(self) -> None:
        content = render_module_md(
            video_title="Title",
            video_id="testId12345",
            transcript_text="Text",
        )
        assert "https://www.youtube.com/watch?v=testId12345" in content

    def test_includes_duration_and_date(self) -> None:
        content = render_module_md(
            video_title="Title",
            video_id="id123",
            transcript_text="Text",
            duration=3600,
            upload_date="20230101",
        )
        assert "1:00:00" in content
        assert "2023-01-01" in content

    def test_includes_playlist_title(self) -> None:
        content = render_module_md(
            video_title="Title",
            video_id="id123",
            transcript_text="Text",
            playlist_title="My Playlist",
        )
        assert "My Playlist" in content

    def test_includes_transcript_method(self) -> None:
        content = render_module_md(
            video_title="Title",
            video_id="id123",
            transcript_text="Text",
            transcript_method="whisper",
        )
        assert "whisper" in content

    def test_unknown_duration_and_date(self) -> None:
        content = render_module_md(
            video_title="Title",
            video_id="id123",
            transcript_text="Text",
        )
        assert "Unknown" in content


# ---------------------------------------------------------------------------
# scaffold_course (real file I/O)
# ---------------------------------------------------------------------------


class TestScaffoldCourse:
    """Tests for scaffold_course using real file operations."""

    def _create_transcripts(self, tmp_path: Path, video_ids: list[str]) -> Path:
        """Helper to create transcript files."""
        transcript_dir = tmp_path / "data"
        transcripts_path = transcript_dir / "transcripts"
        transcripts_path.mkdir(parents=True)
        for vid in video_ids:
            (transcripts_path / f"{vid}.txt").write_text(
                f"Transcript content for {vid}", encoding="utf-8"
            )
        return transcript_dir

    def test_creates_course_directory(self, tmp_path: Path) -> None:
        """Creates course directory with module.md files."""
        transcript_dir = self._create_transcripts(tmp_path, ["v1", "v2"])
        courses_dir = tmp_path / "courses"

        videos = [
            {"id": "v1", "title": "First Video", "duration": 600},
            {"id": "v2", "title": "Second Video", "duration": 1200},
        ]

        result = scaffold_course(
            course_slug="test-course",
            videos=videos,
            transcript_dir=transcript_dir,
            courses_dir=courses_dir,
            playlist_title="Test Course",
        )

        assert result["created"] == 2
        assert result["failed"] == 0
        assert (courses_dir / "test-course").is_dir()
        assert (courses_dir / "test-course" / "course.json").exists()

        # Check module directories exist with module.md files
        for module_info in result["modules"]:
            module_dir = courses_dir / "test-course" / module_info["name"]
            assert (module_dir / "module.md").exists()

    def test_module_md_content(self, tmp_path: Path) -> None:
        """Generated module.md has expected content."""
        transcript_dir = self._create_transcripts(tmp_path, ["abc123"])
        courses_dir = tmp_path / "courses"

        videos = [{"id": "abc123", "title": "My Video", "duration": 300}]

        scaffold_course(
            course_slug="my-course",
            videos=videos,
            transcript_dir=transcript_dir,
            courses_dir=courses_dir,
        )

        md_files = list((courses_dir / "my-course").rglob("module.md"))
        assert len(md_files) == 1

        content = md_files[0].read_text()
        assert "# My Video" in content
        assert "abc123" in content
        assert "Transcript content for abc123" in content

    def test_course_json_created(self, tmp_path: Path) -> None:
        """course.json is created with correct metadata."""
        transcript_dir = self._create_transcripts(tmp_path, ["v1"])
        courses_dir = tmp_path / "courses"

        scaffold_course(
            course_slug="test",
            videos=[{"id": "v1", "title": "V1"}],
            transcript_dir=transcript_dir,
            courses_dir=courses_dir,
            playlist_title="Test Playlist",
        )

        course_json = courses_dir / "test" / "course.json"
        assert course_json.exists()
        data = json.loads(course_json.read_text())
        assert data["title"] == "Test Playlist"
        assert data["video_count"] == 1

    def test_skips_existing_modules(self, tmp_path: Path) -> None:
        """Existing module.md files are skipped by default."""
        transcript_dir = self._create_transcripts(tmp_path, ["v1"])
        courses_dir = tmp_path / "courses"
        videos = [{"id": "v1", "title": "V1"}]

        # First scaffold
        result1 = scaffold_course("test", videos, transcript_dir, courses_dir)
        assert result1["created"] == 1

        # Second scaffold should skip
        result2 = scaffold_course("test", videos, transcript_dir, courses_dir)
        assert result2["skipped"] == 1
        assert result2["created"] == 0

    def test_force_overwrites(self, tmp_path: Path) -> None:
        """Force=True overwrites existing module.md files."""
        transcript_dir = self._create_transcripts(tmp_path, ["v1"])
        courses_dir = tmp_path / "courses"
        videos = [{"id": "v1", "title": "V1"}]

        scaffold_course("test", videos, transcript_dir, courses_dir)
        result = scaffold_course("test", videos, transcript_dir, courses_dir, force=True)
        assert result["created"] == 1
        assert result["skipped"] == 0

    def test_missing_transcript_counts_as_failed(self, tmp_path: Path) -> None:
        """Videos without transcripts are counted as failed."""
        transcript_dir = tmp_path / "data"
        (transcript_dir / "transcripts").mkdir(parents=True)
        courses_dir = tmp_path / "courses"

        result = scaffold_course(
            "test",
            [{"id": "missing", "title": "No Transcript"}],
            transcript_dir,
            courses_dir,
        )
        assert result["failed"] == 1
        assert result["created"] == 0

    def test_numbered_module_directories(self, tmp_path: Path) -> None:
        """Module directories are numbered sequentially."""
        transcript_dir = self._create_transcripts(tmp_path, ["a", "b", "c"])
        courses_dir = tmp_path / "courses"

        videos = [
            {"id": "a", "title": "First"},
            {"id": "b", "title": "Second"},
            {"id": "c", "title": "Third"},
        ]

        result = scaffold_course("test", videos, transcript_dir, courses_dir)

        names = [m["name"] for m in result["modules"]]
        assert names[0].startswith("01_")
        assert names[1].startswith("02_")
        assert names[2].startswith("03_")
