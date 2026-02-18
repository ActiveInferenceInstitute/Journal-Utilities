"""
Channel video enumeration for Journal Utilities.

This module provides functionality to enumerate all videos from a YouTube
channel using yt-dlp (no API key required). It produces a channel manifest
that can be consumed by the downloader module.
"""

import json
import logging
import re
import subprocess
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class VideoInfo:
    """Metadata for a single YouTube video."""
    id: str
    title: str = ""
    upload_date: str = ""
    duration: Optional[float] = None
    description: str = ""
    view_count: Optional[int] = None
    url: str = ""

    def __post_init__(self) -> None:
        if not self.url and self.id:
            self.url = f"https://www.youtube.com/watch?v={self.id}"


@dataclass
class ChannelManifest:
    """Manifest of all videos on a YouTube channel."""
    channel_id: str
    channel_url: str = ""
    enumerated_at: str = ""
    total_videos: int = 0
    videos: list[VideoInfo] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.channel_url and self.channel_id:
            self.channel_url = f"https://www.youtube.com/channel/{self.channel_id}"
        if not self.enumerated_at:
            self.enumerated_at = datetime.now(timezone.utc).isoformat()


def enumerate_channel_videos(
    channel_id: str,
    max_videos: Optional[int] = None,
    date_after: Optional[str] = None,
    date_before: Optional[str] = None,
    output_path: Optional[Path] = None,
) -> ChannelManifest:
    """
    Enumerate all videos from a YouTube channel using yt-dlp.

    Uses ``yt-dlp --flat-playlist --dump-json`` to list every video on
    the channel without downloading any media.

    Args:
        channel_id: YouTube channel ID (e.g. ``UCbPq2w41ZaJSWtpCq4BE6Dg``).
        max_videos: Optional limit on the number of videos to retrieve.
        date_after: Optional YYYYMMDD — only include videos uploaded after this date.
        date_before: Optional YYYYMMDD — only include videos uploaded before this date.
        output_path: If provided, save the manifest JSON to this path.

    Returns:
        A :class:`ChannelManifest` containing all discovered videos.

    Raises:
        RuntimeError: If yt-dlp exits with a non-zero status.
    """
    # Use the "Uploads" playlist (UU...) for robust enumeration of all videos
    # including Shorts and Live streams, bypassing tab/UI variances.
    if channel_id.startswith("UC") and len(channel_id) == 24:
        uploads_id = "UU" + channel_id[2:]
        channel_url = f"https://www.youtube.com/playlist?list={uploads_id}"
        logger.info("Enumerating videos from Uploads playlist %s (derived from %s)", uploads_id, channel_id)
    else:
        channel_url = f"https://www.youtube.com/channel/{channel_id}"
        logger.info("Enumerating videos for channel %s", channel_id)

    cmd: list[str] = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--no-warnings",
        "--ignore-errors",
    ]

    if date_after:
        cmd.extend(["--dateafter", date_after])
    if date_before:
        cmd.extend(["--datebefore", date_before])
    if max_videos:
        cmd.extend(["--playlist-end", str(max_videos)])

    cmd.append(channel_url)

    logger.debug("Running command: %s", " ".join(cmd))
    start_time = time.monotonic()

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=1200,  # Allow more time for large channels (600+ videos)
    )

    elapsed = time.monotonic() - start_time
    logger.info("yt-dlp enumeration completed in %.1fs (exit code %d)", elapsed, result.returncode)

    if result.returncode != 0 and not result.stdout.strip():
        logger.error("yt-dlp stderr: %s", result.stderr)
        raise RuntimeError(
            f"yt-dlp failed with exit code {result.returncode}: {result.stderr[:500]}"
        )

    # Parse JSON lines output
    videos: list[VideoInfo] = []
    for line in result.stdout.strip().splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            video = _parse_video_entry(entry)
            if video:
                videos.append(video)
                if max_videos and len(videos) >= max_videos:
                    break
        except json.JSONDecodeError as exc:
            logger.warning("Skipping malformed JSON line: %s", exc)
            continue

    manifest = ChannelManifest(
        channel_id=channel_id,
        total_videos=len(videos),
        videos=videos,
    )

    logger.info("Found %d videos on channel %s", len(videos), channel_id)

    if output_path:
        save_channel_manifest(manifest, output_path)

    return manifest


def _parse_video_entry(entry: dict) -> Optional[VideoInfo]:
    """Parse a single yt-dlp JSON entry into a VideoInfo."""
    video_id = entry.get("id") or entry.get("url")
    if not video_id:
        return None

    # yt-dlp --flat-playlist sometimes gives just the ID in 'url' field
    # Strip any URL prefix to get just the ID
    video_id = str(video_id)
    # Handle full YouTube URLs: extract ID from watch?v= pattern
    match = re.search(r'[?&]v=([a-zA-Z0-9_-]{11})', video_id)
    if match:
        video_id = match.group(1)
    elif "/" in video_id:
        video_id = video_id.rsplit("/", 1)[-1]

    return VideoInfo(
        id=video_id,
        title=entry.get("title", ""),
        upload_date=entry.get("upload_date", ""),
        duration=entry.get("duration"),
        description=entry.get("description", ""),
        view_count=entry.get("view_count"),
    )


def save_channel_manifest(manifest: ChannelManifest, path: Path) -> None:
    """
    Save a channel manifest to a JSON file.

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
        "total_videos": manifest.total_videos,
        "videos": [asdict(v) for v in manifest.videos],
    }

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("Saved channel manifest to %s (%d videos)", path, manifest.total_videos)


def load_channel_manifest(path: Path) -> ChannelManifest:
    """
    Load a previously saved channel manifest from a JSON file.

    Args:
        path: Path to the manifest JSON file.

    Returns:
        A :class:`ChannelManifest` populated from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    path = Path(path)
    logger.info("Loading channel manifest from %s", path)

    data = json.loads(path.read_text(encoding="utf-8"))
    videos = [VideoInfo(**v) for v in data.get("videos", [])]

    manifest = ChannelManifest(
        channel_id=data.get("channel_id", ""),
        channel_url=data.get("channel_url", ""),
        enumerated_at=data.get("enumerated_at", ""),
        total_videos=data.get("total_videos", len(videos)),
        videos=videos,
    )

    logger.info("Loaded manifest with %d videos", manifest.total_videos)
    return manifest
