# JournalRAG - Entity Extraction Pipeline

Cohere AI-powered entity extraction from Active Inference transcripts with SurrealDB graph storage.

## Overview

JournalRAG analyzes transcripts to extract:

- **Concepts** - Theoretical concepts and ideas
- **Researchers** - People mentioned (speakers, authors, collaborators)
- **Citations** - Papers, books, articles referenced
- **Technical Terms** - Domain-specific terminology
- **Key Insights** - Important conclusions

Advanced extraction also captures:

- Methods and techniques
- Mathematical notation and equations
- Tools and resources
- Research problems
- Applications

## Usage

### Command Line

```bash
make extract-entities
# Or directly:
python -m journalrag.main
```

### Python API

```python
import asyncio
from journalrag.main import JournalRAGPipeline

async def main():
    pipeline = JournalRAGPipeline()
    await pipeline.connect()
    
    # Process all unprocessed transcripts
    stats = await pipeline.process_from_database()
    print(f"Processed {stats['processed']} transcripts")
    
    await pipeline.disconnect()

asyncio.run(main())
```

## Architecture

```
journalrag/
├── main.py           # Pipeline orchestrator
├── extractors/       # Cohere AI extraction
│   └── cohere_extractor.py
├── graph/            # SurrealDB client
│   └── surreal_client.py
├── models/           # Pydantic entity models
│   └── entities.py
├── schemas/          # JSON schemas
│   ├── active_inference_schema_core.json
│   └── active_inference_schema_detailed.json
├── adapters/         # Format conversion
│   └── entity_adapter.py
├── utils/            # Utilities
│   └── logging.py
└── settings.py       # Configuration
```

## Entity Types

| Type | Description | Example |
|------|-------------|---------|
| Concept | Theoretical ideas | "Free Energy Principle" |
| Researcher | People | "Karl Friston" |
| Citation | References | "Active Inference: A Process Theory (2017)" |
| TechnicalTerm | Jargon | "Markov Blanket" |

## Configuration

Environment variables (`.env`):

```env
COHERE_API_KEY=your_key_here
COHERE_MODEL=command-a-03-2025
SURREALDB_URL=ws://0.0.0.0:8080/rpc
```

## Requirements

- **Cohere API Key** - For entity extraction
- **SurrealDB** - Running database instance
