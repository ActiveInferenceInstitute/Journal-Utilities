#! ...python3
acIIAuthKey  = "5a030052b923451aa82ce5776a91fd34"     # "1b98316b53374f6f877961104b8f2e40"
davesAuthKey = "69a859d5af954f4f99adb583c76380a5"
useThisAuthKey = acIIAuthKey

# cd "/mnt/d/Documents/FEP-AI/2022 Livestreams/ls042/ls042-0"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper_textbook.py" "ls042-0" "http://crisiscenter.us/AILab01/2022Livestreams" "ls042-0.m4a" | tee ls042-0_whisper_m4a.json &

# For more logic, see "Transcribe ls036 Modelling ourselves.txt" in "D:\Documents\FEP-AI\2022 Livestreams\ActInf Livestream #036 Modeling Ourselves"

import requests
import time
import sys
import math
import csv
import json


#call with python3 - BerlinSym2021KJFKey "http://crisiscenter.us/AILab01/Karl_Friston_Applied_Active_Inference_Symposium_2021-06-22" "Quadrille.wav"
#call with python3 - quadriTest "http://crisiscenter.us/AILab01/Karl_Friston_Applied_Active_Inference_Symposium_2021-06-22" "Quadrille.wav"	rzw49dpr1n-4856-4172-adf4-e502720c93de

#call with python3 - ls051-0 "http://crisiscenter.us/AILab01/2022Livestreams" "ls051-0.wav"	rskfsnu6hj-8e56-4c7d-a4d1-76aa04ab873a
#call with python3 - ls051-0-2 "http://crisiscenter.us/AILab01/2022Livestreams" "ls051-0-2.mp3"	rsk599qwnx-7e0e-49c2-bafd-8cb0ad4745db

#python3 - ls036-0 "http://crisiscenter.us/AILab01/2022Livestreams" "ls036-0.m4a"
#call with python3 - ls036-2 "http://crisiscenter.us/AILab01/2022Livestreams" "ls036-2.m4a"	

if __name__ == "__main__":
    print(f'Arguments count: {len(sys.argv)}')
    if len(sys.argv) < 3:
        print("Need at least docLabel, onlinePath, and onlineFile; exiting!")
        quit()
    

#for i, arg in enumerate(sys.argv):
#    print(f'Argument {i:>6}: {arg}')

docLabel = sys.argv[1]
onlinePath = sys.argv[2]
onlineFile = sys.argv[3]
print("docID, onlinePath, onlineFile " + "'" + docLabel + "', '" +  onlinePath + "', '" + onlineFile + "'")
if len(sys.argv) > 4:
    outputPath = sys.argv[4]
    print("outputPath: " + "'" + outputPath + "'")

# modifiable globals
auto_highlights_value = True
language_model_value = "medium",     # "large"  "medium"

