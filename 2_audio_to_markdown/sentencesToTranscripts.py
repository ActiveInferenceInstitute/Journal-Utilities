#
# Cloned from "sentencesToTranscripts - Copy (35).py" of 2/22/2023
#
# After "sentencesToTranscripts - Copy (21).py" add SRT-Speaker logic:
#    generate fresh SRT *_transcript.srt from *.sentences.csv); insert speaker names formulated from 
#
# cd "/mnt/d/Documents/FEP-AI/2022 GuestStream/Mass 2022 GuestStreams"
#	python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/sentencesToTranscripts.py" "gs014-1" "." "gs014-1_gs014-1.m4a.sentences.csv" | tee gs014-1.m4a_transcript.json
#
# cd "/mnt/d/Documents/FEP-AI/2022 GuestStream/Mass 2022 GuestStreams"
#	python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/sentencesToTranscripts.py" "gs014-1" "." "gs014-1_gs014-1.m4a.sentences.csv" | tee gs014-1.m4a_transcript.json
#
# cd "D:\Documents\Religion\Judaism, Kabbalah\Doooovid\Deep Dive Into Monism"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/sentencesToTranscripts.py" "doooov_20230508" "." "doooov_20230508_Week in Review  -  Deep Dive Into Monism, Pauli–Jung Conjecture, Advaita.m4a.sentences.csv" | tee doooov_20230508_transcript.json
#
#AllSpeakers "/mnt/d/Documents/FEP-AI/Active Inference Podcast/AllSpeakers.csv"

# DEFECTS
#   1. Timestamps in generated .SRT often have wrong values.
#

import csv
import time
import sys
import math
import json
from os.path import exists
from html.parser import HTMLParser
import re

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) == 1:
        print("sentencesToTranscripts. Needs parameters docLabel (key binding references to this doc),")
        print("inSentDir (path to incoming files), inSentFile (name of driver file *.sentences.csv).")
        print("Optional params outDir (defaults to working directory '.'), speakers (defaults to a central CSV identifying all speakers).")
        print("Created in outDir: *_transcript.txt, *_built.srt, *_built.xhtml")
        print("If inSentDir holds a *.paragraphs.csv file, it's used to force paragraph ends.")
        quit()
    elif len(sys.argv) < 4:
        print("Need at least docLabel, inSentDir, and inSentFile; optional outDir, speakers. Exiting!")
        quit()

#File references:
#	inSentDir/inSentFile     Driver
#	inSpeakerDir/inSpeakers When mappings known
#   [inSentDir]/inWords    Improves timestamp splitting; optional
#	outDir/ One destination for everything
#Parameters:
#   maxCharsPerCaption    For SRT: Max line len in chars

"""
start	end	sentNum	speaker	confidence	text
0	19080	1	A	0	I want to welcome you all to the Science, Sanity and Semantic and the Semantic Environment
2173360	2181120	472		0	And the title of her talk is Dead Man's Labor, reading Alfred Korzybski's Manhood of Humanity.
2183440	2191440	473		0	Yeah. Hello. Good morning, good afternoon and good evening. I do like this full mix of time zones that
"""
#outDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #035 A tale of Two architectures/ls035-0/publish"

mDPubF       = ""
pPubF        = ""
sPubF        = ""
srtPubF      = ""
speakerLabelsUsed = []

# overridable globals
outDir       = "."    #publish to working directory!
speakerFile  = "/mnt/d/Documents/FEP-AI/Active Inference Podcast/AllSpeakers.csv"
inSpeakerDir = "/mnt/d/Documents/FEP-AI/Active Inference Podcast/"
maxCharsPerCaption = 40    # cloned from AssemblyAI default - set up override!
srtPosStart = 0             # One less than starting line number (terminolog?) in SRT output
srtPosInc   = 1               # increment of line number in SRT output

