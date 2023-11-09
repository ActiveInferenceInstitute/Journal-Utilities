#! ...python3

# DEFECTS
#   1. Timestamps in generated .SRT should align with upstream SRT (so open this if present).
#       Same for .MD, as far as possible.
#   2. ALLOW several formats of timestamp in inputs to all processing.
#   3. CREATE convenient-timestamp formats everywhere.
#   4. Directly put out .json dumps of main, sentences, paragraphs return values
#       Coded.
#   5. Dump only skeleton of trace to sysout (related to (4))
#   6. Allow optional sources: 6a. work ID in AssemblyAI's cloud (bypass Step 1)
#      6b. Local json/txt file (if 'dirty,' i.e. old ".json" then search for indicated content)
#   7. Optional "raw" alternate input in any of several formats. Normalize punctuation, capitalization (per options)
#      7a. Scraped YouTube transcript.
#      7b. Adobe 
#   8. If alternate input is present, optionally (a) insert {}, [], [[]] (this with overridable default trigger length)
#      8b. Explicit CHANGES output
#   9. Suppress spurious sentence breaks, e.g. at NEVEREOS punctuation where following fragment starts with lower case (or non-cap)
#      9b. Allow more aggressive sentence-integrity logic; may rely on reparsing.
#   10. More flexible sentence numbering, with explicit start and increment numbers.

# cd "/mnt/d/Documents/FEP-AI/2022 Livestreams/ls042/ls042-0"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls042-0" "http://crisiscenter.us/AILab01/2022Livestreams" "ls042-0.m4a" | tee ls042-0_whisper_m4a.json &

# For more logic, see "Transcribe ls036 Modelling ourselves.txt" in "D:\Documents\FEP-AI\2022 Livestreams\ActInf Livestream #036 Modeling Ourselves"

import requests
import time
from datetime import datetime
import sys
import math
import csv
import json as jsfmt
import re


#call with python3 - BerlinSym2021KJFKey "http://crisiscenter.us/AILab01/Karl_Friston_Applied_Active_Inference_Symposium_2021-06-22" "Quadrille.wav"
#call with python3 - quadriTest "http://crisiscenter.us/AILab01/Karl_Friston_Applied_Active_Inference_Symposium_2021-06-22" "Quadrille.wav"	rzw49dpr1n-4856-4172-adf4-e502720c93de

#call with python3 - ls051-0 "http://crisiscenter.us/AILab01/2022Livestreams" "ls051-0.wav"	rskfsnu6hj-8e56-4c7d-a4d1-76aa04ab873a
#call with python3 - ls051-0-2 "http://crisiscenter.us/AILab01/2022Livestreams" "ls051-0-2.mp3"	rsk599qwnx-7e0e-49c2-bafd-8cb0ad4745db

#python3 - ls036-0 "http://crisiscenter.us/AILab01/2022Livestreams" "ls036-0.m4a"
#call with python3 - "ls036-2" "http://crisiscenter.us/AILab01/2022Livestreams" "ls036-2.m4a"

if __name__ == "__main__":
    print(f'Arguments count: {len(sys.argv)}')
    if len(sys.argv) < 3:
        print("Need at least docLabel, onlinePath, and onlineFile; exiting!")
        quit()
    
#
dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# modifiable globals
## affect transcription call
useThisAuthKey        = ""
authKeyFilename       = ""
auto_highlights_value = True
language_model        = "medium"     # "large"  "medium"
boost_param_value     = "default"           # "default" "high"
language_detection    = False
speaker_labels_value  = True         # not yet supported for Portuguese
entity_detection_value = True
iab_categories_value  = False
auto_chapters_value   = True
sentiment_analysis_value = False
language_code         = "en_us"

##
onlinePath            = ""          # used only when initially invoking transcription
outputPath            = "."
transcriptId          = ""
custom_spell_boosted  = False       # should we add any single-word word_boost to custom_spelling, if non-trivial?
# audio_start_from    = 0         # presence is trigger
# audio_end_at        = 0         # presence is trigger
# speech_threshold    = 0.9461       # presence is trigger
# punctuate           = True      # False
# format_text         = True      # False
# dual_channel      = True       # presence is trigger
# disfluencies      = True       #      presence is trigger
# redact_pii (complex)
# filter_profanity  = True

vaultDir        = ""
authKeyFilename = "acIIAuthKey.txt"     # holds AssemblyAI authorization key belonging to Active Inference Institute
#       "5a03************************fd34"     # "1b98************************2e40"
#       davesAuthKey = "30e7************************5b88"   # old "69a8************************80a5"
#       useThisAuthKey = acIIAuthKey

# populable globals
word_boost_list           = []
boost_param               = []
word_boost_file_list      = []
custom_spelling_list      = []
custom_spelling_file_list = []

# static globals
lookupWordPat = r"\b(a|an|the|of|in|and|is|to|it|that|this|for|with|on|from|by|at|as|but|they|not|or|we|you|i|he|she|me|him|her|my|your|their|our|us|them|some|any|all|many|much|few|each|every|other)\b"


