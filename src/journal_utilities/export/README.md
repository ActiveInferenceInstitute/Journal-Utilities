# Export Module

Multi-format transcript exporter for the Active Inference video library.

## Overview

The export module converts raw `.txt` transcripts from `data/output/transcripts/` into publication-ready formats:

| Format    | Extension | Description                              |
| --------- | --------- | ---------------------------------------- |
| Plaintext | `.txt`    | Clean text with whitespace normalization |
| PDF       | `.pdf`    | Formatted document via `fpdf2`           |
| Markdown  | `.md`     | Document with YAML frontmatter metadata  |
| JSON      | `.json`   | Structured data with word/char counts    |
| HTML      | `.html`   | Standalone page with embedded CSS        |

## Usage

### Python API

```python
from pathlib import Path
from journal_utilities.export import export_transcripts, export_single, ExportFormat

# Batch export all transcripts
results = export_transcripts(
    transcript_dir=Path("data/output/transcripts"),
    output_dir=Path("data/export"),
    formats=[ExportFormat.PLAINTEXT, ExportFormat.PDF, ExportFormat.MARKDOWN],
)

# Export a single transcript
result = export_single(
    source_path=Path("data/output/transcripts/abc123.txt"),
    output_dir=Path("data/export/pdf"),
    fmt=ExportFormat.PDF,
)
print(f"Exported to {result.output_path} ({result.file_size_str})")
```

### Config File (`config.ini`)

```ini
[export]
plaintext = true
pdf = false
markdown = false
json = false
html = false
output_dir = data/export
```

### CLI (via `run.py`)

```bash
python run.py export        # Export using config.ini settings
python run.py config        # Show current configuration
```

## Output Structure

```text
data/export/
├── plaintext/
│   ├── video_id_1.txt
│   └── video_id_2.txt
├── pdf/
│   ├── video_id_1.pdf
│   └── video_id_2.pdf
└── markdown/
    ├── video_id_1.md
    └── video_id_2.md
```

## Dependencies

PDF export requires the `export` optional dependency group:

```bash
uv pip install -e ".[export]"
```

All other formats (plaintext, markdown, JSON, HTML) work with no extra dependencies.