# other globals
minInterSrtGap = 0.000     # Milliseconds
speakerDesc  = {}
srtSpeaker   = ""
# srtPosInc
srtStartTime = 0
srtEndTime   = 0
pauseLength  = 0.75
rawParags    = {}

#in public "../"
inSpeakers = "AllSpeakers.csv"

def get_input_options(scl):
    global outDir, speakerFile, inSpeakerDir, maxCharsPerCaption
    global srtPosStart, srtPosInc
    scl_len = len(scl)
    # ii typically = 4 
    return_dict = {}
    ii = 0
    while ii < scl_len:
        label = scl[ii].upper().replace("_","")     # to match keyword to logic, uppercase and ignore underbars
        value = scl[ii + 1].strip()
        ii += 2
        #
        if label == "OUTDIR":
            outDir = value
            return_dict["OUTDIR"] = outDir
        #
        elif label == "SPEAKERFILE":
            speakerFile = value
            return_dict["SPEAKERFILE"] = speakerFile
        #
        elif label == "INSPEAKERDIR":
            inSpeakerDir = value
            return_dict["INSPEAKERDIR"] = inSpeakerDir
        #
        elif label == "MAXCHARSPERCAPTION":
            maxCharsPerCaption = value
            return_dict["MAXCHARSPERCAPTION"] = maxCharsPerCaption
        #
        elif label == "SRTPOSSTART":
            srtPosStart = value
            return_dict["SRTPOSSTART"] = srtPosStart
        #
        elif label == "SRTPOSINC":
            srtPosInc = value
            return_dict["SRTPOSINC"] = srtPosInc
        #
    #
    return return_dict
#

docLabel = sys.argv[1]
inSentDir = sys.argv[2]
inSentFile = sys.argv[3]
print("docLabel, inSentDir, inSentFile " + "'" + docLabel + "', '" +  inSentDir + "', '" + inSentFile + "'")

#inSentDir = "/mnt/d/Documents/2022 Org Streams/os003/"
inParagFile   = inSentFile.replace('.sentences.', '.paragraphs.')

if len(sys.argv) > 4:
    #outDir = sys.argv[4]
    inputParams = sys.argv[4:]
    print(f'inputParams: {inputParams}')
    # fetch keyword parameters
    inputOptions = get_input_options(inputParams)  # directly sets several globals; ignore first two (explicit) incoming args
    print("All keyword parameters, aka 'inputOptions'")
    print(inputOptions)
#
srtPosCount  = srtPosStart  # defaults to 0, overridable

print("outDir: " + "'" + outDir + "'")

print('speakers File: ' + "'" + speakerFile + "'")

if (speakerFile):
    inSpeakers = speakerFile

print('inSpeakerDir: ' + "'" + inSpeakerDir + "'")


# ++++++ notes ++++++

#create new version of "sentencesToTranscripts.py" (of 12/28, 12:48)

#BUILDING WORD_BOOST LIST

#Exclude all digit-only.z
#Select all base forms whose first character is always cap as "capitalized"
#	Enter all as word_boost
#	Enter all single word as spelling
#Decrease the cutoff for number of occurrence, starting with eight, until  the next batch will take you over 1000.
#Maybe when you hit that zone, you can exclude "common nouns" and try for a last tranch that keeps you below the largest allowed number of boosts.
#
#prepare to compare to Google/YouTube word list
#confidSentWordList = sentWordVec
#confidSentWordList.sort(reverse=True, key = lambda x: x[3])     # descending by confidence
#print(confidSentWordList)

#where the fourth component of sentenceWords is confidence, the following gives the highest-confidence words at the top:
#sentenceWords.sort(reverse=True, key = lambda x: x[3])

# "Correct Whisper per YouTube (ls038-2).ods"


# ----- notes -----



# ------- Utility functions --------------

