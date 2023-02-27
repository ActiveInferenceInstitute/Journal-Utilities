#
# cd /mnt/e/Documents/DiscourseAnalysis/podcast_Mindscape/2022/09/19
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/StanzaNLP_parse-only.py" "ms211" "ms211_211-solo einsteins equation.mp3.sentences.csv_transcript.txt"
# cd "/mnt/d/Documents/FEP-AI/2023 GuestStream/gs035-1"
#	python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/StanzaNLP_parse-only.py" "gs035-1" "gs035-1_ActInf GuestStream 035.1 ~ Jordan Hall & Matthew Pirkowski.m4a.sentences.csv_transcript.txt" | tee gs035-1.m4a_stanza.json &
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/StanzaNLP_parse-only.py" "gs035-1" "ActInf GuestStream 035.1 ~ Jordan Hall & Matthew Pirkowski.txt"
#   python3 - "gs035-1" "ActInf GuestStream 035.1 ~ Jordan Hall & Matthew Pirkowski.txt"
# https://github.com/stanfordnlp/stanza/

import stanza
import requests
import time
import re
import sys
import math
import csv
import json

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) == 1:
        print("StanzaNLP. Needs parameters docLabel (key binding references to this doc),")
        print("    inSentFile (incoming text transcript file *.m4a.sentences.csv_transcript.txt; - would pipe this in as stdin.)")
        print("Optional params outDir (defaults to working directory '.').")
        print("Created at outDir: *_stanza_ner.csv (per-sentence), *_stanza_nerSumm.csv (consolidated across doc), *_stanza_Parse.csv ")
        quit()
    elif len(sys.argv) < 3:
        print("Need at least docLabel, inSentFile; optional outDir. Exiting!")
        quit()
    #
#
docLabel = sys.argv[1]
inSentFile = sys.argv[2]
print("docLabel, inSentFile " + "'" + docLabel + "', '" +  inSentFile + "'")

if len(sys.argv) > 3:
    outDir = sys.argv[3]
else:
    outDir = "."    #publish to working directory!

print("outDir: " + "'" + outDir + "'")

proxies = {'http': 'http://ip:port', 'https': 'http://ip:port'}
#stanza.download('en', proxies=proxies)  # This downloads the English models for the neural pipeline
stanza.download('en')  # This downloads the English models for the neural pipeline

# Following sets up a default neural pipeline in English
nlp = stanza.Pipeline('en')

#nlp = stanza.Pipeline('en', processors='tokenize,ner', package={"ner": ["ncbi_disease", "ontonotes"]})
#nlp = stanza.Pipeline('en', processors='tokenize,ner', package={"ner": ["ncbi_disease", "ontonotes"], 'coref': [], 'coref.algorithm' : 'neural'})
#nlpX = stanza.Pipeline('en', processors='tokenize,ner', package={"ner": ["ncbi_disease", "ontonotes"], 'coref': [], 'coref.algorithm' : 'neural'})
s1="All right, hello everyone. Welcome. This is ActInf livestream number 51 one. We are in the second discussion of this paper, canonical Neural Networks perform Active Inference. Welcome to the active inference institute. We're a participatory online institute that is communication, learning and practicing applied active inference. You can find us on this slide and this is recorded in an archived livestream. So please provide us feedback so we can improve our work. All backgrounds and perspectives are welcome and we'll follow good video etiquette for live streams, head over active inference.org to learn more about the institute and how to participate in projects and learning groups. All right, we're in ActInf livestream number 51 one, and having our first nonsolo discussion on this paper, canonical Neural Networks perform active inference and really appreciative that you've joined today. It's going to be a great discussion. We'll begin with introductions. I'll say hello and then please just jump in however you'd like. And we can start by setting some context. So I'm Daniel, I'm a researcher in California, and I was interested in this paper because we've been talking a lot about active inference from a variety of different perspectives, from the more fundamental math and physics to some applications, philosophy, embodiment, all these really interesting threads. And this paper seems to make a really clear meaningful contribution and connection by connecting active inference entities and this approach of modeling to neural networks which are in daily use globally. So thought it was a fascinating connection and really appreciate that we can talk about this today. So to you and welcome. Go forward, Takuya, however you'd like to introduce and say hello. Yeah. Hi. I'm Takuya Isomura, neuroscientist in Lique Brain Science Institute in Japan. I'm particularly interested in universal characterization of neural network and brain using mathematical techniques. So this work I believe important as a link between active brain forest aspect, Bayesian aspect of the brain, and the dynamics system aspect of the neural network. So I'm very happy to join this discussion session. Thank you for invitation. Nice to meet you."
s1="Because there might be settings where that is strictly effective and the simplest rule whereas there's other settings where that's going to be tragic. So in the special case where the entire environment is observable without errors like a chess game, then there's an equivalence between correlation of risk or loss on observables or on hidden states. But also I'm sure there's ways to construct them that are overfit. Worst case, there's some computational complexity, trade offs, but the problem becomes fully stateable. There's a parallelism or a concordance being drawn between the loss function of Neural networks and the variational free energy of the parameterized model there."
s1="If a catalog is an instance of set menu and an agent offers items for sale in the catalog and a kind of entity is in the catalog and a kind of entity is a subclass of prepared food and a physical is an instance of a class and another physical is an instance of the kind of entity and the physical is not equal to the other physical and the physical is price a currency measure for the agent1 and the other physical is price another currency measure for the agent2, then the currency measure is equal to the other currency measure"
s1="Mr. Phelps, the man over there, bought these toys for his children. They're very happy now!"
#print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
#print(*[f'id: {word.id}\tword: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
#print(*[f'id: {word.id}\tword: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
#print('id\tword\tUPoS\tXPoS\theadId\thead\tfeats')
#print(*[f'{word.id}\t{word.text}\t{word.upos}\t{word.xpos}\t{word.head}\t{sent.words[word.head-1].text if word.head > 0 else "root"}\t{word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')

