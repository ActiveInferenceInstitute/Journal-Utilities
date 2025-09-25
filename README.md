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

3. Configure environment variables:
```bash
cp .env.sample .env
```

Update the following values in `.env`:
- `HUGGINGFACE_TOKEN`: Your Hugging Face token
- `API_KEY`: Your YouTube Data API v3 key
- `WAV_DIRECTORY`: Directory for WAV file storage
- `OUTPUT_DIR`: Output directory for processed files
- `JOURNAL_REPO_DIR`: Path to Active Inference Journal repository

## Usage

### Start Database
```bash
surreal start --log trace --user root --pass root --bind 0.0.0.0:8080 rocksdb:///mnt/md0/projects/Journal-Utilities/data/database
```

### Process MP4 Files and Create WAV Files
```bash
cd src
python ingest_db_create_wav.py
```
This script:
- Reads MP4 files from the configured directory
- Extracts metadata using YouTube Data API
- Stores information in SurrealDB
- Converts MP4 files to WAV format for transcription

### Run Transcription
```bash
cd src
python transcribe.py
```
This script:
- Loads WAV files from the database
- Performs transcription using WhisperX
- Applies speaker diarization and alignment
- Stores results back in SurrealDB

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
SELECT * FROM session WHERE transcribed = false;

-- View specific session by name
SELECT * FROM session WHERE session_name = 'video_id';
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
│   ├── ingest_db_create_wav.py
│   └── transcribe.py
├── tests/                   # Unit tests
├── data/                    # Database and output files
│   ├── database/           # SurrealDB storage
│   ├── input/              # Input data files
│   └── output/             # Processed outputs
├── Archive/                 # Archived AssemblyAI tools
│   ├── 1_youtube_to_audio/
│   ├── 2_audio_to_markdown/
│   ├── 5_markdown_to_final/
│   └── ...
├── CLAUDE.md               # Documentation for Claude Code
├── README.md               # This file
└── .env.sample             # Environment configuration template
```

## Archived Components

The AssemblyAI-based transcription tools have been moved to the `Archive/` directory. These legacy tools provided cloud-based transcription with features like custom vocabulary boosting, spell checking, and document conversion. They remain available for historical reference but are no longer actively maintained.

## Acknowledgements

- WhisperX transcription pipeline and SurrealDB integration contributed by Holly Grimm @hollygrimm, 2024
- Initial AssemblyAI scripts and documentation contributed by Dave Douglass, November 2022


