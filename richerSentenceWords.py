#cd "/mnt/d/Documents/FEP-AI/2021 Livestreams/ls016"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/richerSentenceWords.py" ls016-1 "." "ls016-2_ls016-1.m4a.sentWords.csv" "." "ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.en.srt"  | tee ls016-2_trace.txt
#   ls048-1_ls048-1.m4a.srt Often-cleaner SRT file, extracted from
#       docLabel + "_" + inFileName + ".srt"


import csv
import time
import sys
import math
import json
from html.parser import HTMLParser
import matplotlib.pyplot as plt
import scipy.interpolate

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) == 1:
        print("enrichSentencesFromYouTube.py -- Needs parameters docLabel (key binding references to this doc),")
        print("    inSentDir (path to incoming sentWords file, often '.'), inSentWordFile (name of driver file *.sentWords.csv),")
        print("    inSrtDir  (path to incoming SRT file from YouTube (or other independent source), often 'youtube'),")
        print("    inSrtFile (name of flat file *.srt from Google/YouTube or Adobe Premier Plus, used to improve spelling, as *.en.srt or *.en(ca).srt).")
        print("Optional params speakers (defaults to a central CSV identifying all speakers), outDir (defaults to working directory '.').")
        print("Created in outDir: *_transcript.txt, *_built.srt, *_built.xhtml")
        print("If inSentDir holds a *.paragraphs.csv file, it's used to force paragraph ends.")
        quit()
    elif len(sys.argv) < 6:
        print("Need at least docLabel, inSentDir, inSentWordFile, inSrtDir, inSrtFile; optional outDir.")
        print("  *** Exiting! ***")
        quit()


docLabel = sys.argv[1]
inSentDir = sys.argv[2]
inSentWordFile = sys.argv[3]
inSrtDir = sys.argv[4]
inSrtFile = sys.argv[5]
print("docLabel, inSentDir, inSentWordFile, inSrtDir, inSrtFile: " + "'" + docLabel + "', '" +  inSentDir + "', '" + inSentWordFile + "', '" + inSrtDir + "', '" + inSrtFile + "'")

if len(sys.argv) > 6:
    speakerFile = sys.argv[6]
else:
    speakerFile = "/mnt/d/Documents/FEP-AI/Active Inference Podcast/AllSpeakers.csv"      #default - really, load from config file

print('speakers File: ' + "'" + speakerFile + "'")

if len(sys.argv) > 7:
    outDir = sys.argv[7]
else:
    outDir = "."    #publish to working directory!

print("outDir: " + "'" + outDir + "'")


# ++++++ notes ++++++

#prepare to compare to Google/YouTube word list
#confidSentWordList = sentWordVec
#confidSentWordList.sort(reverse=True, key = lambda x: x[3])     # descending by confidence
#print(confidSentWordList)

#where the fourth component of sentenceWords is confidence, the following gives the highest-confidence words at the top:
#sentenceWords.sort(reverse=True, key = lambda x: x[3])

# "Correct Whisper per YouTube (ls038-2).ods"


# ----- notes -----


# -------------- immutable globals -------------

punct = "'\"`‘.’“”¡¿,!?;&();~"


# --------------- mutable globals --------------

paragTimes = []
chapterTimes = []
speakerDesc = {}
rawParags = {}
srtLexemes = {}
sentWordLexemes = {}
sentWordAlignsSrt = []


# ------- Utility functions --------------

def hhMmSsToTime(ts):
    tsLen = len(ts)
    #print("in hhMmSsToTime; ts/tsLen:")
    #print(ts)
    #print(tsLen)
    if tsLen == 8:		# hh:mm:ss
        hh = int(ts[0:2])
        mm = int(ts[3:5])
        ss = int(ts[6:8])
        to_time= 3600000*hh + 60000*mm + 1000*ss
        return to_time
    elif tsLen == 7:		# h:mm:ss
        hh = int(ts[0:1])
        mm = int(ts[2:4])
        ss = int(ts[5:7])
        to_time= 3600000*hh + 60000*mm + 1000*ss
        return to_time
    elif tsLen == 5:		# mm:ss
        mm = int(ts[0:2])
        ss = int(ts[3:5])
        to_time= 60000*mm + 1000*ss
        return to_time
    elif tsLen == 4:  		# m:ss
        mm = int(ts[0:1])
        ss = int(ts[2:4])
        to_time= 60000*mm + 1000*ss
        return to_time
    else:
        return 9999999
    #
#


def hhMmSsMssToTime(ts):
    tsLen = len(ts)     # 01:58:14,639
    print(tsLen)
    hh = int(ts[0:2])
    mm = int(ts[3:5])
    ss = int(ts[6:8])
    mss = int(ts[9:12])
    to_time= 3600000*hh + 60000*mm + 1000*ss + mss
    return to_time
    #
#


def ToDisplayTime(tt):
    ts=float(0.0+int(tt))
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
    ts=float(0.0+int(tt))
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


def secToTime(ss):
    if ss >= 3600000:
        h0=int(ss/3600000.0)
        hh = str(100+h0)
        m0=int( (ss-(3600000.0*h0))/60000.0)
        mm=str(100+m0)
        s0=int( (ss - (3600000.0*h0) - (60000.0*m0) ) /1000.0)
        ss=str(100+s0)
        mms0=int(ss - (3600000.0*h0) - (6000*m0) - s0)
        mms=str(1000+mms0)
        to_time= hh[1:3] + ":" + mm[1:3] + ":" + ss[1:3] + "," + mms[1:4]
        return to_time
    else:
        m0=int( ss / 60000.0)
        mm=str(100+m0)
        s0=int( (ss  - (60000.0*m0) ) /1000.0)
        ss=str(100+s0)
        mms0=int(ss - (6000*m0) - s0)
        mms=str(1000+mms0)
        to_time= mm[1:3] + ":" + ss[1:3] + "," + mms[1:4]
        return to_time
    #
#


# ------- "Business" functions --------------

def speakerIdToName(doc, id, myTime):
# Default; override if possible from inSpeakers
    #print("ord, len of '" + id)
    #print(ord(id))
    #print(len(id))
    if len(id) > 1:     # speaker already spelled out in 'sentences' input
        return id
    #
    speaker = "Speaker " + id   # default
    #print("speakerDesc")
    #print(speakerDesc)
    spDesc = speakerDesc.get(id)
    #print("spDesc")
    #print(spDesc)
    if spDesc is not None:
        dName = spDesc.get('displayedName')
        #print("dName")
        #print(dName)        
        if dName is not None and len(dName)>0:
            speaker = dName
        #
    #
    return speaker
    #
#

#def soundex(word):
    # Step 1- Retain the first letter of the name.
    # Step 2- Drop all other occurrences of y, h, w.
    # Step 3- Change each run of the following into a single 0 (except for an initial vowel): a, e, i, o, u.
    # Step 4- Replace consonants with digits as follows (after the first letter):
    # 	b, f, p, v → 1
	#    # c, g, j, k, q, s, x, z → 2
	#    # d, t → 3
	#    # l → 4
	#    # m, n → 5
	#    # r → 6
    # Step 5- If two or more of the same number are adjacent, only retain the first letter;
    # Step 5- If the initial letter and the following digit have the same If two or more of the same number are adjacent, only retain the first letter;
    # Step 6- Delete all zeros;
    # Step 7- If there are too few letters in the word to assign three numbers, append zeros until there are three numbers. 
    #  #If there are four or more numbers, retain only the first three.
    #
    # Alternate, for SQL:
    #1 Save the first letter. Map all occurrences of a, e, i, o, u, y, h, w. to zero(0)
    #2 Replace all consonants (include the first letter) with digits as in [2.] above.
    #3 Replace all adjacent same digits with one digit, and then remove all the zero (0) digits
    #4 If the saved letter's digit is the same as the resulting first digit, remove the digit (keep the letter).
    #5 Append up to 3 zeros if result contains less than 3 digits. Remove all except first letter and 3 digits after it (This step same as [4.] in explanation above).
