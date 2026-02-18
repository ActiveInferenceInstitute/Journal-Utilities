"""
Tests for playlist enumeration and manifest management (playlist.py).

All tests use real methods — no mocks. Offline tests use real file I/O.
Network tests enumerate a small batch from the Active Inference channel.
"""

import json
import time
from pathlib import Path

import pytest

from journal_utilities.youtube.playlist import (
    PlaylistInfo,
    PlaylistManifest,
    enumerate_playlist_videos,
    enumerate_playlists,
    load_playlist_manifest,
    rate_limit_sleep,
    save_playlist_manifest,
)


# ---------------------------------------------------------------------------
# PlaylistInfo dataclass
# ---------------------------------------------------------------------------


class TestPlaylistInfo:
    """Tests for the PlaylistInfo dataclass."""

    def test_url_auto_populated(self) -> None:
        """URL is filled from ID when not provided."""
        p = PlaylistInfo(id="PLtest123")
        assert p.url == "https://www.youtube.com/playlist?list=PLtest123"

    def test_explicit_url_preserved(self) -> None:
        """Explicitly provided URL is preserved."""
        p = PlaylistInfo(id="PLtest", url="https://custom.url/")
        assert p.url == "https://custom.url/"

    def test_default_fields(self) -> None:
        """Default fields are empty or zero."""
        p = PlaylistInfo(id="PLx")
        assert p.title == ""
        assert p.video_count == 0

    def test_full_construction(self) -> None:
        """All fields set correctly."""
        p = PlaylistInfo(id="PL1", title="My Playlist", video_count=10)
        assert p.title == "My Playlist"
        assert p.video_count == 10


# ---------------------------------------------------------------------------
# PlaylistManifest dataclass
# ---------------------------------------------------------------------------


class TestPlaylistManifest:
    """Tests for the PlaylistManifest dataclass."""

    def test_channel_url_auto_populated(self) -> None:
        m = PlaylistManifest(channel_id="UCtest123")
        assert m.channel_url == "https://www.youtube.com/channel/UCtest123"

    def test_enumerated_at_auto_set(self) -> None:
        m = PlaylistManifest(channel_id="UCtest123")
        assert len(m.enumerated_at) > 10
        assert "T" in m.enumerated_at

    def test_total_playlists_default_zero(self) -> None:
        m = PlaylistManifest(channel_id="UCtest123")
        assert m.total_playlists == 0

    def test_empty_playlists_dict(self) -> None:
        m = PlaylistManifest(channel_id="UCtest123")
        assert m.playlists == {}


# ---------------------------------------------------------------------------
# Manifest persistence (real file I/O)
# ---------------------------------------------------------------------------


class TestPlaylistManifestPersistence:
    """Tests for save/load playlist manifest using real file operations."""

    def test_round_trip(self, tmp_path: Path) -> None:
        """Save then load produces identical manifest."""
        original = PlaylistManifest(
            channel_id="UCtest",
            total_playlists=2,
            playlists={
                "course-one": {
                    "id": "PL1",
                    "title": "Course One",
                    "videos": [{"id": "v1", "title": "Video 1"}],
                },
                "course-two": {
                    "id": "PL2",
                    "title": "Course Two",
                    "videos": [],
                },
            },
        )

        manifest_path = tmp_path / "playlists.json"
        save_playlist_manifest(original, manifest_path)
        assert manifest_path.exists()

        loaded = load_playlist_manifest(manifest_path)
        assert loaded.channel_id == "UCtest"
        assert loaded.total_playlists == 2
        assert "course-one" in loaded.playlists
        assert loaded.playlists["course-one"]["title"] == "Course One"

    def test_save_creates_parents(self, tmp_path: Path) -> None:
        """Saving to a nested path creates intermediate directories."""
        path = tmp_path / "a" / "b" / "manifest.json"
        m = PlaylistManifest(channel_id="UCx", total_playlists=0)
        save_playlist_manifest(m, path)
        assert path.exists()

    def test_load_nonexistent_raises(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError):
            load_playlist_manifest(tmp_path / "nope.json")

    def test_load_invalid_json_raises(self, tmp_path: Path) -> None:
        bad = tmp_path / "bad.json"
        bad.write_text("not json", encoding="utf-8")
        with pytest.raises(json.JSONDecodeError):
            load_playlist_manifest(bad)

    def test_manifest_json_structure(self, tmp_path: Path) -> None:
        """Saved JSON has expected top-level keys."""
        path = tmp_path / "m.json"
        m = PlaylistManifest(channel_id="UC1", total_playlists=0)
        save_playlist_manifest(m, path)

        data = json.loads(path.read_text())
        assert "channel_id" in data
        assert "playlists" in data
        assert "total_playlists" in data
        assert "enumerated_at" in data

    def test_empty_manifest_round_trip(self, tmp_path: Path) -> None:
        """Empty manifest round-trips correctly."""
        m = PlaylistManifest(channel_id="UC_empty", total_playlists=0)
        path = tmp_path / "empty.json"
        save_playlist_manifest(m, path)
        loaded = load_playlist_manifest(path)
        assert loaded.total_playlists == 0
        assert loaded.playlists == {}


