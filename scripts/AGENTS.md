# Agent guide — scripts/

CLI tools over `src/journal_utilities/`. See [`README.md`](README.md) for usage.

## Key scripts
- `download_channel.py` — enumerate (videos+streams+shorts) + download transcripts/audio.
  Runs **cookie-free** when no `cookies.txt` exists; never pass `--cookies-from-browser`
  into a tracked path, never commit `cookies.txt`.
- `transcribe_missing.py` — local Whisper (`mlx-whisper`) for caption-less videos.
- `refactor_journal.py` — build the ActiveInferenceJournal v2 schema (source-namespaced,
  `data/video/activeinferenceinstitute/`); `--build <dir>` stages out-of-place and audits
  for zero data loss before any in-place apply. See [`../docs/JOURNAL_SCHEMA.md`](../docs/JOURNAL_SCHEMA.md).

## Conventions
- `PYTHONPATH=src` + the project venv. `timeout` is absent on macOS (use `gtimeout`/none).
- Structured logging via `logging.getLogger(__name__)`; lazy-import heavy deps (whisper).

Parent: [`../README.md`](../README.md) · [`../AGENTS.md`](../AGENTS.md).
