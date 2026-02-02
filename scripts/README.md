# Scripts

Utility scripts for environment setup and patching.

## `patch_whisperx.py`

Patches WhisperX for compatibility with pyannote.audio 4.0+.

### Usage

Run after installing WhisperX:

```bash
python scripts/patch_whisperx.py
```

### What It Does

Applies compatibility fixes to WhisperX's diarization pipeline for newer pyannote versions. Required for speaker diarization to work correctly.

### When to Run

- After initial `uv sync` installation
- After upgrading WhisperX or pyannote.audio
- If speaker diarization fails with API errors
