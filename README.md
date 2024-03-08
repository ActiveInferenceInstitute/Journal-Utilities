# Journal-Utilities
Utilities and Documentation for creating contents for the Active Inference Journal
https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal

(A) The Python scripts

(1) invoke OpenAI Whisper Cloud service, and reformat the output to CSV.
Invocation from local Linux command line. (The suffixed "&" makes each python invocation run in background. Each instance of the process polls OpenAI every two minutes, and kicks off the four steps of the Extract-and-save phase of processing when main processing of its request has completed or failed.)  
```
python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls039-0" "http://crisiscenter.us/AILab01/2022Livestreams" "ActInf Livestream 039.0 ~ 'Morphogenesis as Bayesian inference'.m4a" | tee mass_ls039-0.m4a.json &
python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls039-1" "http://crisiscenter.us/AILab01/2022Livestreams" "ActInf Livestream 039.1 ~ 'Morphogenesis as Bayesian inference'.m4a" | tee mass_ls039-1.m4a.json &
python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls039-2" "http://crisiscenter.us/AILab01/2022Livestreams" "ActInf Livestream 039.2 ~ 'Morphogenesis as Bayesian inference'.m4a" | tee mass_ls039-2.m4a.json &
```
(2) extracts speech and context data from the new local CSVs, and create a simple text file that can be manually imported into a word processor and formatted with Title, Heading 1 (session), Heading 2 (speakers, contents, transcript).


(B) The CSV should be filled out manually using any spreadsheet program.

These data are read by sentencesToTranscripts script, so the latter can convert Whisper-generated speaker labels "A" "B"... into "Daniel" "Bleu"...
Even if AllSpeakers.csv is correct, the raw, editable .txt file may still have to have Speaker adjusted - this happens when Whisper gets confused about accents or prosody.


--------

Initial Scripts 1 & 2, and initial README contributed by Dave Douglass, November 2022. 


## Step 5: Markdown to Final Outputs

The `parse_markdown` function in `5_markdown_to_final/markdown_transcript_parser.py` converts the markdown file to an SRT and MD file (without timestamps). `write_output_files` will save the files to disk. Look at `tests/test_output_final_artifacts.py` for usage.

In the case of a course with multiple lectures like Physics as Information Processsing , `concatenate_markdown_files` will combine the markdown files into one file. This file can then be converted to a PDF or HTML using pandoc.

### Create a venv

```
python -m venv venv
source venv/bin/activate
```

Install Pandoc

for font support xeLaTeX required:
```
sudo apt-get install texlive-xetex
```

### Convert Markdown to PDF

```
cd /mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields
pandoc --pdf-engine xelatex -f markdown-implicit_figures all_transcripts.md --lua-filter=images/scholarly-metadata.lua --lua-filter=images/author-info-blocks.lua -o all_transcripts.pdf
```

### Convert Markdown to HTML

```
cd /mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields
pandoc -f markdown-implicit_figures all_transcripts.md --lua-filter=images/scholarly-metadata.lua --lua-filter=images/author-info-blocks.lua -o all_transcripts.html
```

remove all instances of `/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/` from the HTML file to make the images work.