#
#
def normalizeWord(word):
    prefix=""
    suffix=""
    cleanWord = word
    wordLen = len(word)
    normWord = word.strip(punct)         # no affixes
    normWordLen = len(normWord)
    if normWordLen !=  wordLen:
        prefixLen = word.find(normWord)
        if prefixLen < 1:
            cleanWord = word[:normWordLen]
            suffix = word[normWordLen:]
        else:
            cleanWord = word[prefixLen:(prefixLen+normWordLen)]
            prefix = word[0:prefixLen]
            suffix = word[(prefixLen+normWordLen):]
        #
    normWord = normWord.upper()     # make blatant that this form is case-insensitive
    #
    return [cleanWord, normWord, prefix, suffix]
#
#
def saveLexeme(lexemeTable, word, when, where, confid = None):
    #
    normVec = normalizeWord(word)
    #   returns [cleanWord, normWord, prefix, suffix]
    cleanWord = normVec[0]
    normWord  = normVec[1]
    prefix    = normVec[2]
    suffix    = normVec[3]
    #   syntax: a ={}
    #       a["k"].update([["m","n"]["x","y"]])
    #       
    #                    a possible sort-key: number of words in phrase, chars in phrase...
    lexVec = [cleanWord, when, where, len(cleanWord.split()), len(cleanWord), prefix, suffix]
    if confid != None:
        lexVec.append(confid)
    #
    if normWord in lexemeTable:
        lexemeTable[normWord][0] += 1
        #normCount = 1 + lexemeTable[normWord][0]
        #lexemeTable[normWord][0] = normCount
        lexemeTable[normWord][1].append(lexVec)
    else:
        lexemeTable[normWord] = [1, [lexVec]]
    #
    #print("'" + normWord + "' '" + prefix + "' '" + suffix + "'")
    #print(lexemeTable)
    return [cleanWord, normWord, prefix, suffix]
#
#following may be better organization:
#    #                    a possible sort-key: number of words in phrase, chars in phrase...
#    lexVec = [cleanWord, when, where, prefix, suffix]
#    if confid != []:
#        lexVec.append(confid)
#    #
#    if normWord in lexemeTable:
#        lexemeTable[normWord][0] += 1
#        #normCount = 1 + lexemeTable[normWord][0]
#        #lexemeTable[normWord][0] = normCount
#        lexemeTable[normWord][3].append(lexVec)
#    else:
#        lexemeTable[normWord] = [1, len(cleanWord.split()), len(cleanWord), [lexVec]]
#    
#

def bestWord(word, when, confid):

    # returns per reportString = bestWord(word, start, confid)[0]
    if confid > 1.00:	# get constant from config  !## restore logic
        print("bestWord says, high confidence '" + word + "'")
        return [word, False]
    #
    normVec = normalizeWord(word)
    cleanWord = normVec[0]
    normWord  = normVec[1]
    prefix    = normVec[2]
    suffix    = normVec[3]

    # check index across following: sentWordAlignsSrt.append([when, normWord, srtWhereGuess, normWord])

    #if sentWordLexemes[normWord][0] > 10:    # three or more occurrences? Stet.
    #    return [word, False]
    #
    #if normWord in srtLexemes:
    #    srtLex = srtLexemes.get(normWord)
    #    srcLexCount = srtLex[0]
    #    srtLexVecList = srtLex[1]
    #    srtMatchesMe = False
    #    srtMatchesOther = False
    #    #for srtLexVec in srtLexVecList:
    #    #    #
    #    #
    #
    gg = y_interp(when)
    hh = 0.0 + gg
    srtWhereGuess = int(round(hh,0))    # is there anything in the corresponding WHERE position of SRT?
    #
    #   Index SRT on When-Start time (milliseconds)
    #   srtWordsWhen[srtStart] = {'end':srtEnd, 'srtLineNum':srtLineCount, 'wordPosInSrt':myWordCount, 'wordPosInDoc':srtWordCount, 'word':myWord, 'cleanWord':cleanWord, 'normWord':normWord, 'prefix':prefix, 'suffix':suffix}
    #if srtWhereGuess in srtWordsWhen:   # need to find SRT event on WHERE (i.e. internal slot), not on milliseconds
    if srtWhereGuess in srtLineWords:
        srtWordDict = srtWordsWhen[srtWhereGuess]
        if normWord == srtWordDict.get('normWord'):
            print("bestWord says, already in srtLineWords '" + word + "'")
            return [word, False]        # trivial: SRT contains the same word (maybe differently decorated)
        else:
            print("bestWord says, '" + word + "' aligns with SRT, but different (normed) word.")
            print(srtWhereGuess)
        #
    else:
        print("bestWord says, no sentence WHEN alignment with SRT for '" + word + "':")
        print(when)
        print(srtWhereGuess)
    #
    return [word, False]
    #
#



# ---------------- MAIN -----------------



if inSrtDir[-1] != "/":
    inSrtDir += "/"


# --------------------- Speaker-name lookup file -----------------


with open(speakerFile) as speaker_file:
    speaker_reader = csv.reader(speaker_file, delimiter=',')
    line_count = 0
    for row in speaker_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            rowLen=len(row)
            reportString = ""
            if rowLen > 2 and row[1] is not None and len(row[1]) > 0:
                if row[0] is not None and len(row[0]) > 0:
                    videoLabel = row[0]
                    #reportString += "In video " + row[0] + ", "
                else:
                    videoLabel = ""
                #
                speakerLabel = row[1]
                #
                if rowLen > 2 and row[2] is not None and len(row[2]) > 0:
                    displayedName = row[2]
                    #reportString += "In video " + row[0] + ", "
                else:
                    displayedName = "Speaker " + speakerLabel
                #
                #reportString += "'" + row[1] + "' stands for '" + row[2] + "'"
                if rowLen > 3 and row[3] is not None and len(row[3]) > 0:
                    fullName = row[3]
                else:
                    fullName = ""
                    #reportString += " (better known as '" + row[3] + "')"
                #
                if rowLen > 4 and row[4] is not None and len(row[4]) > 0:
                    firstTurn = row[4]
                else:
                    firstTurn = ""
                    #reportString += " after timestamp " + row[5]
                #
                if rowLen > 5 and row[5] is not None and len(row[5]) > 0:
                    rangeFrom = row[5]
                else:
                    rangeFrom = ""
                # 
                if rowLen > 6 and row[6] is not None and len(row[6]) > 0:
                    rangeTo = row[6]
                else:
                    rangeTo = ""
                # 
                if rowLen > 7 and row[7] is not None and len(row[7]) > 0:
                    notes = row[7]
                else:
                    notes = ""
                # 
                #
                if videoLabel == docLabel:      # maybe allow defaulting with videoLabel = ''?
                    speakerDesc[speakerLabel] = {'videoLabel': videoLabel, 'displayedName': displayedName, 'fullName':fullName, 'firstTurn':firstTurn, 'rangeFrom':rangeFrom, 'rangeTo':rangeTo, 'notes':notes}
                    #print(f'Loaded speaker description {", ".join([videoLabel, speakerLabel, displayedName, fullName, firstTurn, rangeFrom, rangeTo, notes])}')
                #
            line_count += 1

#print(f'Processed {line_count} speaker descriptions.')

speaker_file.close()



