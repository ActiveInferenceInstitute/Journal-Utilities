# Allow reading supplementary "words" file, with better per-word quality.
#   Can be a real SRT SubRip, 2-column screen-scraped YouTube transcript, or drawn from YouTube via API!
#cd "/mnt/e/Documents/DiscourseAnalysis/World Science Festival/Rethinking Thinking - How Intelligent Are Other Animals"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/enrichSentencesFromYouTube.py" "wsf20200201-1" "." "wsf20200201-1_Rethinking Thinking How Intelligent Are Other Animals.m4a.words.csv" "." "Rethinking Thinking How Intelligent Are Other Animals.en.srt"  | tee wsf20200201-1_SRT_publish.txt
#
# TEMPORARY bypass, cloned from "/Active Inference Podcast/sentencesToTranscripts - Copy (46).py"
#
#AllSpeakers "/mnt/d/Documents/FEP-AI/Active Inference Podcast/AllSpeakers.csv"

import csv
import time
import sys
import math
import json
from html.parser import HTMLParser
from youtube_transcript_api import YouTubeTranscriptApi
from requests_html import HTMLSession
import difflib as dl


if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) == 1:
        print("enrichSentencesFromYouTube.py -- Needs parameters docLabel (key binding references to this doc),")
        print("    inSentDir (path to incoming Sentence file, often '.'), inSentFile (name of driver file *.sentences.csv),")
        #print("    inSentWordFile (name of driver file *.sentWords.csv),")
        print("    inSrtDir  (path to incoming SRT file derived from YouTube (or from other source, e.g. AssemblyAI) -")
        print("              if special value '((youtube))', then inSrtFile will be interpreted as an 11-character YouTube videoTag.),")
        print("              if special value '((none))', then ignore this pair of arguments,")
        print("    inSrtFile (name of flat SRT in SubRip format, or 2-column .txt; or YouTube ID - see inSrtDir comments above.")
        print("Optional params outDir (defaults to working directory '.'), speakers (defaults to a central CSV identifying all speakers),")
        print("    ((other options))")
        print("Created in outDir: *_transcript.txt, *_built.srt, *_built.xhtml")
        print("If inSentDir holds a *.paragraphs.csv file, it's used to force paragraph ends.")
        quit()
    elif len(sys.argv) < 6:
        print("Need at least docLabel, inSentDir, inSentFile, inSrtDir, inSrtFile; optional outDir, speakers, ....")
        print("  *** Exiting! ***")
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
inSrtDir = sys.argv[4]
inSrtFile = sys.argv[5]
inSentWordFile = inSentFile.replace(".sentences.csv",".sentWords.csv")
if len(sys.argv) > 6:
    outDir = sys.argv[6]
else:
    outDir = "."    #publish to working directory!

if inSrtDir == "((youtube))":
    videoTag = inSrtFile
    print("docLabel, inSentDir, inSentFile, YouTube videoTag: " + "'" + docLabel + "', '" +  inSentDir + "', '" + inSentFile + "', '" + videoTag + "'")
else:
    print("docLabel, inSentDir, inSentFile, inSrtDir, inSrtFile: " + "'" + docLabel + "', '" +  inSentDir + "', '" + inSentFile + "', '" + inSrtDir + "', '" + inSrtFile + "'")
#

print("outDir: " + "'" + outDir + "'")

if len(sys.argv) > 7:
    speakerFile = sys.argv[7]
else:
    speakerFile = "/mnt/d/Documents/FEP-AI/Active Inference Podcast/AllSpeakers.csv"      #default - really, load from config file

print('speakers File: ' + "'" + speakerFile + "'")

#inSentDir = "/mnt/d/Documents/2022 Org Streams/os003/"
inParagFile   = inSentFile.replace('.sentences.', '.paragraphs.')



# -------------- globals -------------
punct="'\".,!?;&();~"


# -------------- mutable globals -------------
speakerDesc   = {}
realSRT       = False        # I.e. the only reliable raw items in srtLines are start and text
srtLineWords  = []
srtLines      = []           # all data about all SRTs packets
srtWords = {}
srtCharCount  = 0
allWords      = []           # merge SRT (or other high-accuracy, untrimmed word vector) with parsed, punctuated text
totalSrtWords = 0            # counts words in SRT (of whatever format)
totalSrtLines = 0
totalSrtChars = 0
paragTimes    = []
chapterTimes  = []
speakerDesc   = {}
rawParags     = {}
srtLexemes    = {}
sentLexemes   = {}
sentWordLexemes = {}

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


