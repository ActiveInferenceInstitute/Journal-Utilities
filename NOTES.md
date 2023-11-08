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

### Create the custom_spelling.txt file

A single word (no spaces nor hyphens), which (I think) is treated as case insensitive inside AssemblyAI; a space character, then a "to" word with the correct spelling.

```txt
actinf ActInf
bayesian Bayesian
```

save the file to the session's metadata folder: custom_spelling.txt

### Create an speakers.csv file

```csv
DocLabel,Speaker Label,Displayed Speaker Name,Full Speaker Name,First Turn,RangeFrom,RangeTo,Notes,,,,
CCL2023-08,A,Daniel,Daniel Friedman,00:08,,,,,,,
CCL2023-08,B,Mahault,Mahault Albarracin,00:29,,,,,,,
```

save the file to the session's metadata folder: speakers.csv

## Call AssemblyAI

fill in the API Key into the `authkey.txt` file

cd into the session's metadata folder

run this command:

```bash
python '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/SubmitToCloudWhisper.py' 'CCL2023-08' 'wMeQ52fdz_U1vbhGE4mmiDYCFlc1QgH3CFrv3Ah2HXg' ONLINEPATH 'https://arweave.net' AUTHKEYFILENAME '/mnt/md0/projects/Journal-Utilities/2_audio_to_markdown/authkey.txt' WORD_BOOST_FILE_LIST 'word_boost.txt' SENTIMENT_ANALYSIS False IAB_CATEGORIES False CUSTOM_SPELL_BOOSTED True CUSTOM_SPELLING_FILE_LIST 'custom_spelling.txt' | tee 'trace.txt'
```