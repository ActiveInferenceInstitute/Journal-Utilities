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
#cd "/mnt/d/Documents/FEP-AI/2022 ModelStream/mo007/SPtest"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/sentencesToTranscripts.py" mo007-1 "." "mo007-1_mo007-1.mp3.sentences.csv" | tee mo007-1_publish.txt
#
#AllSpeakers "/mnt/d/Documents/FEP-AI/Active Inference Podcast/AllSpeakers.csv"

import csv
import time
import sys
import math
import json
from html.parser import HTMLParser

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
#   charsPerCaption    For SRT: Max line len in chars

charsPerCaption = 40    # cloned from AssemblyAI default - allow override from command line!
lastMDTs = -1           # initialize last MarkDown timestamp (any possible value is later!)

#outDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #035 A tale of Two architectures/ls035-0/publish"

mDPubF = ""
pPubF        = ""
sPubF        = ""
srtPubF      = ""

inSpeakerDir = "/mnt/d/Documents/FEP-AI/Active Inference Podcast/"
inSpeakers = "AllSpeakers.csv"

docLabel = sys.argv[1]
inSentDir = sys.argv[2]
inSentFile = sys.argv[3]
print("docLabel, inSentDir, inSentFile " + "'" + docLabel + "', '" +  inSentDir + "', '" + inSentFile + "'")

#inSentDir = "/mnt/d/Documents/2022 Org Streams/os003/"
inParagFile   = inSentFile.replace('.sentences.', '.paragraphs.')

if len(sys.argv) > 4:
    outDir = sys.argv[4]
else:
    outDir = "."    #publish to working directory!

print("outDir: " + "'" + outDir + "'")

if len(sys.argv) > 5:
    speakerFile = sys.argv[5]
else:
    speakerFile = "/mnt/d/Documents/FEP-AI/Active Inference Podcast/AllSpeakers.csv"

print('speakers File: ' + "'" + speakerFile + "'")

# globals
speakerDesc = {}
srtSpeaker = ""
srtPosCount  = 0
srtStartTime = 0
srtEndTime   = 0

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

def writeToMD(textOut, lineCount, mySpeakerName, startTime, endTime, myParagBreak):
    global lastMDTs
    #print("In writeToMD, lineCount:")
    if len(mySpeakerName) > 0:
        mDPubF.write("\r\n" + ToDisplayTime(startTime) + " _" + mySpeakerName + ":_")
        mDPubF.write("\r\n")
        mDPubF.write("\r\n")
        mDPubF.write(textOut)
        mDPubF.write("\r\n")
        lastMDTs = startTime
    elif myParagBreak:
        print("parag hit in writeToMD " + str(startTime))
        mDPubF.write("\r\n" + ToDisplayTime(startTime) + " " + textOut)
        mDPubF.write("\r\n")
        lastMDTs = startTime
    elif (0 + startTime) > (lastMDTs + 60000):
        print("60-second hit in writeToMD " + str(startTime))
        mDPubF.write("\r\n" + ToDisplayTime(startTime) + " " + textOut)
        mDPubF.write("\r\n")
        lastMDTs = startTime
    else:
        mDPubF.write(textOut)
        mDPubF.write("\r\n")
    #
#


