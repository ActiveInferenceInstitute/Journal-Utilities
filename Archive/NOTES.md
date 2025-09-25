# Transcribe a Session

## Determine the docLabel for the Session

## Download Session Audio

### Download M4A file from Youtube

### Split Up Large Session Files (Symposium)

### Upload M4A file to Arweave

## Generate Transcript

### Create the word_boost.txt file

Listen to the session and watched the scrolling transcript. Write down two kinds of phrases (one or more words):
- Important ones
- Ones that are misspelled in the scrolling CC (or seem likely to be misspelled)

don't use hyphens in the phrases

```txt
Mahault Albarracin
Active Inference
deontic value
```

save the file to the session's metadata folder: word_boost.txt

### Create the custom_spelling.csv file

A single word (no spaces nor hyphens), which (I think) is treated as case insensitive inside AssemblyAI; a comma, then a "to" word with the correct spelling.

```csv
actinf,ActInf
bayesian,Bayesian
```

save the file to the session's metadata folder: custom_spelling.txt

save the file to the session's metadata folder: speakers.csv

## Call AssemblyAI

fill in the API Key into the `authkey.txt` file

cd into the session's metadata folder

run this command:

```bash
python '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/SubmitToCloudWhisper.py' 'CCL2023-08' 'wMeQ52fdz_U1vbhGE4mmiDYCFlc1QgH3CFrv3Ah2HXg' ONLINEPATH 'https://arweave.net' AUTHKEYFILENAME '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/authkey.txt' WORD_BOOST_FILE_LIST 'word_boost.txt' SENTIMENT_ANALYSIS False IAB_CATEGORIES False CUSTOM_SPELL_BOOSTED True CUSTOM_SPELLING_FILE_LIST 'custom_spelling.csv' | tee 'trace.txt'
```

## Create the Editable Transcript

### Create an <filename> speakers.csv file

Look at `<filename>.paragSpeakers.csv` to create `<filename>.speakers.csv` in this format:

```csv
DocLabel,Speaker Label,Displayed Speaker Name,Full Speaker Name,First Turn,RangeFrom,RangeTo,Notes,,,,
CCL2023-08,A,Daniel,Daniel Friedman,00:08,,,,,,,
CCL2023-08,B,Mahault,Mahault Albarracin,00:29,,,,,,,
```

Save in the session's metadata folder

### Run the sentencesToTranscripts.py script

cd to the session's Transcripts/Prose folder and run this command:

```bash
python '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/sentencesToTranscripts.py' 'CCL2023-08' '/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/NormsScripts_Lecture/Metadata' 'CCL2023-08_wMeQ52fdz_U1vbhGE4mmiDYCFlc1QgH3CFrv3Ah2HXg.sentences.csv' INSPEAKERDIR '/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/NormsScripts_Lecture/Metadata' SPEAKERFILE 'CCL2023-08_wMeQ52fdz_U1vbhGE4mmiDYCFlc1QgH3CFrv3Ah2HXg.speakers.csv' | tee CCL2023-08.m4a_transcript.json
```

/mnt/md0/projects/ActiveInferenceJournal/Courses/ActiveInferenceForTheSocialSciences/NormsScripts_Lecture/Metadata/CCL2023-08_wMeQ52fdz_U1vbhGE4mmiDYCFlc1QgH3CFrv3Ah2HXg.speakers.csv