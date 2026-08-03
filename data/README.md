# Data Directory

Storage for input files and processed outputs.

## Structure

```
data/
├── input/         # Source data files
│   └── livestream_fulldata_table.json  # Coda API export
├── output/        # Processed transcripts
│   └── <video_id>/                     # Per-video artifacts (see below)
└── database/      # SurrealDB RocksDB storage — created on first `make db-start`,
                   # NOT committed to git
```

## Folders

### `database/`

SurrealDB RocksDB storage (created locally on first use; not tracked by git).
Contains session metadata, transcription status, and extracted entities when the
SurrealDB-backed data/RAG pipelines are used.

**Start database:**

```bash
make db-start
```

(starts `surreal start … rocksdb://./data/database` on `0.0.0.0:8080`).

### `input/`

Source data from Coda API. Fetched with:

```bash
make fetch-coda
```

### `output/`

Downloaded/transcribed artifacts, one set per video id (`<video_id>` is the 11-char
YouTube id):

- `<video_id>.json` — full transcript metadata/details
- `<video_id>.simple.json` — simplified transcript JSON (without word arrays)
- `<video_id>.simple.txt` — plain-text transcript
- `whisperx/` — WhisperX work-dir cache (diarization, used by
  `scripts/transcribe_worklist.py`)
- `../private_videos.json` — private-video registry written by the YouTube metadata
  pipeline (at `<repo>/data/private_videos.json`, honoring `PRIVATE_VIDEOS_PATH`)

(The repo also carries legacy `<id>.vtt` / `<id>.ytdl` / `.part` files from earlier
download runs; new downloads write the `.json`/`.simple.*` set above.)

## Maintenance

**Backup the local database:**

```bash
cp -r data/database data/database_backup
```

**Clear outputs:**

```bash
rm -rf data/output/*
```
