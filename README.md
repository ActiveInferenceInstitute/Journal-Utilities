# Journal-Utilities
Utilities and Documentation for creating contents for the Active Inference Journal
https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal

This repository provides a local transcription pipeline using WhisperX with SurrealDB for storage and retrieval.

---
## WhisperX Transcription Pipeline

## Installation

### Prerequisites

1. Install [uv](https://github.com/astral-sh/uv) - Fast Python package installer
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Ensure CUDA 11.8 is installed for GPU support (optional but recommended)

### Setup with uv

```bash
# Clone the repository
git clone https://github.com/ActiveInferenceInstitute/Journal-Utilities.git
cd Journal-Utilities

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all dependencies including PyTorch with CUDA support
uv pip install -e .
# For CUDA 11.8 support (optional, for GPU acceleration)
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For development
uv pip install -e ".[dev]"
```

### Alternative: Conda Setup (Legacy)

If you prefer using Conda:
```bash
conda create --name whisperx python=3.10
conda activate whisperx
conda install pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
uv pip install -e .
```

### Install ffmpeg
```bash
wget -O - -q  https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz | xz -qdc| tar -x
```

### Setup .env file

1. [Generate a Hugging Face Token](https://huggingface.co/settings/tokens) and accept the user agreement for the following models:
   - [Segmentation](https://huggingface.co/pyannote/segmentation-3.0)
   - [Speaker-Diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)

2. Get the YouTube Data API v3 Key from https://console.developers.google.com/apis/
3. Get Your Coda API Token at https://coda.io/account, scroll to "API settings," and generate an API token.

4. Configure environment variables:
```bash
cp .env.sample .env
```

Update the following values in `.env`:
- `HUGGINGFACE_TOKEN`: Your Hugging Face token
- `API_KEY`: Your YouTube Data API v3 key
- `WAV_DIRECTORY`: Directory for WAV file storage
- `OUTPUT_DIR`: Output directory for processed files
- `JOURNAL_REPO_DIR`: Path to Active Inference Journal repository
- `CODA_API_TOKEN`: Your Coda API token (for fetching session data)

## Usage

### Complete Workflow

The typical workflow consists of these steps:

```bash
# 1. Start the database
make db-start

# 2. Fetch latest data from Coda API
make fetch-coda

# 3. Import sessions into SurrealDB (with audit trail)
make import-sessions

# 4. Fetch metadata from YouTube API
make fetch-metadata

# 5. Run WhisperX transcription
make transcribe

# 6. Copy processed files to journal repository
make copy-to-journal
```

### Individual Steps

#### Fetch Data from Coda
```bash
make fetch-coda
```
Downloads the latest session data from Coda API. The JSON file can be formatted in VS Code with `Format Document` for better readability.

#### Import Sessions
```bash
make import-sessions
# Or with custom JSON file:
python src/ingest_db_create_wav.py --step import --json /path/to/file.json
```
Imports sessions with full audit trail tracking. Use rollback functions if needed.

#### Fetch YouTube Metadata
```bash
make fetch-metadata
```
Any "private video" failures should be added to `src/private_videos.json` to skip youtube metadata fetching and transcription.

#### Run Transcription
```bash
make transcribe
```
This script:
- Loads WAV files from the database
- Performs transcription using WhisperX
- Applies speaker diarization and alignment
- Stores results back in SurrealDB

#### Copy to Journal
```bash
make copy-to-journal
```
Organizes transcripts by category/series/episode in the journal repository.

### Query Database
```bash
surreal sql --endpoint http://localhost:8080 --username root --password root --namespace actinf --database actinf
```

Example queries:
```sql
-- View all sessions
SELECT * FROM session;

-- View transcribed sessions
SELECT * FROM session WHERE transcribed = true;

-- View sessions pending transcription
SELECT * FROM session WHERE transcribed = false AND is_private != true;

-- View specific session by name
SELECT * FROM session WHERE session_name = 'video_id';

-- View import audit trail
SELECT * FROM import_audit ORDER BY timestamp DESC LIMIT 10;

-- View recent import summary
SELECT * FROM import_audit WHERE operation = 'import_summary' ORDER BY timestamp DESC;
```

### Database Maintenance
```bash
# Upgrade SurrealDB
sudo surreal upgrade

# Fix database after upgrade
surreal fix rocksdb://database
```

## Testing

Run unit tests:
```bash
python -m unittest tests.test_output_final_artifacts
python -m unittest tests.test_transcript
```

## Project Structure

```
Journal-Utilities/
├── src/                     # Main transcription pipeline
│   ├── ingest_db_create_wav.py  # Multi-step ingestion with CLI
│   ├── transcribe.py            # WhisperX transcription
│   ├── output_final_artifacts.py # Process final outputs
│   └── private_videos.json      # List of private video IDs
├── tests/                   # Unit tests
├── data/                    # Database and output files
│   ├── database/           # SurrealDB storage
│   ├── input/              # Input data files (Coda JSON)
│   └── output/             # Processed outputs
├── Archive/                 # Archived AssemblyAI tools
│   ├── 1_youtube_to_audio/
│   ├── 2_audio_to_markdown/
│   ├── 5_markdown_to_final/
│   └── ...
├── Makefile                # Workflow automation
├── CLAUDE.md               # Documentation for Claude Code
├── README.md               # This file
├── .env.sample             # Environment configuration template
└── pyproject.toml          # Python package configuration
```

## Archived Components

The AssemblyAI-based transcription tools have been moved to the `Archive/` directory. These legacy tools provided cloud-based transcription with features like custom vocabulary boosting, spell checking, and document conversion. They remain available for historical reference but are no longer actively maintained.

## Acknowledgements

- WhisperX transcription pipeline and SurrealDB integration contributed by Holly Grimm @hollygrimm, 2024
- Initial AssemblyAI scripts and documentation contributed by Dave Douglass, November 2022