#       Note: Please make sure to import the required libraries, such as `re` for regular expressions, before using this translated function. Additionally, this translation assumes that the `maybeNorms` variable and related commented logic are not necessary for the Python implementation.
def get_input_options(scl):
    global vaultDir, authKeyFilename, word_boost_file_list, custom_spelling_file_list, custom_spell_boosted
    global boost_param, outputPath, cap_files, index_files, onlinePath
    global parse_map_files, language_detection
    global language_code, language_model, wordBoostList

    scl_len = len(scl)
    # ii typically = 4 
    return_dict = {}
    ii = 0
    while ii < scl_len:
        label = scl[ii].upper()     # .replace("_","")
        value = scl[ii + 1].strip()
        ii += 2
        
        #if label == "TRANSCRIPTS":
        #    if ":" in value:
        #        file_names = value.split(":")
        #    else:
        #        file_names = [value]
        #    return_dict["transcripts"] = file_names
        
        if label == "OUTPUTPATH":
            outputPath = value
            return_dict["OUTPUTPATH"] = outputPath
        
        elif label == "VAULTDIR":   # override directory to hide secrets
            vaultDir = value
            return_dict["VAULTDIR"] = vaultDir
        
        elif label == "AUTHKEYFILENAME":    # override name of file (in vault) holding AssemblyAI authorization key
            authKeyFilename = value
            return_dict["AUTHKEYFILENAME"] = authKeyFilename
        
        elif label == "ONLINEPATH":
            onlinePath = value
            return_dict["ONLINEPATH"] = onlinePath
        
        elif label == "CAPFILES":
            if ":" in value:
                cap_files = value.split(":")
            else:
                cap_files = [value]
            return_dict["CAPFILES"] = cap_files
        
        elif label == "PARSEMAPFILES":
            if ":" in value:
                parse_map_files = value.split(":")
            else:
                parse_map_files = [value]
            return_dict["PARSEMAPFILES"] = parse_map_files
        
        elif label == "INDEXES":
            if ":" in value:
                index_files = value.split(":")
            else:
                index_files = [value]
            return_dict["INDEXES"] = index_files
        
        elif label == "WORD_BOOST_FILE_LIST":
            if ":" in value:
                word_boost_file_list = value.split(":")
            else:
                word_boost_file_list = [value]
            return_dict["WORD_BOOST_FILE_LIST"] = word_boost_file_list
        
        elif label == "CUSTOM_SPELLING_FILE_LIST":
            if ":" in value:
                custom_spelling_file_list = value.split(":")
            else:
                custom_spelling_file_list = [value]
            return_dict["CUSTOM_SPELLING_FILE_LIST"] = custom_spelling_file_list
      
        elif label == "BOOST_PARAM":
            boost_param = value.strip()
            return_dict["BOOST_PARAM"] = boost_param
        
        elif label == "LANGUAGE_MODEL":
            language_model = value.strip()
            return_dict["LANGUAGE_MODEL"] = language_model
        
        elif label == "LANGUAGE_CODE":
            language_code = value.strip()
            return_dict["LANGUAGE_CODE"] = language_code
        
        elif label == "INDEXES":
            if ":" in value:
                index_files = value.split(":")
            else:
                index_files = [value]
            return_dict["INDEXES"] = index_files
        
        elif label == "OPTIONS":
            options = value.split(" ")
            return_dict["OPTIONS"] = options

        elif label == "TRANSCRIPTID":
            transcriptId = value
            return_dict["TRANSCRIPTID"] = transcriptId

        elif label == "AUDIO_START_FROM":
            audio_start_from = value
            return_dict["AUDIO_START_FROM"] = audio_start_from

        elif label == "AUDIO_END_AT":
            audio_end_at = value
            return_dict["AUDIO_END_AT"] = audio_end_at
        #
        elif label == "AUTO_CHAPTERS":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                auto_chapters_value = True
                return_dict["AUTO_CHAPTERS"] = auto_chapters_value
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                auto_chapters_value = False
                return_dict["AUTO_CHAPTERS"] = auto_chapters_value
            #
        elif label == "CUSTOM_SPELL_BOOSTED":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                custom_spell_boosted = True
                return_dict["CUSTOM_SPELL_BOOSTED"] = custom_spell_boosted
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                custom_spell_boosted = False
                return_dict["CUSTOM_SPELL_BOOSTED"] = custom_spell_boosted
            #
        elif label == "AUTO_HIGHLIGHTS":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                auto_highlights_value = True
                return_dict["AUTO_HIGHLIGHTS"] = auto_highlights_value
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                auto_highlights_value = False
                return_dict["AUTO_HIGHLIGHTS"] = auto_highlights_value
            #
        elif label == "DISFLUENCIES":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                disfluencies = True
                return_dict["DISFLUENCIES"] = disfluencies
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                disfluencies = False
                return_dict["DISFLUENCIES"] = disfluencies
            #
        elif label == "DUAL_CHANNEL":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                dual_channel = True
                return_dict["DUAL_CHANNEL"] = dual_channel
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                dual_channel = False
                return_dict["DUAL_CHANNEL"] = dual_channel
            #
        elif label == "ENTITY_DETECTION":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                entity_detection_value = True
                return_dict["ENTITY_DETECTION"] = entity_detection_value
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                entity_detection_value = False
                return_dict["ENTITY_DETECTION"] = entity_detection_value
            #
        elif label == "FILTER_PROFANITY":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                filter_profanity = True
                return_dict["FILTER_PROFANITY"] = filter_profanity
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                filter_profanity = False
                return_dict["FILTER_PROFANITY"] = filter_profanity
            #
        elif label == "FORMAT_TEXT":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                format_text = True
                return_dict["FORMAT_TEXT"] = format_text
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                format_text = False
                return_dict["FORMAT_TEXT"] = format_text
            #
        elif label == "IAB_CATEGORIES":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                iab_categories_value = True
                return_dict["IAB_CATEGORIES"] = iab_categories_value
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                iab_categories_value = False
                return_dict["IAB_CATEGORIES"] = iab_categories_value
            #
        elif label == "LANGUAGE_DETECTION":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                language_detection = True
                return_dict["LANGUAGE_DETECTION"] = language_detection
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                language_detection = False
                return_dict["LANGUAGE_DETECTION"] = language_detection
            #
        elif label == "PUNCTUATE":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                punctuate = True
                return_dict["PUNCTUATE"] = punctuate
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                punctuate = False
                return_dict["PUNCTUATE"] = punctuate
            #
        elif label == "SENTIMENT_ANALYSIS":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                sentiment_analysis_value = True
                return_dict["SENTIMENT_ANALYSIS"] = sentiment_analysis_value
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                sentiment_analysis_value = False
                return_dict["SENTIMENT_ANALYSIS"] = sentiment_analysis_value
            #
        elif label == "SPEAKER_LABELS":
            if value in ['True', 'Y', 'YES', 'TRUE', 1, '1', 'T']:
                speaker_labels_value = True
                return_dict["SPEAKER_LABELS"] = speaker_labels_value
            elif value in ['False', 'N', 'NO', 'FALSE', 0, '0', 'F']:
                speaker_labels_value = False
                return_dict["SPEAKER_LABELS"] = speaker_labels_value
            #
        #
    #
    return return_dict
