# cd "/mnt/e/DSD-Documents/FEP-AI/2023 GuestStream/gs059/gs059-1/Images"
#	python3 "/mnt/e/DSD-Documents/FEP-AI/Active Inference Podcast/renameImageFiles.py" "gs014-1" "." "gs014-1_gs014-1.m4a.sentences.csv" | tee gs014-1.m4a_transcript.json

#renameImageFiles.py
#import OS module
import os
import time
import sys
import math
from os.path import exists
import re

path     = "."      # defaults to local directory (cd, where utility is run from)
baseFile = ""      # must be overridden or calculated
workFrom = baseFile # defaults to baseFile, or can be overridded to LATER from
workTo   = ""       # if not overridden, work proceeds to end of directory
outDir   = path     # defaults is rename-in-place
renameOp = "RENAME" # calculated based on invocation parameters - alternative is "COPY"
offset   = 0        # first output file name is *_0-01-00-0000.*, i.e. offset zero seconds relative to BASEFILE
labelMS  = True     # should we insert milliseconds in output name?
scaling  = 1.0      # output timescale same as input
types    = ["png"]  # to ADD file types, must add "png" back in
baseFileSuffix = "_i-00001.png"

inputOptions = {}

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) == 1:
        print("renameImageFiles.py - Needs 1 positional parameter: docLabel (prefix to use for all outputs),")
        print("Optional keyword parameters: BASEFILE (name of file relative to whose modification time output names will be generated, defaults to docLabel+'_i-00001.png');")
        print("    PATH (location of image files to be renamed, defaults to '.' i.e. current directory),")
        print("    OUTDIR (director to write renamed files - defaults to input, i.e. rename-in-place),")
        print("    OFFSET (starting 'timestamp' of output file, in milliseconds(integer) or [H:]:MM:SS[.mmmm]),")
        print("    TYPES (list of file types to be processed; defaults to 'png',")
        print("    SCALING (stretch-factor from incoming to outgoing times (if <1, output times shrink...), default to 1, i.e. no stretching,")
        print("    WORKFROM (name of file FROM which copying and/or renaming proceeds; must not have lexical name less than baseFile,")
        print("    WORKTO (name of file TO which copying proceeds; if zero-length, works per default to last file in directory.")
        quit()
    elif len(sys.argv) < 2:
        print("Need at least docLabel (prefix to use for all outputs). Exiting!")
        quit()

docLabel = sys.argv[1]

def get_input_options(scl):
    global basefile, outdir, path, types, workFrom, workTo, offset, scaling, labelMS
    scl_len = len(scl)
    # ii typically = 4 
    return_dict = {}
    ii = 0
    while ii < scl_len:
        label = scl[ii].upper().replace("_","").replace("-","")     # to match keyword to logic, uppercase and ignore underbars and hyphens
        value = scl[ii + 1].strip()
        ii += 2
        #
        if label == "PATH":
            path = value
            return_dict["PATH"] = path
        elif label == "BASEFILE":
            baseFile = value
            return_dict["BASEFILE"] = baseFile
        elif label == "OUTDIR":
            outDir = value
            return_dict["OUTDIR"] = outDir
        elif label == "TYPES":
            types = value
            return_dict["TYPES"] = types
        elif label == "OFFSET":
            offset = value
            return_dict["OFFSET"] = offset
        elif label == "SCALING":
            scaling = value
            return_dict["SCALING"] = scaling
        elif label == "WORKFROM":
            workFrom = value
            return_dict["WORKFROM"] = workFrom
        elif label == "WORKTO":
            workTo = value
            return_dict["WORKTO"] = outDir
        elif label == "LABELMS":
            if value.upper() in ['TRUE', 'Y', 'YES', 1, '1', 'T']:
                labelMS = True
                return_dict["LABELMS"] = labelMS
            elif value.upper() in ['FALSE', 'N', 'NO', 0, '0', 'F']:
                labelMS = False
                return_dict["LABELMS"] = labelMS
            #
            # if no valid value, SHOULD complain... now, just ignoring
        #
    #
    return return_dict


