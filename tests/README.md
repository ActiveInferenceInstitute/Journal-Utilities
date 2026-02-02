# Tests

Test suite for Journal-Utilities (35 tests).

## Running Tests

```bash
# All tests
uv run pytest tests/ -v

# With coverage
uv run pytest tests/ -v --cov=src --cov-report=term-missing

# Specific package
uv run pytest tests/journal_utilities/ -v
uv run pytest tests/journalrag/ -v
```

## Test Structure

```
tests/
├── conftest.py              # Shared fixtures
├── fixtures/                # Test data files
│   └── sample_transcript.txt
├── images/                  # Test images
├── journal_utilities/       # Transcription tests
│   ├── test_audit_functions.py
│   └── test_transcribe.py
└── journalrag/              # Entity extraction tests
    ├── unit/                # Fast, no API calls
    │   ├── test_models.py
    │   └── test_pipeline.py
    └── integration/         # Real API calls
        └── test_pipeline_integration.py
```

## Test Categories

### Unit Tests (No API Keys)

- Model validation
- Pipeline logic (mocked extractors)
- Audit functions (mocked DB)
- Transcription output formatting

### Integration Tests (Require API Keys)

- Real Cohere extraction
- End-to-end pipeline with file loading

Run integration tests:

```bash
uv run pytest tests/journalrag/integration/ -v -s
```

## Coverage

35 tests covering:

- 7 journal_utilities tests
- 28 journalrag tests (17 unit + 3 integration)