def writeToSrt(textOut, lineCount, mySpeakerName, startTime, endTime):
    print("In writeToSrt, lineCount:")
    print(lineCount)
    myLineCount = lineCount
    if len(mySpeakerName) == 0:
        textRem = ""
    else:
        textRem = mySpeakerName + ": "   # We will count length of speaker name as though it were audible.
        #                                   This may be convenient for viewing; but it makes 
        #                                   detailed SRT time-labels useless for reconstructing speech timing
    #
    textRem   += textOut.strip()
    charsRem  = len(textRem)
    timeRem   = endTime - startTime
    msPerChar = (timeRem / charsRem) if charsRem > 0 else charsRem
    oc1 = charsPerCaption+1     # lets us see a single character at end of window
    oc2 = oc1 + 1               # sees single character at end of window
    #if charsRem > 0:         # should try to split last pair of lines evenly
    while charsRem > 0:         # should try to split last pair of lines evenly
        if charsRem <= charsPerCaption:
            myLineCount += 1
            srtPubF.write(str(myLineCount))
            srtPubF.write("\r\n")
            srtStart = ToSRTTime(startTime)
            srtEnd   = ToSRTTime(endTime)
            srtLine  = srtStart + " --> " + srtEnd
            srtPubF.write(srtLine)
            srtPubF.write("\r\n")
            srtPubF.write(textRem)
            srtPubF.write("\r\n")
            srtPubF.write("")
            srtPubF.write("\r\n")
            charsRem = 0
        else:
            prevSpace = textRem[0:oc2].rfind(" ")
            if prevSpace >= 0:  # leading integral block of text; dump thru following space
                myText0  = textRem[0:prevSpace+1].strip()
                myLineCount += 1
                srtPubF.write(str(myLineCount))
                srtPubF.write("\r\n")
                srtStart = ToSRTTime(startTime)
                srtEnd   = ToSRTTime(endTime)
                srtLine  = srtStart + " --> " + srtEnd
                srtPubF.write(srtLine)
                srtPubF.write("\r\n")
                startTime = endTime
                srtPubF.write(myText0)
                srtPubF.write("\r\n")                
                srtPubF.write("")
                srtPubF.write("\r\n")       # close this SRT block
                textRem = textRem[prevSpace:].strip()   # remainder
                charsRem  = len(textRem)
            else:
                #  Maybe add test for line terminators, notably "-"
                nextSpace = textRem.find(" ")
                if nextSpace < 0:   # solid block of text; dump all
                    myLineCount += 1
                    srtPubF.write(str(myLineCount))
                    srtPubF.write("\r\n")
                    srtStart = ToSRTTime(startTime)
                    srtEnd   = ToSRTTime(endTime)
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
                    myText0  = textRem[0:oc1].strip()
                    textRem = textRem[oc1:].strip()
                    textRem = textRem[oc1:].strip()
                    charsRem  = len(textRem)
                    srtStart = ToSRTTime(startTime)
                    srtEnd   = ToSRTTime(endTime)
                    srtLine  = srtStart + " --> " + srtEnd
                    srtPubF.write(srtLine)
                    srtPubF.write("\r\n")
                    srtPubF.write(textRem)
                    srtPubF.write("\r\n")
                    srtPubF.write("")
                    srtPubF.write("\r\n")
                    charsRem = 0
                #
            #
        #
    #
    charsRem = 0
    return myLineCount
#


# ---------------- MAIN -----------------

#outDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #035 A tale of Two architectures/ls035-1/publish"

inSpeakerDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #040 - Chris Fields... A free energy principle for generic quantum systems/ls040-1_noSpeaker"
inSpeakers = "noSpeaker_ls040-0.Speakers.csv"
inSpeakerDir = "/mnt/d/Documents/FEP-AI/Active Inference Podcast"
inSpeakers = "AllSpeakers.csv"


#inSentDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #040 - Chris Fields... A free energy principle for generic quantum systems/ls040-1_noSpeaker"
#inSentFile = "ls036-0_ls036-0.m4a.paragraphs.csv"
#inSentDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #036 Modeling Ourselves/ls036-0"
#inSentFile = "ls036-0_ls036-0.m4a.paragraphs.csv"
#inSentDir = "/mnt/d/Documents/FEP-AI/2022 Org Streams/os003"
#inSentFile = "Bijan_os003-1.m4a.paragraphs.csv"

charsPerCaption = 40    # cloned from AssemblyAI default - set up override!
#lastMDTs = -1           # initialize last MarkDown timestamp (any possible value is later!)

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


