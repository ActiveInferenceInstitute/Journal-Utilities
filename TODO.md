## TODO
- test `download_and_transcribe`, `pip install yt-dlp`
- add `ActiveInferenceJournal` paths to the session table based on session full name
    - `data/output/ActInf GuestStream 072.1 ~ Open Source AI： The truth is the first casualty in war [jI3wnTbpkNo].json`, `.simple.json`, and `.simple.txt`
    - to https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal/tree/main/GuestStream/GuestStream_072/Metadata
    - If there are multiple sub sessions, they all reside in one folder, e.g. LiveStream_017 has
    .0, .1 ...
- move `data/output` transcripts to their respective folders in `ActiveInferenceJournal`
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
