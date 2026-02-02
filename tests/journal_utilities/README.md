# Journal Utilities Tests

Tests for the WhisperX transcription pipeline.

## Test Files

### `test_categorizer.py`

Pattern matching tests (35 tests):

- Stream type categorization
- Project meeting patterns
- Textbook group patterns
- Edge cases and unknown patterns

### `test_youtube.py`

YouTube utilities tests (18 tests):

- ID extraction from various URL formats
- YouTube ID pattern validation
- Private video detection

### `test_database.py`

Mock-based database tests (12 tests):

- Connection management
- Session operations
- Import rollback
- Audit trail creation

### `test_importer.py`

Session import tests (10 tests):

- JSON parsing (dict and list formats)
- Audit tracking
- Error handling

### `test_audit_functions.py`

Tests for import audit trail (requires DB):

- `test_get_recent_import_runs` - List recent imports
- `test_get_import_summary` - Import statistics
- `test_get_failed_imports` - Failed operation retrieval

### `test_transcribe.py`

Tests for transcription output:

- Single speaker formatting
- Multi-speaker formatting
- Empty input handling

## Running

```bash
# Run all tests (no DB required)
uv run pytest tests/journal_utilities/ -v --ignore=tests/journal_utilities/test_audit_functions.py

# Run with coverage
uv run pytest tests/journal_utilities/ -v --cov=journal_utilities

# Run specific test file
uv run pytest tests/journal_utilities/test_categorizer.py -v
```

## Test Coverage

| Module | Coverage |
|--------|----------|
| categorizer.py | 94% |
| importer.py | 89% |
| database.py | 47% |
| youtube.py | 36% |

## Fixtures

See `tests/journal_utilities/conftest.py` for test fixtures including sample database mocks.
