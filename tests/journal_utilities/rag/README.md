# RAG Tests

Tests for the entity extraction pipeline.

## Test Structure

```
rag/
├── conftest.py              # Shared fixtures (sample entities)
├── unit/                    # Fast tests, no API calls
│   ├── test_models.py       # Pydantic model validation (17 tests)
│   ├── test_pipeline.py     # Pipeline logic with mocks
│   ├── test_cohere_extractor.py  # Extractor logic
│   ├── test_surreal_client.py    # SurrealDB client (10 tests)
│   └── test_entity_adapter.py   # Entity conversion (12 tests)
└── integration/             # Real API tests
    └── test_pipeline_integration.py
```

## Unit Tests

Run without API keys:

```bash
uv run pytest tests/journal_utilities/rag/unit/ -v
```

### `test_models.py` (17 tests)

- Entity creation and validation
- JSON serialization
- Enum validation
- All entity types (Concept, Researcher, Citation, etc.)

### `test_pipeline.py`

- Pipeline orchestration with mocked components

### `test_cohere_extractor.py`

- Extractor initialization and configuration
- Extraction logic with mocked API responses

### `test_surreal_client.py` (10 tests)

- Client initialization and configuration
- Connection and disconnection
- Entity creation and updates
- Transcript operations
- Relationship creation
- Error handling

### `test_entity_adapter.py` (12 tests)

- CoreEntities to Entity conversion
- Concept, Researcher, Citation conversion
- Technical term and key insight conversion
- Relationship extraction

## Integration Tests

Require `COHERE_API_KEY` in `.env`:

```bash
uv run pytest tests/journal_utilities/rag/integration/ -v -s
```

### `test_pipeline_integration.py` (3 tests)

- Real Cohere extraction
- Expected content verification
- Full end-to-end pipeline

## Test Coverage

| Module | Coverage |
|--------|----------|
| entities.py | 100% |
| entity_adapter.py | 63% |
| main.py | 57% |
| surreal_client.py | 52% |
| cohere_extractor.py | 41% |

## Sample Fixtures

```python
@pytest.fixture
def sample_core_entities():
    return CoreEntities(
        concepts=[Concept(name="Active Inference", ...)],
        researchers=[Researcher(name="Karl Friston", ...)],
        ...
    )
```
