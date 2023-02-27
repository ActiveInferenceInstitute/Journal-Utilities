
#cd "/mnt/d/Documents/FEP-AI/2022 ModelStream/mo007/SPtest"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/sentencesToTranscripts.py" mo007-1 "." "mo007-1_mo007-1.mp3.sentences.csv" | tee mo007-1_publish.txt

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
        print("paragraphsToTranscripts. Needs parameters docLabel (key binding references to this doc),")
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
#   MaxChars    For SRT: Max line len in chars

#outDir = "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #035 A tale of Two architectures/ls035-0/publish"

inSpeakerDir = "/mnt/d/Documents/FEP-AI/Active Inference Podcast/"
inSpeakers = "AllSpeakers.csv"

docLabel = sys.argv[1]
inSentDir = sys.argv[2]
inSentFile = sys.argv[3]
print("docLabel, inSentDir, inSentFile " + "'" + docLabel + "', '" +  inSentDir + "', '" + inSentFile + "'")

#inSentDir = "/mnt/d/Documents/2022 Org Streams/os003/"
inParagFile = inSentFile.replace('.sentences.', '.paragraphs.')

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

# ++++++ notes ++++++

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


1

#j=ToDisplayTime(64968112)
#print(j)
#j = ToDisplayTime(4968112)
#print(j)
#j = ToDisplayTime(70337)
#print(j)
#j = ToDisplayTime(2337)
#print(j)


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

#j=ToSRTTime(64968112)
#print(j)
#j = ToSRTTime(4968112)
#print(j)
#j = ToSRTTime(70337)
#print(j)
#j = ToSRTTime(2337)
#print(j)

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

paragPubPath = outDir 

if paragPubPath[-1] != "/":
    paragPubPath += "/"

paragPubPath += inSentFile + "_paragTranscript.txt"

pPubF = open(paragPubPath, "w")

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
            if row[2] is not None and len(row[2]) > 0:
                speaker = row[2]
            else:
                speaker = ""
            
            #
            if rowLen > 3 and row[3] is not None and len(row[3]) > 0:
                confid = row[3]
                #reportString += ", confidence " + row[3] + " "
            else:
                confid = ""
            
            #
            if rowLen > 4 and row[4] is not None and len(row[4]) > 0:
                startTime = row[4]
                #reportString += '"' + row[4].strip('\n') + '"'
            else:
                startTime = ""
            
            if rowLen > 5 and row[5] is not None and len(row[5]) > 0:
                text = row[5]
                #reportString += '"' + row[5].strip('\n') + '"'
            else:
                text = ""
            
            if rowLen > 6 and row[6] is not None and len(row[6]) > 0:
                correctedText = row[6]
                #reportString += '"' + row[6].strip('\n') + '"'
            else:
                correctedText = ""

            if rowLen > 7 and row[7] is not None and len(row[7]) > 0:
                firstWordCount = row[7]
                #reportString += '"' + row[7].strip('\n') + '"'
            else:
                firstWordCount = 0

            if rowLen > 8 and row[8] is not None and len(row[8]) > 0:
                lastWordCount = row[8]
                #reportString += '"' + row[8].strip('\n') + '"'
            else:
                lastWordCount = 0

            rawParags.update( {start : [end, speaker, confid, firstWordCount, lastWordCount] } )

            #
            if len(speaker)>0 or len(startTime) > 0 or len(text) > 0 or len(correctedText) > 0:
                # Now build next one, two, or three lines of output ([emptyLine] [speaker line] text)
                if len(correctedText) > 0:
                    myText = correctedText
                else:
                    myText = text
                
                #
                if len(speaker) > 0 and speaker != current_speaker:
                    pPubF.write("")     # empty line before next speech act
                    pPubF.write("\r\n")
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
                    pPubF.write(reportString)
                    pPubF.write("\r\n")
                    current_speaker = speaker
                    reportString = myText
                    print(reportString)
                    pPubF.write(reportString)
                    pPubF.write("\r\n")
                else:
                    #reportString = ToDisplayTime(start) + " " + text
                    reportString = startTime + " " + myText
                    print(reportString)
                    pPubF.write(reportString)
                    pPubF.write("\r\n")
                
                #
            
            #
        
    #
    print(f'Processed {pCount} paragraphs.')

#
parag_file.close()
pPubF.close()

print(rawParags)


# -------- sentences CSV

inSentPath = inSentDir + "/" + inSentFile

sentPubPath = outDir 

sentPubPath += inSentFile + "_transcript.txt"

sPubF = open(sentPubPath, "w")
rawSents = {}
accumedParag = ""
sent_count = 0
sentWordCount = 0
lastReportTime = 0
currentSpeaker = "(Unknown Speaker)"
lastReportTime = 0

paragTimes = rawParags.keys()
print("")
print(paragTimes)
print("")

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
            if rowLen >= 3 and row[2] is not None and len(row[2]) > 0:
                speaker = row[2]
            else:
                speaker = ""
            
            #
            if rowLen >= 4 and row[3] is not None and len(row[3]) > 0:
                confid = float(row[3])
                #reportString += ", confidence " + row[3] + " "
            else:
                confid = ""
            
            #
            if rowLen >= 5 and row[4] is not None and len(row[4]) > 0:
                startTime = row[4]
                #reportString += '"' + row[4].strip('\n') + '"'
            else:
                startTime = ""
            
            if rowLen >= 6 and row[5] is not None and len(row[5]) > 0:
                text = row[5].rstrip()
                #reportString += '"' + row[5].strip('\n') + '"'
            else:
                text = ""
            
            if rowLen >= 7 and row[6] is not None and len(row[6]) > 0:
                correctedText = row[6].rstrip()
                #reportString += '"' + row[6].strip('\n') + '"'
            else:
                correctedText = ""
            
            if rowLen >= 8 and row[7] is not None and len(row[7]) > 0:
                speakerName = row[7]
                #reportString += '"' + row[7].strip('\n') + '"'
            else:
                speakerName = 0
            
            #
            if str(start) in paragTimes:
                paragBreak = True
                #print(str(start) + " in paragTimes")
            else:
                paragBreak = False
                #print(str(start) + " NOT in paragTimes")
            
            #if len(speaker)>0 or len(startTime) > 0 or len(text) > 0 or len(correctedText) > 0:
            if len(speaker)>0 or len(text) > 0:
                # Now build next one, two, or three lines of output ([emptyLine] [speaker line] text)
                if len(correctedText) > 0:
                    myText = correctedText
                else:
                    myText = text
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
                    print(reportString)
                    sPubF.write(reportString)
                    sPubF.write("\r\n")
                    currentSpeaker = speaker
                    lastReportTime = reportableTime                    
                    reportString = myText
                    print(reportString)
                    #sPubF.write(reportString)
                    #sPubF.write("\r\n")
                    if len(accumedParag) > 0:
                        accumedParag += " " + reportString
                    else:
                        accumedParag = reportString
                    #
                elif paragBreak:
                    print("New paragraph per upstream Whisper heuristic")
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
                    print("[typeOf] lastReportTime:")
                    print(type(lastReportTime))
                    print(lastReportTime)                    
                    print("[typeOf] reportableTime:")
                    print(type(reportableTime))                    
                    print(reportableTime)
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
                #
            #
        #
    #
    print(f'Processed {pCount} sentences.')

#
sent_file.close()
sPubF.close()

