# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Journal-Utilities is a Python-based transcription and processing pipeline for the Active Inference Journal using WhisperX for local transcription with SurrealDB for storage. The system processes YouTube videos from the Active Inference Institute, storing metadata in SurrealDB and generating transcripts for the Active Inference Journal.

Note: The AssemblyAI-based transcription tools have been archived and are no longer actively used. They can be found in the `Archive/` directory for historical reference.

## Development Commands

### Environment Setup

Using uv (recommended):
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -e .
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For development
uv pip install -e ".[dev]"
```

### Database Operations

Start SurrealDB:
```bash
surreal start --log trace --user root --pass root --bind 0.0.0.0:8080 rocksdb:///mnt/md0/projects/Journal-Utilities/data/database
```

Query database:
```bash
surreal sql --endpoint http://localhost:8080 --username root --password root --namespace actinf --database actinf
```

### Running Tests

Tests use unittest framework:
```bash
make test  # Run all tests
# Or manually:
python -m unittest tests.test_output_final_artifacts
python -m unittest tests.test_transcript
```

### Complete Workflow

The project now has a streamlined workflow with Makefile commands:

```bash
# Step 1: Fetch latest data from Coda API
make fetch-coda

# Step 2: Import sessions from JSON to database
make import-sessions

# Step 3: Fetch YouTube metadata for sessions
make fetch-metadata

# Step 4: Run WhisperX transcription
make transcribe

# Step 5: Copy transcripts to journal repository
make copy-to-journal
```

### Individual Script Usage

**ingest_db_create_wav.py** now supports command-line arguments:
```bash
# Import sessions from Coda JSON
python src/ingest_db_create_wav.py --step import

# Fetch YouTube metadata
python src/ingest_db_create_wav.py --step metadata

# Copy to journal repository
python src/ingest_db_create_wav.py --step copy

# Run all steps (except transcription)
python src/ingest_db_create_wav.py --step all

# Use a different JSON file
python src/ingest_db_create_wav.py --step import --json /path/to/file.json
```

**transcribe.py** runs the WhisperX transcription:
```bash
python src/transcribe.py
```

## Architecture Overview

The project focuses on a streamlined local transcription pipeline:

### Core Scripts (`src/`)

- **ingest_db_create_wav.py**: Multi-function script with command-line interface
  - `--step import`: Import sessions from Coda JSON with full audit trail
  - `--step metadata`: Fetch YouTube metadata via API
  - `--step copy`: Copy transcripts to journal repository structure
  - Includes audit functions: `rollback_import()`, `get_import_summary()`, `get_failed_imports()`
  - Private video detection via `private_videos.json`

- **transcribe.py**: WhisperX transcription with alignment and diarization
- **output_final_artifacts.py**: Process transcripts into final formats

### Data Flow
1. Coda API → JSON export with session data
2. JSON → SurrealDB (with audit trail)
3. YouTube API → Video metadata enrichment
4. MP4 files → WAV extraction → WhisperX transcription
5. Transcripts → Journal repository (organized by category/series/episode)

## Key Configuration

Environment variables (`.env`):
- `CODA_API_TOKEN`: Coda API token for fetching session data
- `HUGGINGFACE_TOKEN`: Required for WhisperX speaker diarization
- `API_KEY`: YouTube Data API v3 key for metadata retrieval
- `DB_URL`: SurrealDB connection URL (ws://0.0.0.0:8080/rpc)
- `DB_USER`, `DB_PASSWORD`: Database credentials
- `DB_NAME`, `DB_NAMESPACE`: Database and namespace (actinf)
- `WAV_DIRECTORY`: Directory for WAV file storage
- `OUTPUT_DIR`: Output directory for processed files
- `JOURNAL_REPO_DIR`: Active Inference Journal repository path

## Recent Updates (2024)

- **Removed old CSV-based utilities**: Cleaned up deprecated functions for CSV processing
- **Added Coda API integration**: Direct fetch from Coda API via Makefile
- **Parameterized main script**: Command-line arguments for flexible execution
- **Enhanced Makefile**: Separate commands for each workflow step
- **Import audit trail**: Full tracking of import operations with rollback capability
- **Private video detection**: Automatic marking of private videos via `private_videos.json`

## External Dependencies

- **Coda API**: Source of session/event data
- **Hugging Face models**: pyannote models for speaker diarization
- **SurrealDB**: Database for storing transcription metadata
- **WhisperX**: Local transcription with speaker diarization
- **YouTube Data API v3**: Video metadata retrieval
- **FFmpeg**: Audio/video processing

## Archived Components

The following AssemblyAI-based components have been moved to `Archive/`:
- `1_youtube_to_audio/`: YouTube to audio conversion tools
- `2_audio_to_markdown/`: AssemblyAI transcription submission and processing
- `5_markdown_to_final/`: Markdown to final output conversion
- `May_2023_testing/`: Historical testing scripts
- `docs/`: Original documentation

These archived tools used AssemblyAI API for cloud-based transcription and included features for:
- Custom vocabulary boosting
- Spell checking
- Sentiment analysis
- IAB categorization
- Document conversion to PDF/HTML using Pandoc

For historical reference or if you need to use these tools, they remain available in the Archive directory.