def hhMmSsToTime(ts):
    tsLen = len(ts)
    print("in hhMmSsToTime; ts/tsLen:")
    print(ts)
    print(tsLen)
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
        # check whether (a) per spDesc.get('fullName') we have a fullName; 
        #   (b) per speakerLabelsUsed[], has fullName has been emitted?
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
def loadParagFile():
    global inParagPath, rawParags, current_speaker
    reportString     = ""
    reportStringNoTS = ""

    parag_file = open(inParagPath, "r", newline=None)
    if (parag_file == None):
        print(inParagPath + " not found")
    else:
        allParags = parag_file.readlines()
        for pCount, paragRow in enumerate(allParags):
            if pCount == 0:
                print("Paragraph headers: " + paragRow)
            else:
                row = paragRow.split('\t')
                rowLen = len(row)
                #print(row)
                #if row[0] is not None and len(row[0]) > 0:
                reportString = ""
                reportStringNoTS = ""
                start = row[0]
                end = row[1]            
                if row[2] is not None and len(row[2]) > 0:
                    paragNum = row[2]
                else:
                    paragNum = ""
                
                #
                if rowLen > 3 and row[3] is not None and len(row[3]) > 0:
                    speaker = row[3]
                else:
                    speaker = ""
                
                #
                if rowLen > 4 and row[4] is not None and len(row[4]) > 0:
                    confid = row[4]
                else:
                    confid = ""
                
                #
                if rowLen > 5 and row[5] is not None and len(row[4]) > 0:
                    startTime = row[5]
                else:
                    startTime = ""
                #
                if rowLen > 5 and row[5] is not None and len(row[5]) > 0:
                    text = row[5]
                else:
                    text = ""
                #
                textLen = len(text)
                if rowLen > 6 and row[6] is not None and len(row[6]) > 0:
                    wordCount = row[6]
                else:
                    wordCount = len(text.split())
                #
                # no longer receiving edit-oriented correctedText, firstWordCount, lastWordCount
                #
                rawParags.update( {start : [end, speaker, confid, firstWordCount, lastWordCount] } )
                #
                #
                if len(speaker)>0 or len(startTime) > 0 or len(text) > 0:
                    # Now build next one, two, or three lines of output ([emptyLine] [speaker line] text)
                    myText = text
                    # lastBlank = testSrt.rFind(" ")
                    #
                    if len(speaker) > 0 and speaker != current_speaker:
                        #pPubF.write("")     # empty line before next speech act
                        #pPubF.write("\r\n")
                        reportString     = startTime + " " # + speakerIdToName(speaker) + ":"        # Also account for missing or illformed start-time
                        mySpeakerName    = speakerIdToName(docLabel, speaker, reportableTime) + ":"
                        reportString     += mySpeakerName
                        reportStringNoTS = mySpeakerName                # treat reportStringNoTS as empty
                        #
                        print(reportString)
                        #pPubF.write(reportString)
                        #pPubF.write("\r\n")
                        current_speaker = speaker
                        reportString = myText
                        print(reportString)
                        #pPubF.write(reportString)
                        #pPubF.write("\r\n")
                    else:
                        #reportString = ToDisplayTime(start) + " " + text
                        reportString = startTime + " " + myText
                        print(reportString)
                        #pPubF.write(reportString)
                        #pPubF.write("\r\n")
                    #
                #
            #
        #
        print(f'Processed {pCount} paragraphs.')
    #
    parag_file.close()
    #pPubF.close()

    print(rawParags)
#

#Here's the translation of the Wolfram Language function `loadIndexes` to Python:


def loadIndexes(indexFileName):
    phrasesToIndex = {}
    lookupWordPat = r"\b(a|an|the|of|in|and|is|to|it|that|this|for|with|on|from|by|at|as|but|they|not|or|we|you|i|he|she|me|him|her|my|your|their|our|us|them|some|any|all|many|much|few|each|every|other)\b"
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

#Note: Please make sure to import the required libraries, such as `re` for regular expressions, before using this translated function. Additionally, this translation assumes that the `maybeNorms` variable and related commented logic are not necessary for the Python implementation.


