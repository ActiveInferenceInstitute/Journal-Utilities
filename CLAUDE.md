# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Journal-Utilities is a Python-based transcription and processing pipeline for the Active Inference Journal using WhisperX for local transcription with SurrealDB for storage.

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
python -m unittest tests.test_output_final_artifacts
python -m unittest tests.test_transcript
```

### Transcription Workflow

**WhisperX workflow:**
```bash
cd src
python ingest_db_create_wav.py  # Process MP4 files and create WAV files
python transcribe.py             # Run transcription with WhisperX
```

## Architecture Overview

The project focuses on a streamlined local transcription pipeline:

### Database Integration (`src/`)
- **ingest_db_create_wav.py**: Processes MP4 files, extracts metadata from YouTube, stores in SurrealDB, and converts to WAV
- **transcribe.py**: Manages WhisperX transcription with alignment and diarization, updates database with results

### Data Flow
1. YouTube/MP4 files → WAV files
2. WAV files → WhisperX transcription
3. Transcription results → SurrealDB storage
4. Database → Query and retrieval for further processing

## Key Configuration

Environment variables (`.env`):
- `HUGGINGFACE_TOKEN`: Required for WhisperX speaker diarization
- `API_KEY`: YouTube Data API v3 key for metadata retrieval
- `DB_URL`: SurrealDB connection URL (ws://0.0.0.0:8080/rpc)
- `DB_USER`, `DB_PASSWORD`: Database credentials
- `DB_NAME`, `DB_NAMESPACE`: Database and namespace (actinf)
- `WAV_DIRECTORY`: Directory for WAV file storage
- `OUTPUT_DIR`: Output directory for processed files
- `JOURNAL_REPO_DIR`: Active Inference Journal repository path

## External Dependencies

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