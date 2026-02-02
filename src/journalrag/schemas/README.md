# JSON Schemas

JSON schemas for Cohere structured extraction.

## Files

### `active_inference_schema_core.json`

Schema for core entity extraction:

- Concepts (name, definition, category, related concepts)
- Researchers (name, affiliation, role, contribution)
- Citations (type, title, authors, year, venue)
- Technical terms (term, explanation, domain, synonyms)
- Key insights (list of strings)

### `active_inference_schema_detailed.json`

Schema for detailed technical extraction:

- Methods/techniques (name, description, context)
- Mathematical notation (symbol, meaning, context)
- Equations (name, formula, explanation)
- Tools/resources (name, type, description, url)
- Research problems (description, status, related concepts)
- Applications (domain, description, examples)

## Usage

Schemas are loaded by `CohereExtractor`:

```python
from journalrag.schemas import load_core_schema, load_detailed_schema

core_schema = load_core_schema()
detailed_schema = load_detailed_schema()
```

The schemas are used with Cohere's `response_format`:

```python
response = client.chat(
    model=model,
    messages=[...],
    response_format={"type": "json_object", "schema": core_schema}
)
```
