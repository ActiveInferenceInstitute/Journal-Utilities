# Journal-Utilities
Utilities and Documentation for creating contents for the Active Inference Journal
https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal

## Installation

### Create a python virtual environment

```
python -m venv venv
source venv/bin/activate
```

### Install Pandoc, XeLaTeX
Install [Pandoc](https://pandoc.org/installing.html) 

install xeLaTeX for font support:
```
sudo apt-get install texlive-xetex
```

## Step 1: Download Audio Transcript

Download the audio file from YouTube and upload to a https  accessible location.

## Step 2: Generate Single Source Transcript

### Setup environment variables
Add new row in the Coda spreadsheet:
https://coda.io/d/ActInf-Journal_dwYsKMwppRN/Tracking-Spreadsheet_supJk#_luEV4

### Run transcription
cd into the session's root folder
```
cd ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_1/
```

Copy transcribe command that calls `2_audio_to_markdown/SubmitToCloudWhisper.py`. Should look like this:
```
python '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/SubmitToCloudWhisper.py' 'cFPIP-06W' '4WKy_TVLReB2KAN6cGr5zk-GvfzfsRAihgK7Kc_Equw' ONLINEPATH 'https://arweave.net' AUTHKEYFILENAME '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/authkey.txt' WORD_BOOST_FILE_LIST 'word_boost.txt' SENTIMENT_ANALYSIS False IAB_CATEGORIES False CUSTOM_SPELL_BOOSTED True CUSTOM_SPELLING_FILE_LIST 'custom_spelling.csv' | tee 'trace.txt'
```

### Generate single source transcript

update the AssemblyAI-generated speaker labels "A" "B"... into "Daniel" "Bleu".

add words to the `word_boost.txt` file

cd into the session's metadata folder
```
cd metadata/
```

Copy transcribe command that calls `2_audio_to_markdown/sentenceToTranscripts.py`. Should look like this:
```
python '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/sentencesToTranscripts.py' 'cFPIP-06W' '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Metadata' 'cFPIP-06W_4WKy_TVLReB2KAN6cGr5zk-GvfzfsRAihgK7Kc_Equw.sentences.csv' INSPEAKERDIR '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Metadata' SPEAKERFILE 'cFPIP-06W_4WKy_TVLReB2KAN6cGr5zk-GvfzfsRAihgK7Kc_Equw.speakers.csv' | tee cFPIP-06W.m4a_transcript.json
```

## Step 5: Markdown to Final Outputs

The `parse_markdown` function in `5_markdown_to_final/markdown_transcript_parser.py` converts the markdown file to an SRT and MD file (without timestamps). `write_output_files` will save the files to disk. Look at `tests/test_output_final_artifacts.py` for usage.

In the case of a course with multiple lectures like Physics as Information Processsing , `concatenate_markdown_files` will combine the markdown files into one file. This file can then be converted to a PDF or HTML using pandoc.

### Convert Markdown to PDF

```
cd /mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields
pandoc --pdf-engine xelatex -f markdown-implicit_figures all_transcripts.md --lua-filter=images/scholarly-metadata.lua --lua-filter=images/author-info-blocks.lua -o all_transcripts.pdf
```

### Convert Markdown to HTML

```
cd /mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields
pandoc -f markdown-implicit_figures all_transcripts.md --lua-filter=images/scholarly-metadata.lua --lua-filter=images/author-info-blocks.lua -o all_transcripts.html
```

remove all instances of `/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/` from the HTML file to make the images work.


## Acknowledgements

- Initial Scripts 1 & 2, and initial README contributed by Dave Douglass, November 2022.
- Initial Scripts 5 contributed by Holly Grimm @hollygrimm, December 2023.


