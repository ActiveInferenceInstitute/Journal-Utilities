# Journal Utilities - Transcription Pipeline

WhisperX-based local transcription pipeline, YouTube download and export tools for Active Inference Journal videos.

## Overview

This package handles the complete transcription workflow:

1. **Import** — Fetch session data from Coda API and import to SurrealDB
2. **Download** — Download transcripts, audio, and video from YouTube
3. **Metadata** — Enrich with YouTube metadata via API
4. **Transcribe** — Local WhisperX transcription with speaker diarization
5. **RAG** — Entity extraction and graph construction (Cohere)
6. **Export** — Batch-export transcripts to plaintext, PDF, Markdown, JSON, HTML
7. **Interface** — Search and browse transcripts
8. **LLM** — AI tool integration

## Modular Components

### `rag/main.py`

Entity extraction pipeline:

```python
from journal_utilities.rag.main import JournalRAGPipeline

pipeline = JournalRAGPipeline()
await pipeline.process_transcripts()
```

### `data/database.py`

Modular database client for SurrealDB operations:

```python
from journal_utilities.data.database import DatabaseClient

async with DatabaseClient() as db:
    await db.insert_session(session_data)
    summary = await db.get_import_summary()
```

**Features:**

- Async context manager for connection management
- Session import with audit trail
- Import rollback capability
- Statistics and summary queries

### `youtube/categorizer.py`

Pattern matching for event categorization:

```python
from journal_utilities.youtube.categorizer import categorize_event, get_category_patterns

category = categorize_event("ActInf GuestStream 2024")  # Returns "Guest_Stream"
patterns = get_category_patterns()
```

**Supported Categories:**

- Guest_Stream, Roundtable, Livestream
- Textbook_Group, Research_Papers
- Project meetings (Math, Research, Social, etc.)

### `youtube/youtube.py`

YouTube utilities for ID extraction and metadata:

```python
from journal_utilities.youtube.youtube import extract_youtube_id, YOUTUBE_ID_PATTERN

video_id = extract_youtube_id("https://youtu.be/abc123_XYZ")
```

### `youtube/playlist.py`

YouTube playlist enumeration and manifest management:

```python
from journal_utilities.youtube.playlist import enumerate_playlists, enumerate_playlist_videos

playlists = enumerate_playlists("UCbPq2w41ZaJSWtpCq4BE6Dg", max_playlists=5)
videos = enumerate_playlist_videos(playlists[0].url)
```

### `render/renderer.py`

Course scaffolding and module.md generation from transcripts:

```python
from journal_utilities.render.renderer import scaffold_course, render_module_md

result = scaffold_course(
    course_slug="my-course",
    videos=video_list,
    transcript_dir=Path("data/output"),
    courses_dir=Path("data/courses"),
    playlist_title="My Playlist",
)
```

### `interface/app.py`

FastAPI web interface for browsing the video library:

```python
uv run python -m journal_utilities.interface.app  # http://localhost:8000
```

**Features:**

- Searchable, filterable video library with pagination
- Video detail with embedded YouTube player, audio, and transcript
- Ollama-powered RAG chat with transcript context
- Knowledge/category browser with progress tracking

### `download/downloader.py`

YouTube content downloader (transcripts, audio, video):

```python
from journal_utilities.download.downloader import download_all

results = download_all(
    video_id="abc123XYZ_q",
    output_dir=Path("data/output"),
    transcripts=True,
    audio=True,
    video=False,
)
```

### `export/exporter.py`

Multi-format transcript exporter:

```python
from journal_utilities.export import export_transcripts, ExportFormat

results = export_transcripts(
    transcript_dir=Path("data/output/transcripts"),
    output_dir=Path("data/export"),
    formats=[ExportFormat.PLAINTEXT, ExportFormat.PDF, ExportFormat.MARKDOWN],
)
```

**Supported formats:** Plaintext, PDF, Markdown (with frontmatter), JSON, HTML

---

## Transcription Engines

### `transcribe/transcriber.py` (Local Whisper)

```python
from journal_utilities.transcribe.transcriber import transcribe_audio

result = transcribe_audio(
    audio_path="video.mp3",
    output_dir="transcripts/",
    model="mlx-community/whisper-large-v3-turbo"
)
```

### `transcribe/transcribe.py` (WhisperX)

```python
from journal_utilities.transcribe.transcribe import TranscriptionService

service = TranscriptionService(hf_token, device="cuda", batch_size=48)
service.transcribe(output_dir, audio_file)
```

---

## Requirements

- **Python 3.12+**
- **Hugging Face Token** — For pyannote speaker diarization models
- **YouTube API Key** — For metadata fetching
- **Coda API Token** — For session data
- **SurrealDB** — Running database instance

## Database Schema

Sessions are stored with:

- `session_name` — YouTube video ID
- `title` — Video title
- `scheduled_date` — Event date
- `transcribed` — Transcription status
- `is_private` — Private video flag

## Audit Trail

All imports are tracked in `import_audit` table:

- Operation timestamps
- Success/failure status
- Rollback capability