# --------------------- inbound Paragraph boundaries - e.g. ls016-1_ls016-1.m4a.rawParag.csv

onlineFile = inSentWordFile.replace(".sentWords.csv","")

rawParagFileName = onlineFile + ".rawParag.csv"
#rawParagFileName = docLabel + "_" + onlineFile + ".rawParag.csv"
# example: ls016-1_ls016-1.m4a.rawParag.csv; generated in parallel to:
#          ls016-1_ls016-1.m4a.sentWords.csv
inParagPath = inSrtDir + rawParagFileName

inParagF = open(inParagPath, "r", newline=None)
if (inParagF == None):
    print("  ** >> " + inParagF + " not found << ** ")
    quit()
#
allParags = inParagF.readlines()
paragFileLen=len(allParags)

paragMod=0
#for pCount, paragRow in enumerate(allParags):

paragLines = 0
paragLineCount = 0
paragWords = {}
paragWordCount = 0

paragCharCount = 0
paragLines = []
paragLineWords = []

for pCount, paragRow in enumerate(allParags):
    if pCount == 0:
        print("Raw paragraph-summary headers: " + paragRow)
    else:
        row = paragRow.split('\t')
        rowLen = len(row)
        #print(row)
        #if row[0] is not None and len(row[0]) > 0:
        start        = int(row[0])
        end          = int(row[1])
        paragNum     = int(row[2])
        if row[3] is not None and len(row[3]) > 0:
            sp = row[3]
        else:
            sp = ""
        #
        pconfid      = float(row[4])
        wordPos      = int(row[5])
        paragWordPos = int(row[6])
        paragFirstWordCount = int(row[7])
        paragLastWordCount  = int(row[8])
        rawParags[start] = [end, paragNum, sp, pconfid, wordPos, paragWordPos, paragFirstWordCount, paragLastWordCount]
        #print("loaded new 'raw paragraph' row; start/paragNum:")
        #print(start)
        #print(paragNum)
        #rawParags.update( {start: [end, paragNum, sp, pconfid, wordPos, paragWordPos, paragFirstWordCount, paragLastWordCount] } )
    #
#

# ---------------------------------------------------------

#---------------------- inbound SRT (supplementary input, for correcting Whisper mistranscriptions!) ------------------
#--- May also use to create fresh SRT that RETAINS, as Gold Standard transcript, words discarded by Whisper transcription

# needs:
#docLabel  = "ls049-1"
#inSrtDir  = "D:\Documents\FEP-AI\2022 Livestreams\ActInf Livestream #049 ~  Dalton, A Worked Example\ActInf Livestream _049.1 YouTube, Adobe"
#inSrtFile = "ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.en.srt"


inSrtPath = inSrtDir +  inSrtFile

srt_file = open(inSrtPath, "r", newline=None)
if (srt_file == None):
    print(inSrtPath + " not found")
    quit()
#

allSrts = srt_file.readlines()
srtFileLen=len(allSrts)

srtMod=0
#for pCount, srtRow in enumerate(allSrts):

srtWords = {}   # indexed by normalized word
srtWordsWhen = {}   # indexed by start-time
srtWordCount = 0
srtCharCount = 0
srtLineWords = []
srtLineCount = 0

for i in range(0, srtFileLen, 4):   # four fields over three lines, then empty line
    srtLineCount += 1
    srtSeq = str(allSrts[i])
    srtTimes = allSrts[i+1]
    #       01:58:14,639 --> 01:58:16,139
    srtStart = hhMmSsMssToTime(srtTimes[0:12])
    srtEnd   = hhMmSsMssToTime(srtTimes[17:29])
    srtLineDuration = srtEnd - srtStart
    srtText = allSrts[i+2]
    srtLineCharCount = len(srtText)     # may be useful for fuzzy locating within SRT text
    srtCharCount += srtLineCharCount
    mySrtWords = srtText.split()
    myWordCount = 0
    myLineCharLen = 0
    lastTime = 0
    startWordCount = srtWordCount+1   # what is the word count (within the whole SRT) of my first word?
    for j, word in enumerate(mySrtWords):
        myWord = word
        myWordLen = len(myWord)
        if myWordLen > 0:
            myLineCharLen += myWordLen
            myWordCount += 1
            srtWordCount += 1
            # Save this word (stripped of non-lexical affixes), return 'clean' form (i.e. preserving typographical case) and 'normalized' form (upper case)
            normWordVec = saveLexeme(srtLexemes, word, srtStart, srtWordCount)
            #   returns [cleanWord, normWord, prefix, suffix]
            cleanWord = normWordVec[0]
            normWord = normWordVec[1]
            normWordLen = len(normWord)
            prefix = normWordVec[2]
            suffix  = normWordVec[3]        
            #
            #
            if normWord in srtWords:
                srtWords.update({normWord: srtWords.get(normWord) + 1 })
            else:
                srtWords[normWord] = 1
            #
            # Index SRT word on normalized word (upper case, etc)
            srtLineWords.append({'srtWordCount':srtWordCount, 'myWordLen': myWordLen, 'srtLineCount':srtLineCount, 'cleanWord':cleanWord, 'normWord': normWord})
            
            # Index SRT on When-Start time (milliseconds)
            srtWordsWhen[srtStart] = {'end':srtEnd, 'srtLineNum':srtLineCount, 'wordPosInSrt':myWordCount, 'wordPosInDoc':srtWordCount, 'word':myWord, 'cleanWord':cleanWord, 'normWord':normWord, 'prefix':prefix, 'suffix':suffix}
        #
    #  Some SRT words ("uh," some repetitions, some "You know...") are not matched in "matching" OpenAIWhisper/Adobe Pro transcripts!
    #       Duration of an actually-matching word (including a misspelling) could be used to correct durations of adjacent matched and unmatched words.
    #print(saveLexeme(srtLexemes, "Stella!", 16035, 320))
    myStartExact = float(srtStart)
    for j in range(startWordCount-1, srtWordCount):
        myStart = round(myStartExact)       # estimate TIME start of each word, from the fraction of CHARACTERS the word occupies in the line
        srtLineWords[j]['srtWordStart'] = myStart
        myWordLen = srtLineWords[j].get('myWordLen')
        myStartExact += (myWordLen*srtLineDuration / myLineCharLen)
    #
#
print("srtWordsWhen:")
print(srtWordsWhen)

srtPubPath = outDir

srtPubPath += inSrtFile + "_publish.csv"
srtPF = open(srtPubPath, "w")
srtWordOut = 'srtWordStart' + "\t" + 'srtWordEnd' + "\t" + 'srtLine' + "\t" + 'linePos' + "\t" + 'wordLen' + "\t" + 'cleanWord' + "\t" + 'normWord'
srtPF.write(srtWordOut)
srtPF.write("\r\n")

for j, lineWord in enumerate(srtLineWords):
    #print(lineWord)
    srtWordPos = j+1    # dodge chronic Python off-by-one design flaw!
    normWord = lineWord.get('normWord')
    cleanWord = lineWord.get('cleanWord')
    myWordLen = lineWord.get('myWordLen')
    srtLineCount = lineWord.get('srtLineCount')
    srtWordCount = lineWord.get('srtWordCount')
    myStart = lineWord.get('srtWordStart')      # most of these are interpolations
    
    # THIS is the most accurate list of the speeches, before suppression of time-fillers... but don't fill in word-end yet.
    srtWordOut = str(myStart) + "\t" + "\t" + str(srtLineCount) + "\t" + str(srtWordCount) + "\t" + str(myWordLen) + "\t" + cleanWord  + "\t" + normWord
    srtPF.write(srtWordOut)
    srtPF.write("\r\n")

#
srt_file.close()
srtPF.close()

