# AGENTS.md - RAG Pipeline

## Module Purpose

Entity extraction pipeline using Cohere AI with SurrealDB graph storage.

## Key Files

| File | Purpose |
|------|---------|
| `main.py` | Pipeline orchestrator (`JournalRAGPipeline`) |
| `extractors/cohere_extractor.py` | Cohere API client |
| `graph/surreal_client.py` | SurrealDB graph client |
| `models/entities.py` | Pydantic entity models |
| `adapters/entity_adapter.py` | Entity format conversion |

## Extraction Flow

```python
# 1. Initialize extractor
extractor = CohereExtractor(api_key, model)

# 2. Extract core entities
core = extractor.extract_core_entities(transcript)

# 3. Extract detailed analysis (optional)
detailed = extractor.extract_detailed_analysis(transcript)

# 4. Convert to storage format
adapter = EntityAdapter()
entities = adapter.core_to_entities(core, transcript_id)

# 5. Store in graph database
client = SurrealDBClient()
await client.connect()
for entity in entities:
    await client.create_entity(entity)
```

## Key Classes

- `CohereExtractor` - Cohere API wrapper
- `SurrealDBClient` - Database operations
- `EntityAdapter` - Format conversion
- `JournalRAGPipeline` - Full orchestration

## Entity Models

```python
from journal_utilities.rag.models import (
    CoreEntities,      # Basic extraction
    DetailedAnalysis,  # Technical details
    ExtractedEntities, # Combined result
    Entity,            # Storage format
    Relationship,      # Graph edges
)
```

## Testing

```bash
# Unit tests (no API needed)
uv run pytest tests/journal_utilities/rag/unit/ -v

# Integration tests (requires COHERE_API_KEY)
uv run pytest tests/journal_utilities/rag/integration/ -v -s
```

## Common Tasks

**Add new entity type:**

1. Add model to `models/entities.py`
2. Update schema in `schemas/`
3. Update adapter in `adapters/entity_adapter.py`

**Modify extraction prompt:**
Edit system messages in `extractors/cohere_extractor.py`
