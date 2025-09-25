# cd "/mnt/d/zip"
# python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/RunLocalWhisper.py" Beast666 "." "Aleister Crowley Legend Of The Beast 05-22.m4a" | tee Beast666_Beast_0522_text5.json

import requests
import time
import sys
import math
import csv
import json
import whisper

if __name__ == "__main__":
    print(f'Arguments count: {len(sys.argv)}')
    if len(sys.argv) < 3:
        print("Need at least docLabel, onlinePath, and audioInput; exiting!")
        quit()
#    
#for i, arg in enumerate(sys.argv):
#    print(f'Argument {i:>6}: {arg}')

docLabel   = sys.argv[1]
onlinePath = sys.argv[2]
audioInput = sys.argv[3]

# -------------- globals -------------
punct="'\".,!?;&();~"
defaultConfidence = 0.6
defaultConfidenceStr = str(defaultConfidence)

model = whisper.load_model("large")      # "large" "base"
result = model.transcribe(audioInput)
print("***  result ***")
print(result)

for iii, resElem in enumerate(result):
    print(">>> " + str(iii) + " <<<")
    print(resElem)
    print("")
#
print("")
print("***  result[text] ***")
print(result["text"])
mySegments=result["segments"]

sentenceFileName = docLabel + "_" + audioInput + ".sentences.csv"
sssf = open(sentenceFileName, "w")
sentOut = "start" + "\t" + "end" + "\t" + "sentNum" + "\t" + "speaker" + "\t" + "confidence" + "\t" + "text"
sssf.write(sentOut)
sssf.write("\r\n")

sentenceWordFileName = docLabel + "_" + audioInput + ".sentencesWords.csv"
sswf = open(sentenceWordFileName, "w")
sentWordOut = "start" + "\t" + "end" + "\t" + "sentNum" + "\t" + "wordNum" + "\t" + "speaker" + "\t" + "confidence" + "\t" + "text"
#sentWordOut = "sentNum" + "\t" + "wordNum" +"\t" + "word"
sswf.write(sentWordOut)
sswf.write("\r\n")


speaker = ""
tokenTable = {}

for mySeg in mySegments:
    print(mySeg)
    sentNum = mySeg["id"]
    start   = round(1000*mySeg["start"])
    end     = round(1000*mySeg["end"])
    text    = mySeg["text"].strip()
    tokens  = mySeg["tokens"]
    temperature       = mySeg["temperature"]
    avg_logprob       = mySeg["avg_logprob"]
    compression_ratio = mySeg["compression_ratio"]
    no_speech_prob    = mySeg["no_speech_prob"]
    sentOut = str(start) + "\t" + str(end) + "\t" + str(1+sentNum) + "\t" 
    sentOut += speaker
    sentOut += "\t" + str(temperature) + "\t" + text
    sssf.write(sentOut)
    sssf.write("\r\n")
    words = text.split()
    wordCount = len(words)
    tokenCount = len(tokens)
    #
    sentWordOutX = str(1+sentNum) + "\t"
    for wordNum, word in enumerate(words):
        #word = tokens[tokenNum]
        #word  = words[tokenNum]
        myWord    = word.strip().strip(punct)
        # insert logic to approximate word start/end timepoints!
        sentWordOut = "\t"      # start
        sentWordOut += "\t"     # end
        sentWordOut += sentWordOutX + str(1+wordNum) + "\t" + speaker + "\t" + defaultConfidenceStr + "\t" + myWord
        sswf.write(sentWordOut)
        sswf.write("\r\n")
    #
    """ 
    #print("tokenCount, wordCount")
    #print(tokenCount)
    #print(wordCount)
    #if tokenCount == (1+wordCount):
    sentWordOutX = str(1+sentNum) + "\t"
    tokenNum = 0
    token = tokens[tokenNum]
    word  = words[tokenNum]
    sentWordOut = sentWordOutX + str(tokenNum) + "\t" + str(token) + "\t" + word
    sswf.write(sentWordOut)
    sswf.write("\r\n")
    """
    """
    if tokenCount != (wordCount+1):
        print("skip " + str(1+sentNum))
    else:
        for tokenNum, token in enumerate(tokens):
            token = tokens[tokenNum]
            word  = words[tokenNum]
            sentWordOut = sentWordOutX + "\t" + str(tokenNum) + "\t"  + str(tokenNum) + "\t" + str(token) + "\t" + "\t" + word
            sswf.write(sentWordOut)
            sswf.write("\r\n")
            #print("tokenNum")
            #print(tokenNum)
        #
    #
    """
    #print(sentNum)
    #print(start)
    #print(text)
#
sssf.close()
sswf.close()

quit()