srtKeyList = list(srtLineWords)
srtKeyCount = len(srtKeyList)
print("srtKeyCount, another measure of SRT speech gestures, srtLineWord, via list, Three samples.")
print(srtKeyCount)
print(srtKeyList[0])
srtWordStart = srtKeyList[0].get('srtWordStart')
print("srtWordStart")
print(srtWordStart)
#print(srtLineWords.get(srtKeyList[0]))
print(srtKeyList[1])
print(srtKeyList[2])
#print(srtLineWords.get(srtKeyList[1]))
print("sample srtKeyList[2101,2022]")
print(srtKeyList[2101])
print(srtKeyList[2022])
print("")
print("srtLineWords:")
print(srtLineWords)
print("")

# -------- sentence WORDS -------------------

#inSentWordFile

inSentWordPath = inSentDir + "/" + inSentWordFile

sentPubPath = outDir 

sentPubPath += inSentWordFile + "_transcript.txt"

sPubF = open(sentPubPath, "w")
rawSents = {}
accumedParag = ""
sentCount = 0
sentLineWords = []      #linear list of words from Whisper. co-indexed with 
sentWordCount = 0
lastReportTime = 0
currentSpeaker = "(Unknown Speaker)"
reportableTime = 0
sentWords = {}

paragTimes = rawParags.keys()
#print("paragTimes:")
#print(paragTimes)
print("")

#with io.open("file", "r", newline=None) as fd:
sent_file = open(inSentWordPath, "r", newline=None)
if (sent_file == None):
    print(inSentWordPath + " not found")
else:
    allSentWords = sent_file.readlines()
    # First Phase: Normalize words in place, in allSentWords[]
    #
    for pCount, sentRow in enumerate(allSentWords):
        row = sentRow.split('\t')
        if pCount == 0:
            print("Sentence headers: " + sentRow)
        else:
            rowLen = len(row)
            sentWordCount += 1
            start        = int(row[0])
            end          = int(row[1])
            sentNum      = int(row[2])
            #
            if row[3] is not None and len(row[3]) > 0:
                speaker = row[3]
            else:
                speaker = ""
            
            if row[4] is not None and len(row[4]) > 0:
                confid = float(row[4])
            else:
                confid = ""
            #
            if row[5] is not None and len(row[5]) > 0:  # position of this word within sentence
                wordPosInSent = row[5].rstrip()
            else:
                wordPosInSent = ""
            #
            if rowLen >= 6 and row[6] is not None and len(row[6]) > 0:
                wordPosInDoc = int(row[6].rstrip())
            else:
                wordPosInDoc = 0
            #
            if rowLen >= 7 and row[7] is not None and len(row[7]) > 0:
                word = row[7].rstrip()
            else:
                word = ""
            #
            #   normalize word from this sentence; maybe later correct it per other resources
            #       Record any prefix/suffix to restore after wordFix!
            #   Save this word (stripped of non-lexical affixes), return 'clean' form (i.e. preserving typographical case) and 'normalized' form (upper case)
            #       normWordVec  = saveLexeme(sentWordLexemes, word, when, where, confid)
            normWordVec  = saveLexeme(sentWordLexemes, word, start, wordPosInDoc, confid)
            #    returns [cleanWord, normWord, prefix, suffix]
            cleanWord   = normWordVec[0]
            normWord    = normWordVec[1]
            prefix      = normWordVec[2]
            suffix      = normWordVec[3]
            #
            sentWords[start] = {'end':end, 'sentNum':sentNum, 'speaker':speaker, 'confid':confid, 'wordPosInSent':wordPosInSent, 'wordPosInDoc':wordPosInDoc, 'word':word, 'cleanWord':cleanWord, 'normWord':normWord, 'prefix':prefix, 'suffix':suffix}
            sentLineWords.append({'sentWordCount':sentWordCount, 'myWordLen': myWordLen, 
		        'sentWordLineCount':sentNum, 'cleanWord':cleanWord, 'normWord': normWord})
            #
        #
    #
#


print(" ================================================ ")

sentWordKeyList = list(sentWords)
sentWordKeyCount = len(sentWordKeyList)
print("sentWordKeyCount, another measure of sentWord words, sentWords, via list, Three samples.")
print(sentWordKeyCount)
#print(sentWordKeyList)
sentWordDict=sentWords[sentWordKeyList[0]]
print(sentWordDict)
print(sentWordKeyList[1])
sentWordDict=sentWords[sentWordKeyList[1]]
print(sentWordDict)
print(sentWordKeyList[2])
sentWordDict=sentWords[sentWordKeyList[2]]
print(sentWordDict)
#sentWordStart = sentWordKeyList[0].get('sentWordWordStart')
#     srtWordStart = srtKeyList[0].get('srtWordStart')
print("sentWordWordStart")
#print(sentWordWordStart)
#print(sentWords.get(sentWordKeyList[0]))
#print(sentWords.get(sentWordKeyList[1]))
print("sample sentWordKeyList[2101,2022]")
print(sentWordKeyList[2101])
print(sentWordKeyList[2022])

#
# ----------------------------------------------------------------------
#
# Second phase: Normalize words in place, in allSentWords[]
#
#   Skip over enrichment
#       where the fourth component of sentenceWords is confidence, the following gives the highest-confidence words at the top:
#          #sentenceWords.sort(reverse=True, key = lambda x: x[3])
#
print(" ================================================ ")

print("srtWordCount: total number of 'word tokens' ('speech gestures?') across all SRT captions")
print(srtWordCount)

print("srtLexemes")
#print(srtLexemes)
srtLexemeKeys      = srtLexemes.keys()  # an "alias" or "view" or "index," always in synch with srtLexemes, even if latter changes!
srtLexemeList      = list(srtLexemes)   # indexible SNAPSHOT; can get out of sync with srtLexemes
srtLexemeListCount = len(srtLexemeList)
print("srtLexemeListCount: total number of unique lexeme tokens across all SRT captions")
print(srtLexemeListCount)
print("Sample srtLexemeList items:")
print(srtLexemeList[0])
print(srtLexemeList[1])
print("srtLexemeList[srtLexemeListCount-1]")
print(srtLexemeList[srtLexemeListCount-1])
print("")


print(" ================================================ ")

print("sentWordCount: total number of words across all sentences")
print(sentWordCount)
sentWordLexemeKeys      = sentWordLexemes.keys()
sentWordLexemeList      = list(sentWordLexemes)
sentWordLexemeListCount = len(sentWordLexemeList)
print("sentWordLexemeListCount: should = total number of lexeme tokens across all sentences")
print(sentWordLexemeListCount)

interpolXY = []     # must populate THIS from data, since numpy must be called on data sorted on x
#where the first component of interpolXY is the abcissa, following sorts on x:
#interpolXY.sort(key = lambda x: x[0])
#interpolX = []
#interpolY = []