word_boost_list = [
"ActInf Lab",
"basal ganglia",
"Bayes rule",
"Bayesian mechanics",
"Bayes",
"Bayesian ontology",
"Bayesian brain",
"Bayesian surprise",
"birdsong",
"cortical microcircuit",
"Da Costa",
"Bert DeVries",
"DeVries",
"Dirichlet distribution",
"dopamine",
"ergodicity",
"Bayesian",
"Euler Lagrange equations",
"factor graph",
"FEP",
"free energy",
"Free Energy Principle",
"generalized coordinates of motion",
"generalized synchrony",
"generative adversarial networks",
"goal directed behaviour",
"habits",
"Hamiltonian",
"hippocampus",
"hybrid models",
"ideomotor theory",
"information gain",
"interoceptive inference",
"Jakub",
"Jensen",
"KL divergence",
"Kullback Leibler divergence",
"Laplace approximation",
"Lorenz systems",
"Lotka Volterra systems",
"meta Bayesianism",
"microcircuit",
"motivation",
"navigation",
"NESS",
"neurotransmitters",
"Newtonian dynamics",
"nonequilibrium steady state",
"Occam",
"optimality",
"parametric empirical Bayes",
"Parkinson",
"Partially Observed Markov Decision Process",
"PEB",
"perceptual control theory",
"planning",
"POMDP",
"qualia",
"random dynamical system",
"reading",
"reinforcement learning",
"saccades",
"self evidencing",
"social dynamics",
"softmax",
"synaptic efficacy",
"self organization",
"surprise",
"Taylor series",
"thalamus",
"Thomas Metzinger",
"value function",
"variational autoencoders",
"variational free energy",
"variational Laplace",
"variational message passing",
"working memory",
"Parkinsonism",
"Parkinsonian",
# ---------
"Thomas Parr",
"Parr",
"Giovanni Pezzulo",
"Pezzulo",
"Rohan",
"Lagrange",
"Lagrangian",
"centripetal force",
"Mahault Albarracin",
"Mahault",
"Beren Millidge",
"Anil Seth",
"Axel Constant",
"Andy Clark",
"Michael Kirchhoff",
"Lancelot Costa",
"Axel Constant",
"Andy Clark",
"Michael Kirchhoff",
"Tim Verbelen",
#
"ActInf GuestStream",
"ActInf Livestream",
"ActInf project",
"ActInf",
"Active Inference",
"Active Inference GuestStream",
"Active Inference Institute",
"Active Inference Livestream",
"Active Inference MathStream",
"Active Inference ModelStream",
"Active Inference OrgStream",
"Ali",
"Bayesian",
"Bayesian inference",
"Bleu",
"Daniel",
"Dean",
"Free Energy Principle",
"Friston",
"Friston blanket",
"Karl Friston",
"Karl J. Friston",
"Karl",
"Markov blanket",
"Markov decision",
"Stephen",
"YouTube",
# -----------------
"Principle of Least Action",
"Least Action",
"action oriented representation",
"action planning",
"action prediction",
"action",
"active states",
"active",
"activity",
"affordance",
"agency",
"agent",
"agreement",
"allostasis",
"allostat",
"ambiguity",
"aspects",
"assumptions",
"asymmetry",
"attention",
"Bayesian statistics physics",
"behavior",
"belief updating",
"Bellman equation",
"Bijan Khezri",
#
"I'll",
"I've",
"I'm",
#                   Following section comes from whisper output (minus many "common" words)
"afterthought",
"application",
"appropriate",
"approximate",
"approximately",
"articulation",
"associations",
"categorical",
"communicate",
"computation",
"computational",
"conditionally",
"consequence",
"consideration",
"considering",
"constituting",
"construction",
"customization",
"derivations",
"description",
"descriptions",
"development",
"discussions",
"distinction",
"distinguishing",
"distribution",
"educationally",
"efficiently",
"elaborating",
"environment",
"expectation",
"formulation",
"formulations",
"fundamental",
"generalization",
"hierarchical",
"independent",
"inferential",
"information",
"ingredients",
"interaction",
"interactive",
"interesting",
"justification",
"mathematical",
"mathematically",
"minimization",
"misconceptions",
"necessarily",
"observables",
"observation",
"observations",
"parameterize",
"parameterizes",
"perspective",
"possibilities",
"possibility",
"presentation",
"probabilistic",
"psychological",
"relationships",
"simulations",
"sophisticated",
"specifically",
"statistical",
"statistically",
"supplementary",
"symmetrical",
"temperature",
"terminology",
"trajectories",
"uncertainty",
"variational"
]

custom_spelling_list = [ 
{"from": ["fep"], "to": "FEP"},
{"from": ["hamiltonian"], "to": "Hamiltonian"},
{"from": ["jensen"], "to": "Jensen"},
{"from": ["bayesianism"], "to": "Bayesianism"},
{"from": ["ness"], "to": "NESS"},
{"from": ["occam"], "to": "Occam"},
{"from": ["parkinson"], "to": "Parkinson"},
{"from": ["peb"], "to": "PEB"},
{"from": ["pomdp"], "to": "POMDP"},
{"from": ["parkinsonism"], "to": "Parkinsonism"},
{"from": ["parkinsonian"], "to": "Parkinsonian"},
# ----
{"from": ["Yaakup","Jakup"], "to": "Jakub"},
{"from": ["Yvonne","ivan"], "to": "Ivan"},
{"from": ["rohan","Rohan","Roland"], "to": "Rohan"},
{"from": ["ali"], "to": "Ali"},
{"from": ["mahault", "Malva", "mal", "mao"], "to": "Mahault"},
{"from": ["Abarasan","Hasan"], "to": "Albarracin"},
{"from": ["Saffron"], "to": "Safron"},
{"from": ["parr"], "to": "Parr"},
{"from": ["beren"], "to": "Beren"},
{"from": ["millidge"], "to": "Millidge"},
{"from": ["anil"], "to": "Anil"},
{"from": ["pease","peas"], "to": "Pease"},
{"from": ["seth"], "to": "Seth"},
{"from": ["verbelen"], "to": "Verbelen"},
{"from": ["actinf"], "to": "ActInf"},
{"from": ["bayesian"], "to": "Bayesian"},
{"from": ["jakub","yakub","yacub"], "to": "Jakub"},
{"from": ["daniel"], "to": "Daniel"},
{"from": ["karl", "carl"], "to": "Karl"},
{"from": ["fristen", "friston"], "to": "Friston"},
{"from": ["markov"], "to": "Markov"},
{"from": ["ness"], "to": "NESS"},
{"from": ["youtube"], "to": "YouTube"},
{"from": ["gueststream"], "to": "GuestStream"},
{"from": ["livestream"], "to": "Livestream"},
{"from": ["mathstream"], "to": "MathStream"},
{"from": ["modelstream"], "to": "ModelStream"},
{"from": ["orgstream"], "to": "OrgStream"},
#
{"from": ["bleu"], "to": "Bleu"},
{"from": ["actinflab", "Activeflab"], "to": "ActInfLab"},
{"from": ["google"], "to": "Google"},
{"from": ["aristotelian"], "to": "Aristotelian"},
{"from": ["i'm"], "to": "I'm"},
{"from": ["i'll"], "to": "I'll"},
{"from": ["i've"], "to": "I've"},
#-------------------
{"from": ["lagrange"], "to": "Lagrange"},
{"from": ["lagrangian"], "to": "Lagrangian"}
]

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



