#! ...python3

acIIAuthKey  = "15683d311c6e4769915e064f579faae6"
davesAuthKey = "a14f484d11984e00bf7105cda4bc0c9a"
useThisAuthKey = acIIAuthKey

# cd "/mnt/d/Documents/FEP-AI/2022 Livestreams/ls042/ls042-0"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls042-0" "http://crisiscenter.us/AILab01/2022Livestreams" "ls042-0.m4a" | tee ls042-0_whisper_m4a.json &

# cd "/mnt/d/Documents/FEP-AI/2021 Livestreams/ls025"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls025-2" "http://crisiscenter.us/AILab01/2022Gueststreams" "ls025-2.m4a" | tee ls025-2.m4a.json &

# cd "/mnt/d/Documents/FEP-AI/2022 GuestStream/Mass 2022 GuestStreams"
#   #python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "gs014-1" "http://crisiscenter.us/AILab01/2022Gueststreams" "gs014-1.m4a" | tee gs014-1.m4a.json &

#cd "/mnt/d/Documents/FEP-AI/2022 Livestreams/Mass 2022 Livestreams"
    #python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" ls048-1 "http://crisiscenter.us/AILab01/2022Livestreams" "ls048-1.m4a" | tee ls048-1.m4a.json &
    # myID['ls048-0']= "rx1rvgss4t-2e6c-46ee-a0d4-42777283a9b1"
    # myID['ls048-1']= 'rxytoplp16-7b8b-41a6-be1b-78a0a837d8d4'

#cd "/mnt/d/Documents/FEP-AI/2022 Livestreams/Mass 2022 Livestreams"
    #python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" ls048-1 "http://crisiscenter.us/AILab01/2022Livestreams" "ls048-1.m4a" | tee ls048-1.m4a.json &

#cd "/mnt/d/Documents/FEP-AI/2021 Livestreams/ls016/"   rxzfu6wsa1-06f3-4028-8bf7-355d7f61eb00
    #python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" ls016-1 "http://crisiscenter.us/AILab01/2022Livestreams" "ls016.m4a" | tee ls016-1.m4a.json &

#D:\Documents\FEP-AI\Active Inference Podcast\Transcribe via Whisper.json
#call with python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/Transcribe via Whisper.py" ls037-0 "http://crisiscenter.us/AILab01/2022Livestreams" "ls037-0.m4a"	rs3z2z81w6-4507-4918-b001-7c08ebad22a6
#call with python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/Transcribe via Whisper.py" ls037-1 "http://crisiscenter.us/AILab01/2022Livestreams" "ls037-1.mp3" | tee ls037-1.mp3.json	rsury59afm-90b2-4049-9d08-cbb116e36808
#cd /mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #037 Stephen Mann - Free Energy A User's Guide/ls037-2
    #python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" ls037-2 "http://crisiscenter.us/AILab01/2022Livestreams" "ls037-2.m4a" | tee ls037-2.m4a.json	
#cd /mnt/d/Music/Fugs
   #python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" PBF "http://crisiscenter.us/misc" "DrStrangelovePreciousBodilyFluids.m4a" | tee PBF.m4a.json rsuh9skgre-a056-486e-8138-2e6608d21f04
#cd "/mnt/d/Documents/FEP-AI/2022 Livestreams/ActInf Livestream #040 - Chris Fields... A free energy principle for generic quantum systems/ls040-1"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" ls040-1 "http://crisiscenter.us/AILab01/2022Livestreams" "ls040-1.m4a" | tee ls040-1.m4a.json

#cd "/mnt/d/Documents/FEP-AI/2022 Livestreams\ActInf Livestream #041 - Axel Constant - Extended Active Inference beyond Skulls/ls040-1"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" ls041-1 "http://crisiscenter.us/AILab01/2022Livestreams" "ls041-1.m4a" | tee ls041-1.m4a.json
#cd "/mnt/d/Documents/FEP-AI/2022 Livestreams/ls042/ls042-0"
#   python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" ls042-0 "http://crisiscenter.us/AILab01/2022Livestreams" "ls042-0.m4a" | tee ls042-0.m4a.json


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