#print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')

s1="My sister is married to Mwaga and has two children. Barack Obama was born in Hawaii. Barack Obama was elected in 2008. He is the president. I flew to Mwaga, Indonesia, last year. Obama was elected in 2008."
#   012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
#   0         1         2         3         4         5         6         7         8
#doc = nlp(s1)

# -------- sentences CSV

inSentPath = inSentFile

sent_file = open(inSentPath, "r", newline=None)
if (sent_file == None):
    print(inSentPath + " not found")
else:
    #allSents = sent_file.readlines()
    allSents = sent_file.read()


doc = nlp(allSents)

stanzaParsePath = outDir 

if stanzaParsePath[-1] != "/":
    stanzaParsePath += "/"

# Created at outDir: *_stanza_ner.csv (per-sentence), *_stanza_nerSumm.csv (consolidated across doc), *_stanza_Parse.csv 
stanzaParsePath += docLabel + "_" + inSentFile + "_stanza_Parse.csv"

print("to write-open stanzaParsePath:")
print(stanzaParsePath)

sPubF = open(stanzaParsePath, "w")

# *_stanza_Parse.csv        combined dependency and constituent parses across doc
print('sent\tid\tword\tlemma\tUPoS\tXPoS\tstartChar\tendChar\theadId\thead\tdepRel\tfeats')
sPubF.write('sent\tid\tword\tlemma\tUPoS\tXPoS\tstartChar\tendChar\theadId\thead\tdepRel\tfeats')
sPubF.write("\r\n")

#  When depRel == "goeswith"

for sentId, sent in enumerate(doc.sentences):
    #print(*[f'{1+sentId}\t{word.id}\t{word.text}\t{word.lemma}\t{word.upos}\t{word.xpos}\t{word.start_char}\t{word.end_char}\t{word.head}\t{sent.words[word.head-1].text if word.head > 0 else "(root)"}\t{word.deprel}\t{word.feats if word.feats else "_"}' for word in sent.words], sep='\n')
    for word in sent.words:
        #if len(word.text) > 0:
        #wordId   = word.id
        #wordText = word.text
        depRel   = word.deprel
        if depRel == "goeswith":
            print(*[f'****{1+sentId}\t{word.id}\t{word.text}\t{word.deprel}' for word in sent.words], sep='\n')
            #continue
        #
        sPubOut = str(1+sentId) + "\t"
        sPubOut += str(word.id) if word.id > 0 else ""
        sPubOut += "\t" 
        sPubOut += ( str(word.text) if word.text.isnumeric() else word.text )
        sPubOut += "\t"
        if word.lemma is not None:
            sPubOut += ( str(word.lemma) if word.lemma.isnumeric() else word.lemma) 
        #
        sPubOut += "\t"
        sPubOut += ( str(word.upos) if word.upos.isnumeric() else word.upos ) 
        sPubOut += "\t"
        sPubOut += ( str(word.xpos) if word.xpos.isnumeric() else word.xpos ) 
        sPubOut += "\t"
        sPubOut += str(word.start_char) if word.start_char >= 0 else ""
        sPubOut += "\t"
        sPubOut += str(word.end_char) if word.end_char >= 0 else ""
        sPubOut += "\t"
        sPubOut += str(word.head) if word.head >= 0 else ""
        sPubOut += "\t"
        if word.head >= 0:
            sPubOut += ( sent.words[word.head-1].text if word.head > 0 else "(root)" )
        #
        sPubOut += "\t"
        if word.deprel is not None:
            sPubOut += word.deprel 
        #
        sPubOut += "\t"
        sPubOut += word.feats if word.feats else "_"
        #sPubF.write(str(1+sentId) + "\t" + str(word.id) + "\t" + word.text + "\t" + word.lemma + "\t" + word.upos + "\t" + word.xpos + "\t" + str(word.start_char) + "\t" + str(word.end_char) + "\t" + str(word.head) + "\t" + sent.words[word.head-1].text if word.head > 0 else "(root)" + "\t" + word.deprel + "\t" + word.feats if word.feats else "_")
        sPubF.write(sPubOut)
        sPubF.write("\r\n")
        #
    #
#

""" 
2023-02-03 21:19:34 INFO: Loading these models for language: en (English):
============================
| Processor    | Package   |
----------------------------
| tokenize     | combined  |
| pos          | combined  |
| lemma        | combined  |
| depparse     | combined  |
| sentiment    | sstplus   |
| constituency | wsj       |
| ner          | ontonotes |
============================

2023-02-03 21:19:34 INFO: Use device: cpu
2023-02-03 21:19:34 INFO: Loading: tokenize
2023-02-03 21:19:34 INFO: Loading: pos
2023-02-03 21:19:35 INFO: Loading: lemma
2023-02-03 21:19:35 INFO: Loading: depparse
2023-02-03 21:19:35 INFO: Loading: sentiment
2023-02-03 21:19:35 INFO: Loading: constituency
2023-02-03 21:19:36 INFO: Loading: ner
2023-02-03 21:19:36 INFO: Done loading processors!
"""

sPubF.close()