# ---------------------


#"audio_url": " + onlinePath + "/" + onlineFile + ",
#"audio_url": "http://crisiscenter.us/AILab01/Karl_Friston_Applied_Active_Inference_Symposium_2021-06-22/Quadrille.wav",

endpoint = "https://api.assemblyai.com/v2/transcript"
audio_url = onlinePath + "/" + onlineFile

#    "speaker_labels": True,

# for a fatter list - one containing an error - see "SubmitToCloudWhisper - Copy (13) - Try word_boost, spell again.py"

#following word_boost list was 'generated' from YouTube SRT using srtToCsv.py (plus some filtering in a spreadsheet)
json = {
    "audio_url":       audio_url,
    "word_boost":      word_boost_list,
    "custom_spelling": custom_spelling_list,
    #"summarization": True,
    #"summary_type": "bullets",
    "word_boost":      word_boost_list,
    "custom_spelling": custom_spelling_list,
    "auto_highlights": auto_highlights_value,
    "language_model":  language_model_value,     # "large"  "medium"
    "boost_param": "low",           # "default" "high"
    "speaker_labels": True,         # not yet supported for Portuguese
    "entity_detection": True,
    "iab_categories": True,
    "auto_chapters": True,
    "sentiment_analysis": True,
    "language_code": "en_us"        #"pt"
}
#headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a","content-type": "application/json"}
headers = {"authorization": useThisAuthKey,"content-type": "application/json"}
response = requests.post(endpoint, json=json, headers=headers)
#print(response.json())
jj=response.json()
myId=jj.get('id')
print(myId)
myStatus=jj.get('status')
print(myStatus)
time.sleep(30)


import requests
import time
import sys
import math
import csv

#myId = "rsuh9skgre-a056-486e-8138-2e6608d21f04"
while myStatus == "queued" or myStatus == "processing":
    time.sleep(120)
    endpoint = "https://api.assemblyai.com/v2/transcript/" + myId
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
print(jj)
print()
print(myId)
print(myStatus)

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


    ccf.close()


# ----------- chapters ----------
chapterVec = []
chapterVecs = []
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


# ----------- sentiment analysis ----------

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

# ----------- utterances ----------

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


eef.close()



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


#needs myId, docLabel, onlineFile
#myId       ="rsuh9skgre-a056-486e-8138-2e6608d21f04"
#docLabel   = "mo007-1-SP"
#onlineFile = "mo007-1.m4a"

import requests
import time
import sys
import math
import csv

endpoint = "https://api.assemblyai.com/v2/transcript/" + myId + "/paragraphs"
#headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a"}
headers = {"authorization": useThisAuthKey}
response = requests.get(endpoint, headers=headers)
time.sleep(60)
kk=response.json()
print("")
print("")
print(" *** Response from /paragraphs call ***")
print(kk)
print("")
print(" *************************************")
print("")

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

#myId="rs8dx3ybuk-75db-405d-950b-560ec269d003"
endpoint = "https://api.assemblyai.com/v2/transcript/" + myId + "/sentences"
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
print(sss)
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
import math
import csv

#docLabel = "parseSRT" 
#onlineFile = "ls040-0"

srtFileName = docLabel + "_" + onlineFile + ".srt"
srtf = open(srtFileName, "w")

#myId="rsfzjbpypn-f1ff-4dc4-9aca-0526544dc4ed"

endpoint = "https://api.assemblyai.com/v2/transcript/" + myId + "/srt?chars_per_caption=40"        # "/srt?chars_per_caption=40"  "/paragraphs"
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
