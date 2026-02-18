# AGENTS.md - Journal Utilities

## Module Purpose

Transcription pipeline, playlist enumeration, and course scaffolding for Active Inference Journal videos.

## Key Files

| File | Purpose |
| --- | --- |
| `data/database.py` | Database connection, audit trails |
| `data/importer.py` | Session import with audit logging |
| `transcribe/transcribe.py` | WhisperX transcription service (GPU) |
| `transcribe/transcriber.py` | Local Whisper transcription (Apple Silicon) |
| `youtube/playlist.py` | Playlist enumeration, manifest management |
| `render/renderer.py` | Course scaffolding, module.md rendering |
| `download/downloader.py` | YouTube download logic |
| `interface/app.py` | FastAPI web server + REST API |
| `interface/data_loader.py` | Video manifest builder from `data/output/` |
| `interface/chat_engine.py` | Ollama RAG chat engine |
| `export/exporter.py` | Multi-format transcript export |
| `rag/main.py` | Entity extraction pipeline orchestrator |

## Entry Points

```bash
# Channel Download (New)
python scripts/download_channel.py --transcripts --audio --resume --transcribe-missing

# Local Transcription (Standalone)
python scripts/transcribe_missing.py

# Legacy Operations (via Makefile)
make fetch-coda        # Get Coda data
make import-sessions   # Import to DB
make fetch-metadata    # YouTube metadata
make transcribe        # Run WhisperX transcription (GPU)
make copy-to-journal   # Export transcripts

# Web Interface
uv run python run.py serve  # http://localhost:8000
# Or: journal-ui
```

## Database Operations

All operations use async SurrealDB:

```python
async with AsyncSurreal(db_url) as db:
    await db.signin({"user": user, "pass": password})
    await db.use(namespace, database)
    result = await db.query("SELECT * FROM session")
```

## Audit Functions

```python
# Get recent imports
runs = await get_recent_import_runs(db_url, ...)

# Rollback failed import
await rollback_import(import_run_id, db_url, ...)

# Get import summary
summary = await get_import_summary(import_run_id, db_url, ...)
```

## Testing

```bash
uv run pytest tests/journal_utilities/ -v
```

Tests cover:

- Database and audit trail functions
- Web interface endpoints (FastAPI)
- Data loader and search index
- Chat engine (Ollama RAG)
- Transcription output formatting
- Playlist enumeration and manifest persistence
- Course scaffolding and module.md rendering
- Multi-format export (plaintext, PDF, Markdown, JSON, HTML)
- Video categorization
