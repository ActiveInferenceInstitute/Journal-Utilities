# AGENTS.md

This file provides guidance to AI coding agents working with this repository.

## Project Overview

Journal-Utilities is a two-pipeline system for processing Active Inference Journal content:

1. **Transcription Pipeline** (`journal_utilities/`) - WhisperX-based local transcription with SurrealDB storage
2. **Entity Extraction Pipeline** (`journalrag/`) - Cohere AI-powered entity and relationship extraction

## Quick Start Commands

```bash
# Setup
uv sync --all-extras

# Run tests
uv run pytest tests/ -v

# Start database
make db-start

# Complete transcription workflow
make fetch-coda && make import-sessions && make fetch-metadata && make transcribe && make copy-to-journal

# Entity extraction
make extract-entities
```

## Architecture

```
src/
├── journal_utilities/     # Transcription pipeline
│   ├── ingest_db_create_wav.py  # Data ingestion with audit trail
│   └── transcribe.py            # WhisperX transcription
└── journalrag/            # Entity extraction pipeline
    ├── main.py            # Pipeline orchestrator
    ├── extractors/        # Cohere AI extraction
    ├── graph/             # SurrealDB client
    ├── models/            # Pydantic entity models
    ├── schemas/           # JSON schemas for extraction
    └── adapters/          # Entity format conversion
```

## Key Entry Points

| Task | Command | Main File |
|------|---------|-----------|
| Import sessions | `make import-sessions` | `src/journal_utilities/ingest_db_create_wav.py` |
| Transcription | `make transcribe` | `src/journal_utilities/transcribe.py` |
| Entity extraction | `make extract-entities` | `src/journalrag/main.py` |

## Testing

- **35 tests** across unit and integration suites
- Unit tests run without API keys (use mocks where needed)
- Integration tests require `COHERE_API_KEY` for real API calls

```bash
# Run all tests
uv run pytest tests/ -v

# Run only unit tests
uv run pytest tests/journalrag/unit/ -v

# Run integration tests (requires API key)
uv run pytest tests/journalrag/integration/ -v -s
```

## Environment Variables

Required in `.env` (copy from `.env.example`):

- `HUGGINGFACE_TOKEN` - For WhisperX speaker diarization
- `API_KEY` - YouTube Data API v3
- `CODA_API_TOKEN` - Coda session data
- `COHERE_API_KEY` - Entity extraction

## Database

SurrealDB stores all session and entity data:

```bash
# Query database
surreal sql --endpoint http://localhost:8080 --username root --password root --namespace actinf --database actinf
```

## Code Patterns

- **Async-first**: Database operations use `asyncio`
- **Pydantic models**: Type-safe entity definitions
- **Structured logging**: Uses `structlog` with rich output
- **Audit trail**: All imports tracked with rollback capability
