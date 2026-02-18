# Tests

Test suite for Journal-Utilities (272 tests).

## Running Tests

```bash
# All tests
uv run pytest tests/ -v

# With coverage
uv run pytest tests/ -v --cov=src --cov-report=term-missing

# Specific suites
uv run pytest tests/journal_utilities/ -v            # Download + transcription pipeline
uv run pytest tests/journal_utilities/rag/ -v        # Entity extraction (RAG)
uv run pytest tests/journal_utilities/rag/unit/ -v   # RAG unit tests only
```

## Test Structure

```
tests/
├── conftest.py                          # Shared fixtures
├── fixtures/                            # Test data files
│   └── sample_transcript.txt
├── images/                              # Test images
├── journal_utilities/                   # Pipeline + download tests
│   ├── conftest.py                      # Transcript fixtures
│   ├── test_audit_functions.py          # Import audit trail
│   ├── test_categorizer.py              # Event categorization
│   ├── test_channel.py                  # Channel enumeration
│   ├── test_database.py                 # Database client
│   ├── test_downloader.py               # Download logic
│   ├── test_importer.py                 # Session import
│   ├── test_playlist.py                 # Playlist enumeration
│   ├── test_renderer.py                 # Course scaffolding
│   ├── test_transcribe.py               # WhisperX transcription
│   ├── test_transcriber.py              # Local Whisper transcription
│   ├── test_youtube.py                  # YouTube URL utilities
│   └── rag/                             # Entity extraction tests
│       ├── conftest.py                  # Entity model fixtures
│       ├── unit/                        # No API calls needed
│       │   ├── test_cohere_extractor.py # Extractor logic
│       │   ├── test_entity_adapter.py   # Format conversion
│       │   ├── test_models.py           # Pydantic validation
│       │   ├── test_pipeline.py         # Pipeline flow
│       │   └── test_surreal_client.py   # DB client logic
│       └── integration/                 # Requires API keys
│           └── test_pipeline_integration.py
```

## Test Categories

### Unit Tests (No API Keys)

- Model validation (Pydantic entity models)
- Pipeline logic (mocked extractors)
- Audit trail functions (mocked DB)
- Transcription output formatting
- Download and channel enumeration
- Playlist management
- Course scaffolding and rendering
- YouTube URL parsing and categorization

### Integration Tests (Require API Keys)

- Real Cohere extraction (`COHERE_API_KEY`)
- End-to-end pipeline with file loading

Run integration tests:

```bash
uv run pytest tests/journal_utilities/rag/integration/ -v -s
```

## Coverage

272 tests covering:

- 12 journal_utilities tests (download, transcription, categorization, etc.)
- 5 RAG unit tests (models, extractors, pipeline, adapters, DB client)
- Integration tests (Cohere extraction pipeline)
