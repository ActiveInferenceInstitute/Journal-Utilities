# AGENTS.md - Tests

## Test Suite Overview

The suite is a live snapshot (currently ~466 passing, 3 API-gated skips); run
`uv run pytest tests/ -q` for the current count.

## Running Tests

```bash
# All tests
uv run pytest tests/ -v

# Unit tests only (no API keys needed)
uv run pytest tests/journal_utilities/rag/unit/ -v

# Integration tests (requires COHERE_API_KEY)
uv run pytest tests/journal_utilities/rag/integration/ -v -s
```

## Key Fixtures

From `tests/conftest.py`:

- `fixtures_dir` - Path to test fixtures
- `sample_transcript_file` - Sample transcript for testing
- `images_dir` - Test images directory

From `tests/journal_utilities/conftest.py`:

- `sample_transcript` - Sample transcript text

From `tests/journal_utilities/rag/conftest.py`:

- `sample_concept` - Test Concept model
- `sample_researcher` - Test Researcher model
- `sample_citation` - Test Citation model
- `sample_core_entities` - Full CoreEntities example

## Test Patterns

**Unit tests use mocks where needed:**

```python
from unittest.mock import AsyncMock, patch

@patch("journal_utilities.rag.graph.SurrealDBClient")
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

1. Pipeline tests: `tests/journal_utilities/test_*.py`
2. RAG unit tests: `tests/journal_utilities/rag/unit/test_*.py`
3. RAG integration tests: `tests/journal_utilities/rag/integration/test_*.py`