#


#for i, arg in enumerate(sys.argv):
#    print(f'Argument {i:>6}: {arg}')

docLabel   = sys.argv[1]
onlineFile = sys.argv[2]    # only mandatory use is to generate file names. May also be name of actual online file.
#onlinePath = sys.argv[2]    # used only if actually fetching data from an online file.
#onlineFile = sys.argv[3]    # only mandatory use is to generate file names. May also be name of actual online file.
print("docLabel, onlineFile " + "'" + docLabel + "', '" + onlineFile + "'")
if len(sys.argv) > 3:           # optional component of argv is flat property value list
    inputParams = sys.argv[3:]
    print(f'inputParams: {inputParams}')
    # fetch keyword parameters
    inputOptions = get_input_options(inputParams)  # directly sets several globals; ignore first two (explicit) incoming args
    #outputPath = sys.argv[4]
    #print("outputPath: " + "'" + outputPath + "'")
    print("All keyword parameters, aka 'inputOptions'")
    print(inputOptions)

    # Fetch all resources indicated in parameters
    #print("word_boost_file_list")
    #print(word_boost_file_list)
    #print()
    
    customSpellDict = {}
    for wordBoostFile in word_boost_file_list:
        file = open(wordBoostFile, mode='r', newline=None)
        boostWords = file.readlines()        # read all lines at once
        #print("boostWords")
        #print(boostWords)
        file.close()
        for boostWord in boostWords:
            boostWord = boostWord.strip()
            #print(boostWord)
            if boostWord[0:1] != "#":    # suppress this line
                if boostWord not in word_boost_list:
                    word_boost_list.append(boostWord)
                    #custom_spelling_list.append({"from": [boostWord.lower()], "to": boostWord},)
                    if custom_spell_boosted:
                        if len(boostWord.split()) == 1:      # single word
                            boostWordLower = boostWord.lower()
                            if boostWordLower != boostWord:
                                if boostWord in customSpellDict:
                                    if boostWordLower not in customSpellDict[boostWord]:
                                        customSpellDict[boostWord].append(boostWordLower)
                                    #
                                else:
                                    customSpellDict[boostWord] = [boostWordLower]
                            #
                        #
                    #
                #custom_spelling_list.append({"from": [boostWord.lower()], "to": boostWord},)
                #{"from": ["fristen", "friston"], "to": "Friston"},
            #
        #
    #
    print()
    #print("customSpellDict from word_boost:")
    #print(customSpellDict)
    #print()
    
    #print("word_boost_list:")
    #print(word_boost_list)
    #print()
    
    for customSpellingFile in custom_spelling_file_list:
        file = open(customSpellingFile, "r", newline=None)
        customSpellings = file.readlines()        # read all lines at once
        #print("boostWords")
        #print(boostWords)
        file.close()
        for customSpelling in customSpellings:
            #print(customSpelling)
            customSpellingPieces = customSpelling.strip("\n").split()
            #print(customSpellingPieces)
            customSpellingFrom = customSpellingPieces[0]   #.strip("\n")
            #print(customSpellingFrom)
            if customSpellingFrom[0:1] != "#":
                customSpellingTo   = customSpellingPieces[1]   #.strip()
                #print(customSpellingTo)
                #custom_spelling_list.append({"from": [customSpellingFrom], "to": customSpellingTo})
                if customSpellingTo in customSpellDict:
                    if customSpellingFrom not in customSpellDict[customSpellingTo]:
                        customSpellDict[customSpellingTo].append(customSpellingFrom)
                    #
                else:
                    customSpellDict[customSpellingTo] = [customSpellingFrom]
                #
            #
        #
    #
    customSpellDictKeys = customSpellDict.keys()
    for customSpellingTo in customSpellDictKeys:
        custom_spelling_list.append({"from": customSpellDict[customSpellingTo], "to": customSpellingTo})
        #    for customSpellingFrom in customSpellDict[]
    #
    #custom_spelling_list.append({"from": [customSpellingFrom], "to": customSpellingTo})
    #
#



# ---------------------


def ToDisplayTime(tt):
    ts=float(tt)
    h0=int(ts/3600000.0)
    hh=""
    if h0 > 9:
        hh = str(100+h0)
        hh = hh[1:3] + ":"
    elif h0 > 0:
        hh = str(h0) + ":"
    
    m0=int( (ts-(3600000.0*h0))/60000.0)
    mm=str(100+m0)
    s0=int( (ts - (3600000.0*h0) - (60000.0*m0) ) /1000.0)
    ss=str(100+s0)
    to_time= hh + mm[1:3] + ":" + ss[1:3]
    return to_time


def ToSRTTime(tt):
    ts=float(tt)
    h0=int(ts/3600000.0)
    hh = str(100+h0)
    m0=int( (ts-(3600000.0*h0))/60000.0)
    mm=str(100+m0)
    s0=int( (ts - (3600000.0*h0) - (60000.0*m0) ) /1000.0)
    ss=str(100+s0)
    mms0=int(ts - (3600000.0*h0) - (6000*m0) - s0)
    mms=str(1000+mms0)
    to_time= hh[1:3] + ":" + mm[1:3] + ":" + ss[1:3] + "," + mms[1:4]
    return to_time