# SAMPLES: Get the list of all files and directories
#path = "C://Users//Vanshi//Desktop//gfg"
dir_list = os.listdir(path)

print(f'docLabel: {docLabel}')

if len(sys.argv) > 2:
    #outDir = sys.argv[4]
    inputParams = sys.argv[2:]
    print(f'inputParams: {inputParams}')
    # fetch keyword parameters
    inputOptions = get_input_options(inputParams)  # directly sets several globals; ignore first two (explicit) incoming args
    print("All keyword parameters, aka 'inputOptions'")
    print(inputOptions)
#
if not(path.endswith("/")):
    path += "/"

if len(baseFile) == 0:
    baseFile = docLabel + baseFileSuffix

baseFileModifyTime = os.path.getctime(path+baseFile)
print(f'baseFileModifyTime: {baseFileModifyTime}')
#baseFileCreateTime = os.path.getctime(path+baseFile)
#print(f'baseFileCreateTime: {baseFileCreateTime}')

for x in os.listdir(path):
    if os.path.isfile(path+x):
        for myType in types:
            if(x.endswith("."+myType)):
                if x != baseFile:
                    timeDiff = os.path.getctime(path+x) - baseFileModifyTime
                    #timeDiff = os.path.getctime(path+x) - baseFileCreateTime
                    timeHH = math.trunc(timeDiff/3600)
                    timeMM = math.trunc((timeDiff-(timeHH*3600))/60)
                    timeSS = math.trunc(timeDiff-(timeHH*3600)-(timeMM*60))
                    timemmmm = round((timeDiff - timeHH*3600 - timeMM*60 - timeSS)*1000,0)
                    if labelMS:         # depending on the frequency of extracting images, milliseconds may not provide any increased information; it does separate and sequence images.
                        outFile = docLabel + "_" + str(timeHH) + "-" + (str(100+timeMM))[-2:] + "-" + (str(100+timeSS))[-2:] + "-" + (str(1000+timemmmm))[-5:-2] + "." + myType
                    else:
                        outFile = docLabel + "_" + str(timeHH) + "-" + (str(100+timeMM))[-2:] + "-" + (str(100+timeSS))[-2:] + "." + myType
                    #
                    #outFile = docLabel + "_" + str(timeHH) + "-" + ("100"+str(timeMM))[-2:] + "-" + ("100"+str(timeSS))[-2:] + "-" + ("0000"+str(timemmmm))[-3:] + "." + myType
                    print(f'mv \"{x}\" \"{outFile}\"')
                    #print(f'file: {x}, outFile: {outFile}, timeDiff: {timeDiff}, timeHH: {timeHH}, timeMM: {timeMM}, timeSS: {timeSS}, timemmmm: {timemmmm}')
            #
        #
    #

"""
>>> path = "/mnt/e/DSD-Documents/FEP-AI/2023 GuestStream/gs059/gs059-1/Images/"
>>> fn00001= "gs059-1_i-00001.png"
>>> i00001=os.path.getctime(dir+fn00001)
>>> print(i133001-i00001)
4447.358132839203
>>> print((i133001-i00001)/60)
74.12263554732004
>>> fn139001="gs059-1_i-139001.png"
>>> i139001=os.path.getctime(dir+fn139001)
>>> print((i139001-i00001)/60)
77.46607292493185

#To get all the files, and no folders.
files = os.listdir(path)
files = [f for f in files if os.path.isfile(Direc+'/'+f)] #Filtering only the files.
    print(*files, sep="\n")

#To get only .txt files
for x in os.listdir():
    if x.endswith(".txt"):
        # Prints only text file present in My Folder
        print(x)
    #

# OS.walk() generates file names in a directory tree. This function returns a list of files in a tree structure. The method loops through all of the directories in a tree.
# to store files in a list
list = []
 
# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.txt' in f:
            print(f)
        #
    #

"""
