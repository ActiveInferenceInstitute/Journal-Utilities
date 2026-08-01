"""Shared pytest configuration and fixtures for all test packages."""

from pathlib import Path

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env() -> None:
    """Load environment variables for all tests."""
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        load_dotenv(env_file)


@pytest.fixture(scope="session")
def fixtures_dir() -> Path:
    """Path to shared test fixtures directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def sample_transcript_file(fixtures_dir: Path) -> Path:
    """Path to sample transcript file."""
    return fixtures_dir / "sample_transcript.txt"


@pytest.fixture(scope="session")
def images_dir(fixtures_dir: Path) -> Path:
    """Path to test images directory."""
    # Images are in tests/images, not tests/fixtures/images
    return Path(__file__).parent / "images"