rawParags = {}
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
            start = row[0]
            #print(start)
            #reportString += "Paragraph starts at millisecond " + row[0] + ", "
            end = row[1]            
            #reportString += "ends at " + row[1] + " "
            # Whisper extract now inserts paragNum as row[2]
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
                #reportString += ", confidence " + row[3] + " "
            else:
                confid = ""
            
            #
            if rowLen > 5 and row[5] is not None and len(row[4]) > 0:
                startTime = row[5]
                #reportString += '"' + row[4].strip('\n') + '"'
            else:
                startTime = ""
            #
            if rowLen > 5 and row[5] is not None and len(row[5]) > 0:
                text = row[5]
                #reportString += '"' + row[5].strip('\n') + '"'
            else:
                text = ""
            #
            textLen = len(text)
            if rowLen > 6 and row[6] is not None and len(row[6]) > 0:
                wordCount = row[6]
                #reportString += '"' + row[7].strip('\n') + '"'
            else:
                wordCount = len(text.split())
            #
            # no longer receiving edit-oriented correctedText, firstWordCount, lastWordCount
            #
            rawParags.update( {start : [end, speaker, confid, firstWordCount, lastWordCount] } )
            #
            #
            if len(speaker)>0 or len(startTime) > 0 or len(text) > 0 or len(correctedText) > 0:
                # Now build next one, two, or three lines of output ([emptyLine] [speaker line] text)
                if len(correctedText) > 0:
                    myText = correctedText
                else:
                    myText = text
                # lastBlank = testSrt.rFind(" ")
                #
                if len(speaker) > 0 and speaker != current_speaker:
                    #pPubF.write("")     # empty line before next speech act
                    #pPubF.write("\r\n")
                    reportString = startTime + " " # + speakerIdToName(speaker) + ":"        # Also account for missing or illformed start-time
                    
                    reportString += speakerIdToName(docLabel, speaker, reportableTime) + ":"
                    #
                    #xx=speakerIdToName(docLabel, speaker, reportableTime)
                    #if len(speaker) == 1:
                    #    reportString += "Speaker " + speaker + ":"      # use lookup instead
                    #else:
                    #    reportString += speaker + ":"
                    #
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
    print(f'Processed {pCount} paragraphs.')

#
parag_file.close()
#pPubF.close()

print(rawParags)


# -------- sentences CSV

#inSentPath = inSentDir + "/" + inSentFile
inSentPath = inSentDir + inSentFile

sentPubPath = outDir
srtPubPath  = outDir
mDPubPath   = outDir

sentPubPath += inSentFile + "_transcript.txt"
srtPubPath  += inSentFile + "_transcript.srt"
mDPubPath   += inSentFile + "_transcript.md"

print("to write-open sentPubPath:")
print(sentPubPath)

sPubF   = open(sentPubPath, "w")
srtPubF = open(srtPubPath, "w")
mDPubF  = open(mDPubPath, "w")

#   charsPerCaption limits character length of (brand-new!) SRT file - check above for override logic

rawSents = {}
accumedParag = ""
accumedSrt = ""
sent_count = 0
sentWordCount = 0
lastReportTime = 0
currentSpeaker = "(Unknown Speaker)"
lastReportTime = 0

srtLine      = ""
srtLineLen   = len(srtLine)
#srtStart = ToSRTTime(srtStartTime)
#srtEnd   = ToSRTTime(srtEndTime)
#srtLine = setStart + " --> "
#lastBlank = testSrt.rFind(" ")
"""
>>> a="I am the witch, Doctor!"
>>> print(a.rfind(" "))
15
>>> h="abc"
>>> a=h.rfind("b")
>>> print(a)
1
>>> print(h.rfind("b"))
1
>>> print(h.rfind("a"))
0
>>> print(h.rfind("c"))
2
>>> print(h.rfind("d"))
-1

>>> h="aba"
>>> print(h.rfind("a"))
2
>>> print(h.rfind("b"))
1
>>> print(h.rfind("c"))
-1
 """

