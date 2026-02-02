# Entity Models

Pydantic models for Active Inference entity extraction and storage.

## `entities.py`

Type-safe entity definitions with validation.

### Extraction Models

**Core Entities:**

```python
from journalrag.models import (
    Concept,          # Theoretical concepts
    Researcher,       # People mentioned
    Citation,         # Papers/books/articles
    TechnicalTerm,    # Domain terminology
    CoreEntities,     # Container for above
)
```

**Detailed Analysis:**

```python
from journalrag.models import (
    MethodTechnique,      # Research methods
    MathematicalNotation, # Math symbols
    Equation,             # Formulas
    ToolResource,         # Software/tools
    ResearchProblem,      # Open questions
    Application,          # Use cases
    DetailedAnalysis,     # Container
)
```

**Combined:**

```python
from journalrag.models import ExtractedEntities
# Contains core + detailed + transcript_id
```

### Storage Models

```python
from journalrag.models import (
    Entity,        # Generic entity for DB storage
    Relationship,  # Graph edge between entities
    Transcript,    # Source transcript metadata
)
```

### Enums

- `ConceptCategory` - THEORETICAL, COMPUTATIONAL, NEUROSCIENCE, etc.
- `ResearcherRole` - SPEAKER, CITED_AUTHOR, COLLABORATOR, etc.
- `CitationType` - PAPER, BOOK, ARTICLE, etc.
- `TermDomain` - MATHEMATICS, NEUROSCIENCE, COMPUTER_SCIENCE, etc.
