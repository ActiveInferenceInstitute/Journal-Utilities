# Utilities

Shared utility functions for the RAG pipeline.

## `logging.py`

Structured logging setup using `structlog` with rich console output.

### Usage

```python
from journal_utilities.rag.utils import setup_logging
import structlog

# Initialize logging (usually done once at startup)
setup_logging(debug=True)

# Get logger
logger = structlog.get_logger(__name__)

# Log messages
logger.info("Processing transcript", transcript_id="abc123")
logger.error("Extraction failed", error=str(e))
```

### Features

- JSON-structured log messages
- Rich console formatting
- Debug mode toggle
- Automatic context binding
