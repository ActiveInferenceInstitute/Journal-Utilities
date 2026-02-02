# AGENTS.md - Tests

## Test Suite Overview

35 tests across unit and integration suites.

## Running Tests

```bash
# All tests
uv run pytest tests/ -v

# Unit tests only (no API keys needed)
uv run pytest tests/journalrag/unit/ -v

# Integration tests (requires COHERE_API_KEY)
uv run pytest tests/journalrag/integration/ -v -s
```

## Key Fixtures

From `tests/conftest.py`:

- `fixtures_dir` - Path to test fixtures
- `sample_transcript_file` - Sample transcript for testing
- `images_dir` - Test images directory

From `tests/journalrag/conftest.py`:

- `sample_concept` - Test Concept model
- `sample_researcher` - Test Researcher model
- `sample_citation` - Test Citation model
- `sample_core_entities` - Full CoreEntities example

## Test Patterns

**Unit tests use mocks:**

```python
from unittest.mock import AsyncMock, patch

@patch("journalrag.graph.SurrealDBClient")
async def test_pipeline(mock_client):
    mock_client.return_value.connect = AsyncMock()
    # ...
```

**Integration tests use real APIs:**

```python
async def test_real_extraction():
    extractor = CohereExtractor()  # Uses real API key from .env
    result = extractor.extract_core_entities(transcript)
    # ...
```

## Adding Tests

1. Unit tests: `tests/journalrag/unit/test_*.py`
2. Integration tests: `tests/journalrag/integration/test_*.py`
3. Journal utilities tests: `tests/journal_utilities/test_*.py`