# build intersections from earliest moments
for i, kk in enumerate(srtLexemeKeys):
    if i > 100:
        break
    #
    if kk in sentWordLexemeKeys:
        print("SRT key also in sentWordLexemes:")
        print(kk)
        srtLex = srtLexemes.get(kk)
        sentWordLex = sentWordLexemes.get(kk)
        #   for THIS and the END-of-array loop, drop test on the number of items.
        if srtLex[0] < 10 and srtLex[0] == sentWordLex[0]:
            print( srtLex )
            srtLexVec = srtLex[1]
            srtStart = srtLexVec[0][1]
            srtWhere = srtLexVec[0][2]            
            #print("first 'start' value:")
            print(srtStart)
            print( sentWordLex )
            sentWordLexVec = sentWordLex[1]
            sentWordStart = sentWordLexVec[0][1]
            print(sentWordStart)
            #
            for ii in range(srtLex[0]):
                confid = sentWordLexVec[ii][7]
                sentWordStart = sentWordLexVec[ii][1]
                srtStart = srtLexVec[ii][1]
                srtWhere = srtLexVec[ii][2]
                if (confid > .9):
                    # to align to internal data structure for SRT, Y must be "slot number" (which may happen to align with linear occurrence number of SRT speech gesture). In outbound *_publish.csv, column [3], linePos, holds an appropriate value; linePos is populated from srtWordCount and stored in srtLexemes{} at position [2] of lexVec. (srtStart does NOT do this job. If we also need this, then do more work.) 
                    interpolXY.append( [sentWordStart, srtWhere] )
                    #       wrong: interpolXY.append( [sentWordStart, srtStart] )                    
                #
            #
            # sentWords[start] = {'end':end, 'sentNum':sentNum, 'speaker':speaker, 'confid':confid, 'wordPosInSent':wordPosInSent, 'wordPosInDoc':wordPosInDoc, 'word':word, 'cleanWord':cleanWord, 'normWord':normWord, 'prefix':prefix, 'suffix':suffix}
            #     sentWordLexemes[] = [occurrences, [cleanWord, when, where, len(cleanWord.split()), len(cleanWord), prefix, suffix]]
            #print( sentWordLexemes.get(kk) )
            #        sentWordValues = sentWords[start]
            #interpolSentX = sentWordValues.get.
        #
    else:
        print("SRT key missing from sentWordLexemes:")
        print(kk)
    #        
#
print("build from last moments")
for jj in range(srtLexemeListCount-100, srtLexemeListCount-1):
    kk = srtLexemeList[jj]
    if kk in sentWordLexemeKeys:
        print("SRT key also in sentWordLexemes:")
        print(kk)
        srtLex = srtLexemes.get(kk)
        sentWordLex = sentWordLexemes.get(kk)
        #
        #   if srtLex[0] < 10 and srtLex[0] == sentWordLex[0]:
        if srtLex[0] == sentWordLex[0]:
            print( srtLex )
            srtLexVec = srtLex[1]
            srtStart = srtLexVec[0][1]
            #print("first 'start' value:")
            print(srtStart)
            print( sentWordLex )
            sentWordLexVec = sentWordLex[1]
            sentWordStart = sentWordLexVec[0][1]
            print(sentWordStart)
            #
            for ii in range(srtLex[0]):
                confid = sentWordLexVec[ii][7]
                sentWordStart = sentWordLexVec[ii][1]
                srtStart = srtLexVec[ii][1]
                srtWhere = srtLexVec[ii][2]                
                if (confid > .9):
                    interpolXY.append( [sentWordStart, srtWhere] )                    
                    #interpolXY.append([sentWordStart, srtStart])
                    # to align to internal data structure, Y must be "slot" (which may happen to align with linear occurrence number of SRT speech gesture)

                    #interpolX.append(sentWordStart)
                    #interpolY.append(srtStart)
                #
            #
            # sentWords[start] = {'end':end, 'sentNum':sentNum, 'speaker':speaker, 'confid':confid, 'wordPosInSent':wordPosInSent, 'wordPosInDoc':wordPosInDoc, 'word':word, 'cleanWord':cleanWord, 'normWord':normWord, 'prefix':prefix, 'suffix':suffix}
            #     sentWordLexemes[] = [occurrences, [cleanWord, when, where, len(cleanWord.split()), len(cleanWord), prefix, suffix]]
            #print( sentWordLexemes.get(kk) )
            #        sentWordValues = sentWords[start]
            #interpolSentX = sentWordValues.get.
        #
    else:
        print("SRT key missing from sentWordLexemes:")
        print(kk)
    #
#
print("late interpolation seeds:")
#print(interpolX[-6:-1])
#print(interpolY[-6:-1])

print("index of midpoint thru sentWord text, dict there:")
sentWordMid = int(sentWordKeyCount/2)
print(sentWordMid)
sentWordListMidStart = sentWordKeyList[sentWordMid]
print(sentWordListMidStart)
print(sentWords[sentWordListMidStart])

print("index of midpoint thru SRT text, dict there:")
sentWordMid = int(sentWordKeyCount/2)
print(sentWordMid)
sentWordListMidStart = sentWordKeyList[sentWordMid]
print(sentWordListMidStart)
print(sentWords[sentWordListMidStart])


#sentWordKeyList = list(sentWords)
#sentWordKeyCount = len(sentWordKeyList)

#A few points from the middle
print('srtLexemeList[jj]: ')
#for jj in range(sentWordMid, sentWordMid+10):
#    sentWordKey = sentWordKeyList[jj]
#    sentWordDict = sentWords[sentWordKey]
#    print(sentWordDict)
for jj in range(srtLexemeListCount-99, srtLexemeListCount-1):
    kk = srtLexemeList[jj]
    if kk in sentWordLexemeKeys:
        print("SRT key also in sentWordLexemes:")
        print(kk)
        srtLex = srtLexemes.get(kk)
        sentWordLex = sentWordLexemes.get(kk)
        #
        #if srtLex[0] < 10 and srtLex[0] == sentWordLex[0]:
        if srtLex[0] == sentWordLex[0]:            
            print( srtLex )
            srtLexVec = srtLex[1]
            srtStart = srtLexVec[0][1]
            #print("first 'start' value:")
            print(srtStart)
            print( sentWordLex )
            sentWordLexVec = sentWordLex[1]
            sentWordStart = sentWordLexVec[0][1]
            print(sentWordStart)
            #
            for ii in range(srtLex[0]):
                confid = sentWordLexVec[ii][7]
                sentWordStart = sentWordLexVec[ii][1]
                srtStart = srtLexVec[ii][1]
                srtWhere = srtLexVec[ii][2]
                if (confid > .9):
                    #   to align to internal data structure, Y must be "slot number" agreeing with calculated word NUMBER in incoming file *.sentWords.csv (which may happen to align with linear occurrence number of SRT speech gesture). (In incoming field *.sentWords.csv, slot [6], wordPosDoc, works for this alignment.)             
                    interpolXY.append( [sentWordStart, srtWhere] )
                    #interpolX.append(sentWordStart)
                    #interpolY.append(srtStart)
                #
            #
            # sentWords[start] = {'end':end, 'sentNum':sentNum, 'speaker':speaker, 'confid':confid, 'wordPosInSent':wordPosInSent, 'wordPosInDoc':wordPosInDoc, 'word':word, 'cleanWord':cleanWord, 'normWord':normWord, 'prefix':prefix, 'suffix':suffix}
            #     sentWordLexemes[] = [occurrences, [cleanWord, when, where, len(cleanWord.split()), len(cleanWord), prefix, suffix]]
            #print( sentWordLexemes.get(kk) )
            #        sentWordValues = sentWords[start]
            #interpolSentX = sentWordValues.get.
        #
    else:
        print("SRT key missing from sentWordLexemes:")
        print(kk)
    #        
#
# Must sort on x before generating interpolation function

#interpolXY = [[120,43],[12,65],[120,6],[16,8],[14,1], [7213055, 7367075], [7378925, 7383965], [7387115, 7213139], [7365900, 7378800], [7382639, 7387139], [7637, 296670], [19062, 45090], [910365, 7398757], [11027, 57537], [141762, 171510], [525602, 795555], [909959, 7397940], [9780, 57600], [141900, 168720], [522419, 795540], [831600, 7213139], [7365900, 7378800], [7382639, 7387139] ]
print("interpolX/Y")
print(interpolXY)

