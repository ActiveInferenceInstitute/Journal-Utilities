# ActiveInferenceJournal — v2 Schema (agent- & program-navigable)

Target schema for the refactor of the `ActiveInferenceJournal` repo. Goal: uniform,
flat, machine-readable item folders with a canonical `metadata.json`, no placeholder
cruft, audio kept off `main`, and top-level indexes.

## Top-level namespace

Content is source-namespaced so other channels and non-video sources coexist:

```
data/video/activeinferenceinstitute/<Series>/...   # this channel
data/video/<other-channel>/...                      # other YouTube channels
data/<other-type>/<source>/...                      # non-video sources
docs/                                               # technical documentation
INDEX.json  INDEX.md  README.md                     # top level
```

Every non-duplicate channel video is represented (idempotent build from the JU channel
manifest + transcripts); deliberate secondary copies carry `duplicate_of` and are
excluded from coverage counts. Uncategorized videos live under
`<namespace>/Other/<video_id>/`.

## Per-item folder

```
data/video/activeinferenceinstitute/<Series>/<Series>_<NNN[.E]>/
  metadata.json        # canonical record (see below) — single source of truth
  README.md            # generated human nav: title(s), date, links, contents
  transcript.txt       # clean text (per part: "## Part N" headers when multi-part)
  transcript.json      # timestamped segments (array; part-tagged)
  captions/            # original-language *.srt
  translations/        # translated *.srt (one per language) — preserved verbatim
  assets/
    images/   html/   prose/   appendices/   bibliography/   # curated content, by type
  # audio/ is NOT on main (gitignored). The `audio` branch carries audio/<video_id>.64k.m4a
```

### `metadata.json`

```json
{
  "series": "GuestStream",
  "item": "GuestStream_094",
  "title": "ActInf GuestStream 094 ~ ...",
  "source": "youtube",
  "channel": "ActiveInferenceInstitute",
  "parts": [
    {"part": "094.1", "video_id": "1Qr7um2W-Rc",
     "url": "https://www.youtube.com/watch?v=1Qr7um2W-Rc",
     "title": "...", "published": "2026-..", "duration": 0,
     "has_transcript": true, "has_captions": true, "has_audio": true}
  ]
}
```

## Enrichment fields

`scripts/enrich_metadata.py` owns the enrichment fields in `metadata.json` and keeps
URL fields URL-only. Non-URL Coda display text is preserved as `slides_label` or
`paper_title`; placeholder values such as `n/a` are omitted. `duplicate_of` identifies
a deliberate secondary copy whose video ID is also present on the canonical item.

The derived indexes are regenerated with:

```bash
python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal
python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal --check
```

`INDEX.json` contains `count`, `videos` (part records, including deliberate duplicates),
`unique_videos`, and item records.

Split-file transcript records use their session identity (`<video_id>_sessNN`) in both
the `transcript.txt` headings and `transcript.json` `video_id` fields. Repair derived
outputs with `scripts/repair_split_transcripts.py` when source session pairs are present.

## Top-level

- `INDEX.json` — machine index: every item + parts + paths + flags, including record and
  unique-video counts.
- `INDEX.md` — human index grouped by series.
- `SCHEMA.md` — this spec (mirrored into the journal repo).
- `sources/` — registry of channels/sources (channel id → series rules) so other
  open-source sources plug in (Institute-first, source-pluggable).

## Refactor rules (non-destructive)

- Drop placeholders: `blank_document.txt`, `blank.txt`, empty `.gitkeep`-only dirs.
- `Metadata/<item>.json` → `metadata.json` parts; `*.simple.txt` → `transcript.txt`;
  timestamped json → `transcript.json`.
- `Captions/`, `Transcripts/Captions/` `*.srt` → `captions/`.
- `Translations/*.srt` → `translations/` (verbatim).
- `Images/`→`assets/images/`, `HTML/`/`Transcripts/HTML/`→`assets/html/`,
  `Transcripts/Prose/`/`Prose/`→`assets/prose/`, `Appendices/`→`assets/appendices/`,
  `Bibliographic Information/`→`assets/bibliography/`. `pdf/odt/zip` → `assets/` by type.
- `Audio/*.m4a` → moved to the `audio` branch as `audio/<video_id>.64k.m4a`; removed from `main`.
- **Coverage invariant:** every non-duplicate channel video is a part in exactly one
  canonical item; `duplicate_of` records are excluded from coverage reconciliation.
- **File invariant:** every non-placeholder source file is accounted for (moved or
  intentionally dropped). The converter's `--dry-run` reports any unmapped file.
```