def readYouTubeTranscript():       # end and duration are not (reliably) populated
    global videoTag
    global totalSrtLines
    global totalSrtWords
    global totalSrtChars
    
    srtLineCount     = 0
    srtLineCharStart = 0
    srtLineWordStart = 0
    srtCharCount     = 0
    srtWordCount     = 0
    
    video_url = "https://www.youtube.com/watch?v=" + videoTag
    #session  = HTMLSession()
    #response = session.get(video_url)      # Don't we need this?
    allSrts = YouTubeTranscriptApi.get_transcript(videoTag)
    for srtPkt in allSrts:
        srtText     = srtPkt.get('text')
        srtStart    = int(round(1000*srtPkt.get('start'),0))
        srtDuration = int(round(1000*srtPkt.get('duration'),0))
        srtLineCount += 1
        srtLineCharCount = len(srtText)
        srtCharCount += srtLineCharCount
        mySrtWords = srtText.split()
        srtLineCharLen = len(srtText)
        srtLineWordCount = len(mySrtWords)
        srtWordCount += srtLineWordCount
        srtLines.append( {'srtLine':srtLineCount, 'srtStart': srtStart, 'srtDuration':srtDuration,
                          'srtLineWordStart':srtLineWordStart, 'srtLineCharStart':srtLineCharStart, 'srtWordCount':srtWordCount,
                          'srtLineCharCount':srtLineCharCount, 'srtLineCharLen': srtLineCharLen, 'srtWords': mySrtWords} )
        srtLineCharStart += srtLineCharLen                 # may be useful for fuzzy locating within SRT text
        srtLineWordStart += srtLineWordCount
        #
    #
    totalSrtLines = len(allSrts)
    totalSrtWords = srtWordCount
    totalSrtChars = srtCharCount
    return
#


def readSrtFile():         # arg tells whether "end" and "duration" are meaningful (i.e. whether lines came from a real SRT or from the API call)
    global inSrtDir, inSrtFile
    global totalSrtLines
    global totalSrtWords
    global totalSrtChars
    
    srtLineCount     = 0
    srtLineCharStart = 0
    srtLineWordStart = 0
    srtCharCount     = 0
    srtWordCount     = 0
    
    if inSrtDir[-1] != "/":
        inSrtDir += "/"
    #
    inSrtPath = inSrtDir +  inSrtFile
    
    srt_file = open(inSrtPath, "r", newline=None)
    if (srt_file == None):
        print(inSrtPath + " not found")
        quit()
    #
    allSrts = srt_file.readlines()
    srtFileLen=len(allSrts)
    
    #for pCount, srtRow in enumerate(allSrts):
    
    for i in range(0, srtFileLen-3, 4):   # four fields over three lines, then empty line
        srtLineCount += 1
        srtSeq = str(allSrts[i])
        srtTimes = allSrts[i+1]
        #       01:58:14,639 --> 01:58:16,139
        srtStart = hhMmSsMssToTime(srtTimes[0:12])
        srtEnd   = hhMmSsMssToTime(srtTimes[17:29])
        # srtLineDuration = srtEnd - srtStart
        srtText = allSrts[i+2]
        srtLineCharCount = len(srtText)
        mySrtWords = srtText.split()
        srtLineWordCount = len(mySrtWords)
        srtLines.append( {'srtLine':srtLineCount, 'srtStart': srtStart, 'srtEnd':srtEnd,
                         'srtLineWordStart':srtLineWordStart, 'srtLineCharStart':srtLineCharStart, 'srtWordCount':srtWordCount,
                         'srtLineCharCount':srtLineCharCount, 'srtLineWordCount':srtLineWordCount, 'srtWords': mySrtWords} )
        srtCharCount += srtLineCharCount     # may be useful for fuzzy locating within SRT text
        #
        srtLineCharStart += srtLineCharCount                 # may be useful for fuzzy locating within SRT text
        srtLineWordStart += srtLineWordCount
    #
    totalSrtLines = srtFileLen
    totalSrtWords = srtWordCount
    totalSrtChars = srtCharCount
    return
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
    """ 
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
    """
    #
    return [word, False]
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
            myWordLen = len(word)
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
