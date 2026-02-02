# Entity Extractors

Cohere AI-powered entity extraction from transcripts.

## `cohere_extractor.py`

The `CohereExtractor` class uses Cohere's JSON Schema mode for structured extraction.

### Usage

```python
from journalrag.extractors import CohereExtractor

extractor = CohereExtractor()  # Uses settings from .env

# Extract core entities (faster, run on all transcripts)
core = extractor.extract_core_entities(transcript_text)

# Extract detailed analysis (technical transcripts)
detailed = extractor.extract_detailed_analysis(transcript_text)

# Extract both at once
extracted = extractor.extract_complete(transcript_text, transcript_id="abc123")
```

### Extraction Types

**Core Entities** (`extract_core_entities`):

- Concepts with definitions
- Researchers with affiliations
- Citations (papers, books)
- Technical terms
- Key insights

**Detailed Analysis** (`extract_detailed_analysis`):

- Methods and techniques
- Mathematical notation
- Equations
- Tools and resources
- Research problems
- Applications

### Configuration

Environment variables:

- `COHERE_API_KEY` - Required
- `COHERE_MODEL` - Default: `command-a-03-2025`
