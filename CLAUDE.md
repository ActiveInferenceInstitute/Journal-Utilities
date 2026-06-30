# CLAUDE.md

Guidance for Claude Code (claude.ai/code) when working with this repository.

## Project Overview

Journal-Utilities is a Python processing pipeline for Active Inference Institute YouTube content. It supports six workflows:

1. **YouTube Channel Download** — Enumerate and download transcripts, audio, and video via `yt-dlp`
2. **Local Whisper Transcription** — Apple Silicon–optimized transcription via `mlx-whisper`
3. **WhisperX Transcription** — GPU-based transcription with speaker diarization (CUDA + SurrealDB)
4. **Entity Extraction (RAG)** — Cohere AI entity/relationship extraction into SurrealDB graph
5. **Export** — Multi-format transcript export (plaintext, PDF, Markdown, JSON, HTML)
6. **Web Interface** — FastAPI SPA for browsing the video library with Ollama-powered RAG chat

## Journal v2 refactor

`scripts/refactor_journal.py` transforms the sibling `ActiveInferenceJournal` repo into
the uniform v2 schema — see [`docs/JOURNAL_SCHEMA.md`](docs/JOURNAL_SCHEMA.md) and
[`docs/REFACTOR_READINESS.md`](docs/REFACTOR_READINESS.md). Run `--build <dir>` for an
out-of-place staging tree (audit/dry-run); content-based item detection + a passthrough
pass guarantee zero data loss (reconcile total source files == captured + intentional
drops before any in-place apply). Audio is split to the journal's `audio` branch
(`<item>/audio/<name>.64k.m4a`); `main` carries no audio.

## Operational notes (important)

- **Cookie safety:** the downloader runs **cookie-free** when no `cookies.txt` exists. A
  leaked `cookies.txt` once exposed live Google session cookies in this public repo —
  it is now gitignored and purged from history. **Never use `--cookies-from-browser`**
  into a tracked path; never commit `cookies.txt`.
- **Enumeration:** `channel.py` unions the `/videos` + `/streams` + `/shorts` tabs (the
  `UU...` uploads playlist truncates at ~100). Full channel = ~729 videos.
- `timeout` is not on macOS (use `gtimeout` or none). For transcript-only work, a
  lightweight venv (`yt-dlp` + `youtube-transcript-api`) is enough — `whisperx` is only
  for diarization.

## Development Commands

### Environment Setup

```bash
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Running Tests

```bash
uv run pytest tests/ -v
uv run pytest tests/journal_utilities/ -v       # YouTube download + transcription
uv run pytest tests/journal_utilities/rag/ -v   # Entity extraction (RAG)
```

### Pipeline Runner (run.py)

```bash
python run.py --help           # Show all commands
python run.py config           # Display current configuration
python run.py export           # Export transcripts (formats from config.ini)
python run.py download         # Download from YouTube (options from config.ini)
python run.py serve            # Start web interface
python run.py test             # Run test suite
python run.py full             # Run full pipeline (download → export)
```

### YouTube Channel Download

```bash
python scripts/download_channel.py --transcripts --audio --resume
python scripts/download_channel.py --transcripts --audio --resume --cookies-from-browser chrome
```

### Local Whisper Transcription

```bash
python scripts/transcribe_missing.py --dry-run
python scripts/transcribe_missing.py
python scripts/transcribe_missing.py --max-files 5
```

### Web Interface

```bash
uv pip install -e ".[interface]"
uv run python -m journal_utilities.interface.app   # → http://localhost:8000
```

### Database

```bash
make db-start
surreal sql --endpoint http://localhost:8080 --username root --password root --namespace actinf --database actinf
```

## Architecture

### Core Modules (`src/journal_utilities/`)

| Module | Purpose |
|--------|---------|
| `channel.py` | Channel enumeration via `yt-dlp --flat-playlist` |
| `downloader.py` | Download transcripts, audio, video |
| `transcriber.py` | Local Whisper transcription using `mlx-whisper` (Apple Silicon) |
| `playlist.py` | Playlist enumeration and metadata |
| `renderer.py` | Markdown/HTML rendering of transcripts |
| `youtube.py` | URL builder helpers |
| `categorizer.py` | Video categorization by series/type |
| `database.py` | Database models and queries |
| `importer.py` | Session import with audit trail |
| `transcribe.py` | WhisperX transcription with diarization (GPU/CUDA) |
| `interface/app.py` | FastAPI web server, REST API routes |
| `interface/data_loader.py` | Video manifest builder from `data/output/` |
| `interface/chat_engine.py` | Ollama RAG chat engine with transcript context |
| `export/exporter.py` | Multi-format transcript export |

### Entity Extraction (`src/journal_utilities/rag/`)

| Module | Purpose |
|--------|---------|
| `main.py` | Pipeline orchestrator |
| `extractors/cohere_extractor.py` | Cohere AI entity extraction |
| `graph/surreal_client.py` | SurrealDB graph client |
| `models/entities.py` | Pydantic entity/relationship models |
| `adapters/entity_adapter.py` | Entity format conversion |

### Top-Level Files

| File | Purpose |
|------|---------|
| `run.py` | Python CLI runner (argparse + configparser) |
| `config.ini` | Pipeline configuration (all options in INI format) |
| `run.sh` | Bash interactive menu (legacy, still functional) |

### Data Flow

```
YouTube Channel → yt-dlp enumeration → video manifest (JSON)
                → yt-dlp download → transcripts (.txt), audio (.mp3), video (.mp4)
                → mlx-whisper → transcripts for missing videos
                → WhisperX → diarized transcripts → SurrealDB
                → Cohere AI → entities + relationships → SurrealDB graph
                → export → plaintext/PDF/MD/JSON/HTML
```

## Key Configuration

### config.ini

All pipeline options in a single plaintext file:

| Section | Keys |
|---------|------|
| `[general]` | `data_dir`, `log_level` |
| `[download]` | `transcripts`, `audio`, `video`, `resume`, `max_videos`, `delay`, `cookies_from_browser` |
| `[transcribe]` | `engine`, `model`, `max_files` |
| `[export]` | `plaintext`, `pdf`, `markdown`, `json`, `html`, `output_dir` |
| `[interface]` | `host`, `port` |
| `[database]` | `url`, `user`, `password`, `namespace`, `database` |

### Environment Variables (`.env`)

| Variable | Required For | Purpose |
|----------|-------------|---------|
| `HUGGINGFACE_TOKEN` | WhisperX | Speaker diarization models |
| `API_KEY` | Metadata | YouTube Data API v3 |
| `CODA_API_TOKEN` | Import | Coda session data |
| `COHERE_API_KEY` | RAG | Entity extraction |

## Code Patterns

- **Dataclasses & Enums**: `DownloadResult`, `TranscriptionResult`, `ExportResult`
- **Lazy imports**: `mlx-whisper` imported lazily to avoid hard dependency
- **Skip-existing**: All functions default to `skip_existing=True`
- **Async-first**: Database operations use `asyncio`
- **Structured logging**: `logging.getLogger(__name__)`
- **Config-driven**: `run.py` reads `config.ini` via Python `configparser`

## Optional Dependencies

| Group | Install | Purpose |
|-------|---------|---------|
| `transcribe-local` | `uv pip install -e ".[transcribe-local]"` | `mlx-whisper` |
| `interface` | `uv pip install -e ".[interface]"` | FastAPI, uvicorn, httpx |
| `export` | `uv pip install -e ".[export]"` | fpdf2 for PDF export |
| `dev` | `uv pip install -e ".[dev]"` | pytest, black, ruff, mypy |
