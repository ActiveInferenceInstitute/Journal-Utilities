# AGENTS.md - Source Code

## Package Overview

| Package | Purpose | Entry Point |
|---------|---------|-------------|
| `journal_utilities` | Transcription pipeline | `ingest_db_create_wav.py`, `transcribe.py` |
| `journalrag` | Entity extraction | `main.py` |

## Key Patterns

### Async Database Operations

Both packages use async SurrealDB connections:

```python
async with AsyncSurreal(url) as db:
    await db.signin({"user": user, "pass": password})
    await db.use(namespace, database)
```

### Entity Models

JournalRAG uses Pydantic models in `journalrag/models/entities.py`:

- `CoreEntities` - Concepts, researchers, citations, terms
- `DetailedAnalysis` - Methods, equations, tools, applications
- `ExtractedEntities` - Combined extraction result

### Extraction Flow

```python
extractor = CohereExtractor()
core = extractor.extract_core_entities(transcript)
detailed = extractor.extract_detailed_analysis(transcript)
```

## Testing

```bash
# Test journal_utilities
uv run pytest tests/journal_utilities/ -v

# Test journalrag
uv run pytest tests/journalrag/ -v
```

## Common Modifications

- **Add entity type**: Modify `journalrag/models/entities.py` and `journalrag/schemas/`
- **Change extraction prompt**: Edit `journalrag/extractors/cohere_extractor.py`
- **Add audit function**: Extend `journal_utilities/ingest_db_create_wav.py`
