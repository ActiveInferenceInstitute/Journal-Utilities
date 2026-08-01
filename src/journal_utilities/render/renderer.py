"""
Course scaffolding and rendering for YouTube playlists.

Transforms YouTube playlists into course directory structures with
transcript-based ``module.md`` files. Works with existing transcript
files produced by the downloader module.
"""

import json
import logging
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------


def slugify(title: str, max_length: int = 60) -> str:
    """Convert a title to a filesystem-safe slug.

    Lowercases, replaces non-alphanumeric characters with hyphens,
    collapses multiple hyphens, strips leading/trailing hyphens,
    and truncates to *max_length* on a word boundary when possible.

    Args:
        title: Input title string.
        max_length: Maximum slug length (default 60).

    Returns:
        Filesystem-safe slug string.
    """
    if not title:
        return ""

    slug = title.lower()
    # Replace non-alphanumeric (keeping hyphens) with hyphens
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    # Collapse multiple hyphens
    slug = re.sub(r"-{2,}", "-", slug)
    # Strip leading/trailing hyphens
    slug = slug.strip("-")

    if len(slug) > max_length:
        truncated = slug[:max_length]
        last_hyphen = truncated.rfind("-")
        if last_hyphen > max_length // 2:
            truncated = truncated[:last_hyphen]
        slug = truncated.rstrip("-")

    return slug


def format_duration(seconds: float | None) -> str:
    """Format a duration in seconds to a human-readable string.

    Args:
        seconds: Duration in seconds, or ``None``.

    Returns:
        ``H:MM:SS`` or ``M:SS`` string, or ``"Unknown"`` if *seconds* is ``None``.
    """
    if seconds is None:
        return "Unknown"
    total = int(seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def format_upload_date(upload_date: str | None) -> str:
    """Format a yt-dlp ``upload_date`` (``YYYYMMDD``) to ``YYYY-MM-DD``.

    Args:
        upload_date: Date string in ``YYYYMMDD`` format, or ``None``.

    Returns:
        ``YYYY-MM-DD`` string, or ``"Unknown"`` if input is invalid.
    """
    if not upload_date or len(upload_date) != 8:
        return "Unknown"
    try:
        return f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
    except (IndexError, ValueError):
        return "Unknown"


# ---------------------------------------------------------------------------
# Module markdown rendering
# ---------------------------------------------------------------------------


def render_module_md(
    video_title: str,
    video_id: str,
    transcript_text: str,
    duration: float | None = None,
    upload_date: str | None = None,
    playlist_title: str = "",
    transcript_method: str = "auto_caption",
) -> str:
    """Generate ``module.md`` content from a video transcript.

    Args:
        video_title: Title of the YouTube video.
        video_id: YouTube video ID.
        transcript_text: Plain text transcript content.
        duration: Video duration in seconds.
        upload_date: Upload date in ``YYYYMMDD`` format.
        playlist_title: Title of the containing playlist.
        transcript_method: How the transcript was obtained.

    Returns:
        Formatted ``module.md`` content string.
    """
    duration_str = format_duration(duration)
    date_str = format_upload_date(upload_date)

    lines = [
        f"# {video_title}",
        "",
        f"> **Source**: [YouTube](https://www.youtube.com/watch?v={video_id})",
    ]
    if playlist_title:
        lines.append(f"> **Playlist**: {playlist_title}")
    lines.extend(
        [
            f"> **Duration**: {duration_str} | **Uploaded**: {date_str}",
            f"> **Transcript method**: {transcript_method}",
            "",
            "---",
            "",
            transcript_text,
            "",
        ]
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Course scaffolding
# ---------------------------------------------------------------------------


def scaffold_course(
    course_slug: str,
    videos: list[dict[str, Any]],
    transcript_dir: Path,
    courses_dir: Path,
    playlist_title: str = "",
    force: bool = False,
) -> dict[str, Any]:
    """Create a course directory structure with ``module.md`` files.

    For each video, creates a numbered module directory containing a
    ``module.md`` with the transcript content. Reads existing transcripts
    from ``transcript_dir/transcripts/{video_id}.txt``.

    Args:
        course_slug: Filesystem-safe course name.
        videos: List of video metadata dicts (``id``, ``title``, ``duration``, etc.).
        transcript_dir: Base directory containing a ``transcripts/`` subdir.
        courses_dir: Base directory for output course directories.
        playlist_title: Title of the source playlist.
        force: Overwrite existing ``module.md`` files instead of skipping.

    Returns:
        Dict with ``created``, ``skipped``, ``failed`` counts and ``modules`` list.
    """
    course_dir = courses_dir / course_slug
    course_dir.mkdir(parents=True, exist_ok=True)

    # Write course.json metadata (moved to after the module loop so last_updated
    # only bumps when something was actually created — see end of function).
    course_json = course_dir / "course.json"
    course_meta = {
        "title": playlist_title,
        "slug": course_slug,
        "video_count": len(videos),
        "last_updated": datetime.now(UTC).isoformat(),
    }

    transcripts_path = transcript_dir / "transcripts"

    created = 0
    skipped = 0
    failed = 0
    modules: list[dict[str, str]] = []

    for idx, video in enumerate(videos):
        video_id = video.get("id", "")
        video_title = video.get("title", video_id)
        video_slug = slugify(video_title)
        module_name = f"{idx + 1:02d}_{video_slug}"
        module_dir = course_dir / module_name
        module_md_path = module_dir / "module.md"

        # Skip existing unless force=True
        if module_md_path.exists() and not force:
            skipped += 1
            modules.append({"name": module_name, "status": "skipped"})
            logger.debug("Skipping existing %s/module.md", module_name)
            continue

        # Find transcript
        transcript_file = transcripts_path / f"{video_id}.txt"
        transcript_text = ""

        if transcript_file.exists():
            transcript_text = transcript_file.read_text(encoding="utf-8").strip()
        else:
            logger.warning("No transcript found for %s (%s)", video_id, video_title)

        if not transcript_text:
            failed += 1
            modules.append({"name": module_name, "status": "no_transcript"})
            continue

        # Create module directory and write module.md
        module_dir.mkdir(parents=True, exist_ok=True)
        content = render_module_md(
            video_title=video_title,
            video_id=video_id,
            transcript_text=transcript_text,
            duration=video.get("duration"),
            upload_date=video.get("upload_date"),
            playlist_title=playlist_title,
        )
        module_md_path.write_text(content, encoding="utf-8")
        created += 1
        modules.append({"name": module_name, "status": "created"})
        logger.info("Created %s/module.md (%d chars)", module_name, len(transcript_text))

    logger.info(
        "Course '%s': %d created, %d skipped, %d failed",
        course_slug,
        created,
        skipped,
        failed,
    )

    # Only bump last_updated when a module was actually created this run, so
    # scaffolding an already-built course isn't non-idempotent timestamp churn.
    if created == 0:
        try:
            existing = json.loads(course_json.read_text(encoding="utf-8"))
            previous = existing.get("last_updated")
            if previous:
                course_meta["last_updated"] = previous
        except (OSError, json.JSONDecodeError):
            pass
    course_json.write_text(
        json.dumps(course_meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    return {"created": created, "skipped": skipped, "failed": failed, "modules": modules}
