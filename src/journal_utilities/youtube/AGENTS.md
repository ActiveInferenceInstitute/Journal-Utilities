# Agent guide — journal_utilities.youtube

The `journal_utilities.youtube` package. See [`README.md`](README.md) for the module map.

## Conventions
- Structured logging (`logging.getLogger(__name__)`); lazy-import heavy deps.
- Dataclasses/Enums for results; `skip_existing=True` defaults; config-driven via `config.ini`.
- Tests mirror this package under `../../../tests/`.

Parent: [`../../../README.md`](../../../README.md) · [`../../../AGENTS.md`](../../../AGENTS.md).
