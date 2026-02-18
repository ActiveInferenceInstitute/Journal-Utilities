# Journal Utilities Tests

Tests for the download, transcription, and categorization pipeline.

## Test Files

### `test_categorizer.py`

Video categorization by stream type, project meetings, textbook groups, edge cases.

### `test_youtube.py`

YouTube URL parsing — ID extraction, format validation, private video detection.

### `test_database.py`

Mock-based SurrealDB client tests — connection, session operations, rollback, audit trail.

### `test_importer.py`

Session import tests — JSON parsing (dict/list), audit tracking, error handling.

### `test_audit_functions.py`

Import audit trail tests (requires DB) — recent imports, summaries, failures.

### `test_transcribe.py`

Transcription output formatting — single speaker, multi-speaker, empty input.

### `test_channel.py`

Channel enumeration and playlist discovery.

### `test_downloader.py`

Download logic — audio/video download, skip-existing, error handling.

### `test_playlist.py`

Playlist enumeration and video listing.

### `test_renderer.py`

Course scaffolding — module.md generation, directory structure.

### `test_transcriber.py`

Local Whisper transcription — model loading, audio processing.

## Running

```bash
# Run all tests (no DB required)
uv run pytest tests/journal_utilities/ -v --ignore=tests/journal_utilities/test_audit_functions.py

# Run with coverage
uv run pytest tests/journal_utilities/ -v --cov=journal_utilities

# Run specific test file
uv run pytest tests/journal_utilities/test_categorizer.py -v
```

## Test Coverage

| Module | Coverage |
|--------|----------|
| categorizer.py | 94% |
| importer.py | 89% |
| database.py | 47% |
| youtube.py | 36% |

## Fixtures

See `tests/journal_utilities/conftest.py` for test fixtures including sample database mocks.