wordBoostList = [
"Dalton Sakthivadivel",
"Thomas Parr",
"Lagrange",
"Lagrangian",
"centripetal force",
"centripetal",
"Jorge Esteves",
"Zoe McParlin",
"Francesco Cerritelli",
"Beren Millidge",
"Anil Seth",
"Christopher L Buckley",
"Chris Buckley",
"Axel Constant",
"Andy Clark",
"Michael Kirchhoff",
"Lancelot Costa",
"Axel Constant",
"Andy Clark",
"Michael Kirchhoff",
"Tim Verbelen",
"Toon Van de Maele",
"Bart Dhoedt",
"Adam Safron",
"Tim Verbelen",
"Toon Van de Maele",
"Bart Dhoedt",
"Adam Safron",
"Verbelen",
#
"ActInf Lab GuestStream",
"ActInf Lab Livestream",
"ActInf Lab MathStream",
"ActInf Lab ModelStream",
"ActInf Lab OrgStream",
"ActInf Lab project",
"ActInf Livestream",
"ActInf",
"ActInfLab project",
"Active Inference",
"Active Inference GuestStream",
"Active Inference Institute",
"Active Inference Lab",
"Active Inference Livestream",
"Active Inference MathStream",
"Active Inference ModelStream",
"Active Inference OrgStream",
"Bayesian",
"Bayesian inference",
"Bleu",
"Daniel",
"Dean",
"Dot One",
"Dot Two",
"Dot Zero",
"Free Energy Principle",
"Friston",
"Friston blanket",
"Karl Friston",
"Karl J. Friston",
"Livestream Number",
"Markov",
"Markov blanket",
"Markov decision",
"Stephen",
"YouTube",
# -----------------
"radial parameterisation",
"tangential forces",
"parameterisation",
"tangential",
"Principle of Least Action",
"Least Action",
"Aaron Fath",
"Aaron J Fath",
"Abbas Edalat",
"accuracy",
"ActInf Lab",
"action oriented representation",
"action planning",
"action prediction",
"action",
"active states",
"active",
"activity",
"Adam Linson",
"Adam Safron",
"Safron",
"adaptive",
"address",
"Adeel Razi",
"advantage function",
"affect",
"affordance",
"agency",
"agent",
"agreement",
"Aikaterini Fotopoulou",
"Alessandra Pedrocchi",
"Alex Kiefer",
"Alexander Strobel",
"align",
"allostasis",
"allostat",
"ambiguity",
"Amir Omidvarnia",
"ancestral",
"Andrea Gajardo Vidal",
"Andreas Kleinschmidt",
"Andrew Corcoran",
"Andrew W Corcoran",
"Anna Belardinelli",
"Annemie Ploeger",
"Anthony Chen",
"Anthony G Chen",
"Anthony Zador",
"and",
"ants",
"ant",
"anxiety",
"architectures",
"Ari E Kahn",
"Ari Kahn",
"Arnold Pfeffer",
"aspects",
"assumptions",
"asymmetry",
"attention",
"Attial",
"attributes",
"awareness",
"bacterium like",
"Ballard",
"Bart Dhoedt",
"Bayesian statistics physics",
"behavior",
"belief updating",
"belief",
"beliefs",
"Bellman equation",
"Bellman",
"Beni",
"Benjamin Illingworth",
"Benucci",
"Bert de Vries",
"Bert de Vries",
"Bijan Khezri",
"Bijan",
"bioelectric",
"biological",
"Biology and Philosophy",
"biology",
"Bitcoin",
"blanket states",
"Blei",
"blueprint",
"bottom up",
"Botvinick",
"boundary",
"brain architecture",
"brain evolution",
"brain",
"Brea",
"Bull",
"Buzsaki",
"Canada",
"canonical",
"capacity curve",
"Carnap",
"Casper Hesp",
"Cathy J Price",
"Cathy Price",
"Chang Kim",
"Chang Sub Kim",
"Chantelle Gaylor",
"Chantelle M Gaylor",
"chaos",
"Charles C H Hong",
"Christian Guckelsberger",
"Christoph Mathys",
"Christoph Salge",
"Christopher D Frith",
"Christopher Frith",
"Christopher Lynn",
"Christopher W Lynn",
"Beren Milledge",
"Anil Seth",
"Calgary",
"Chance",
"Christopher L. Buckley",
"Claudia Clopath",
"Clopath",
"Coda",
"cognition",
"cognitive niche",
"cognitive science",
"cognitive scientist",
"cognitive studies",
"cognitive",
"coherence",
"coherent",
"comma",
"communication",
"competition",
"complexity",
"computational",
"computer",
"concept",
"concepts",
"connectivity",
"Conor Heins",
"Conor",
"continuum",
"control error",
"control theory",
"control",
"controlled process",
"controller",
"controls",
"conversation",
"Conway",
"correlation",
"Costa",
"counterfactuals",
"COVID",
"cue",
"culture",
"cybernetics",
"cycle",
"D Maisto",
"DAG",
"DAGs",
"Daniel Polani",
"Daniel Williams",
"Danielle Bassett",
"Danielle de Kerckhove",
"Danielle Kerckhove",
"Danielle S Bassett",
"Daphne Demekas",
"Daphne",
"Dario Cuevas Rivera",
"Dario Cuevas Rivera",
"Dario Rivera",
"data",
"Dauwels",
"David Benrimoh",
"David Benton",
"David Cittern",
"David Green",
"David Krakauer",
"David McKay",
"David W Green",
"Dayan",
"DCM",
"de Vries",
"Declan Lewis",
"Deneve",
"Dennett",
"Diana Morelen",
"differentiate",
"dimension",
"Dimitrije Markovi",
"Dirichlet",
"distinctions",
"disturbance",
"domain",
"Dot EDU",
"Dutch",
"dynamics",
"Earle Jamieson",
"ecological",
"Edda Bilek",
"Edelman",
"Eirik Sovik",
"Elenora Guanziroli",
"emergence",
"Emmanuel Dauce",
"Emmanuel Dauce",
"enactivism",
"encoding",
"endstopping",
"energy",
"English",
"ensemble",
"Ensor Palacios",
"Ensor Rafael Palacios",
"entorhinal",
"environment",
"enzymes",
"epistemic value",
"ergodicity",
"Erik Rietveld",
"errors",
"Ettore Ambrosini",
"evidence",
"evolution",
"Evolutionary Anthropology",
"exafferent",
"examples",
"expectation",
"expected free energy",
"exploration",
"explore",
"external states",
"exteroception",
"Fabienne Picard",
"Fabrice Bartolomei",
"Faisal Mushtaq",
"feedback control",
"feedback",
"Felix A Pollock",
"Felix Pollock",
"Feynman",
"field",
"fitness",
"flagella",
"Florian Ott",
"flow",
"fMRI imaging",
"fMRI",
"force",
"foraging",
"forage",
"forward model",
"framework",
"Francesco Donnarumma",
"Francesco Rigoli",
"Franco Molteni",
"Franz Kuchling",
"Frederike H Petzschner",
"Frederike Petzschner",
"free energy",
"free",
"function",
"gain",
"generalized capacity curve",
"generalized free energy",
"generative model",
"generative models",
"generative process",
"generative",
"Geoffrey Bingham",
"Georgi Georgiev",
"Geraint Rees",
"Gerry Edelman",
"Giovanni Pezzulo",
"Giuseppe Pagnoni",
"goal directed",
"Graeme D Jackson",
"Graeme Jackson",
"Grigorios A Pavliotis",
"Grigorios Pavliotis",
"Guido Hesselmann",
"Hae Jeong Park",
"Hae Park",
"Harrison",
"Hayley A Young",
"Hayley Young",
"Hebbian",
"Helene Haker",
"Helmholtz Decomposition",
"Helmholtzian",
"Helmholtz",
"heuristic",
"hidden states",
"Hideaki",
"hierarchical model",
"hierarchical",
"Hinton",
"Hipolito",
"Hohwy",
"homeostatic",
"homeostat",
"Hugo Bottemanne",
"Brennan",
"Alexander Tschantz",
"Iain Couzin",
"implication",
"inclination",
"independent",
"individual",
"individuals",
"indoctrination",
"Ines Hipolito",
"introduction",
"Francesco",
"Jorge",
"Cerritelli",
"Esteves",
"musculoskeletal",
"Albarracin",
"Andersen",
"Anna Lembke",
"Atreides",
"Azarian",
"Bayesianism",
"Bobby Azarian",
"Brett",
"Brett Andersen",
"Brett P. Andersen",
"Dalton A R Sakthivadivel",
"Dalton Sakthivadivel",
"David Douglass",
"Dean Tickles",
"Dobson",
"Facchin",
"Giovanni",
"Giovanni Rolla",
"John Vervaeke",
"Julian",
"Julian Kiverstein",
"Kiverstein",
"Kyrtin",
"Alessandro Barp",
"Guilherme Franca",
"Mark Girolami",
"Alessandro",
"Barp",
"Guilherme","Franca",
"Girolami",
"Michael Jordan",
"Kyrtin Atreides",
"Lembke",
"Mahault",
"Marco",
"Marco Facchin",
"Proksch",
"Ramstead",
"Ronen",
"Ronen Tamari",
"Shanna",
"Shanna Dobson",
"Shannon Proksch",
"Stephen Sillett",
"Tamari",
"Vervaeke",
"William Fischer",
"Monod",
"epistemic",
"literalist",
"instrumentalism",
"literalist fallacy",
"deflationary account",
"deflationary",
"vehicle externalism",
"externalism",
"schizotypy",
"diametric",
"stigmergic social annotation",
"collective sensemaking",
"sensemaking",
"stigmergic",
"social annotation",
"annotation",
"Shahaf",
"radically enactive cognition",
"radically enactive",
"Gibsonian",
"dialetheia",
"Deleuze",
"condensed object",
"haecceity",
"Grothendieck",
"governance",
"Ines",
"inference",
"influence",
"information geometry",
"information",
"informational",
"interactions",
"interface",
"internal model",
"internal representation",
"internal states",
"interoception",
"interoceptive",
"interpretation",
"inverse model",
"Isomura",
"Jablonka",
"Jack Brookes",
"Jakob Hohwy",
"Jakub Limanowski",
"Jakub Smekal",
"Jakub",
"James C Harris",
"James Cooke",
"James E Cooke",
"James E Swain",
"James Fallon",
"James H Fallon",
"James Harris",
"James Swain",
"James Whittington",
"Tolman Eichenbaum Machine",
"Javier Sanchez Canizares",
"Jean Decety",
"Jelle Bruineberg",
"Jelle",
"Jiyoung Kang",
"Johannes Lohmann",
"John Doherty",
"John O Doherty",
"Jonathan P Roiser",
"Jonathan Roiser",
"Judea Pearl",
"Jun Tani",
"Justyna Ekert",
"Justyna O Ekert",
"Kai Ueltzhoffer",
"Kant",
"Kappel",
"Karl J Friston",
"Karl",
"Katherine L Rosenblum",
"Katherine Rosenblum",
"Khezri",
"Kilner",
"Kirchhoff",
"Klaas E Stephan",
"Klaas Stephan",
"Kuchling",
"Kuhn",
"Laje",
"Lamme",
"Lancelot",
"language",
"Lars Muckli",
"Laurence J Kirmayer",
"Laurence Kirmayer",
"Laurent Perrinet",
"learning",
"least action",
"least",
"leave it to",
"leave to",
"left it to",
"left to",
"Leipzig",
"levels",
"Lieke de Boer",
"Lilian A E Weber",
"linguistics department",
"Linsker",
"Lisa Barrett",
"Lisa Feldman Barrett",
"living system",
"local",
"Lorenzo Niero",
"loss function",
"Lyapunov",
"M Berk Mirza",
"M Mirza",
"macaque",
"Maell Cullen",
"Mahault Albarracin",
"Majid Beni",
"Majid D Beni",
"Majid",
"Mangor Pedersen",
"Manuel Baltieri",
"Marc Tittgemeyer",
"Marcello Costantini",
"Maria Muzik",
"Mark Mon Williams",
"Mark Solms",
"Mark Williams",
"Markov decision process",
"Marolla",
"Marta Gandolla",
"Martin Biehl",
"Martin Butz",
"Martin V Butz",
"Martin Voss",
"match.com",
"material",
"maths",
"MATLAB",
"Matthew M Nour",
"Matthew Nour",
"Mattia Veronese",
"Max Planck",
"Maxwell J D Ramstead",
"Maxwell Ramstead",
"maze",
"measurement noise",
"measurement",
"membrane",
"mesoanatomical",
"metacognition",
"Micah Allen",
"Michael Levin",
"Michael Moutoussis",
"Michael Weisberg",
"Michael",
"Mike Levin",
"Milledge",
"mind",
"minimization",
"minimizing",
"model based",
"model selection",
"model",
"modelers",
"modularity",
"Moser",
"multimodal expansion",
"multimodal",
"multiple",
"narrative",
"Nathaniel Nyema",
"neoplasia",
"neuroimaging",
"neuromodulator",
"niche",
"Nick S Ward",
"Nick Ward",
"noise",
"nonclassical",
"Noor Sajid",
"novelty",
"numbers",
"objective function",
"observation",
"Oliver D Howes",
"Oliver Howes",
"Olivier Sigaud",
"Omar Khachouf",
"Omar T Khachouf",
"online",
"ontology",
"operating point",
"operations",
"order",
"OrgStream",
"osteopath",
"osteopathy",
"overload",
"overridable",
"Ozan Catal",
"parse",
"partial",
"participants",
"particle",
"Pasco Fearon",
"Patrice Duquette",
"Patrick Connolly",
"Paul B Badcock",
"Paul Badcock",
"Paul Fletcher",
"Peirce",
"perception",
"performance",
"perspective",
"perturbation",
"Peter Bossaerts",
"Peter Culmer",
"Peter Uhlhaas",
"Peter Vincent",
"Pezzulo",
"phase",
"Philipp Schwartenbeck",
"Philipp Sterzer",
"philosophy",
"phyletic gradualism",
"physics",
"physiological",
"Piaget",
"plant",
"plasticity",
"play",
"policy selection",
"policy",
"polyethism",
"POMDP",
"position",
"possibility",
"posterior",
"pragmatic value",
"pragmatics",
"pragmatism",
"prediction error",
"prediction",
"Predictive Coding",
"predictive processing",
"predictive regulation",
"Predrag Petrovic",
"preference",
"principle",
"prior",
"probabilistic graphical model",
"process noise",
"process theory",
"processes",
"processing",
"professional setting",
"program",
"prompting",
"punctuated equilibrium",
"pymdp",
"conor",
"quantum",
"question",
"questions",
"Quigley",
"radical enactivist",
"Rao and Ballard",
"Raphael Kaplan",
"Raymond Dolan",
"Raymond J Dolan",
"reafferent",
"reality",
"realize",
"recognition model",
"recognition",
"reference distribution",
"reference trajectory",
"reflective",
"refrigerator",
"regime of attention",
"regulated resource",
"relationships",
"representation",
"representational",
"representationalism",
"representations",
"response curve",
"Richard E Rosch",
"Richard M Wilkie",
"Richard Rosch",
"Richard Wilkie",
"Rick A Adams",
"Rick Adams",
"Riemann",
"Robin Carhart Harris",
"Robin Harris",
"role",
"Rosalyn J Moran",
"Rosalyn Moran",
"Ross",
"Roy de Kleijn",
"Roy Kleijn",
"rules",
"Rutger Goekoop",
"Ryan Smith",
"Ryota Kanai",
"S Ho",
"S Shaun Ho",
"Saee Paliwal",
"salience",
"Samarth Swarup",
"Samuel P L Veissiere",
"Samuel Veissiere",
"Sandra Iglesias",
"saturation value",
"scale",
"scenario",
"science",
"section",
"selection",
"Sennesh",
"sense states",
"Sepideh Sadaghiani",
"set point",
"set",
"settling point",
"settling range",
"Shaun Gallagher",
"Shaun Ho",
"Shimazaki",
"Sillett",
"Simon C Smith",
"Simon Smith",
"solenoidal ",
"SPM",
"stability",
"state estimate",
"state space",
"state",
"states",
"stationarity",
"Stefan J Kiebel",
"Stefan Kiebel",
"Stefano Poletti",
"Stephen Fleming",
"Stephen Fox",
"Stephen Lawrie",
"Stephen M Fleming",
"Stephen M Lawrie",
"Stephen Mann",
"Sterling Street",
"stigmergic",
"stigmergy",
"stimuli",
"stochastic optimal control",
"stock",
"structures",
"Sukhi Shergill",
"surprise",
"surround",
"Sussillo",
"synaptic",
"Takazumi Matsumoto",
"Takuya Isomura",
"Takuya",
"Tarik Dahoun",
"Taylor Series",
"Taylor",
"teaching",
"teleology",
"temporal depth",
"theorem",
"theory",
"Theriault",
"thermodynamics of the brain",
"thermodynamics",
"Thomas Goschke",
"Thomas H B FitzGerald",
"Thomas Hope",
"Thomas M Hope",
"Thomas Parr",
"threshold value",
"Tim Gard",
"Tim Verbelen",
"Tim Verbelen",
"time scales",
"Timothy Behrens",
"Tobias Nolte",
"Toon Van de Maele",
"top down",
"Torigoe",
"Toronto",
"transfer function",
"transfer",
"transition",
"truth",
"Turrigiano",
"uncertainty",
"understanding",
"University of Surrey",
"value function",
"variable",
"variational free energy",
"variational",
"vehicles",
"Veissiere",
"viscerosensory signaling",
"viscerosensory",
"vision",
"Vivien Ainley",
"Volterra series",
"Volterra",
"Wael Deredy",
"Wael El Deredy",
"wayfinding",
"Yoshio Nakamura",
"Zador",
"zebra",
"Zhang",
"Zina M Manjaly",
"Zina Manjaly",
#
"I",
"I'll",
"I've",
"I'm"
]

