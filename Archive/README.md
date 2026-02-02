# Archive

**Historical reference only** - These AssemblyAI-based tools are no longer actively maintained.

## Overview

The Archive contains legacy cloud-based transcription tools that used AssemblyAI API. The project has since migrated to local WhisperX transcription for improved privacy and control.

## Contents

### `1_youtube_to_audio/`

YouTube to audio conversion tools using yt-dlp.

### `2_audio_to_markdown/`

AssemblyAI transcription submission and processing:

- Transcription submission
- Word boost vocabulary
- Spell checking
- Result retrieval

### `5_markdown_to_final/`

Markdown to final format conversion (PDF, HTML via Pandoc).

### `May_2023_testing/`

Historical testing scripts from initial development.

### `docs/`

Original AssemblyAI documentation.

### Standalone Scripts

- `StanzaNLP.py` - NLP processing with Stanza
- `richerSentenceWords.py` - Sentence enrichment
- `sentencesToTranscripts.py` - Transcript formatting

## Features (Historical)

These tools provided:

- Custom vocabulary boosting
- Spell checking
- Sentiment analysis
- IAB categorization
- PDF/HTML output via Pandoc

## Why Archived

- AssemblyAI requires cloud API (privacy concerns)
- WhisperX provides comparable quality locally
- Better control over transcription process
- No per-minute API costs
