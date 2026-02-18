# AGENTS.md - Export Module

## Module Purpose

Multi-format transcript exporter (plaintext, PDF, Markdown, JSON, HTML).

## Key Files

| File | Purpose |
| --- | --- |
| `exporter.py` | Core export engine with format converters |

## Entry Points

```bash
# Via run.py (reads config.ini)
python run.py export

# Python API
python -c "
from pathlib import Path
from journal_utilities.export import export_transcripts, ExportFormat
results = export_transcripts(
    Path('data/output/transcripts'),
    Path('data/export'),
    formats=[ExportFormat.PLAINTEXT, ExportFormat.PDF],
)
"
```

## Key Classes

- `ExportFormat` — Enum: `PLAINTEXT`, `PDF`, `MARKDOWN`, `JSON`, `HTML`
- `ExportResult` — Dataclass tracking status, path, size, duration

## Common Tasks

**Add a new export format:**

1. Add value to `ExportFormat` enum
2. Create `_to_newformat()` converter function
3. Register in `_FORMAT_WRITERS` dict
4. Add extension mapping in `export_single()`

## Testing

```bash
uv run pytest tests/journal_utilities/test_exporter.py -v
```