# (temporary) value of custom_spelling
customSpellingList = [ 
{"from": ["dalton"], "to": "Dalton"},
{"from": ["sakthivadivel"], "to": "Sakthivadivel"},
{"from": ["lancelot"], "to": "Lancelot"},
{"from": ["noor"], "to": "Noor"},
{"from": ["sajid"], "to": "Sajid"},
{"from": ["conor"], "to": "Conor"},
{"from": ["heins"], "to": "Heins"},
{"from": ["kai"], "to": "Kai"},
{"from": ["ueltzhoffer"], "to": "Ueltzhoffer"},
{"from": ["parr"], "to": "Parr"},
{"from": ["zoe"], "to": "Zoe"},
{"from": ["mcparlin"], "to": "McParlin"},
{"from": ["francesco"], "to": "Francesco"},
{"from": ["cerritelli"], "to": "Cerritelli"},
{"from": ["jorge"], "to": "Jorge"},
{"from": ["esteves"], "to": "Esteves"},
{"from": ["beren"], "to": "Beren"},
{"from": ["millidge"], "to": "Millidge"},
{"from": ["anil"], "to": "Anil"},
{"from": ["pease","peas"], "to": "Pease"},
{"from": ["seth"], "to": "Seth"},
{"from": ["verbelen"], "to": "Verbelen"},
{"from": ["actinf"], "to": "ActInf"},
{"from": ["bayesian"], "to": "Bayesian"},
{"from": ["daniel"], "to": "Daniel"},
{"from": ["friston"], "to": "Friston"},
{"from": ["markov"], "to": "Markov"},
{"from": ["youtube"], "to": "YouTube"},
{"from": ["gueststream"], "to": "GuestStream"},
{"from": ["livestream"], "to": "Livestream"},
{"from": ["mathstream"], "to": "MathStream"},
{"from": ["modelstream"], "to": "ModelStream"},
{"from": ["orgstream"], "to": "OrgStream"},
#
{"from": ["bleu"], "to": "Bleu"},
{"from": ["google"], "to": "Google"},
{"from": ["elizabethan"], "to": "Elizabethan"},
{"from": ["post-it"], "to": "Post-It"},
{"from": ["aristotelian"], "to": "Aristotelian"},
{"from": ["i"], "to": "I"},
{"from": ["i'm"], "to": "I'm"},
{"from": ["i'll"], "to": "I'll"},
{"from": ["i've"], "to": "I've"},
{"from": ["shakespeare"], "to": "Shakespeare"},
#-------------------
{"from": ["lagrange"], "to": "Lagrange"},
{"from": ["lagrangian"], "to": "Lagrangian"},
{"from": ["frankenstein"], "to": "Frankenstein"},
{"from": ["atreides"], "to": "Atreides"},
{"from": ["buddhist"], "to": "Buddhist"},
{"from": ["buddhists"], "to": "Buddhists"},
{"from": ["congress"], "to": "Congress"},
{"from": ["court"], "to": "Court"},
{"from": ["curtin"], "to": "Curtin"},
{"from": ["david"], "to": "David"},
{"from": ["hawking's"], "to": "Hawking's"},
{"from": ["hitchhiker's"], "to": "Hitchhiker's"},
{"from": ["jason"], "to": "Jason"},
{"from": ["jonathan"], "to": "Jonathan"},
{"from": ["kirsten"], "to": "Kirsten"},
{"from": ["marvin"], "to": "Marvin"},
{"from": ["mercurio"], "to": "Mercurio"},
{"from": ["modern"], "to": "Modern"},
{"from": ["natura"], "to": "Natura"},
{"from": ["nord"], "to": "Nord"},
{"from": ["october"], "to": "October"},
{"from": ["scala"], "to": "Scala"},
{"from": ["simon"], "to": "Simon"},
{"from": ["stephen"], "to": "Stephen"},
{"from": ["u.s"], "to": "U.S"},
#-------------------
{"from": ["alzheimer's"], "to": "Alzheimer's"},
{"from": ["andrew"], "to": "Andrew"},
{"from": ["armenia"], "to": "Armenia"},
{"from": ["arty"], "to": "Arty"},
{"from": ["astra"], "to": "Astra"},
{"from": ["atari"], "to": "Atari"},
{"from": ["bacon"], "to": "Bacon"},
{"from": ["bacon's"], "to": "Bacon's"},
{"from": ["becca"], "to": "Becca"},
{"from": ["bible"], "to": "Bible"},
{"from": ["bridges"], "to": "Bridges"},
{"from": ["bucky"], "to": "Bucky"},
{"from": ["cartesian"], "to": "Cartesian"},
{"from": ["chalmers"], "to": "Chalmers"},
{"from": ["charles"], "to": "Charles"},
{"from": ["chris"], "to": "Chris"},
{"from": ["christ"], "to": "Christ"},
{"from": ["claussen"], "to": "Claussen"},
{"from": ["cleanword"], "to": "cleanWord"},
{"from": ["clive"], "to": "Clive"},
{"from": ["clive's"], "to": "Clive's"},
{"from": ["clyde"], "to": "Clyde"},
{"from": ["comas"], "to": "Comas"},
{"from": ["communications"], "to": "Communications"},
{"from": ["constructor"], "to": "Constructor"},
{"from": ["coppola"], "to": "Coppola"},
{"from": ["corey"], "to": "Corey"},
{"from": ["cycles"], "to": "Cycles"},
{"from": ["deek's"], "to": "Deek's"},
{"from": ["dick's"], "to": "Dick's"},
{"from": ["dna"], "to": "DNA"},
{"from": ["dobson"], "to": "Dobson"},
{"from": ["dosh"], "to": "Dosh"},
{"from": ["duluth"], "to": "Duluth"},
{"from": ["dustin"], "to": "Dustin"},
{"from": ["eastern"], "to": "Eastern"},
{"from": ["english"], "to": "English"},
{"from": ["fantasia"], "to": "Fantasia"},
{"from": ["fep"], "to": "FEP"},
{"from": ["fields"], "to": "Fields"},
{"from": ["france"], "to": "France"},
{"from": ["francis"], "to": "Francis"},
{"from": ["freud"], "to": "Freud"},
{"from": ["fuller's"], "to": "Fuller's"},
{"from": ["giants"], "to": "Giants"},
{"from": ["global"], "to": "Global"},
{"from": ["gotham"], "to": "Gotham"},
{"from": ["groff"], "to": "Groff"},
{"from": ["guiles"], "to": "Guiles"},
{"from": ["hannah"], "to": "Hannah"},
{"from": ["harold"], "to": "Harold"},
{"from": ["hedwig"], "to": "Hedwig"},
{"from": ["hegel"], "to": "Hegel"},
{"from": ["ian"], "to": "Ian"},
{"from": ["ide"], "to": "IDE"},
{"from": ["indic"], "to": "Indic"},
{"from": ["indy"], "to": "Indy"},
{"from": ["jedi"], "to": "Jedi"},
{"from": ["jeffrey"], "to": "Jeffrey"},
{"from": ["johnny"], "to": "Johnny"},
{"from": ["kandinsky"], "to": "Kandinsky"},
{"from": ["klein"], "to": "Klein"},
{"from": ["mappy"], "to": "Mappy"},
{"from": ["maslow's"], "to": "Maslow's"},
{"from": ["mr"], "to": "Mr"},
{"from": ["nash"], "to": "Nash"},
{"from": ["nietzsche"], "to": "Nietzsche"},
{"from": ["orlando's"], "to": "Orlando's"},
{"from": ["paul"], "to": "Paul"},
{"from": ["peter"], "to": "Peter"},
{"from": ["plato"], "to": "Plato"},
{"from": ["rgb"], "to": "RGB"},
{"from": ["riverbanks"], "to": "Riverbanks"},
{"from": ["robert"], "to": "Robert"},
{"from": ["rosalyn"], "to": "Rosalyn"},
{"from": ["roth"], "to": "Roth"},
{"from": ["sadi"], "to": "Sadi"},
{"from": ["sadie"], "to": "Sadie"},
{"from": ["saidi"], "to": "Saidi"},
{"from": ["seth"], "to": "Seth"},
{"from": ["shanna"], "to": "Shanna"},
{"from": ["shawna"], "to": "Shawna"},
{"from": ["smothers"], "to": "Smothers"},
{"from": ["stanford"], "to": "Stanford"},
{"from": ["uv"], "to": "UV"},
{"from": ["young's"], "to": "Young's"},
{"from": ["zeman"], "to": "Zeman"},
# --------------------------
{"from": ["aaron"], "to": "Aaron"},
{"from": ["alexandria"], "to": "Alexandria"},
{"from": ["aristotle"], "to": "Aristotle"},
{"from": ["asm"], "to": "ASM"},
{"from": ["byron"], "to": "Byron"},
{"from": ["china"], "to": "China"},
{"from": ["china's"], "to": "China's"},
{"from": ["earth"], "to": "Earth"},
{"from": ["eve"], "to": "Eve"},
{"from": ["iphone"], "to": "iPhone"},
{"from": ["jesuits"], "to": "Jesuits"},
{"from": ["jesus"], "to": "Jesus"},
{"from": ["king"], "to": "King"},
{"from": ["korea"], "to": "Korea"},
{"from": ["leonardo"], "to": "Leonardo"},
{"from": ["monas"], "to": "Monas"},
{"from": ["nasa"], "to": "NASA"},
{"from": ["newton"], "to": "Newton"},
{"from": ["newtonian"], "to": "Newtonian"},
{"from": ["northern"], "to": "Northern"},
{"from": ["paris"], "to": "Paris"},
{"from": ["ramon"], "to": "Ramon"},
{"from": ["sdf"], "to": "SDF"},
{"from": ["serbia"], "to": "Serbia"},
#  -------------------------------
{'from': ['attial'], 'to': 'Attial'},
{'from': ['ballard'], 'to': 'Ballard'},
{'from': ['bayesian'], 'to': 'Bayesian'},
{'from': ['bellman'], 'to': 'Bellman'},
{'from': ['Benny','beni'], 'to': 'Beni'},
{'from': ['beren','beran'], 'to': 'Beren'},
{'from': ['millage','milledge'], 'to': 'Milledge'},
{'from': ['anil'], 'to': 'Anil'},
{'from': ['benucci'], 'to': 'Benucci'},
{'from': ['Bijan'], 'to': 'Bijan'},
{'from': ['bitcoin'], 'to': 'Bitcoin'},
{'from': ['blei'], 'to': 'Blei'},
{'from': ['bleu','Blue'], 'to': 'Bleu'},
{'from': ['botvinick'], 'to': 'Botvinick'},
{'from': ['brea'], 'to': 'Brea'},
{'from': ['bull'], 'to': 'Bull'},
{'from': ['buzsaki'], 'to': 'Buzsaki'},
{'from': ['canada'], 'to': 'Canada'},
{'from': ['carnap'], 'to': 'Carnap'},
{'from': ['clopath'], 'to': 'Clopath'},
{'from': ['coda'], 'to': 'Coda'},
{'from': ['daphne','dakki'], 'to': 'Daphne'},
{'from': ['conor','connor'], 'to': 'Conor'},
{'from': ['demekas'], 'to': 'Demekas'},
{'from': ['conway'], 'to': 'Conway'},
{'from': ['costa'], 'to': 'Costa'},
{'from': ['covid'], 'to': 'COVID'},
{'from': ['francesco'], 'to': 'Francesco'},
{'from': ['jorge'], 'to': 'Jorge'},
{'from': ['cerritelli'], 'to': 'Cerritelli'},
{'from': ['esteves'], 'to': 'Esteves'},
{'from': ['albarracin'], 'to': 'Albarracin'},
{'from': ['andersen'], 'to': 'Andersen'},
{'from': ['atreides'], 'to': 'Atreides'},
{'from': ['azarian'], 'to': 'Azarian'},
{'from': ['bayesianism'], 'to': 'Bayesianism'},
{'from': ['brett'], 'to': 'Brett'},
{'from': ['dobson'], 'to': 'Dobson'},
{'from': ['facchin'], 'to': 'Facchin'},
{'from': ['giovanni'], 'to': 'Giovanni'},
{'from': ['julian'], 'to': 'Julian'},
{'from': ['kiverstein'], 'to': 'Kiverstein'},
{'from': ['kyrtin'], 'to': 'Kyrtin'},
{'from': ['lembke'], 'to': 'Lembke'},
{'from': ['mahault'], 'to': 'Mahault'},
{'from': ['marco'], 'to': 'Marco'},
{'from': ['proksch'], 'to': 'Proksch'},
{'from': ['ramstead'], 'to': 'Ramstead'},
{'from': ['ronen'], 'to': 'Ronen'},
{'from': ['shanna'], 'to': 'Shanna'},
{'from': ['tamari'], 'to': 'Tamari'},
{'from': ['vervaeke'], 'to': 'Vervaeke'},
{'from': ['monod'], 'to': 'Monod'},
{'from': ['gueststream'], 'to': 'Gueststream'},
{'from': ['shahaf'], 'to': 'Shahaf'},
{'from': ['gibsonian'], 'to': 'Gibsonian'},
{'from': ['deleuze'], 'to': 'Deleuze'},
{'from': ['grothendieck'], 'to': 'Grothendieck'},
{'from': ['dag'], 'to': 'DAG'},
{'from': ['dags'], 'to': 'DAGs'},
{'from': ['daniel'], 'to': 'Daniel'},
{'from': ['dauwels'], 'to': 'Dauwels'},
{'from': ['dayan'], 'to': 'Dayan'},
{'from': ['dcm'], 'to': 'DCM'},
{'from': ['dean'], 'to': 'Dean'},
{'from': ['deneve'], 'to': 'Deneve'},
{'from': ['dennett'], 'to': 'Dennett'},
{'from': ['dirichlet'], 'to': 'Dirichlet'},
{'from': ['dutch'], 'to': 'Dutch'},
{'from': ['edelman'], 'to': 'Edelman'},
{'from': ['english'], 'to': 'English'},
{'from': ['feynman'], 'to': 'Feynman'},
{'from': ['fmri'], 'to': 'fMRI'},
{'from': ['Calfistan','fristen','friston','Tristan'], 'to': 'Friston'},
{'from': ['harrison'], 'to': 'Harrison'},
{'from': ['hebbian'], 'to': 'Hebbian'},
{'from': ['hinds','hines'], 'to': 'Heins'},
{'from': ['helmholtz'], 'to': 'Helmholtz'},
{'from': ['hideaki'], 'to': 'Hideaki'},
{'from': ['hinton'], 'to': 'Hinton'},
{'from': ['hipolito'], 'to': 'Hipolito'},
{'from': ['Howe','hohwy'], 'to': 'Hohwy'},
{'from': ['brennan'], 'to': 'Brennan'},
{'from': ['Ian'], 'to': 'Iain'},
{'from': ['Cousin'], 'to': 'Couzin'},
{'from': ['ines','Innes','inez'], 'to': 'Ines'},
{'from': ['isomura'], 'to': 'Isomura'},
{'from': ['jablonka'], 'to': 'Jablonka'},
{'from': ['jelle'], 'to': 'Jelle'},
{'from': ['kappel'], 'to': 'Kappel'},
{'from': ['carl','Calf'], 'to': 'Karl'},
{'from': ['Khezri'], 'to': 'Khezri'},
{'from': ['kilner'], 'to': 'Kilner'},
{'from': ['kirchhoff'], 'to': 'Kirchhoff'},
{'from': ['kuchling'], 'to': 'Kuchling'},
{'from': ['kuhn'], 'to': 'Kuhn'},
{'from': ['laje'], 'to': 'Laje'},
{'from': ['lamme'], 'to': 'Lamme'},
{'from': ['lancelot'], 'to': 'Lancelot'},
{'from': ['leipzig'], 'to': 'Leipzig'},
{'from': ['linsker'], 'to': 'Linsker'},
{'from': ['lyapunov'], 'to': 'Lyapunov'},
{'from': ['majid'], 'to': 'Majid'},
{'from': ['markov','markoff'], 'to': 'Markov'},
{'from': ['marolla'], 'to': 'Marolla'},
{'from': ['matlab'], 'to': 'MATLAB'},
{'from': ['michael'], 'to': 'Michael'},
{'from': ['moser'], 'to': 'Moser'},
{'from': ['orgstream'], 'to': 'OrgStream'},
{'from': ['pezzulo'], 'to': 'Pezzulo'},
{'from': ['piaget', 'PSJA'], 'to': 'Piaget'},
{'from': ['plank','Pluck'], 'to': 'Planck'},
{'from': ['pineapple'], 'to': 'pymdp'},
{'from': ['pomdp'], 'to': 'POMDP'},
{'from': ['quigley'], 'to': 'Quigley'},
{'from': ['riemann'], 'to': 'Riemann'},
{'from': ['ross'], 'to': 'Ross'},
{'from': ['sennesh'], 'to': 'Sennesh'},
{'from': ['shimazaki'], 'to': 'Shimazaki'},
{'from': ['sillett'], 'to': 'Sillett'},
{'from': ['spm'], 'to': 'SPM'},
{'from': ['stephen'], 'to': 'Stephen'},
{'from': ['sussillo'], 'to': 'Sussillo'},
{'from': ['takuya'], 'to': 'Takuya'},
{'from': ['taylor'], 'to': 'Taylor'},
{'from': ['theriault'], 'to': 'Theriault'},
{'from': ['tolman'], 'to': 'Tolman'},
{'from': ['torigoe'], 'to': 'Torigoe'},
{'from': ['toronto'], 'to': 'Toronto'},
{'from': ['turrigiano'], 'to': 'Turrigiano'},
{'from': ['veissiere'], 'to': 'Veissiere'},
{'from': ['volterra', 'voltaire'], 'to': 'Volterra'},
{'from': ['zador'], 'to': 'Zador'},
{'from': ['zhang'], 'to': 'Zhang'}
]