#   append string to list "called by name"
def appendToList(name, list):
    if name not in list:
        list.append(name)
#
#Here's the translation of the Wolfram Language function `loadIndexes` to Python:

def loadIndexes(indexFileName):
    phrasesToIndex = {}
    maxPhraseLen = 100  # assuming a maximum phrase length

    with open(indexFileName, 'r') as file:
        file.readline()  		# skip header
        indexLineNum = 0
        line = file.readline().strip()
        while line:
            indexLineNum += 1
            indexFields = line.split("\t")
            keyPhrase = indexFields[0].strip()
            keyWordCount = len(keyPhrase.split())
            if keyWordCount > maxPhraseLen:		# skip ignore too-long phrases
                line = file.readline().strip()
                continue

            keyWord1 = keyPhrase.split()[0].lower()
            keyWord1 = re.sub(lookupWordPat, "", keyWord1.strip())
            keyWord0 = keyWord1

            if keyWord0 != keyWord1:
                pass
                # Handle WordStem logic if needed
                # e.g., keyWord0 = WordStem(keyWord1)
                # if keyWord1 not in maybeNorms:
                #     maybeNorms[keyWord1] = keyWord0

            reference = indexFields[1].strip()

            if keyWord1 not in phrasesToIndex:
                phrasesToIndex[keyWord1] = {keyWordCount: [keyPhrase]}
            else:
                if keyWordCount not in phrasesToIndex[keyWord1]:
                    phrasesToIndex[keyWord1][keyWordCount] = [keyPhrase]
                else:
                    phrasesToIndex[keyWord1][keyWordCount].append(keyPhrase)

            line = file.readline().strip()

    return phrasesToIndex
#

# ---------------------


#"audio_url": " + onlinePath + "/" + onlineFile + ",
#"audio_url": "http://crisiscenter.us/AILab01/Karl_Friston_Applied_Active_Inference_Symposium_2021-06-22/Quadrille.wav",

endpoint = "https://api.assemblyai.com/v2/transcript"
audio_url = onlinePath + "/" + onlineFile

#    "speaker_labels": True,

# for a fatter list - one containing an error - see "SubmitToCloudWhisper - Copy (13) - Try word_boost, spell again.py"

if len(transcriptId) == 0:      # need AssemblyAI authKey
    #vaultDir        = "/mnt/d/Documents/FEP-AI/ActiveInferenceVault/"
    print("authKeyFilename:")
    print(authKeyFilename)
    authKeyFilePath = vaultDir + authKeyFilename
    file = open(authKeyFilePath, "r", newline=None)
    useThisAuthKey = file.read().strip("\n")        # read all lines at once
    #print("useThisAuthKey")    # No, do not print the KEY!!!
    file.close()
#

if len(transcriptId) == 0:
    #print()
    #print("word_boost_list:")
    #print(word_boost_list)
    #print()
    #print("custom_spelling_list:")
    #print(custom_spelling_list)
    #print()

    json = {
        "audio_url":       audio_url,
        "word_boost":      word_boost_list,
        "custom_spelling": custom_spelling_list,
        #"summarization": True,
        #"summary_type": "bullets",
        #"content_safety": True,
        "auto_highlights": auto_highlights_value,
        "language_model":  language_model,     # "large"  "medium"
        "boost_param": boost_param_value,           # "default" "high"
        "speaker_labels": speaker_labels_value,         # not yet supported for Portuguese
        "entity_detection": entity_detection_value,
        "iab_categories": iab_categories_value,
        "auto_chapters": auto_chapters_value,
        "sentiment_analysis": sentiment_analysis_value,
        "language_code": language_code        #"pt"
        }

    print("json to AssemblyAI:")
    print(json)
    #quit()


    #headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a","content-type": "application/json"}
    headers = {"authorization": useThisAuthKey,"content-type": "application/json"}
    response = requests.post(endpoint, json=json, headers=headers)                      # critical API call
    #print(response.json())
    jj=response.json()
    transcriptId=jj.get('id')
    print(transcriptId)
    myStatus=jj.get('status')
    print(myStatus)
    time.sleep(30)
else:
    myStatus = "processing"
#

import requests
import time
import sys

#transcriptId = "rsuh9skgre-a056-486e-8138-2e6608d21f04"
while myStatus == "queued" or myStatus == "processing":
    time.sleep(120)
    endpoint = "https://api.assemblyai.com/v2/transcript/" + transcriptId
    headers = {"authorization": useThisAuthKey}
    response = requests.get(endpoint, headers=headers)
    #print(response.json())
    jj=response.json()
    myStatus=jj.get('status')
    print(myStatus)

#headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a"}

print()
print()
print("Dump JSON response:")
#print(jj)
print()
print(transcriptId)
print(myStatus)

# dump JSON direct from AssemblyAI return
mainJsonPubPath = docLabel + "_" + onlineFile + "_trace.main.json"
mjf = open(mainJsonPubPath, "w")
mjf.write(jsfmt.dumps(jj))
mjf.close()


if myStatus != "completed":
    myError = jj.get('error')
    print()
    print("Bad results from last main poll. Call if you find work.")
    print(myError)
    quit()

# ----------- words (apparently always identical to those from paragraphs) ----------

wordFileName = docLabel + "_" + onlineFile + ".words.csv"
#wwf = open(wordFileName, "w")

#words = jj.get('words')

#for count, word in enumerate(words):
#    wtext=word.get('text')
#    wstart=word.get('start')
#    wend=word.get('end')
#    wconfid=word.get('confidence')
#    wspeaker=word.get('speaker')
#    #
#    wordOut = str(wstart) + "\t" + str(wend) + "\t"
#    if wspeaker != None:
#        wordOut = wordOut + wspeaker
#    
#    #
#    wordOut = wordOut + "\t" + str(wconfid) + "\t"
#    if wtext != None:
#        wordOut = wordOut + wtext
#    
#    #
#    #wordOut = str(wstart) + "\t" + str(wend) + "\t" + wspeaker + "\t" + str(wconfid) + "\t" + wtext    
#    wwf.write(wordOut)	#    #print(utterOut)	, delimiter='\t', lineterminator='\t\n'
#    wwf.write("\r\n")

