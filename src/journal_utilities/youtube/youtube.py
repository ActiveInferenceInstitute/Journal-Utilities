"""
YouTube-related utilities for Journal Utilities.

This module provides:
- YouTube ID extraction from URLs
- Private video detection
- Metadata fetching via YouTube API
"""

import json
import logging
import os
import re
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


# YouTube ID regex pattern
YOUTUBE_ID_PATTERN = re.compile(
    r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|live/)|youtu\.be/)([a-zA-Z0-9_-]{11})"
)


def build_channel_url(channel_id: str) -> str:
    """Build a YouTube channel URL from a channel ID.

    Args:
        channel_id: YouTube channel ID (e.g. ``UCbPq2w41ZaJSWtpCq4BE6Dg``).

    Returns:
        Full channel URL.
    """
    return f"https://www.youtube.com/channel/{channel_id}"


def build_video_url(video_id: str) -> str:
    """Build a YouTube video URL from a video ID.

    Args:
        video_id: YouTube video ID (11-character string).

    Returns:
        Full video watch URL.
    """
    return f"https://www.youtube.com/watch?v={video_id}"


def extract_youtube_id(url: str) -> str | None:
    """
    Extract YouTube video ID from a URL.

    Args:
        url: YouTube URL in various formats

    Returns:
        11-character YouTube video ID, or None if not found
    """
    if not url:
        return None

    match = YOUTUBE_ID_PATTERN.search(url)
    return match.group(1) if match else None


def _private_videos_path() -> Path:
    """Resolve the private-videos registry path (runtime state, not source).

    Honors ``PRIVATE_VIDEOS_PATH``; otherwise resolves under the repo's data
    dir instead of the installed package directory — the package dir is
    read-only under a non-editable install and would dirty a tracked source
    path (the same rule as the cookie-file policy).
    """
    explicit = os.environ.get("PRIVATE_VIDEOS_PATH")
    if explicit:
        return Path(explicit)
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").exists():
            return parent / "data" / "private_videos.json"
    return current.parent / "private_videos.json"


def is_video_private(youtube_id: str) -> bool:
    """
    Check if a YouTube video ID is marked as private.

    Args:
        youtube_id: 11-character YouTube video ID

    Returns:
        True if the video is marked as private in the local list
    """
    private_videos_file = _private_videos_path()

    if private_videos_file.exists():
        try:
            with open(private_videos_file, encoding="utf-8") as f:
                private_data = json.load(f)
                return youtube_id in private_data.get("private_video_ids", [])
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("Error reading private videos file: %s", e)

    return False


def mark_video_private(youtube_id: str) -> None:
    """
    Mark a YouTube video as private in the local list.

    Args:
        youtube_id: 11-character YouTube video ID
    """
    private_videos_file = _private_videos_path()

    private_data: dict = {"private_video_ids": []}

    if private_videos_file.exists():
        try:
            with open(private_videos_file, encoding="utf-8") as f:
                private_data = json.load(f)
        except (OSError, json.JSONDecodeError):
            pass

    if youtube_id not in private_data.get("private_video_ids", []):
        private_data.setdefault("private_video_ids", []).append(youtube_id)

        private_videos_file.parent.mkdir(parents=True, exist_ok=True)
        with open(private_videos_file, "w", encoding="utf-8") as f:
            json.dump(private_data, f, indent=2)

        logger.info("Marked video %s as private", youtube_id)


async def fetch_video_metadata(session_name: str, db_client: Any) -> dict | None:  # noqa: ANN401 - injected DB client
    """
    Fetch metadata for a YouTube video and update the database.

    Args:
        session_name: YouTube video ID
        db_client: Database client instance

    Returns:
        Metadata dictionary if successful, None otherwise
    """
    try:
        # Lazy import: pyytdata pulls a network library; avoid importing it at
        # module load for every consumer of journal_utilities.youtube.
        from pyytdata import get_video_info  # noqa: PLC0415

        info = get_video_info(session_name)

        metadata = {
            "title": info.title if info.title else "",
            "description": info.description if info.description else "",
            "thumbnails": info.image_url,
            "published_at": info.publisheddate,
            "url": info.link,
            "channel_title": info.channel_title,
        }

        logger.info("Fetched metadata for %s", session_name)
        return metadata

    except Exception as e:  # noqa: BLE001
        logger.error("Failed to fetch metadata for %s: %s", session_name, e)
        return None


async def insert_metadata_youtube_api(db_client: Any) -> int:  # noqa: ANN401 - injected DB client
    """
    Fetch and insert metadata for all sessions missing titles.

    Args:
        db_client: Database client instance

    Returns:
        Number of sessions updated
    """
    result = await db_client.query(
        "SELECT * FROM session WHERE title is NONE AND is_private != true"
    )

    updated_count = 0

    for session in result:
        session_id = session["id"]
        session_name = session["session_name"]

        logger.info("Fetching metadata for %s", session_name)

        try:
            from pyytdata import get_video_info  # noqa: PLC0415

            info = get_video_info(session_name)

            # Parameterized update — never splice API content into SurrealQL.
            await db_client.query(
                """
                UPDATE $id MERGE {
                    title: $title,
                    description: $description,
                    thumbnails: $thumbnails,
                    published_at: $published_at,
                    url: $url,
                    channel_title: $channel_title
                }
                """,
                {
                    "id": session_id,
                    "title": info.title if info.title else "",
                    "description": info.description if info.description else "",
                    "thumbnails": info.image_url,
                    "published_at": info.publisheddate,
                    "url": info.link,
                    "channel_title": info.channel_title,
                },
            )

            logger.info("Updated metadata for %s", session_id)
            updated_count += 1

        except Exception as e:  # noqa: BLE001
            # A transient network/5xx failure must NOT permanently mark the
            # video private (that would silently drop it from the pipeline with
            # no recovery). Only definitive auth/not-found errors are treated as
            # genuinely private; everything else is logged and left for a retry.
            message = str(e).lower()
            definitively_private = (
                "403" in message
                or "404" in message
                or "private" in message
                or "not found" in message
                or "unauthorized" in message
            )
            if definitively_private:
                logger.info("Marking %s private (403/404): %s", session_name, e)
                mark_video_private(session_name)
            else:
                logger.warning(
                    "Transient metadata failure for %s (not marked private): %s", session_name, e
                )

    return updated_count