paragTimes = rawParags.keys()
print("")
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
        else:
            row = sentRow.split('\t')
            rowLen = len(row)
            #print(row)
            #if row[0] is not None and len(row[0]) > 0:
            reportString = ""
            start = int(row[0])
            #print(start)
            #reportString += "Sentence starts at millisecond " + row[0] + ", "
            end = int(row[1])
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
                confid = float(row[4])
                #reportString += ", confidence " + row[3] + " "
            else:
                confid = ""
            
            #
            # dropped textual "startTime"
            #
            if rowLen > 5 and row[5] is not None and len(row[5]) > 0:
                text = row[5].rstrip()
                #reportString += '"' + row[5].strip('\n') + '"'
            else:
                text = ""
            #            
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
                    sPubF.write("")     # empty line before next speech act
                    sPubF.write("\r\n")
                    #if len(startTime) > 0:
                    #    reportableTime = int(hhMmSsToTime(startTime))
                    #    reportString   = startTime
                    #else:
                    reportString   = ToDisplayTime(start)
                    #
                    #reportString += " " 		# + speakerIdToName(speaker) + ":"        # Also account for missing or illformed start-time
                    reportString += " " + speakerName + ":"
                    
                    #xx=speakerIdToName(docLabel, speaker, reportableTime)
                    #if len(speaker) == 1:
                    #    reportString += " Speaker " + speaker + ":"      # use lookup instead
                    #else:
                    #    reportString += " " + speaker + ":"
                    #
                    print(reportString)
                    sPubF.write(reportString)
                    sPubF.write("\r\n")
                    currentSpeaker = speaker
                    lastReportTime = reportableTime                    
                    reportString = myText
                    print(reportString)
                    if len(accumedParag) > 0:
                        accumedParag += " " + reportString
                    else:
                        accumedParag = reportString
                    #
                elif paragBreak:
                    print("New paragraph per transcription heuristic")
                    if len(accumedParag) > 0:
                        sPubF.write(accumedParag)
                        sPubF.write("\r\n")
                        accumedParag = ""
                    #
                    reportableTime = start
                    if (0 + reportableTime) > (60000 + lastReportTime):	# Only some 'forced paragraphs' need timestamp
                        displayTime = ToDisplayTime(start)
                        reportString = displayTime + " "
                        lastReportTime = reportableTime
                    else:
                        reportString = ""
                    #
                    reportString += myText
                    print(reportString)
                    #sPubF.write(reportString)
                    #sPubF.write("\r\n")
                    if len(accumedParag) > 0:
                        accumedParag += " " + reportString
                    else:
                        accumedParag = reportString
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
                    reportString += myText
                    print(reportString)
                    #sPubF.write(reportString)
                    #sPubF.write("\r\n")
                    if len(accumedParag) > 0:
                        accumedParag += " " + reportString
                    else:
                        accumedParag = reportString
                    #
                    if len(accumedSrt) > 0:
                        accumedSrt += " " + reportString
                    else:
                        accumedSrt = reportString
                    #
                #
            #
            if len(myText) > 0:     # SRT written out for each non-empty sentence. 
                writeToMD(myText, srtPosCount, srtSpeaker, start, end, paragBreak)      # pro forma
                # use speakername; ignore paragraph info
                srtEndTime   = end    # reminder: take new start as old end
                srtPosCount  = writeToSrt(text, srtPosCount, srtSpeaker, srtStartTime, srtEndTime)
                srtStartTime = start
            #
        #
    #
    if len(accumedParag) > 0:
        sPubF.write(accumedParag)
        sPubF.write("\r\n")
        accumedParag = ""
    #
    print(f'Processed {pCount} sentences.')

#
sent_file.close()
sPubF.close()
srtPubF.close()
mDPubF.close()
