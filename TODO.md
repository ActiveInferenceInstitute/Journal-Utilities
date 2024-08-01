## TODO
- move `data/output` transcripts to their respective folders in `ActiveInferenceJournal`
    - Livestream done
    - Applied Active Inference Symposium
    - BookStream
    - Courses/ActiveInferenceForTheSocialSciences
    - Courses/PhysicsAsInformationProcessing_ChrisFields
    - GuestStream
    - Insights
    - MathStream
    - ModelStream
    - OrgStream
    - ReviewStream
    - Roundtable
    - TextbookGroup/ParrPezzuloFriston2022/Cohort_
    - Twitter Spaces
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