def writeToMD(textOut, lineCount, mySpeakerName, startTime, endTime, timerTime):
    global paragTimes
    print(f'In writeToMD, lineCount: {lineCount}, textOut: {textOut}')
    print(textOut)
    #
    if len(mySpeakerName.strip()) > 0:
        mDPubF.write("\r\n" + ToDisplayTime(startTime) + " _" + mySpeakerName.strip() + ":_")
        mDPubF.write("\r\n")
        mDPubF.write(textOut)
        mDPubF.write("\r\n")
    elif str(startTime) in paragTimes:
        mDPubF.write("\r\n" + ToDisplayTime(startTime) + " " + textOut)
        mDPubF.write("\r\n")
    elif timerTime:
        mDPubF.write("\r\n" + ToDisplayTime(startTime) + " " + textOut)
        mDPubF.write("\r\n")
    else:
        mDPubF.write(textOut)
        mDPubF.write("\r\n")
    #
#


def writeToSrt(textOut, lineCount, mySpeakerName, inStartTime, inEndTime):
    ## minimum inter-line pause 16 ms. SRT_MIN_ENDLINE_GAP

    global maxCharsPerCaption, minInterSrtGap
    #print("In writeToSrt, lineCount:")
    #print(lineCount)
    textOut = textOut.strip()
    startTime = inStartTime
    endTime   = inEndTime
    myLineCount = lineCount
    if len(mySpeakerName.strip()) == 0:
        textRem = ""
    else:
        textRem = mySpeakerName.strip() + ": "   # We will count length of speaker name as though it were audible.
        #                                   This may be convenient for viewing; but it makes 
        #                                   detailed SRT time-labels useless for reconstructing speech timing
    textRem   += textOut.strip()
    charsRem  = len(textRem)

    inTimeRem   = endTime - startTime
    timeRem   = inTimeRem
    msPerChar = (timeRem / charsRem) if charsRem > 0 else 0.01  #arbitrary

    inMsPerChar = msPerChar
    oc1 = maxCharsPerCaption+1     # lets us see a single character at end of window
    oc2 = oc1 + 1               # sees single character at end of window

    while charsRem > 0:         # should add logic to try to split last pair of lines evenly
        if charsRem <= maxCharsPerCaption:
            myLineCount += 1
            srtPubF.write(str(myLineCount))
            srtPubF.write("\r\n")
            srtStart = ToSRTTime(startTime)
            srtEnd   = ToSRTTime(inEndTime)
            srtLine  = srtStart + " --> " + srtEnd
            srtPubF.write(srtLine)
            srtPubF.write("\r\n")
            srtPubF.write(textRem)
            srtPubF.write("\r\n")
            srtPubF.write("")
            srtPubF.write("\r\n")
            charsRem = 0
        else:
            wordsText = textRem[0:oc2].replace("-"," ").replace(","," ").replace("."," ").replace(";"," ").replace("'"," ").replace("\""," ")
            prevSpace = wordsText.rfind(" ")    # wordsText is good for finding only rightmost potential line-break
            if prevSpace >= 0:  # leading integral block of text; dump thru following space
                myText0  = textRem[0:prevSpace+1].strip()
                myTextLen = len(myText0)
                myLineCount += 1
                srtPubF.write(str(myLineCount))
                srtPubF.write("\r\n")
                srtStart = ToSRTTime(startTime)
                #msPerChar = (timeRem / charsRem)       # should re-calculate on actual remaining characters and time!
                endTime  = startTime + int(msPerChar * myTextLen)
                timeRem   = endTime - startTime
                srtEnd   = ToSRTTime(endTime)
                srtLine  = srtStart + " --> " + srtEnd
                srtPubF.write(srtLine)
                srtPubF.write("\r\n")
                srtPubF.write(myText0)
                srtPubF.write("\r\n")                
                srtPubF.write("")
                srtPubF.write("\r\n")       # close this SRT block
                textRem  = textRem[prevSpace:].strip()   # remainder
                charsRem = len(textRem)
                startTime = endTime + minInterSrtGap
            else:       # this "line" is very long! - break at arbitrary location.
                #  Maybe add test for line terminators, notably "-"
                nextSpace = wordsText.find(" ")
                if nextSpace < 0:   # solid block of text; dump all
                    myLineCount += 1
                    srtPubF.write(str(myLineCount))
                    srtPubF.write("\r\n")
                    srtStart = ToSRTTime(startTime)
                    srtEnd   = ToSRTTime(inEndTime)
                    srtLine  = srtStart + " --> " + srtEnd
                    srtPubF.write("\r\n")
                    srtPubF.write(textRem)
                    srtPubF.write("\r\n")
                    srtPubF.write("")
                    srtPubF.write("\r\n")
                    charsRem = 0
                else:
                    myLineCount += 1
                    srtPubF.write(str(myLineCount))
                    srtPubF.write("\r\n")
                    myText0   = textRem[0:nextSpace].strip()
                    myTextLen = len(myText0)
                    srtStart  = ToSRTTime(startTime)
                    timeRem   = endTime - startTime
                    msPerChar = (timeRem / charsRem)
                    newStartTime = endTime + minInterSrtGap
                    endTime   = startTime + int(msPerChar * myTextLen)
                    srtEnd    = ToSRTTime(endTime)
                    srtLine   = srtStart + " --> " + srtEnd
                    srtPubF.write(srtLine)
                    srtPubF.write("\r\n")
                    srtPubF.write(myText0)
                    srtPubF.write("\r\n")
                    srtPubF.write("")
                    srtPubF.write("\r\n")
                    startTime = newStartTime
                    textRem   = textRem[nextSpace:].strip()
                    charsRem  = len(textRem)
                #
            #
        #
        #
        """
        textRem   += textOut.strip()
        charsRem  = len(textRem)
        timeRem   = endTime - startTime
        msPerChar = (timeRem / charsRem) if charsRem > 0 else charsRem
        oc1 = maxCharsPerCaption+1     # lets us see a single character at end of window
        oc2 = oc1 + 1               # sees single character at end of window
        #if charsRem > 0:         # should try to split last pair of lines evenly
        
        """
        
    #
    charsRem = 0
    return myLineCount