# ---------------------------------------------------------------------------
# Rate limiting (real timing)
# ---------------------------------------------------------------------------


class TestRateLimitSleep:
    """Tests for rate_limit_sleep function using real timing."""

    def test_basic_delay(self) -> None:
        """Applies base delay."""
        start = time.monotonic()
        rate_limit_sleep(0, delay=0.05, batch_size=100, batch_delay=0.0)
        elapsed = time.monotonic() - start
        assert elapsed >= 0.04, f"Delay too short: {elapsed}"

    def test_batch_boundary_extra_delay(self) -> None:
        """Extra delay is applied at batch boundary."""
        start = time.monotonic()
        rate_limit_sleep(
            index=49,  # (49 + 1) % 50 == 0 → batch boundary
            delay=0.05,
            batch_size=50,
            batch_delay=0.05,
        )
        elapsed = time.monotonic() - start
        # Should have base_delay + batch_delay
        assert elapsed >= 0.08, f"Total delay too short: {elapsed}"

    def test_no_batch_delay_mid_batch(self) -> None:
        """No extra delay when not at batch boundary."""
        start = time.monotonic()
        rate_limit_sleep(index=5, delay=0.05, batch_size=50, batch_delay=5.0)
        elapsed = time.monotonic() - start
        # Should only have base delay, not the 5s batch delay
        assert elapsed < 1.0, f"Unexpected batch delay applied: {elapsed}"


# ---------------------------------------------------------------------------
# Real yt-dlp enumeration (network required)
# ---------------------------------------------------------------------------


class TestEnumeratePlaylistsReal:
    """Real yt-dlp tests for playlist enumeration.

    These tests make real network calls to YouTube via yt-dlp.
    """

    def test_enumerate_playlists_small_batch(self) -> None:
        """Enumerate 2 playlists from the Active Inference channel."""
        playlists = enumerate_playlists(
            channel_id="UCbPq2w41ZaJSWtpCq4BE6Dg",
            max_playlists=2,
        )
        # Channel should have playlists
        assert len(playlists) >= 1
        assert len(playlists) <= 2

        for p in playlists:
            assert p.id, "Playlist should have an ID"
            assert p.title, f"Playlist {p.id} should have a title"


class TestEnumeratePlaylistVideosReal:
    """Real yt-dlp tests for playlist video enumeration."""

    def test_enumerate_playlist_videos(self) -> None:
        """Enumerate 3 videos from a known Active Inference playlist."""
        # Use the playlist URL for ActInf Livestreams (known to have many videos)
        playlist_url = "https://www.youtube.com/playlist?list=PLNm0u2n1IwdpwA70LPijr7eJgW3aVf9B5"
        videos = enumerate_playlist_videos(playlist_url, max_videos=3)

        assert len(videos) >= 1
        assert len(videos) <= 3

        for v in videos:
            assert len(v.id) >= 5, f"Video ID too short: {v.id}"