#wwf.close()


# ----------- IAB categories ----------
if iab_categories_value:
    iabCats = jj.get('iab_categories_result')
    catStatus=iabCats.get('status')
    if catStatus == 'success':
        catDetFileName = docLabel + "_" + onlineFile + ".categoryDetails.csv"
        cdf = open(catDetFileName, "w")
        catDetOut = "start" + "\t" + "end" + "\t" + 'relevance' + "\t" + 'label'
        cdf.write(catDetOut)
        cdf.write("\r\n")
        catDetails=iabCats.get('results')
        for rCount, cDKey in enumerate(catDetails):     # retrieve by POSITION
            #for count, cKey in enumerate(cDKey):            # retrieve by KEY
            cTKey  = cDKey.get('timestamp')
            #print(cTKey)
            cStart = cTKey.get('start')         # will use same timestamps for all label/relevance pairs
            #print(cStart)
            cEnd   = cTKey.get('end')
            #print(cEnd)
            cLabels  = cDKey.get('labels')
            #print(cLabels)
            for labelCount, labelPair in enumerate(cLabels):    # retrieve by POSITION
                cRelev = labelPair.get('relevance')
                cLabel = labelPair.get('label')
                catDetOut = str(cStart) + "\t" + str(cEnd) + "\t" + str(cRelev) + "\t" + str(cLabel)
                #print(catDetOut)
                cdf.write(catDetOut)	#    print(utterOut)	, delimiter='\t', lineterminator='\t\n'
                cdf.write("\r\n")
        
        cdf.close()

    # also (separately) save summaries (i.e. session-level IAB categories)
    if catStatus == 'success':
        catFileName = docLabel + "_" + onlineFile + ".categories.csv"
        ccf = open(catFileName, "w")
        catOut="key" + "\t" + "relevance"
        ccf.write(catOut)	#    print(utterOut)	, delimiter='\t', lineterminator='\t\n'
        ccf.write("\r\n")
        summaries=iabCats.get('summary')
        summKeys=summaries.keys()
        for count, cKey in enumerate(summKeys):
            cRelev=summaries.get(cKey)
            catOut=cKey + "\t" + str(cRelev)
            ccf.write(catOut)	#    print(utterOut)	, delimiter='\t', lineterminator='\t\n'
            ccf.write("\r\n")
        #
        ccf.close()
    #
#
# ----------- chapters ----------
chapterVec = []
chapterVecs = []
if auto_chapters_value:
    chapFileName = docLabel + "_" + onlineFile + ".chapters.csv"
    ccf = open(chapFileName, "w")

    chapters = jj.get('chapters')   # also insert timestamp
    #write header
    chapterOut = "start" + "\t" + "end" + "\t" + "startTime" + "\t" + "summary" + "\t" + "headline" + "\t" + "gist"
    ccf.write(chapterOut)
    ccf.write("\r\n")

    for count, chapter in enumerate(chapters):
        cSummary=chapter.get('summary')
        cHeadline=chapter.get('headline')
        cGist=chapter.get('gist')
        cStart=chapter.get('start')
        cStartTime = ToDisplayTime(cStart)     #supplement with legible timestamp
        cEnd=chapter.get('end')
        chapterOut = str(cStart) + "\t" + str(cEnd) + "\t" + str(cStartTime) + "\t" + cSummary + "\t" + cHeadline + "\t" + cGist
        ccf.write(chapterOut)
        ccf.write("\r\n")
        chapterVec=[cStart, cEnd, cSummary, cHeadline, cGist]
        chapterVecs.append(chapterVec)
    ccf.close()
#

# ----------- sentiment analysis ----------

if sentiment_analysis_value:
    ss=jj.get('sentiment_analysis_results')
    #print(ss)

    #   Better to use CSV package throughout!
    #with open('records.tsv', 'w', newline='') as tsvfile:
    #    writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
    #    for record in SeqIO.parse("/home/fil/Desktop/420_2_03_074.fastq", "fastq"):
    #        writer.writerow([record.id, record.seq, record.format("qual")])

    sentimentFileName = docLabel + "_" + onlineFile + ".sentiments.csv"
    ssf = open(sentimentFileName, "w")

    sentimOut = "start" + "\t" + "end" + "\t" + "speaker" + "\t" +  'sentiment' + "\t" + "confidence" + "\t" + "text"
    ssf.write(sentimOut)	#    print(sentimOut)	, delimiter='\t', lineterminator='\t\n'
    ssf.write("\r\n")

    #with open(sentimentFileName, 'w', encoding='utf8', newline='') as csvfile:
    #    writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    #    writer.writeheader(["start","end","speaker","sentiment","confidenct","text"])
    #    #for record in SeqIO.parse("/home/fil/Desktop/420_2_03_074.fastq", "fastq"):
    #        writer.writerow([record.id, record.seq, record.format("qual")])

    for count, sentim in enumerate(ss):
        stext = sentim.get('text')
        sstart = sentim.get('start')
        send = sentim.get('end')
        ssentim = sentim.get('sentiment')
        sconfid = sentim.get('confidence')
        sspeaker = sentim.get('speaker')
        #sentimOut = str(sstart) + "\t" + str(send) + "\t" + sspeaker + "\t" + ssentim + "\t" + str(sconfid) + "\t" + stext
        sentimOut = str(sstart) + "\t" + str(send) + "\t"
        if sspeaker != None:
            sentimOut = sentimOut + sspeaker
        
        #
        sentimOut = sentimOut + "\t" + str(sconfid) + "\t" + stext
        ssf.write(sentimOut)	#    print(sentimOut)	, delimiter='\t', lineterminator='\t\n'
        ssf.write("\r\n")

    ssf.close()