#

# ---------------- MAIN -----------------

#outDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #035 A tale of Two architectures/ls035-1/publish"

# inSpeakerDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #040 - Chris Fields... A free energy principle for generic quantum systems/ls040-1_noSpeaker"
# inSpeakers = "noSpeaker_ls040-0.Speakers.csv"
# inSpeakerDir = "/mnt/d/Documents/FEP-AI/Active Inference Podcast"
# inSpeakers = "AllSpeakers.csv"


#inSentDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #040 - Chris Fields... A free energy principle for generic quantum systems/ls040-1_noSpeaker"
#inSentFile = "ls036-0_ls036-0.m4a.paragraphs.csv"
#inSentDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #036 Modeling Ourselves/ls036-0"
#inSentFile = "ls036-0_ls036-0.m4a.paragraphs.csv"
#inSentDir = "/mnt/d/Documents/FEP-AI/2022 Org Streams/os003"
#inSentFile = "Bijan_os003-1.m4a.paragraphs.csv"

#CSV column headers:
#   paragraph: start, end, speaker, confid, text
#   speakers: VideoLabel, SpeakerLabel, DisplayedSpeakerName, FullSpeakerName, FirstTurn, RangeFrom, RangeTo, Notes

inSpeakerPath = inSpeakerDir
if inSpeakerPath[-1] != "/":
    inSpeakerPath += "/"

inSpeakerPath += inSpeakers
#docLabel = "ls21-04"
#
#csv_reader = csv.reader(csv_file, delimiter=',')
#csv_reader = csv.DictReader(csv_file)
#csv_reader = csv.DictReader(csv_file, fieldnames = ("VideoLabel", "SpeakerLabel", "DisplayedSpeakerName", "FullSpeakerName", "FirstTurn", "RangeFrom", "RangeTo", "Notes" ), delimiter=',')
#with io.open("file", "r", newline=None) as fd:
with open(inSpeakerPath) as speaker_file:
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

