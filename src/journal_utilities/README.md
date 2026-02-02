# Journal Utilities - Transcription Pipeline

WhisperX-based local transcription pipeline for Active Inference Journal videos.

## Overview

This package handles the complete transcription workflow:

1. **Import** - Fetch session data from Coda API and import to SurrealDB
2. **Metadata** - Enrich with YouTube metadata via API
3. **Transcribe** - Local WhisperX transcription with speaker diarization
4. **Export** - Copy organized transcripts to journal repository

## Modular Components

### `database.py`

Modular database client for SurrealDB operations:

```python
from journal_utilities.database import DatabaseClient

async with DatabaseClient() as db:
    await db.insert_session(session_data)
    summary = await db.get_import_summary()
```

**Features:**

- Async context manager for connection management
- Session import with audit trail
- Import rollback capability
- Statistics and summary queries

### `categorizer.py`

Pattern matching for event categorization:

```python
from journal_utilities.categorizer import categorize_event, get_category_patterns

category = categorize_event("ActInf GuestStream 2024")  # Returns "Guest_Stream"
patterns = get_category_patterns()
```

**Supported Categories:**

- Guest_Stream, Roundtable, Livestream
- Textbook_Group, Research_Papers
- Project meetings (Math, Research, Social, etc.)

### `youtube.py`

YouTube utilities for ID extraction and metadata:

```python
from journal_utilities.youtube import extract_youtube_id, YOUTUBE_ID_PATTERN

video_id = extract_youtube_id("https://youtu.be/abc123_XYZ")
```

### `importer.py`

Session import from Coda JSON exports:

```python
from journal_utilities.importer import import_sessions_from_json

async with DatabaseClient() as db:
    stats = await import_sessions_from_json(db, "data/coda_export.json")
```

---

## Original Scripts

### `ingest_db_create_wav.py`

Multi-function script for data management:

```bash
# Import sessions from Coda JSON
python ingest_db_create_wav.py --step import

# Fetch YouTube metadata
python ingest_db_create_wav.py --step metadata

# Copy to journal repository
python ingest_db_create_wav.py --step copy

# Run all steps
python ingest_db_create_wav.py --step all
```

### `transcribe.py`

WhisperX transcription service:

```python
from journal_utilities.transcribe import TranscriptionService

service = TranscriptionService(hf_token, device="cuda", batch_size=48)
service.transcribe(output_dir, audio_file)
```

**Features:**

- GPU-accelerated transcription (CUDA)
- Speaker diarization via pyannote
- Word-level alignment
- JSON and TXT output formats

### `fix_scheduled_dates.py`

Utility for correcting scheduled dates in the database.

## Requirements

- **Hugging Face Token** - For pyannote speaker diarization models
- **YouTube API Key** - For metadata fetching
- **Coda API Token** - For session data
- **SurrealDB** - Running database instance
- **CUDA** - For GPU acceleration (optional but recommended)

## Database Schema

Sessions are stored with:

- `session_name` - YouTube video ID
- `title` - Video title
- `scheduled_date` - Event date
- `transcribed` - Transcription status
- `is_private` - Private video flag

## Audit Trail

All imports are tracked in `import_audit` table:

- Operation timestamps
- Success/failure status
- Rollback capability
