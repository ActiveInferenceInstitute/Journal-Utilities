# Source Code (`src/`)

This directory contains the two main Python packages that power Journal-Utilities.

## Packages

### `journal_utilities/`

**WhisperX Transcription Pipeline**

Local transcription of YouTube videos using WhisperX with speaker diarization. Stores metadata and transcripts in SurrealDB.

- `ingest_db_create_wav.py` - Session import, metadata fetch, file organization
- `transcribe.py` - WhisperX transcription with alignment and diarization
- `fix_scheduled_dates.py` - Date correction utilities

### `journalrag/`

**Entity Extraction Pipeline (JournalRAG)**

Cohere AI-powered entity extraction from transcripts. Extracts concepts, researchers, citations, and technical terms into a graph structure.

- `main.py` - Pipeline orchestrator
- `extractors/` - Cohere extraction logic
- `graph/` - SurrealDB graph client
- `models/` - Pydantic entity models
- `schemas/` - JSON schemas for extraction
- `adapters/` - Entity format adapters
- `utils/` - Logging utilities

## Data Flow

```
Coda API → JSON → SurrealDB (sessions)
                         ↓
YouTube API → Metadata → SurrealDB
                         ↓
MP4 → WAV → WhisperX → Transcripts → SurrealDB
                                          ↓
                    Cohere AI → Entities → SurrealDB (graph)
```

## Usage

```bash
# Transcription pipeline
make transcribe

# Entity extraction
make extract-entities
```