# -------- paragraphs CSV

if inSentDir[-1] != "/":
    inSentDir += "/"

inParagPath = inSentDir + inParagFile
#inSentencePath = inParagPath
#inParagPath += inSentFile
#inSentencePath += inSentFile

#parag_reader = csv.DictReader(parag_file, fieldnames = ("start", "end", "speaker", "confid", "text" ))
#parag_reader = csv.DictReader(parag_file, fieldnames = ("start", "end", "speaker", "confid", "text" ), delimiter='\t')
#parag_reader = csv.reader(parag_file, delimiter=',')



# deleted following from input
correctedText = ""
firstWordCount = 0
lastWordCount = 0

if outDir[-1] != "/":
    outDir += "/"
#

paragPubPath = outDir 

if paragPubPath[-1] != "/":
    paragPubPath += "/"

paragPubPath += inSentFile + "_paragTranscript.txt"

#pPubF = open(paragPubPath, "w")

reportableTime = 0
parag_count = 0
paragWordCount = 0
current_speaker = "(Unknown Speaker)"
#with io.open("file", "r", newline=None) as fd:
print("inParagPath:")
print(inParagPath)
if exists(inParagPath):
    print("exists(inParagPath)")
    loadParagFile()
else:
    print("NO inParagPath!")
#


# -------- sentences CSV

#inSentPath = inSentDir + "/" + inSentFile
inSentPath = inSentDir + inSentFile

sentPubPath     = outDir
sentPubPathNoTS = outDir
srtPubPath      = outDir
mDPubPath       = outDir

srtPubPath      += inSentFile + "_transcript.srt"
mDPubPath       += inSentFile + "_transcript.md"
sentPubPath     += inSentFile + "_transcript.txt"
sentPubPathNoTS += inSentFile + "_transcriptNoTS.txt"   # Per Paul P, create version of text output with no timestamps

print("to write-open sentPubPath:")
print(sentPubPath)

srtPubF   = open(srtPubPath, "w")
mDPubF    = open(mDPubPath, "w")
sPubF     = open(sentPubPath, "w")
sPubFNoTS = open(sentPubPathNoTS, "w")

#   maxCharsPerCaption limits character length of (brand-new!) SRT file - check above for override logic

rawSents         = {}
accumedParag     = ""
accumedParagNoTS = ""
accumedSrt       = ""
sent_count     = 0
sentWordCount  = 0
lastReportTime = 0
currentSpeaker = "(Unknown Speaker)"
lastReportTime = 0

srtLine      = ""
srtLineLen   = len(srtLine)
#srtStart = ToSRTTime(srtStartTime)
#srtEnd   = ToSRTTime(srtEndTime)
#srtLine = setStart + " --> "
#lastBlank = testSrt.rFind(" ")

paragTimes = rawParags.keys()
print("paragTimes")
print(paragTimes)
print("")

print("to read-open inSentPath:")
print(inSentPath)

#with io.open("file", "r", newline=None) as fd:
sent_file = open(inSentPath, "r", newline=None)
if (sent_file == None):
    print(inSentPath + " not found")
