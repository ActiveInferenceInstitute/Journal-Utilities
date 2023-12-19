import re
from docx import Document
from docx.shared import Mm
from bs4 import BeautifulSoup
import markdown
import csv

def parse_markdown(md_path, md_file_name):

    with open(md_path + md_file_name , 'r') as file:
        markdown = file.readlines()

    clean_markdown = []
    srt_entries = []
    srt_index = 1
    metadata_block = True  # Flag to indicate we are in the metadata block

    for line in markdown:
        # Check if we are past the metadata block
        if line.strip() == '...':
            metadata_block = False

        # Remove timestamp annotations for markdown
        clean_line = re.sub(r'\[\[start:\d+]\[end:\d+]]', '', line)
        clean_markdown.append(clean_line)

        # Skip metadata lines for SRT processing
        if metadata_block:
            continue

        # Extract timestamps and text for SRT
        timestamps = re.findall(r'\[\[start:(\d+)]\[end:(\d+)]]', line)
        if timestamps:
            start_time, end_time = timestamps[0]
            srt_start = format_timestamp(int(start_time))
            srt_end = format_timestamp(int(end_time))

            # Removing unwanted minutes:seconds like "00:20" and "01:49"
            text = re.sub(r'\d{2}:\d{2} ', '', clean_line).strip()

            srt_entries.append(f"{srt_index}\n")
            srt_entries.append(f"{srt_start} --> {srt_end}\n")
            srt_entries.append(f"{text}\n")
            srt_entries.append("\n")
            srt_index += 1

    # Read ontology CSV file into csv_content https://coda.io/@active-inference-institute/active-inference-ontology-website/definitions-3
    with open('/mnt/md0/projects/Journal-Utilities/5_markdown_to_final/ontology.csv', 'r') as csv_file:
        csv_content = csv_file.read()

    # Parse the CSV content
    terms_definitions = {}
    reader = csv.DictReader(csv_content.splitlines())
    for row in reader:
        term = row['Term']
        definition = row['Proposed Definition 1']
        terms_definitions[term] = definition

    # Search for the terms in the markdown file and add to a list if found
    found_terms = []
    clean_markdown_string = ' '.join(clean_markdown)
    for term, definition in terms_definitions.items():
        if re.search(r'\b' + re.escape(term) + r'\b', clean_markdown_string, re.IGNORECASE):
            found_terms.append((term, definition))

    # Alphabetize the list
    found_terms.sort()

    # Print to the markdown file in the specified format
    if found_terms:
        clean_markdown.append("\n")
        clean_markdown.append("## Appendix: Terminology\n")
        clean_markdown.append("\n")
        for term, definition in found_terms:
            clean_markdown.append(f"{term}\n")
            clean_markdown.append("\n")
            clean_markdown.append(f":   {definition}\n")
            clean_markdown.append("\n")

    clean_markdown.append("\n")
    clean_markdown.append("![Act. Infer. Serve](images/logo.png){ width=5% } Act to connect with The Institute by [web](https://activeinference.org), [email](mailto:Blanket@ActiveInference.Institute), [YouTube](https://www.youtube.com/c/ActiveInference/videos), [Discord](https://discord.gg/8VNKNp4jtx), or [LinkedIn](https://www.linkedin.com/company/active-inference/).\n")

    return clean_markdown, srt_entries


def format_timestamp(ms):
    hours = ms // 3600000
    minutes = (ms % 3600000) // 60000
    seconds = (ms % 60000) // 1000
    milliseconds = ms % 1000
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def write_output_files(markdown, srt, markdown_path, srt_path):
    with open(markdown_path, 'w') as md_file:
        md_file.writelines(markdown)

    with open(srt_path, 'w') as srt_file:
        srt_file.writelines(srt)
