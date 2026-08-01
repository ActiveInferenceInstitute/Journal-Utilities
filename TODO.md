# Journal-Utilities — Backlog

**Status:** Maintained
**Owner:** Active Inference Institute / Journal-Utilities maintainers
**Last reviewed:** 2026-08-01 (deepest hostile red-team pass — 3 parallel subagent reviews; all
Minor/Medium **and** every Major finding now implemented and verified; gates green)

---

## Completed / Closed

Everything below was implemented and verified in the 2026-08-01 pass. Final gates:
`uv run pytest tests/` = **471 passed, 3 API-gated skips, 2 warnings (~100s)**;
`uv run ruff check src/ tests/ scripts/` = **All checks passed**;
`uv run mypy src` = **Success: no issues in 41 files**; CI golded gate
`scripts/validate_journal.py` = **All checks passed**. No further action required.

> Historical note: the earlier "Major — Scoped (deferred)" list from this pass is now fully
> resolved. All items below were previously scoped; each has since been **implemented** in
> source + tests + docs and verified green. Nothing major remains open.

### MAJORS — implemented this pass (M1–M11)

**M1 — yt-dlp transcript strategy dead path — `download/downloader.py` + `tests/test_downloader.py`**
`_convert_vtt_to_text(best_file, final_path)` (was a one-arg `TypeError` swallowed at runtime, always
falling back to the API). Added `_pick_transcript_vtt` (manual-over-auto, deterministic) and a no-mock
regression test asserting the yt-dlp `SUCCESS` path converts a real VTT → `.txt`.

