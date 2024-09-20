# Journal-Utilities
Utilities and Documentation for creating contents for the Active Inference Journal
https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal

There are two transcription methods in this repo. The first uses the AssemblyAI tools and the second runs WhisperX locally with SurrealDB for storage

---
## Assembly AI Transcription

## Installation

### Create a python virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Pandoc, XeLaTeX
Install [Pandoc](https://pandoc.org/installing.html) 

install xeLaTeX for font support:
```bash
sudo apt-get install texlive-xetex
```

## Step 1: Download Audio Transcript

Download the m4a audio file from YouTube and upload to a https accessible location.

## Step 2: Generate Single Source Transcript

### Setup environment variables
Add new row in the Coda spreadsheet:
https://coda.io/d/ActInf-Journal_dwYsKMwppRN/Tracking-Spreadsheet_supJk#_luEV4

### Run transcription
cd into the session's root folder
```bash
cd ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_1/
```

Copy transcribe command that calls `2_audio_to_markdown/SubmitToCloudWhisper.py`. Should look like this:
```bash
python '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/SubmitToCloudWhisper.py' 'cFPIP-06W' '4WKy_TVLReB2KAN6cGr5zk-GvfzfsRAihgK7Kc_Equw' ONLINEPATH 'https://arweave.net' AUTHKEYFILENAME '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/authkey.txt' WORD_BOOST_FILE_LIST 'word_boost.txt' SENTIMENT_ANALYSIS False IAB_CATEGORIES False CUSTOM_SPELL_BOOSTED True CUSTOM_SPELLING_FILE_LIST 'custom_spelling.csv' | tee 'trace.txt'
```

### Generate single source transcript

update the AssemblyAI-generated speaker labels "A" "B"... into "Daniel" "Bleu".

add words to the `word_boost.txt` file

cd into the session's metadata folder
```bash
cd metadata/
```

Copy transcribe command that calls `2_audio_to_markdown/sentenceToTranscripts.py`. Should look like this:
```bash
python '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/sentencesToTranscripts.py' 'cFPIP-06W' '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Metadata' 'cFPIP-06W_4WKy_TVLReB2KAN6cGr5zk-GvfzfsRAihgK7Kc_Equw.sentences.csv' INSPEAKERDIR '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Metadata' SPEAKERFILE 'cFPIP-06W_4WKy_TVLReB2KAN6cGr5zk-GvfzfsRAihgK7Kc_Equw.speakers.csv' | tee cFPIP-06W.m4a_transcript.json
```

## Step 5: Markdown to Final Outputs

The `parse_markdown` function in `5_markdown_to_final/markdown_transcript_parser.py` converts the markdown file to an SRT and MD file (without timestamps). `write_output_files` will save the files to disk. Look at `tests/test_output_final_artifacts.py` for usage.

In the case of a course with multiple lectures like Physics as Information Processsing , `concatenate_markdown_files` will combine the markdown files into one file. This file can then be converted to a PDF or HTML using pandoc.

### Convert Markdown to PDF

```bash
cd /mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields
pandoc --pdf-engine xelatex -f markdown-implicit_figures all_transcripts.md --lua-filter=images/scholarly-metadata.lua --lua-filter=images/author-info-blocks.lua -o all_transcripts.pdf
```

### Convert Markdown to HTML

```bash
cd /mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields
pandoc -f markdown-implicit_figures all_transcripts.md --lua-filter=images/scholarly-metadata.lua --lua-filter=images/author-info-blocks.lua -o all_transcripts.html
```

remove all instances of `/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/` from the HTML file to make the images work.


---
## Database and WhisperX Tools 2024

### Installation

#### Create Conda Environment
```bash
conda create --name whisperx python=3.10
conda activate whisperx
```

#### Install PyTorch CUDA 11.8

```bash
conda install pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
```

#### Install WhisperX
```bash
pip install git+https://github.com/m-bain/whisperx.git
pip install python-dotenv
pip install mkl==2024.0 # downgrade to fix `libtorch_cpu.so: undefined symbol: iJIT_NotifyEvent`
pip install surrealdb
pip install pyytdata
```

#### Install ffmpeg
```bash
wget -O - -q  https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz | xz -qdc| tar -x
```

#### Setup .env file

[Generate a Hugging Face Token](https://huggingface.co/settings/tokens) and accept the user agreement for the following models: [Segmentation](https://huggingface.co/pyannote/segmentation-3.0) and [Speaker-Diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)

```bash
cp .env.sample .env
```
Update `HUGGINGFACE_TOKEN` value in `.env` with your token.

Get the YouTube Data API v3 Key from https://console.developers.google.com/apis/ and update `API_KEY` value in `.env`.

### Start Database
```bash
surreal start --log trace --user root --pass root --bind 0.0.0.0:8080 rocksdb:///mnt/md0/projects/Journal-Utilities/data/database
```

### Ingest MP4 files into Database, Convert to WAV files
```bash
cd src
python ingest_db_create_wav.py
```

### Run Transcribe
```bash
cd src
python transcribe.py
```

### Query DB
```bash
surreal sql --endpoint http://localhost:8080 --username root --password root --namespace actinf --database actinf
```

### Upgrade DB
```
sudo surreal upgrade
surreal fix rocksdb://database
```

## Acknowledgements

- Initial Scripts 1 & 2, and initial README contributed by Dave Douglass, November 2022.
- Initial Scripts 5 contributed by Holly Grimm @hollygrimm, December 2023.


