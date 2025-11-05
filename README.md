# Journal-Utilities
Utilities and Documentation for creating contents for the Active Inference Journal
https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal

This repository provides a complete pipeline for processing Active Inference Journal content:
- **Transcription**: Local transcription pipeline using WhisperX
- **Entity Extraction**: Extract entities and relationships from transcripts using Cohere AI
- **Graph Storage**: Store and query data in SurrealDB graph database

---
## WhisperX Transcription Pipeline

## Installation

### Prerequisites

1. Install [uv](https://github.com/astral-sh/uv) - Fast Python package installer
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Ensure CUDA 12.8 is installed for GPU support (optional but recommended)

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
# For CUDA 12.8 support (required for GPU acceleration)
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# Install cuDNN 8 (required for pyannote speaker embeddings)
sudo apt install libcudnn8 libcudnn8-dev -y
sudo ldconfig

# For development
uv pip install -e ".[dev]"
```

**Note:** After installation, you'll need to apply compatibility patches to WhisperX for pyannote.audio 4.0+. Run:
```bash
python scripts/patch_whisperx.py
```

### Install ffmpeg
```bash
wget -O - -q  https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz | xz -qdc| tar -x
```

### Setup .env file

1. [Generate a Hugging Face Token](https://huggingface.co/settings/tokens) and accept the user agreement for the following models:
   - [Segmentation](https://huggingface.co/pyannote/segmentation-3.0)
   - [Speaker-Diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)
   - [Speaker-Diarization-Community-1](https://hf.co/pyannote/speaker-diarization-community-1) (for speaker embeddings)

2. Get the YouTube Data API v3 Key from https://console.developers.google.com/apis/
3. Get Your Coda API Token at https://coda.io/account, scroll to "API settings," and generate an API token.

4. Configure environment variables:
```bash
cp .env.example .env
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

---
## Entity Extraction Pipeline (JournalRAG)

### Overview

The entity extraction pipeline uses Cohere AI to analyze transcripts and extract:
- **Entities**: People, organizations, concepts, theories, methodologies, publications, events, and locations
- **Relationships**: Connections between entities (collaborations, studies, applications, etc.)

All extracted data is stored in the SurrealDB graph database for semantic queries and analysis.

### Entity Types

- **Person**: Researchers, contributors, speakers
- **Organization**: Institutions, research groups
- **Concept**: Theoretical concepts, ideas
- **Theory**: Formal theories, frameworks
- **Methodology**: Research methods, approaches
- **Publication**: Papers, books, articles
- **Event**: Conferences, workshops, meetings
- **Location**: Physical or virtual locations

### Relationship Types

- `collaborates_with`: Between persons or organizations
- `studies`: Person studying a concept/theory
- `applies`: Application of methodology/theory
- `extends`: One theory extending another
- `member_of`: Person member of organization
- `located_at`: Entity at a location
- `publishes`: Publication relationships

### Usage

#### Process a Transcript for Entity Extraction

```python
import asyncio
from pathlib import Path
from journalrag.main import JournalRAGPipeline

async def main():
    pipeline = JournalRAGPipeline()
    await pipeline.connect()

    # Process a transcript file
    transcript_path = Path("path/to/transcript.txt")
    stats = await pipeline.process_transcript_file(transcript_path)

    print(f"Extracted {stats['entities']} entities")
    print(f"Extracted {stats['relationships']} relationships")

    await pipeline.disconnect()

asyncio.run(main())
```

#### Query Extracted Entities

```python
import asyncio
from journalrag.graph import SurrealDBClient

async def main():
    client = SurrealDBClient()
    await client.connect()

    # Get an entity by name
    entity = await client.get_entity_by_name("Active Inference")
    print(entity)

    # Query entities by type
    results = await client.query(
        "SELECT * FROM entity WHERE type = $type",
        {"type": "concept"}
    )
    print(results)

    await client.disconnect()

asyncio.run(main())
```

### Configuration

The entity extraction pipeline requires additional environment variables in `.env`:

```env
# Cohere API (for entity extraction)
COHERE_API_KEY=your_cohere_api_key_here
COHERE_MODEL=command-a-03-2025
```

---
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
├── src/
│   ├── journal_utilities/       # Transcription pipeline
│   │   ├── ingest_db_create_wav.py
│   │   ├── transcribe.py
│   │   └── fix_scheduled_dates.py
│   ├── journalrag/             # Entity extraction pipeline
│   │   ├── main.py             # Main pipeline
│   │   ├── extractors/         # Entity extraction (Cohere)
│   │   │   └── cohere_extractor.py
│   │   ├── graph/              # Graph database (SurrealDB)
│   │   │   └── surreal_client.py
│   │   ├── models/             # Pydantic data models
│   │   │   └── entities.py
│   │   ├── adapters/           # Data adapters
│   │   │   └── entity_adapter.py
│   │   ├── schemas/            # JSON schemas for entity extraction
│   │   ├── settings.py         # Configuration management
│   │   └── utils/              # Utilities
│   │       └── logging.py
│   └── private_videos.json     # List of private video IDs
├── tests/                      # Unit tests
├── data/                       # Database and output files
│   ├── database/               # SurrealDB storage
│   ├── input/                  # Input data files (Coda JSON)
│   └── output/                 # Processed outputs
├── Archive/                    # Archived AssemblyAI tools
├── Makefile                    # Workflow automation
├── CLAUDE.md                   # Documentation for Claude Code
├── README.md                   # This file
├── .env.example                # Environment configuration template
└── pyproject.toml              # Python package configuration
```

## Archived Components

The AssemblyAI-based transcription tools have been moved to the `Archive/` directory. These legacy tools provided cloud-based transcription with features like custom vocabulary boosting, spell checking, and document conversion. They remain available for historical reference but are no longer actively maintained.

## Acknowledgements

- WhisperX transcription pipeline and SurrealDB integration contributed by Holly Grimm @hollygrimm, 2024
- Initial AssemblyAI scripts and documentation contributed by Dave Douglass, November 2022


