# Entity Adapters

Converts extracted entities from Cohere format to database storage format.

## `entity_adapter.py`

The `EntityAdapter` class handles conversion between:

- `CoreEntities` → List of `Entity` models for storage
- Creates `Entity` and `Relationship` objects from extracted data

### Usage

```python
from journal_utilities.rag.adapters import EntityAdapter
from journal_utilities.rag.models import CoreEntities

adapter = EntityAdapter()

# Convert core entities to storage format
entities, relationships = adapter.core_to_entities(
    core_entities=core,
    transcript_id="transcript:abc123"
)

# Store in database
for entity in entities:
    await client.create_entity(entity)
for rel in relationships:
    await client.create_relationship(rel)
```

### Entity Types Generated

- Person (from researchers)
- Concept (from concepts)
- Citation/Publication (from citations)
- TechnicalTerm (from technical_terms)
