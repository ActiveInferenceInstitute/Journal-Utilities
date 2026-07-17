# Scripts

CLI utilities for data processing, transcription, and course scaffolding.

## `download_channel.py`

Primary CLI for enumerate-and-download of YouTube channel content.

### Usage — download_channel

```bash
python scripts/download_channel.py --help

# Download transcripts only (fastest)
python scripts/download_channel.py --transcripts --resume

# Download transcripts + audio + local Whisper fallback
python scripts/download_channel.py --transcripts --audio --resume --transcribe-missing

# Full download with cookies for rate limiting
python scripts/download_channel.py --transcripts --audio --video --cookies-from-browser chrome
```

### Features — download_channel

- Enumerate all playlists from a YouTube channel
- Download transcripts (YouTube captions), audio (m4a/mp3), and video (mp4)
- Resume interrupted downloads
- Fallback to local Whisper transcription when YouTube captions unavailable
- Cookie-based auth to bypass rate limiting

## `transcribe_missing.py`

Standalone local transcription for videos missing transcripts.

### Usage — transcribe_missing

```bash
python scripts/transcribe_missing.py --help

# Transcribe all missing (Apple Silicon, mlx-whisper)
python scripts/transcribe_missing.py

# Dry run to preview what would be transcribed
python scripts/transcribe_missing.py --dry-run

# Limit to N files
python scripts/transcribe_missing.py --max-files 5
```

## `scaffold_youtube_courses.py`

Generate course directory structures from downloaded transcripts.

### Usage — scaffold_youtube_courses

```bash
python scripts/scaffold_youtube_courses.py --help

# Scaffold courses from all playlists
python scripts/scaffold_youtube_courses.py
```

### Features — scaffold_youtube_courses

- Creates numbered module directories per video
- Generates `module.md` files with metadata and transcript content
- Filesystem-safe slugification of titles

## `patch_whisperx.py`

Patches WhisperX for compatibility with pyannote.audio 4.0+.

### Usage — patch_whisperx

Run after installing WhisperX:

```bash
python scripts/patch_whisperx.py
```

### When to Run

- After initial `uv sync` installation
- After upgrading WhisperX or pyannote.audio
- If speaker diarization fails with API errors

## `fix_scheduled_dates.py`

One-time database migration utility that fixes `scheduled_date` fields stored as strings instead of proper datetime objects in SurrealDB.

### Usage — fix_scheduled_dates

```bash
python scripts/fix_scheduled_dates.py
```

> **Note**: Requires a running SurrealDB instance and valid credentials in `.env`.

## Journal v2 metadata and indexes

```bash
python scripts/enrich_metadata.py --journal ../ActiveInferenceJournal --snapshot-only --apply
python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal
python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal --check
```

`enrich_metadata.py` is dry-run by default and preserves journal-owned
`sessions[]`. `generate_journal_indexes.py` derives `INDEX.json` and `INDEX.md`
from canonical metadata, including duplicate and unique-video counts.

Use the combined read-only integrity gate before committing or publishing a
journal update:

```bash
python scripts/validate_journal.py \
  --journal ../ActiveInferenceJournal \
  --manifest data/output/channel_videos.json
```

The gate checks metadata/path consistency, URL-only enrichment fields, derived
indexes, duplicate targets and canonical ID uniqueness, transcript JSON shape,
manifest coverage, and the no-audio/no-credentials rule for the journal's
`main` branch. `--strict-manifest` also rejects canonical IDs that are absent
from the supplied manifest; the default warning is useful when the manifest is
older than the journal and should be re-enumerated first.

For split-file items whose merged transcript sections need rebuilding:

```bash
python scripts/repair_split_transcripts.py --journal ../ActiveInferenceJournal --utilities .
python scripts/repair_split_transcripts.py --journal ../ActiveInferenceJournal --utilities . --check
```

The repair is idempotent and writes only when complete `<video_id>_sessNN`
source pairs are available.