#

# ----------- utterances ----------
#if utterances...
utteranceFileName = docLabel + "_" + onlineFile + ".utterances.csv"
uuf = open(utteranceFileName, "w")

utterOut = "start" + "\t" + "end" + "\t" + "speaker" + "\t" + "confidence" + "\t" + "text"
uuf.write(utterOut)	#    print(utterOut)	, delimiter='\t', lineterminator='\t\n'
uuf.write("\r\n")

utterances = jj.get('utterances')

for count, utterance in enumerate(utterances):
    uconfid = utterance.get('confidence')
    uend = utterance.get('end')
    uspeaker = utterance.get('speaker')    
    ustart = utterance.get('start')
    utext = utterance.get('text')
    #utterOut = str(ustart) + "\t" + str(uend) + "\t" + uspeaker + "\t" + str(uconfid) + "\t" + utext
    utterOut = str(ustart) + "\t" + str(uend) + "\t"
    if uspeaker != None:
        utterOut = utterOut + uspeaker
    
    #
    utterOut = utterOut + "\t" + str(uconfid) + "\t" + utext
    uuf.write(utterOut)	#    print(utterOut)	, delimiter='\t', lineterminator='\t\n'
    uuf.write("\r\n")

uuf.close()


# ----------- entities ----------
if entity_detection_value:
    entityFileName = docLabel + "_" + onlineFile + ".entities.csv"
    eef = open(entityFileName, "w")

    entityOut = "text" + "\t" + 'entity_type' + "\t" + "\t" + "start" + "\t" + "end"
    eef.write(entityOut)
    eef.write("\r\n")

    entities = jj.get('entities')
    for count, entity in enumerate(entities):
        eType=entity.get('entity_type')
        eText=entity.get('text')
        eStart=entity.get('start')
        eEnd=entity.get('end')
        entityOut = eText + "\t" + eType + "\t" + "\t" + str(eStart) + "\t" + str(eEnd)
        eef.write(entityOut)
        eef.write("\r\n")
    #
eef.close()
#


#------- auto-highlights -------------------
 
if auto_highlights_value:
    auto_highlights_returned = jj.get('auto_highlights_result')
    if auto_highlights_returned.get('status') == "success":
        highlightFileName = docLabel + "_" + onlineFile + ".highlight.csv"
        hhf = open(highlightFileName, "w")
        highlightOut = "docLabel" + "\t" + "start" + "\t" + "end" + "\t" + "count" + "\t" + 'rank' + "\t" + 'text'
        hhf.write(highlightOut)
        hhf.write("\r\n")
        #
        highlightDetFileName = docLabel + "_" + onlineFile + ".highlightDetails.csv"
        hdf = open(highlightDetFileName, "w")
        highlightDetOut = "docLabel" + "\t" + "start" + "\t" + "end" + "\t" + "count" + "\t" + 'rank' + "\t" + 'text'
        hdf.write(highlightDetOut)
        hdf.write("\r\n")
        #
        highlights = auto_highlights_returned.get('results')
        for hiCount, highlight in enumerate(highlights):
            count = highlight.get('count')
            rank  = highlight.get('rank')
            text  = highlight.get('text')
            firstStart   = 999999999
            lastEnd      = 0
            timestamps   = highlight.get('timestamps')
            for myCount, timestamp in enumerate(timestamps):
                start = timestamp.get('start')
                end   = timestamp.get('end')
                if start < firstStart:
                    firstStart = start
                if end > lastEnd:
                    lastEnd = end
                highlightDetOut = docLabel + "\t" + str(start) + "\t" + str(end) + "\t" + str(1 + myCount) + "\t" + str(rank) + "\t" + text
                hdf.write(highlightDetOut)
                hdf.write("\r\n")
            #
            highlightOut = docLabel + "\t" + str(firstStart) + "\t" + str(lastEnd) + "\t" + str(count) + "\t" + str(rank) + "\t" + text
            hhf.write(highlightOut)
            hhf.write("\r\n")
        #
        hdf.close()
        hhf.close()        
    #
#

#------- paragraphs -------------------

#needs transcriptId, docLabel, onlineFile
#transcriptId       ="rsuh9skgre-a056-486e-8138-2e6608d21f04"
#docLabel   = "mo007-1-SP"
#onlineFile = "mo007-1.m4a"

import requests
import time
import sys

endpoint = "https://api.assemblyai.com/v2/transcript/" + transcriptId + "/paragraphs"
#headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a"}
headers = {"authorization": useThisAuthKey}
response = requests.get(endpoint, headers=headers)
time.sleep(60)
kk=response.json()
print("")
print("")
print(" *** Response from /paragraphs call ***")

#print(kk)
print("")
print(" *************************************")
print("")

# dump JSON direct from AssemblyAI return
paragJsonPubPath = docLabel + "_" + onlineFile + "_trace.paragraphs.json"
pjf = open(paragJsonPubPath, "w")
pjf.write(jsfmt.dumps(kk))
pjf.close()

parags=kk.get("paragraphs")	#fetch all paragraphs
paragCount = len(parags)	#how many paragraphs?
#print(paragCount)
paragNum = 0
wordPos = 0

paragraphFileName = docLabel + "_" + onlineFile + ".paragraphs.csv"
ppf = open(paragraphFileName, "w")

rawParagFileName = docLabel + "_" + onlineFile + ".rawParag.csv"
rppf = open(rawParagFileName, "w")

current_speaker = "(Undefined Speaker)"
paragSpeakers = dict()

paragSpeakerFileName = docLabel + "_" + onlineFile + ".paragSpeakers.csv"
psf = open(paragSpeakerFileName, "w")