**M2 — lint/type gates green + CI enforcement — repo-wide (`src/`, `tests/`, `scripts/`, `pyproject.toml`, `.github/workflows/test.yml`)**
Auto-fixed 399 mechanical ruff issues; fixed the substantive remaining rules (F401/F841/B904/E702/N806/
E402/UP031 + script + src annotations). `make lint` (`ruff check src/ tests/`) and `ruff check scripts/`
now pass. mypy strict reduced 91→0: parametrized/typed fixes across the `data/`/`youtube/`/`rag/`/
`download/`/`export` modules, plus documented mypy config (third-party SDK
stub noise disabled; legacy untyped GPU/Cohere modules scoped via per-module ignore; bare-generic
relaxation). CI now runs `ruff check src/ tests/ scripts/` + `mypy src` in addition to the existing gate.
(A `ruff format --check` CI step was considered and dropped: the tree is black-formatted, so a ruff-format
gate would force a 50-file style-only diff against the repo's established `black` convention.)

**M3 — SurrealQL injection via f-string interpolation — `data/database.py`, `youtube/youtube.py`, `transcribe/transcribe.py`, `scripts/fix_scheduled_dates.py`**
All dynamic values parameterized through `query(sql, params)` (`WHERE import_run_id = $id`,
`UPDATE $id …`, `LIMIT $limit`, youtube metadata `UPDATE $id MERGE {…}`); invalid backslash "escaping"
removed.

**M4 — `rollback_import` cross-run delete — `data/database.py` + `tests/test_audit_functions.py`**
Rollback now deletes the **exact** record id created during that run (from `import_audit.result_data`),
never re-matching by `session_name`; audit update parameterized (`$rid`/`$ts`). Test updated to the new
contract and asserts the delete/update bind params.

**M5 — transient error permanently marked a video private — `youtube/youtube.py`**
`insert_metadata_youtube_api` now only calls `mark_video_private` on definitive 403/404/
"not found"/"unauthorized"; transient failures log + skip instead of silently dropping the video forever.

**M6 — runtime state written into the source tree — `youtube/youtube.py`**
Private-video registry moved out of the package dir via `_private_videos_path()`: honors
`PRIVATE_VIDEOS_PATH`, otherwise resolves under `<repo>/data/`. Env-configurable and non-editable-install safe.

**M7 — library module global side effects — `transcribe/transcribe.py`**
Removed import-time `load_dotenv('../.env')` + root-`logging.basicConfig`; added
`logger = logging.getLogger(__name__)` (%-style); `.env` loaded only in `__main__`.

**M8 — rows without a YouTube URL silently dropped — `data/importer.py`**
Empty-`YouTube` rows now each write a `parse_youtube_id`/`skipped` `import_audit` record and are counted
in `stats["skipped"]` — every row is accounted for (no invisible provenance break).

**M9 — DOM / markup XSS in the SPA — `interface/static/app.js`**
`renderMarkdown()` now HTML-escapes as its first step (assistant/streamed output can no longer execute).
`video_id` sanitized through a new `safeVideoId()` (`^[A-Za-z0-9_-]{11}$`) at all four interpolation
sites (card onclick/data-id, youtube embed src, `askAboutVideo`, chat context tags). Replaced the
no-op `patch(ChatEngine)` test with a real behavioral test + a 413 oversized-message test.

**M10 — cross-transcript entity merging in the graph — `rag/adapters/entity_adapter.py` + `rag/graph/surreal_client.py`**
`convert_extracted_entities` stamps `metadata["source"]` (from `core.source`) onto every entity;
`SurrealDBClient.create_entity` scopes the merge (SELECT/create) by source when present — generic names
like "Insight 1" no longer merge across videos.

**M11 — `refactor_journal.py --apply` no-op stub — `scripts/refactor_journal.py`**
`--apply` now refuses (exit 1, clear message) pointing at the safe out-of-place `--build <dir>` +
`validate_journal.py` workflow; the misleading docstring was corrected. No more silent false-success.

### Deferred backlog — now all implemented (previously MINOR/MEDIUM)

- `/api/videos?q=` search mode now honors `offset`/`limit` and reports the **true** result total
  (`SearchIndex.search(limit=None)`; `Interface app.py` returns real `total`).
- `fix_scheduled_dates.py`: `.env` load made CWD-independent; `UPDATE {id}` parameterized to `UPDATE $id`.
- `apply_speaker_names.py` / `patch_whisperx.py` / `recover_whisperx.py` annotations + cleanups.
- `transcriber.find_missing_transcripts`: single-pass count (minor double-iteration removed).
- `render/renderer.py`: `course.json` `last_updated` only bumps when a module was actually created
  (idempotent scaffolding).
- `transcribe/transcribe.py`: blocking WhisperX run moved onto `asyncio.to_thread`.
- RAG: `settings.py` secrets optional at import (no import crash); transcript `date` derived
  deterministically from the filename (`_date_from_filename`) instead of `datetime.now()`.

### Earlier pass — implemented in the same day (Medium/Minor)

**Download/source:** yt-dlp UA centralized on every path; `download_audio`/`download_video` no longer
report false SUCCESS on 0-byte/missing artifacts; `channel.py`/`playlist.py` UA; `playlist.py`
`TimeoutExpired` handled; `transcribe.py` `download_audio` UA + timeout.

**Interface/chat:** `/api/audio` Range handler (suffix/open-ended/bounds/416); CORS
`allow_credentials=False`; chat session bound + size caps; chat error sanitization; `data_loader` sort
whitelist + numeric coercion + tail-window + tokenizer threshold; chat model persistence.

**Export:** HTML title/URL escaping; markdown YAML frontmatter escaping.

**Data/scripts/utils:** `--transcribe-missing` import fix; coda pagination cap + retry deadline;
`naming.slugify` no longer collapses to "" (+2 tests); `patch_whisperx` `rmtree(ignore_errors=True)`;
`importer` print→logger; `database` URL credential redaction; `youtube` lazy `pyytdata` + module logger;
`categorizer` dead code removed.

**Docs/policy:** `tests/README.md` + `tests/AGENTS.md` live test counts; `interface/AGENTS.md` API table;
root `AGENTS.md` mock-policy reconciled; `docs/REFACTOR_READINESS.md` marked a historical snapshot.

---

## Notes for the next reviewer

- Test/corpus counts are live snapshots — run `uv run pytest tests/ -q`; do not hardcode totals
  (`docs/AGENTS.md`).
- Gate workflow: `uv run pytest tests/ -q`, `uv run ruff check src/ tests/ scripts/`,
  `uv run mypy src`. Both ruff and mypy are now enforced in `.github/workflows/test.yml`.
- The v2 journal maintenance pipeline lives in `docs/JOURNAL_SCHEMA.md` and the read-only/idempotent
  gate scripts `scripts/{enrich_metadata,repair_split_transcripts,generate_journal_indexes,validate_journal}.py`.