else:
    allSents = sent_file.readlines()
    for pCount, sentRow in enumerate(allSents):
        if pCount == 0:
            print("Sentence headers: " + sentRow)
            continue
        #
        row = sentRow.split('\t')
        rowLen = len(row)
        #print(row)
        #if row[0] is not None and len(row[0]) > 0:
        reportString = ""
        reportStringNoTS = ""
        start = int(row[0])
        #print(start)
        #reportString += "Sentence starts at millisecond " + row[0] + ", "
        end = int(row[1])
        timerTime = False
        #reportString += "ends at " + row[1] + " "
        # Whisper extract now generates sentNum at row[2]
        speechDuration = end - start
        
        if rowLen > 2 and row[2] is not None and len(row[2]) > 0:
            sentNum = row[2]
        else:
            sentNum = ""
        #
        if rowLen > 3 and row[3] is not None and len(row[3]) > 0:
            speaker = row[3]
        else:
            speaker = ""
        
        #
        if rowLen > 4 and row[4] is not None and len(row[4]) > 0:
            confid = row[4]
            #confid = float(row[4])
            #reportString += ", confidence " + row[3] + " "
        else:
            confid = 0.5
        
        #
        # dropped textual "startTime"
        #
        if rowLen > 5 and row[5] is not None and len(row[5].rstrip()) > 0:
            text = row[5].rstrip()
            #reportString += '"' + row[5].strip('\n') + '"'
        else:
            text = ""
        #
        textLen = len(text)
        
        speechChars = len(text)
                    
        msPerChar = (speechDuration / speechChars) if speechChars > 0 else speechDuration   # pretend speech lasts one millisecond!
        
        # Dropped edit-related columns - RESTORE, maybe!
        #
        if str(start) in paragTimes:
            paragBreak = True
            #print(str(start) + " in paragTimes")
        else:
            paragBreak = False
            #print(str(start) + " NOT in paragTimes")
        
        #if len(speaker)>0 or len(startTime) > 0 or textLen > 0 or len(correctedText) > 0:
        srtSpeaker = ""     # SRT displays only NEW speaker ID
        if len(speaker)>0 or textLen > 0:
            # Now build next one, two, or three lines of output ([emptyLine] [speaker line] text)
            if len(correctedText) > 0:
                myText = correctedText
            else:
                myText = text
            #
            if len(speaker) > 0 and speaker != currentSpeaker:
                speakerName = speakerIdToName(docLabel, speaker, reportableTime)
                srtSpeaker = speakerName
                reportableTime = start
                if len(accumedParag) > 0:
                    sPubF.write(accumedParag)
                    sPubF.write("\r\n")
                    accumedParag = ""
                #
                if len(accumedParagNoTS) > 0:                    
                    sPubFNoTS.write(accumedParagNoTS)
                    sPubFNoTS.write("\r\n")
                    accumedParagNoTS = ""
                #
                sPubF.write("")     # empty line before next speech act
                sPubF.write("\r\n")
                sPubFNoTS.write("")     # empty line before next speech act
                sPubFNoTS.write("\r\n")
                #if len(startTime) > 0:
                #    reportableTime = int(hhMmSsToTime(startTime))
                #    reportString   = startTime
                #else:
                reportString   = ToDisplayTime(start)
                #reportString += " " 		# + speakerIdToName(speaker) + ":"        # Also account for missing or illformed start-time
                reportString += " " + speakerName + ":"

                reportStringNoTS = speakerName + ":"    # note: Timing has NO impact on NoTS output!
                
                #xx=speakerIdToName(docLabel, speaker, reportableTime)
                #if len(speaker) == 1:
                #    reportString += " Speaker " + speaker + ":"      # use lookup instead
                #else:
                #    reportString += " " + speaker + ":"
                #
                print(reportString)
                sPubF.write(reportString)       # contains only speaker name (or ersatz name "Speaker X")
                sPubF.write("\r\n")
                sPubFNoTS.write(reportStringNoTS)
                sPubFNoTS.write("\r\n")

                currentSpeaker = speaker
                lastReportTime = reportableTime                    
                reportString = myText
                reportStringNoTS = myText
                print(reportString)
                if len(accumedParag) > 0:
                    accumedParag += " " + reportString
                else:
                    accumedParag = reportString
                #
                if len(accumedParagNoTS) > 0:
                    accumedParagNoTS += " " + reportStringNoTS
                else:
                    accumedParagNoTS = reportStringNoTS
                #
            elif paragBreak:        # New paragraph within current speech!
                print("New paragraph per transcription heuristic")
                if len(accumedParag) > 0:
                    sPubF.write(accumedParag)
                    sPubF.write("\r\n")
                    accumedParag = ""
                #
                if len(accumedParagNoTS) > 0:
                    sPubFNoTS.write(accumedParagNoTS)
                    sPubFNoTS.write("\r\n")
                    accumedParagNoTS = ""
                #
                reportableTime = start
                if (0 + reportableTime) > (60000 + lastReportTime):	# Only some 'forced paragraphs' need timestamp
                    displayTime = ToDisplayTime(start)
                    reportString = displayTime + " "
                    lastReportTime = reportableTime
                    timerTime = True
                else:
                    reportString = ""
                #
                reportString += myText
                print(reportString)
                reportStringNoTS = myText       # no preceding timestamp
                #sPubF.write(reportString)
                #sPubF.write("\r\n")

                accumedParag = reportString
                #
                accumedParagNoTS = reportStringNoTS
                # 
                if len(accumedSrt) > 0:
                    accumedSrt += " " + reportString
                else:
                    accumedSrt = reportString
                #
            else:
                #if len(startTime) > 0:
                #    reportableTime = int(hhMmSsToTime(startTime))
                #    print("converted startTime:")
                #    print(reportableTime)
                #else:
                reportableTime = start
                #print("saved start:")
                print(reportableTime)
                #
                
                #print("[typeOf] lastReportTime:")
                #print(type(lastReportTime))
                #print(lastReportTime)                    
                #print("[typeOf] reportableTime:")
                #print(type(reportableTime))                    
                #print(reportableTime)
                if (0 + reportableTime) > (60000 + lastReportTime):	# report time every 60 seconds                    
                    if len(accumedParag) > 0:
                        sPubF.write(accumedParag)
                        sPubF.write("\r\n")
                        timerTime        = True
                        accumedParag     = ""
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
                reportString += myText
                print(reportString)
                reportStringNoTS += myText

                #sPubF.write(reportString)
                #sPubF.write("\r\n")
                if len(accumedParag) > 0:
                    accumedParag += " " + reportString
                else:
                    accumedParag = reportString
                #
                if len(accumedParagNoTS) > 0:
                    accumedParagNoTS += " " + reportStringNoTS
                else:
                    accumedParagNoTS = reportStringNoTS
                #
                if len(accumedSrt) > 0:
                    accumedSrt += " " + reportString
                else:
                    accumedSrt = reportString
                #
            #
        #
        if len(text) > 0:     # SRT written out for each non-empty sentence. 
            srtStartTime = start
            srtEndTime   = end    # reminder: take new start as old end
            writeToMD(text, srtPosCount, srtSpeaker, srtStartTime, srtEndTime, timerTime)      # pro forma
            #
            # use speakername; ignore paragraph info
            print(f'before writeToSrt(text: {text}, srtPosCount: {srtPosCount}, srtSpeaker: {srtSpeaker}, srtStartTime: {srtStartTime}, srtEndTime: {srtEndTime}')
            srtPosCount  = writeToSrt(text, srtPosCount, srtSpeaker, srtStartTime, srtEndTime)
            print(f'after writeToSrt(text: {text}, srtPosCount: {srtPosCount}, srtSpeaker: {srtSpeaker}, srtStartTime: {srtStartTime}, srtEndTime: {srtEndTime}')
        #
        #
    #
    if len(accumedParag) > 0:
        sPubF.write(accumedParag)
        sPubF.write("\r\n")
        accumedParag     = ""
    #
    if len(accumedParagNoTS) > 0:
        sPubFNoTS.write(accumedParagNoTS)
        sPubFNoTS.write("\r\n")
        accumedParagNoTS = ""
    #
    print(f'Processed {pCount} sentences.')

#
sent_file.close()
sPubF.close()
srtPubF.close()
sPubFNoTS.close()
mDPubF.close()
