## TODO
- add all existing processed transcripts in Metadata and Transcripts/Prose to database that were not in initial USB card
    - Roundtable_2023.2
- add `insert_metadata_youtube_api` to `download_and_transcribe`, `pip install yt-dlp` and test
- Collect speaker information for all transcripts

---

## Notes on Steps
* download audio transcript
* run through Assembly
* create a speakers list
* generate a single source transcript
* when done, generate final MD (with or w/o terms) and SRT

## If a Single Session
* generate a Pandoc PDF
* generate a Pandoc HTML

## If a course OR Guestreams with multiple sessions
* combine into one MD
* generate Pandoc PDF
* generate Pandoc HTML