interpol31X = []
interpol31Y = []
interpol127XY = []
interpol233XY = []
interpol353XY = []
interpol467XY = []
interpol607XY = []
interpol739XY = []
interpol859XY = []
interpol1019XY = []

oldX = -99  # impossible 
old31X = -99
old127X = -9999
old233X = -9999
old353X = -9999
old467X = -9999
old607X = -9999
old739X = -9999
old859X = -9999
old1019X = -9999

interpolX = []
interpolY = []
interpol127X = []
interpol127Y = []
interpol233X = []
interpol233Y = []
interpol353X = []
interpol353Y = []
interpol467X = []
interpol467Y = []
interpol607X = []
interpol607Y = []
interpol739X = []
interpol739Y = []
interpol859X = []
interpol859Y = []
interpol1019X = []
interpol1019Y = []


# must populate THIS from data, since numpy must be called on data sorted on x
#   where the first component of interpolXY is the abcissa, following sorts on x:
interpolXY.sort(key = lambda x: x[0])
for ii in interpolXY:
    if ii[0] != oldX:
        interpolX.append(ii[0])
        interpolY.append(ii[1])
        oldX = ii[0]
    #
    new31X = int(round(ii[0]/31,0))
    if new31X != old31X:
        interpol31X.append(new31X)
        interpol31Y.append(ii[1])
        old31X = new31X
    #
    new127X = int(round(ii[0]/127,0))
    if new127X != old127X:
        interpol127X.append(new127X)
        interpol127Y.append(ii[1])
        old127X = new127X
    #
    new233X = int(round(ii[0]/233,0))
    if new233X != old233X:
        interpol233X.append(new233X)
        interpol233Y.append(ii[1])
        old233X = new233X
    #
    new353X = int(round(ii[0]/353,0))
    if new353X != old353X:
        interpol353X.append(new353X)
        interpol353Y.append(ii[1])
        old353X = new353X
    #
    new467X = int(round(ii[0]/467,0))
    if new467X != old467X:
        interpol467X.append(new467X)
        interpol467Y.append(ii[1])
        old467X = new467X
    #
    new607X = int(round(ii[0]/607,0))
    if new607X != old607X:
        interpol607X.append(new607X)
        interpol607Y.append(ii[1])
        old607X = new607X
    #
    new739X = int(round(ii[0]/739,0))
    if new739X != old739X:
        interpol739X.append(new739X)
        interpol739Y.append(ii[1])
        old739X = new739X
    #
    new859X = int(round(ii[0]/859,0))
    if new859X != old859X:
        interpol859X.append(new859X)
        interpol859Y.append(ii[1])
        old859X = new859X
    #
    new1019X = int(round(ii[0]/1019,0))
    if new1019X != old1019X:
        interpol1019X.append(new1019X)
        interpol1019Y.append(ii[1])
        old1019X = new1019X
    #
#

print(len(interpolX))
print(interpolX)
print(interpolY)

print(len(interpol31X))
print(interpol31X)
print(interpol31Y)

print(len(interpol127X))
print(interpol127X)
print(interpol127Y)

print(len(interpol233X))
print(interpol233X)
print(interpol233Y)

print(len(interpol353X))
print(interpol353X)
print(interpol353Y)

print(len(interpol467X))
print(interpol467X)
print(interpol467Y)

print(len(interpol607X))
print(interpol607X)
print(interpol607Y)

print(len(interpol739X))
print(interpol739X)
print(interpol739Y)

print(len(interpol859X))
print(interpol859X)
print(interpol859Y)

print(len(interpol1019X))
print(interpol1019X)
print(interpol1019Y)

#calculate mapping of sentWord TIME (x) vs. srt LOCATION (y)
y_interp    = scipy.interpolate.interp1d(interpolX, interpolY)
# others may be unneeded...
y_interp31  = scipy.interpolate.interp1d(interpol31X, interpol31Y)
y_interp233 = scipy.interpolate.interp1d(interpol233X, interpol233Y)
y_interp353 = scipy.interpolate.interp1d(interpol353X, interpol353Y)
y_interp467 = scipy.interpolate.interp1d(interpol467X, interpol467Y)
y_interp607 = scipy.interpolate.interp1d(interpol607X, interpol607Y)
y_interp739 = scipy.interpolate.interp1d(interpol739X, interpol739Y)
y_interp859 = scipy.interpolate.interp1d(interpol859X, interpol859Y)
y_interp1019 = scipy.interpolate.interp1d(interpol1019X, interpol1019Y)

#x_interp = scipy.interpolate.interp1d(interpolY, interpolX)

print("find y-value associated with  2145775, a x-value for 'model'")
sentWordWhen= 2145775
gg = y_interp(sentWordWhen)
hh = 0.0 + gg
srtWhere = int(round(hh,0))
print(srtWhere)
ff=int(round(sentWordWhen/31,0))
gg = y_interp31(ff)
hh = 0.0 + gg
srtWhere = int(round(hh,0))
print(srtWhere)
ff=int(round(sentWordWhen/233,0))
gg = y_interp233(ff)
hh = 0.0 + gg
srtWhere = int(round(hh,0))
print(srtWhere)


print("find y-value associated with 7380665, an x-value for 'participants'")
sentWordWhen=7380665
gg = y_interp(sentWordWhen)
hh = 0.0 + gg
srtWhere = int(round(hh,0))
print(srtWhere)
ff=int(round(sentWordWhen/31,0))
gg = y_interp31(ff)
hh = 0.0 + gg
srtWhere = int(round(hh,0))
print(srtWhere)
ff=int(round(sentWordWhen/233,0))
gg = y_interp233(ff)
hh = 0.0 + gg
srtWhere = int(round(hh,0))
print(srtWhere)



print("--------- Third Phase ----------------------")
#
# Third phase: Repeatedly run thru (punctuated) words in sentWords, AND accurately-transcribed vocal gestures from SRT
# Build sentWordAlignsSrt[] from "islands of certainty" outward
#   sentWordAlignsSrt.append({align: {'sentWordWhen':sentWordWhen, 'sentWordWhere':sentWordWhere,  'sentWord':sentWord,'srtWhen':srtWhen, 'srtWhere':srtWhere, 'srtWord':srtWord})

#Reminders:
# srtLineWords is linear list of words in SRT. Each contains info on normalized word (upper case, etc)
#   srtLineWords.append({'srtWordCount':srtWordCount, 'myWordLen': myWordLen, 'srtLineCount':srtLineCount, 'cleanWord':cleanWord, 'normWord': normWord})
#
# sent*
# sentWords is an index on StartTime over sent* 

#  work from
#       sentWordLexemeList      = list(sentWordLexemes)
#       sentWordLexemeListCount = len(sentWordLexemeList)
#       srtLexemeList      = list(srtLexemes)   # indexible SNAPSHOT
#       srtLexemeListCount = len(srtLexemeList)

# ACTIONs
#   srtOnly         # after sorting on (merged) time, enclose each run of "srtOnly" in "[".."]" per following logic:
#                           first word in phrase: outPref = ("[" if pref[:0] != "[" else "") + pref
#                           last word in phrase:  outSuff = suff + ("]" if suff[:-1] != "]" else "")
#   aligned         # perfect alignment on verbatim word
#   normAligned     # adjust start/end timing of SRT (and do any consequent actions); adjust typographical case per glossary; restore prefix/suffix per SRT
#   sentWordOnly    # may indicate error in present handling, perhaps because of SRT time interpolation. Print warning; otherwise use sentWord form verbatim.
#
# contents of dict sentWordAlignsSrt[align].append([sentWordWhen, sentWordNormWord, srtWhere, srtNormWord, action])
#

align = 0
srtAlignmentTouched      = []
sentWordAlignmentTouched = []