#following word_boost list was 'generated' from YouTube SRT using srtToCsv.py (plus some filtering in a spreadsheet)
json = {
    "audio_url": audio_url,
    "word_boost": wordBoostList,
    "custom_spelling": customSpellingList,
    #"summarization": True,
    #"summary_type": "bullets",
    "speaker_labels": True,         # not yet supported for Portuguese
    "language_model": "large",
    "entity_detection": True,
    "auto_highlights": True,
    "iab_categories": True,
    "auto_chapters": True,
    "sentiment_analysis": True,
    "language_code": "en_us"        #"pt"
}
headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a","content-type": "application/json"}
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
    headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a"}
    response = requests.get(endpoint, headers=headers)
    #print(response.json())
    jj=response.json()
    myStatus=jj.get('status')
    print(myStatus)


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
wwf = open(wordFileName, "w")
wordOut = "start\tend\tspeaker\twconfidence\ttext"
wwf.write(wordOut)
wwf.write("\r\n")

words = jj.get('words')

for count, word in enumerate(words):
    wtext=word.get('text')
    wstart=word.get('start')
    wend=word.get('end')
    wconfid=word.get('confidence')
    wspeaker=word.get('speaker')
    #
    wordOut = str(wstart) + "\t" + str(wend) + "\t"
    if wspeaker != None:
        wordOut = wordOut + wspeaker
    #
    wordOut = wordOut + "\t" + str(wconfid) + "\t"
    if wtext != None:
         wordOut = wordOut + wtext
    #
    #wordOut = str(wstart) + "\t" + str(wend) + "\t" + wspeaker + "\t" + str(wconfid) + "\t" + wtext    
    wwf.write(wordOut)	#    #print(utterOut)	, delimiter='\t', lineterminator='\t\n'
    wwf.write("\r\n")

wwf.close()


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
headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a"}
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
headers = {
    "authorization": "a14f484d11984e00bf7105cda4bc0c9a"}
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
headers = {"authorization": "a14f484d11984e00bf7105cda4bc0c9a"}
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
