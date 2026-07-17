# Configuration Reference

Journal Utilities is configured via a single `config.ini` file in the project root. This file controls the pipeline's behavior across download, transcription, export, and interface serving.

## File Format

Standard INI format. Boolean values can be `true`/`false`. Empty values use internal defaults.

## Sections

### `[general]`

Global settings.

| Key | Default | Description |
| :--- | :--- | :--- |
| `data_dir` | `data/output` | Base directory for all downloaded and generated files. |
| `log_level` | `INFO` | Verbosity of console output (`DEBUG`, `INFO`, `WARNING`, `ERROR`). |

### `[download]`

Controls `scripts/download_channel.py`.

| Key | Default | Description |
| :--- | :--- | :--- |
| `transcripts` | `true` | Download subtitles (.vtt/.txt). |
| `audio` | `true` | Download audio tracks. |
| `video` | `false` | Download full video files. |
| `resume` | `true` | Skip files that already exist. |
| `max_videos` | `0` | Stop after N videos (0 = unlimited). |
| `delay` | `1` | Seconds to wait between requests (rate limiting). |
| `cookies_from_browser` | | Browser to extract cookies from (`chrome`, `firefox`) to bypass 403s. |
| `audio_format` | `mp3` | Format for audio downloads (`mp3`, `wav`, `m4a`). |
| `video_quality` | `best` | Video quality selector (`best`, `720p`, `480p`, `360p`). |
| `transcript_languages` | `en` | Comma-separated list of languages to download (e.g. `en,es`). |

### `[transcribe]`

Controls `scripts/transcribe_missing.py` and pipeline transcription.

| Key | Default | Description |
| :--- | :--- | :--- |
| `engine` | `mlx-whisper` | Transcription backend: `mlx-whisper` (Mac) or `whisperx` (GPU). |
| `model` | `mlx-community/whisper-large-v3-turbo` | Model ID (HuggingFace repo or local path). |
| `max_files` | `0` | Limit number of files to transcribe per run. |

### `[export]`

Controls `src/journal_utilities/export/exporter.py`.

| Key | Default | Description |
| :--- | :--- | :--- |
| `plaintext` | `true` | Generate `.txt` files. |
| `pdf` | `true` | Generate `.pdf` files. |
| `markdown` | `true` | Generate `.md` files with YAML frontmatter. |
| `json` | `true` | Generate `.json` files with metadata. |
| `html` | `true` | Generate standalone `.html` files. |
| `output_dir` | `data/export` | Directory where exported files will be saved. |

### `[interface]`

Controls the Web UI (`run.py serve`).

| Key | Default | Description |
| :--- | :--- | :--- |
| `host` | `0.0.0.0` | Bind address (0.0.0.0 for all interfaces). |
| `port` | `8000` | Port to listen on. |

### `[database]`

Controls SurrealDB connection.

| Key | Default | Description |
| :--- | :--- | :--- |
| `url` | `ws://localhost:8080/rpc` | Database WebSocket URL. |
| `user` | `root` | Username. |
| `password` | `root` | Password. |
| `namespace` | `actinf` | Namespace. |
| `database` | `actinf` | Database name. |

## Environment Variables

Some secrets are better kept in a `.env` file (not committed to git).

| Variable | Usage |
| :--- | :--- |
| `HUGGINGFACE_TOKEN` | Required for WhisperX speaker diarization models. |
| `COHERE_API_KEY` | Required for RAG entity extraction. |
| `OLLAMA_BASE_URL` | Optional override for local LLM URL. |

### `[pipeline]`

Controls the default pipeline steps (`uv run python run.py` with no subcommand).

| Key | Default | Description |
| :--- | :--- | :--- |
| `config` | `true` | Show config summary step. |
| `validate` | `true` | Validate data directories and content. |
| `export` | `true` | Export transcripts to configured formats. |
| `test` | `true` | Run the test suite. |
| `serve` | `true` | Start the web interface (final step). |
| `test_strict` | `true` | If `true`, abort the pipeline on test failures; set `false` only for diagnostics. |
