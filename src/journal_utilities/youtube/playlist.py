"""
Playlist enumeration and manifest management for Journal Utilities.

This module provides functionality to enumerate all playlists from a YouTube
channel and their constituent videos using yt-dlp. It also identifies
uncategorized videos (those not belonging to any playlist).
"""

import json
import logging
import subprocess
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .channel import VideoInfo, _parse_video_entry

logger = logging.getLogger(__name__)


@dataclass
class PlaylistInfo:
    """Metadata for a single YouTube playlist."""

    id: str
    title: str = ""
    url: str = ""
    video_count: int = 0

    def __post_init__(self) -> None:
        if not self.url and self.id:
            self.url = f"https://www.youtube.com/playlist?list={self.id}"


@dataclass
class PlaylistManifest:
    """Manifest of all playlists and their videos for a YouTube channel."""

    channel_id: str
    channel_url: str = ""
    enumerated_at: str = ""
    total_playlists: int = 0
    playlists: dict[str, dict] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.channel_url and self.channel_id:
            self.channel_url = f"https://www.youtube.com/channel/{self.channel_id}"
        if not self.enumerated_at:
            self.enumerated_at = datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Playlist enumeration
# ---------------------------------------------------------------------------


def enumerate_playlists(
    channel_id: str,
    max_playlists: Optional[int] = None,
) -> list[PlaylistInfo]:
    """Enumerate all playlists from a YouTube channel.

    Uses ``yt-dlp --flat-playlist --dump-json`` on the channel's /playlists
    tab to list every playlist without downloading content.

    Args:
        channel_id: YouTube channel ID (e.g. ``UCbPq2w41ZaJSWtpCq4BE6Dg``).
        max_playlists: Optional limit on number of playlists to retrieve.

    Returns:
        List of :class:`PlaylistInfo` for each discovered playlist.

    Raises:
        RuntimeError: If yt-dlp exits with a non-zero status and no output.
    """
    playlists_url = f"https://www.youtube.com/channel/{channel_id}/playlists"
    logger.info("Enumerating playlists for channel %s", channel_id)

    cmd: list[str] = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--no-warnings",
        "--ignore-errors",
    ]

    if max_playlists:
        cmd.extend(["--playlist-end", str(max_playlists)])

    cmd.append(playlists_url)

    logger.debug("Running command: %s", " ".join(cmd))
    start_time = time.monotonic()

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=300,
    )

    elapsed = time.monotonic() - start_time
    logger.info(
        "yt-dlp playlist enumeration completed in %.1fs (exit code %d)",
        elapsed,
        result.returncode,
    )

    if result.returncode != 0 and not result.stdout.strip():
        logger.error("yt-dlp stderr: %s", result.stderr)
        raise RuntimeError(
            f"yt-dlp failed with exit code {result.returncode}: {result.stderr[:500]}"
        )

    playlists: list[PlaylistInfo] = []
    for line in result.stdout.strip().splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            playlist_id = entry.get("id", "")
            if not playlist_id:
                continue
            playlists.append(
                PlaylistInfo(
                    id=playlist_id,
                    title=entry.get("title", ""),
                    url=entry.get(
                        "url",
                        f"https://www.youtube.com/playlist?list={playlist_id}",
                    ),
                    video_count=entry.get("playlist_count", 0) or 0,
                )
            )
        except json.JSONDecodeError as exc:
            logger.warning("Skipping malformed JSON line: %s", exc)

    logger.info("Found %d playlists on channel %s", len(playlists), channel_id)
    return playlists


def enumerate_playlist_videos(
    playlist_url: str,
    max_videos: Optional[int] = None,
) -> list[VideoInfo]:
    """Enumerate all videos in a YouTube playlist.

    Uses ``yt-dlp --flat-playlist --dump-json`` to list videos in order.

    Args:
        playlist_url: YouTube playlist URL.
        max_videos: Optional limit on number of videos to retrieve.

    Returns:
        List of :class:`VideoInfo` for each video in the playlist.

    Raises:
        RuntimeError: If yt-dlp exits with a non-zero status and no output.
    """
    logger.info("Enumerating videos from playlist: %s", playlist_url)

    cmd: list[str] = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--no-warnings",
        "--ignore-errors",
    ]

    if max_videos:
        cmd.extend(["--playlist-end", str(max_videos)])

    cmd.append(playlist_url)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=300,
    )

    if result.returncode != 0 and not result.stdout.strip():
        logger.error("yt-dlp stderr: %s", result.stderr)
        raise RuntimeError(
            f"yt-dlp failed with exit code {result.returncode}: {result.stderr[:500]}"
        )

    videos: list[VideoInfo] = []
    for line in result.stdout.strip().splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            video = _parse_video_entry(entry)
            if video:
                videos.append(video)
        except json.JSONDecodeError as exc:
            logger.warning("Skipping malformed JSON line: %s", exc)

    logger.info("Found %d videos in playlist", len(videos))
    return videos


# ---------------------------------------------------------------------------
# Manifest persistence
# ---------------------------------------------------------------------------


def save_playlist_manifest(manifest: PlaylistManifest, path: Path) -> None:
    """Save a playlist manifest to a JSON file.

    Args:
        manifest: The manifest to save.
        path: Destination file path.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "channel_id": manifest.channel_id,
        "channel_url": manifest.channel_url,
        "enumerated_at": manifest.enumerated_at,
        "total_playlists": manifest.total_playlists,
        "playlists": manifest.playlists,
    }

    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    logger.info("Saved playlist manifest to %s (%d playlists)", path, manifest.total_playlists)


def load_playlist_manifest(path: Path) -> PlaylistManifest:
    """Load a playlist manifest from a JSON file.

    Args:
        path: Path to the manifest JSON file.

    Returns:
        A :class:`PlaylistManifest` populated from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    path = Path(path)
    logger.info("Loading playlist manifest from %s", path)

    data = json.loads(path.read_text(encoding="utf-8"))

    manifest = PlaylistManifest(
        channel_id=data.get("channel_id", ""),
        channel_url=data.get("channel_url", ""),
        enumerated_at=data.get("enumerated_at", ""),
        total_playlists=data.get("total_playlists", 0),
        playlists=data.get("playlists", {}),
    )

    logger.info("Loaded manifest with %d playlists", manifest.total_playlists)
    return manifest


# ---------------------------------------------------------------------------
# Rate limiting
# ---------------------------------------------------------------------------


def rate_limit_sleep(
    index: int,
    delay: float = 1.0,
    batch_size: int = 50,
    batch_delay: float = 5.0,
) -> None:
    """Sleep for rate limiting between successive API/download calls.

    Applies a base delay after each item, plus an extra batch delay
    every ``batch_size`` items to avoid triggering YouTube rate limits.

    Args:
        index: Zero-based index of current item in the sequence.
        delay: Base delay in seconds between items.
        batch_size: Number of items per batch before extra delay.
        batch_delay: Extra delay in seconds at each batch boundary.
    """
    time.sleep(delay)
    if (index + 1) % batch_size == 0:
        logger.info(
            "Batch boundary reached at index %d, sleeping %.1fs",
            index,
            batch_delay,
        )
        time.sleep(batch_delay)