# First, go thru SRT list of vocal gestures. (Adobe Premier Pro and OpeAIWhisper ignore what they consider 'time fillers;' (most?) runs of these should be marked for "srtOnly")

for srtX, kk in enumerate(srtLexemeList):
    srtLex = srtLexemes.get(kk)
    srtLexOcc = srtLex[0]
    srtLexVec = srtLex[1]

    if kk in srtAlignmentTouched:   # Normalized SRT gesture is known in sentWords; but THIS occurrence in SRT doesn't necessarily match one in corresponding position in sentWords!
        print("Phase III sees already in srtAlighmentTouched:")
        print(kk)
        continue    # already considered this SRT vocal gesture, via its normed form. Skip this subphase.
    elif kk not in sentWordLexemeKeys:
        continue    # handle later
    else:       # Normalized SRT gesture is known in sentWords; but THIS occurrence in SRT doesn't necessarily match one in corresponding position in sentWords!
        #print("SRT key also in sentWordLexemes:")
        #print(kk)
        sentWordLex = sentWordLexemes.get(kk)
        sentWordLexOcc = sentWordLex[0]
        sentWordLexVec = sentWordLex[1]
        #   can we brute-force align everything with this 
        if sentWordLexOcc == srtLexOcc:     # equal number of occurrence in both versions licenses aligning all!
            print("Phase III sees " + ("(potential) one-to-one " if sentWordLexOcc > 1 else "singleton ") + " map between SRT vocal gesture and sentWord word(s):")
            print(kk)
            #print( srtLex )
            srtLexVec = srtLex[1]
            srtStart = srtLexVec[0][1]
            #print("first 'start' value:")
            print(srtStart)
            print( sentWordLex )
            sentWordLexVec = sentWordLex[1]
            sentWordStart = sentWordLexVec[0][1]
            print(sentWordStart)
            #
            vec = srtLex[1]
            for ii in range(srtLexOcc):
                srtVec = srtLexVec[ii]
                srtCleanWord = srtVec[0]
                srtStart     = srtVec[1]
                srtWhere     = srtVec[2]
                srtPref      = srtVec[5]
                srtSuff      = srtVec[6]
                #
                vec    = sentWordLexVec[ii]
                cleanWord = vec[0]
                start     = vec[1]
                where     = vec[2]
                pref      = vec[5]
                suff      = vec[6]
                confid    = vec[7]
                # after sorting on (merged) time, enclose each run of "srtOnly" in "[".."]" per following logic
                #outWord = ("[" if pref != "[" else "") + pref + cleanWord + suff + ("]" if suff != "]" else "")
                if srtCleanWord == cleanWord and srtPref == pref and srtSuff == suffix:
                    alignDict = {'srtWhen':srtStart, 'srtWhere': srtWhere, 'srtCleanWord':srtCleanWord, 'srtPrefix': srtPref, 'srtSuffix': srtSuff, 'sentWordWhen':start, 'sentWordWhere': where, 'sentWordWhen':start, 'sentWordWhere': where, 'action':["aligned"] }
                else:
                    alignDict = {'srtWhen':srtStart, 'srtWhere': srtWhere, 'srtCleanWord':srtCleanWord, 'srtPrefix': srtPref, 'srtSuffix': srtSuff, 'sentWordWhen':start, 
                    'sentWordCleanWord':cleanWord, 'sentWordPrefix': srtPref, 'sentWordSuffix': srtSuff, 'sentWordWhen':start, 'sentWordWhere': where, 'action':["normAligned"] }
                #
                align += 1
                sentWordAlignsSrt.append({align: alignDict})
                #
                #if (confid > .9):
                #    #   to align to internal data structure, Y must be "slot number" agreeing with calculated word NUMBER in incoming file *.sentWords.csv (which may happen to align with linear occurrence number of SRT speech gesture). (In incoming field *.sentWords.csv, slot [6], wordPosDoc, works for this alignment.)             
                #    interpolXY.append( [sentWordStart, srtWhere] )
                #    #interpolX.append(sentWordStart)
                #    #interpolY.append(srtStart)
                #
            #
            #sentWordAlignsSrt
        elif sentWordLexOcc == 1:     # equal number of occurrence in both versions licenses aligning all!:
            print("Phase III sees many SRT vocal gestures matching a single sentWord word:")
            print(kk)
            # sentWords[start] = {'end':end, 'sentNum':sentNum, 'speaker':speaker, 'confid':confid, 'wordPosInSent':wordPosInSent, 'wordPosInDoc':wordPosInDoc, 'word':word, 'cleanWord':cleanWord, 'normWord':normWord, 'prefix':prefix, 'suffix':suffix}
            #     sentWordLexemes[] = [occurrences, [cleanWord, when, where, len(cleanWord.split()), len(cleanWord), prefix, suffix]]
            #print( sentWordLexemes.get(kk) )
            #        sentWordValues = sentWords[start]
            #interpolSentX = sentWordValues.get.
        else:     # equal number of occurrence in both versions licenses aligning all!:
            print("Phase III sees many SRT vocal gestures mapping to many sentWord words:")
            print(kk)
        #
    #        
#

# Just as code sample: Instead, check for misspellings in Whisper - start with known multiword technical PHRASES!
for srtX, kk in enumerate(srtLexemeList):
    if srtX > -1:
        break
    #
    align += 1
    srtLex = srtLexemes.get(kk)
    srtLexOcc = srtLex[0]
    srtLexVec = srtLex[1]
    if kk not in sentWordLexemeKeys:    # lexical form as normalized matches nothing in sentWord 
        print("Phase III sees SRT vocal gesture missing from sentWordLexemeKeys:")
        print(kk)
        # Vocal gesture in SRT only. If time-filler, mark "delete in transcript"
        #print("SRT vocal gesture entirely missing from sentWordLexemes:")
        #print(kk)
        for ii, vec in enumerate(srtLexVec):
            cleanWord = vec[0]
            srtStart  = vec[1]
            srtWhere  = vec[2]
            pref      = vec[5]
            suff      = vec[6]
            # after sorting on (merged) time, enclose each run of "srtOnly" in "[".."]" per following logic
            outWord = ("[" if pref != "[" else "") + pref + cleanWord + suff + ("]" if suff != "]" else "")
            action  = ["srtOnly"]       
            alignDict = {'srtWhen':srtStart, 'srtWhere': srtWhere, 'srtWord':cleanWord, 'action':action}    #   , 'outWord': outWord}
            align += 1
            sentWordAlignsSrt.append({align: alignDict})
            #
        #   sentWordAlignsSrt.append([sentWordWhen, sentWordNormWord, srtWhere, srtNormWord])
        srtAlignmentTouched.append(kk)   # mark SRT verbal gesture as touched
    #
#

print("sentWordAlignsSrt")
print(sentWordAlignsSrt)
sentWordAlignsSrtList = list(sentWordAlignsSrt)

alignFilePath = outDir
alignFilePath += inSrtFile + "_align.txt"
alignF = open(alignFilePath, "w")
sentWordAlignsSrtList = list(sentWordAlignsSrt)
dictLine = "\t\t\t\t" + "srtStart" + "\t" + 'srtWhere' + "\t" + 'srtWord' + "\t" + 'outWord'
alignF.write(dictLine)
alignF.write("\r\n")
print("sentWordAlignsSrtList")
print(sentWordAlignsSrtList)
for assoc in sentWordAlignsSrtList:
    #for dict1 in assoc: dict1 is int
    #dict1 = sentWordAlignsSrt.get(assoc)
    dictLine = "\t\t\t\t" + (str(assoc.get('srtWhen')) if 'srtWhen' in assoc else "")  + "\t" 
    dictLine += (str(assoc.get('srtStart')) if 'srtStart' in assoc else "") + "\t"
    dictLine += (str(assoc.get('srtWhere')) if 'srtWhere' in assoc else "") + "\t" 
    dictLine += (assoc.get('srtWord') if 'srtWord' in assoc else "") + "\t" 
    dictLine += (assoc.get('outWord') if 'outWord' in assoc else "")
    #sentWordAlignsSrt.append({align: alignDict})
    alignF.write(dictLine)
    alignF.write("\r\n")
    #
