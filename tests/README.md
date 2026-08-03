# Tests

Test suite for Journal-Utilities (currently 475 passed / 3 skipped, snapshot of
`uv run pytest tests/ -q` on 2026-08-02). The count
is a live snapshot of the suite — run `uv run pytest tests/ -q` for the current
number; it is intentionally not kept hardcoded elsewhere in the docs.

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
│   ├── test_apply_speaker_names.py      # Journal transcript derivation
│   ├── test_app.py                      # FastAPI endpoints
│   ├── test_audit_functions.py          # Import audit trail
│   ├── test_categorizer.py              # Event categorization
│   ├── test_channel.py                  # Channel enumeration
│   ├── test_chat_engine.py              # Ollama chat engine
│   ├── test_coda_client.py              # Coda API client
│   ├── test_data_loader.py              # Video manifest / search
│   ├── test_database.py                 # Database client
│   ├── test_downloader.py               # Download logic
│   ├── test_enrichment.py               # Metadata enrichment
│   ├── test_exporter.py                 # Multi-format export
│   ├── test_importer.py                 # Session import
│   ├── test_journal_indexes.py          # INDEX.json / INDEX.md derivation
│   ├── test_naming.py                   # Slug generation
│   ├── test_playlist.py                 # Playlist enumeration
│   ├── test_renderer.py                 # Course scaffolding
│   ├── test_run.py                      # run.py pipeline runner
│   ├── test_transcribe.py               # WhisperX transcription
│   ├── test_transcribe_worklist.py      # Journal transcription worklist
│   ├── test_transcriber.py              # Local Whisper transcription
│   ├── test_transcript_repair.py        # Split-transcript repair
│   ├── test_validate_journal.py         # Journal integrity gate
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
- Journal index derivation, transcript repair, and the integrity gate

### Integration Tests (Require API Keys)

- Real Cohere extraction (`COHERE_API_KEY`)
- End-to-end pipeline with file loading

Run integration tests:

```bash
uv run pytest tests/journal_utilities/rag/integration/ -v -s
```

## Coverage

The suite runs with coverage against `src` by default
(`--cov=src --cov-report=term-missing`). Per-package line coverage changes as
the suite evolves; run `uv run pytest tests/ --cov-report=term-missing` to see
the live numbers.