paragStartings = []
rawParags = {}
speakerCount = 0
speakerTurns = 0
oldWEnd = 0   # end of preceding word; matches current_speaker
#   needed to end preceding paragraph when change of speaker triggers end-of-paragraph event

#Also record PARAGRAPH version of words: Speaker can VARY within paragraph!        # also insert timestamp, "Corrected Text".
paragWordFileName = docLabel + "_" + onlineFile + ".paragWords.csv"
pwf = open(paragWordFileName, "w")
wordOut = "start" + "\t" + "end" + "\t" + "speaker" + "\t" + "confidence" + "\t" + "paragNum"  + "\t" + "paragWordCount" + "\t" + "wordPos" + "\t" + "text"
pwf.write(wordOut)
pwf.write("\r\n")

rawParagOut = "start" + "\t" +  "end" + "\t" + "paragNum" + "\t" + "speaker" + "\t" + "pconfid" + "\t" + "wordPos" + "\t" + "paragWordPos" + "\t" + "paragFirstWordCount" + "\t" + "paragLastWordCount"
rppf.write(rawParagOut)
rppf.write("\r\n")

#Column headers
paragOut = "start" + "\t" + "end" + "\t" + "paragNum" + "\t" + "speaker" + "\t" + "confidence" + "\t" + "startTime" + "\t" + "wordCount" + "\t" + "text"
ppf.write(paragOut)
ppf.write("\r\n")

#if docLabel in paragSpeakers:       # re-run; delete old slot
#    paragSpeakers[docLabel] = { }
#    print()

for p0 in parags:
    paragNum += 1
    paragWordPos = 0      # count of words within paragraph
    text=p0.get('text')		#text of paragraph
    start=p0.get('start')		#starting milisecond of paragraph
    paragStartings.append(start)
    pStartTime = ToDisplayTime(start)     # supplement with legible timestamp
    end=p0.get('end')		#text of paragraph
    pconfid = p0.get('confidence')	#paragraph-level confidence
    words=p0.get('words')		#list of words
    wordCount = len(words)
    w1_0=words[0]          		#first word - use only "speaker" of first word
    sp=w1_0.get('speaker')      	#Label entire paragraph with first speaker
    
    # Record start of each speech turn (usually several per speaker)
    if sp != current_speaker:
        current_speaker = sp
        speakerTurns += 1
        if sp in paragSpeakers:
            paragSpeakers[sp].append(start)
        else:
            paragSpeakers[sp] = [start]	     # First speech turn only
            speakerCount += 1
        #
    #
    paragFirstWordCount = wordPos + 1     #position within document, of first word in paragraph
    
    for wCount, word in enumerate(words):   # Now extract all info on included words
        wordPos += 1     #position of word within document
        paragWordPos += 1     #position of word within paragraph
        wtext=word.get('text')
        wstart=word.get('start')
        wend=word.get('end')
        wconfid=word.get('confidence')
        wspeaker=word.get('speaker')
        #wordOut = str(wstart) + "\t" + str(wend) + "\t" + wspeaker + "\t" + str(wconfid) + "\t" + wtext    
        wordOut = str(wstart) + "\t" + str(wend) + "\t"
        if wspeaker != None and len(wspeaker)>0:
            wordOut += wspeaker
        
        wordOut += "\t" + str(wconfid) + "\t" + str(paragNum) + "\t" + str(paragWordPos) + "\t" + str(wordPos) + "\t" + wtext
        pwf.write(wordOut)	#    print(utterOut)	, delimiter='\t', lineterminator='\t\n'
        pwf.write("\r\n")
    #
    paragLastWordCount = wordPos  # count of most recently-counted word within document, is last word in paragraph

    paragOut = str(start) + "\t" + str(end) + "\t" + str(paragNum) + "\t"
    if sp != None and len(sp) > 0:
        paragOut += sp
    #
    paragOut += "\t" + str(pconfid)
    paragOut += "\t" + str(pStartTime)
    
    paragOut += "\t" + str(wordCount)
    paragOut += "\t" + text     # '+ "\t" + text' for manual editing. IF you use a spreadsheet, REMEMBER to set the "text" columns very wide before saving!!
    ppf.write(paragOut)
    ppf.write("\r\n")

    # parag start/end millisecond, parag #, first speaker, confid, # words in parag, (document-level) start/last word #
    rawParags.update( {start: [end, paragNum, sp, pconfid, wordPos, paragWordPos, paragFirstWordCount, paragLastWordCount] } )
    #rawParags.update( {start: {'end':wend, 'paragNum':paragNum, 'speaker':wspeaker, 'confid':wconfid, 'wordPos':wordPos, 'paragFirstWordCount':paragFirstWordCount} } )
    rawParagOut = str(start) + "\t" + str(end) + "\t" + str(paragNum) + "\t" + sp + "\t" + str(pconfid) + "\t" + str(wordPos) + "\t" + str(paragWordPos) + "\t" + str(paragFirstWordCount) + "\t" + str(paragLastWordCount)
    rppf.write(rawParagOut)
    rppf.write("\r\n")


#display first occurrence of each speaker, with first time (in three formats)
#print("paragSpeakers:")
#print(paragSpeakers)
#{'A': [1200, 3000], 'B': [2400]}

speakerTimeOut = 'docLabel' + "\t" + "sp" + "\t" + "myTime" + "\t" + "myTimeDisplay" + "\t" + "myTimeSRT"
psf.write(speakerTimeOut)
psf.write("\r\n")

paragSpeakerKeys=paragSpeakers.keys()
for sp in paragSpeakerKeys:
    timeList = paragSpeakers.get(sp)
    for tcc, myTime in enumerate(timeList):
        #paragSpeakers[docLabel]   = {start: sp}
        speakerTimeOut = docLabel + "\t" + sp + "\t" + str(myTime) + "\t" + ToDisplayTime(myTime) + "\t" + ToSRTTime(myTime)
        psf.write(speakerTimeOut)
        psf.write("\r\n")
    #