#
alignF.close()

# 
# 

print("--------- Fourth Phase ----------------------")
#
# Fourth phase: Go thru punctuated words in sentWords; overlay some words with vocal gestures from SRT
print("pCount, rowNum in enumerate(sentWords), sentWordDict = sentWords[start]")
#for pCount, rowNum in enumerate(sentWords):     # go through descriptors of each WORD in SentWords
for rowNum in range(sentWordKeyCount):     # go through descriptors of each WORD in SentWords    
    #if pCount > 17:
    #    break
    #
    #if rowNum in [19062, 19575, 19770, 19920]:
    #    continue
    #
    #print(pCount)
    #print(rowNum)
    if rowNum in sentWordKeyList:
        start = sentWordKeyList[rowNum]     # look up WHEN this word starts
        sentWordDict = sentWords[start]      # look up descriptor for this word
        print(sentWordDict)
        #
        end           = sentWordDict.get('end')
        speaker       = sentWordDict.get('speaker')
        word          = sentWordDict.get('word')
        sentNum       = sentWordDict.get('sentNum')
        confid        = sentWordDict.get('confid')
        wordPosInSent = sentWordDict.get('wordPosInSent')
        wordPosInDoc  = sentWordDict.get('wordPosInDoc')
        # following were calculated by function saveLexeme()
        cleanWord     = sentWordDict.get('cleanWord')
        normWord      = sentWordDict.get('normWord')
        prefix        = sentWordDict.get('prefix')
        suffix        = sentWordDict.get('suffix')
        normWordLen   = len(normWord)
        #
        if start in paragTimes:
            paragBreak = True
        else:
            paragBreak = False
        #
        if start in chapterTimes:
            chapterBreak = True
        else:
            chapterBreak = False
        #
        reportString = ""
        #
        if len(speaker) > 0 or len(word) > 0:
            # Now build next one, two, or three lines of output ([emptyLine] [speaker line] word)
            #
            if len(speaker) > 0 and speaker != currentSpeaker:
                if len(accumedParag) > 0:
                    sPubF.write(accumedParag)
                    sPubF.write("\r\n")
                    accumedParag = ""
                #
                sPubF.write("")     # empty line before next speech act
                sPubF.write("\r\n")
                #if len(startTime) > 0:
                #    reportableTime = int(hhMmSsToTime(startTime))
                #    reportString   = startTime
                #else:
                reportableTime = start
                reportString   = ToDisplayTime(start)
                #
                #reportString += " " 		# + speakerIdToName(speaker) + ":"        # Also account for missing or illformed start-time
                
                reportString += " " + speakerIdToName(docLabel, speaker, reportableTime) + ":"
                
                #xx=speakerIdToName(docLabel, speaker, reportableTime)
                #if len(speaker) == 1:
                #    reportString += " Speaker " + speaker + ":"      # use lookup instead
                #else:
                #    reportString += " " + speaker + ":"
                #
                #print(reportString)
                sPubF.write(reportString)
                sPubF.write("\r\n")
                currentSpeaker = speaker
                lastReportTime = reportableTime                    
                #reportString = word     # Check confidence re SRT override
                reportString = bestWord(word, start, confid)[0]
                #print(reportString)
                #sPubF.write(reportString)
                #sPubF.write("\r\n")
                if len(accumedParag) > 0:
                    accumedParag += " " + reportString
                else:
                    accumedParag = reportString
                #
            elif paragBreak:
                #print("New paragraph per upstream Whisper heuristic")
                if len(accumedParag) > 0:
                    sPubF.write(accumedParag)
                    sPubF.write("\r\n")
                    accumedParag = ""
                #
                reportableTime = start
                #if (0 + reportableTime) > (60000 + lastReportTime):	# Only some 'forced paragraphs' need timestamp
                displayTime = ToDisplayTime(start)
                reportString = displayTime + " "
                lastReportTime = reportableTime
                #else:
                #    reportString = ""
                # 
                #reportString += word
                reportString += bestWord(word, start, confid)[0]     # Check confidence re SRT override
                #print(reportString)
                #sPubF.write(reportString)
                #sPubF.write("\r\n")
                if len(accumedParag) > 0:
                    accumedParag += " " + reportString
                else:
                    accumedParag = reportString
                #
            else:
                #if len(startTime) > 0:
                #    reportableTime = int(hhMmSsToTime(startTime))
                #    print("converted startTime:")
                #    print(reportableTime)
                #else:
                reportableTime = start
                #print("saved start:")
                #print(reportableTime)
                #
                #print("[typeOf] lastReportTime:")
                #print(type(lastReportTime))
                #print(lastReportTime)                    
                #print("[typeOf] reportableTime:")
                #print(type(reportableTime))                    
                #print(reportableTime)
                if (reportableTime) > (60000 + lastReportTime):	# report time every 60 seconds                    
                    if len(accumedParag) > 0:
                        sPubF.write(accumedParag)
                        sPubF.write("\r\n")
                        accumedParag = ""
                    #
                    #if len(startTime) > 0:
                    #    displayTime = startTime
                    #else:
                    displayTime = ToDisplayTime(start)
                    #
                    reportString = displayTime + " "
                    lastReportTime = reportableTime
                else:
                    reportString = ""
                #
                #reportString += word     # Check confidence re SRT override
                reportString += bestWord(word, start, confid)[0]     # Check confidence re SRT override
                #print(reportString)
                #sPubF.write(reportString)
                #sPubF.write("\r\n")
                if len(accumedParag) > 0:
                    accumedParag += " " + reportString
                else:
                    accumedParag = reportString
                #
                #
            #
        #
    #
#
print("Saw any sentWord/SRT alignments? sentWordAlignsSrt:")
print(sentWordAlignsSrt)

print(f'Processed {pCount} sentences.')
#
# ---------------- write out enriched SentenceWord data!



# -----------------------------
#   Try enrichment
#where the fourth component of sentenceWords is confidence, the following gives the highest-confidence words at the top:
#   #sentenceWords.sort(reverse=True, key = lambda x: x[3])
#

# ------- LINEAR interpolation to map from sentences to SRT ------ (spline would be better)

#import scipy.interpolate

#sentWordStart=[1060032,1107267,3838140,4909227,6224795,2000825,5317317,7100360,30055,7076930,7002095]
#srt_publish = [1060136,1107658,3838140,4909424,6224602,2000462,5317454,7101901,29474,7077000,7001709]

#create plot of x vs. y
#plt.plot(sentWordStart, srt_publish, '-ob')

#y_interp = scipy.interpolate.interp1d(sentWordStart, srt_publish)

#find y-value associated with x-value of 2000 milliseconds 
#print(y_interp(7002095))

# ------- QUADRATIC interpolation to map from sentences to SRT ------ (spline would be better?)

#from scipy.interpolate import interp1d 
#x = [5,6,7,8,9,10,11]
#y = [2,9,6,3,4,20,6]

#xx = [2,3,4,5,6,7,8,9,10,11] 
#f = interp1d(x, y, kind='quadratic') 
#yy = f(xx)
#print(yy)





#   Write out trial transcript
#



#
sent_file.close()
sPubF.close()


