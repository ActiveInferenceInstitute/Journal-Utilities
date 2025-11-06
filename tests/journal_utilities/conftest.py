"""Pytest configuration and fixtures specific to journal_utilities tests."""

import os
from pathlib import Path
from typing import Any

import pytest
from dotenv import load_dotenv

# Load .env file
env_file = Path(__file__).parent.parent.parent / ".env"
if env_file.exists():
    load_dotenv(env_file)


@pytest.fixture(scope="session")
def db_config() -> dict[str, str]:
    """Database configuration from environment variables."""
    return {
        "url": os.getenv("DB_URL", "ws://localhost:8080/rpc"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "root"),
        "name": os.getenv("DB_NAME", "actinf"),
        "namespace": os.getenv("DB_NAMESPACE", "actinf"),
    }


@pytest.fixture
def db_url(db_config: dict[str, str]) -> str:
    """Get database URL from config."""
    return db_config["url"]


@pytest.fixture
def db_user(db_config: dict[str, str]) -> str:
    """Get database user from config."""
    return db_config["user"]


@pytest.fixture
def db_password(db_config: dict[str, str]) -> str:
    """Get database password from config."""
    return db_config["password"]


@pytest.fixture
def db_name(db_config: dict[str, str]) -> str:
    """Get database name from config."""
    return db_config["name"]


@pytest.fixture
def db_namespace(db_config: dict[str, str]) -> str:
    """Get database namespace from config."""
    return db_config["namespace"]


@pytest.fixture
def sample_wav_file(tmp_path: Path) -> Path:
    """Create a temporary WAV file path for testing.

    Note: This doesn't create an actual WAV file, just a path.
    Tests should create the file if needed.
    """
    return tmp_path / "test_audio.wav"


@pytest.fixture
def sample_coda_json() -> dict[str, Any]:
    """Sample Coda JSON data for testing imports."""
    return {
        "items": [
            {
                "values": {
                    "YouTube": "https://www.youtube.com/watch?v=TEST12345AB",
                    "Unique event name": "Test Event",
                    "Title or name of stream": "Test Stream",
                }
            }
        ]
    }
