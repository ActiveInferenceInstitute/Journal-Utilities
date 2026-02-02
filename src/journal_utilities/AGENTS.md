# AGENTS.md - Journal Utilities

## Module Purpose

Transcription pipeline for Active Inference Journal videos using WhisperX.

## Key Files

| File | Purpose |
|------|---------|
| `ingest_db_create_wav.py` | Data import, metadata, file organization |
| `transcribe.py` | WhisperX transcription service |
| `fix_scheduled_dates.py` | Date correction utility |

## Entry Points

```bash
# Via Makefile (recommended)
make fetch-coda        # Get Coda data
make import-sessions   # Import to DB
make fetch-metadata    # YouTube metadata
make transcribe        # Run transcription
make copy-to-journal   # Export transcripts
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

- Audit trail functions
- Transcription output formatting
