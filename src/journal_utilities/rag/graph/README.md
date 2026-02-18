# Graph Database Client

SurrealDB client for storing entities and relationships in a graph structure.

## `surreal_client.py`

The `SurrealDBClient` class provides async operations for the entity graph.

### Usage

```python
from journal_utilities.rag.graph import SurrealDBClient

client = SurrealDBClient()  # Uses settings from .env
await client.connect()

# Create entity
entity_id = await client.create_entity(entity)

# Create relationship
rel_id = await client.create_relationship(relationship)

# Query entities
entity = await client.get_entity_by_name("Active Inference")

# Custom queries
results = await client.query(
    "SELECT * FROM entity WHERE type = $type",
    {"type": "concept"}
)

await client.disconnect()
```

### Key Methods

| Method | Purpose |
|--------|---------|
| `create_entity()` | Insert or update entity |
| `create_relationship()` | Create edge between entities |
| `get_entity_by_name()` | Lookup by name |
| `get_or_create_transcript()` | Upsert transcript |
| `update_transcript_status()` | Mark as processed |
| `get_unprocessed_transcript_paths()` | Find pending work |

### Schema

Creates tables:

- `entity` - Nodes with name, type, properties
- `relationship` - Edges between entities
- `transcript` - Source transcript metadata