#
ppf.close()
pwf.close()
psf.close()
rppf.close()

print(" Speakers (from Paragraphs output):")
print(paragSpeakerKeys)
for sp in paragSpeakerKeys:
    timeList = paragSpeakers.get(sp)
    print(sp + " @ " + ToDisplayTime(timeList[0]))

#--------- Sentence(s) -----------------

# dump JSON direct from AssemblyAI return
sentJsonPubPath  = docLabel + "_" + onlineFile + "_trace.sentences.json"

#transcriptId="rs8dx3ybuk-75db-405d-950b-560ec269d003"
endpoint = "https://api.assemblyai.com/v2/transcript/" + transcriptId + "/sentences"
#headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a"}
headers = {
    "authorization": useThisAuthKey}
sResponse = requests.get(endpoint, headers=headers)
time.sleep(30)
sss=sResponse.json()
myStatus=sss.get('status')
print(myStatus)
print("")
print("")
print(" *** Response from /sentences call ***")
# dump JSON direct from AssemblyAI return
sentencesJsonPubPath = docLabel + "_" + onlineFile + "_trace.sentences.json"
sjf = open(sentencesJsonPubPath, "w")
sjf.write(jsfmt.dumps(sss))
sjf.close()

#print(sss)
print("")
print(" *************************************")
print("")

paragTimes = []
paragTimes = rawParags.keys()   # Key (i.e. paragraph-start time) may be all we need hereafter

current_speaker = "(Undefined Speaker)"
wordPos = 0     # starting thru document from top

sents=sss.get("sentences")	#fetch all sentences
sentCount = len(sents)	#how many sentences?
sentNum = 0

sentenceFileName = docLabel + "_" + onlineFile + ".sentences.csv"
sssf = open(sentenceFileName, "w")
#Column headers
sentOut = "start" + "\t" + "end" + "\t" + "sentNum" + "\t" + "speaker" + "\t" + "confidence" + "\t" + "text"
sssf.write(sentOut)
sssf.write("\r\n")

sentWordFileName = docLabel + "_" + onlineFile + ".sentWords.csv"
sswf = open(sentWordFileName, "w")
sentWOut = "start" + "\t" + "end" + "\t" + "sentNum" + "\t" + "speaker"  + "\t" + "confidence" + "\t" "wordPosSent" + "\t" + "wordPosDoc" + "\t" + "text"
sswf.write(sentWOut)
sswf.write("\r\n")

for s0 in sents:
    sentNum += 1
    sentWordPos = 0         # no words yet seen in this sentence
    text=s0.get('text')		#text of sentence
    start=s0.get('start')		#text of sentence
    end=s0.get('end')		#text of sentence
    pconfid = s0.get('confidence')	#sentence-level confidence
    w1=s0.get('words')		#list of words
    w1_0=w1[0]              #first word - use only "speaker" of first word
    sp=w1_0.get('speaker')      	#Label entire sentence with first speaker
    #
    if str(start) in paragTimes:
        paragBreak = True
        paragNum = rawParags.get('paragNum')
    else:
        paragBreak = False
        paragNum = 0
    #
    for wCount, word in enumerate(w1):   # Now extract all info on included words
        wordPos += 1     #position of word within document
        sentWordPos += 1     #position of word within sentence 
        wtext=word.get('text')
        wstart=word.get('start')
        wend=word.get('end')
        wconfid=word.get('confidence')
        wspeaker=word.get('speaker')
        sentenceWords = [wstart, wend, sentNum, wspeaker, wconfid, sentWordPos, wordPos, wtext]
                #wordOut = str(wstart) + "\t" + str(wend) + "\t" + wspeaker + "\t" + str(wconfid) + "\t" + wtext    
        wordOut = str(wstart) + "\t" + str(wend) + "\t" + str(sentNum) + "\t"
        if wspeaker != None and len(wspeaker)>0:
            wordOut += wspeaker
        #
        if paragNum > 0:
            wordOut += str(paragNum)
        #
        wordOut += "\t" + str(wconfid)  + "\t" + str(sentWordPos) + "\t" + str(wordPos) + "\t" + wtext
        sswf.write(wordOut)
        sswf.write("\r\n")
    # sentOut = str(start) + "\t" + str(end) + "\t" + sp + "\t" + str(pconfid) + "\t" + text
    sentOut = str(start) + "\t" + str(end) + "\t" + str(sentNum) + "\t" 
    if sp != None:          # 'sentence-level speaker.' Don't rely on this at word level.
        sentOut += sp
    #
    sentOut += "\t" + str(pconfid) + "\t" + text
    sssf.write(sentOut)
    sssf.write("\r\n")
    #
    #if (sp != current_speaker) or (start in paragStartings):
    #    print("Magic new paragraph, speaker '" + wspeaker + " " + str(wstart))
    #

sssf.close()
sswf.close()


# ------------ SRT -----------

import requests
import time
import sys

#docLabel = "parseSRT" 
#onlineFile = "ls040-0"

srtFileName = docLabel + "_" + onlineFile + ".srt"
srtf = open(srtFileName, "w")

#transcriptId="rsfzjbpypn-f1ff-4dc4-9aca-0526544dc4ed"

endpoint = "https://api.assemblyai.com/v2/transcript/" + transcriptId + "/srt?chars_per_caption=40"        # "/srt?chars_per_caption=40"  "/paragraphs"
#headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a"}
headers = {"authorization": useThisAuthKey}
sResponse = requests.get(endpoint, headers=headers)

srtf.write(sResponse.text)
srtf.write("\r\n")

srtf.close()

#time.sleep(30)
#srts=sResponse.json()
#print(srts)
#myStatus=srts.get('status')
#print(myStatus)


#srtOut = srtOut + "\t" + str(pconfid) + "\t" + text
#srtf.write(srtOut)

print("Thanks for the call!")
quit()
