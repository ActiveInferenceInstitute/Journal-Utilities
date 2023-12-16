import re
from docxtpl import DocxTemplate, RichText, InlineImage
from docx.shared import Mm
import jinja2
from bs4 import BeautifulSoup
import markdown

def parse_markdown(file_path):
    with open(file_path, 'r') as file:
        markdown = file.readlines()

    clean_markdown = []
    srt_entries = []
    srt_index = 1

    for line in markdown:
        # Remove timestamp annotations for markdown
        clean_line = re.sub(r'\[\[start:\d+]\[end:\d+]]', '', line)
        clean_markdown.append(clean_line)

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

    return clean_markdown, srt_entries


def format_timestamp(ms):
    hours = ms // 3600000
    minutes = (ms % 3600000) // 60000
    seconds = (ms % 60000) // 1000
    milliseconds = ms % 1000
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def markdown_to_richtext(md_text):
    html = markdown.markdown(md_text)
    soup = BeautifulSoup(html, features='html.parser')

    rt = RichText()

    for tag in soup.find_all(True):
            if tag.name == 'p':
                # For paragraphs, start a new RichText object or add a line break if not the first paragraph
                if rt.xml:
                    rt.add('\n')
                for child in tag.children:
                    if child.name == 'strong':
                        rt.add(child.get_text(), bold=True)
                    elif child.name == 'em':
                        rt.add(child.get_text(), italic=True)
                    else:
                        rt.add(child.get_text())
            else:
                for child in tag.children:
                    rt.add(child.get_text())
    return rt

# an instance of core or supplemental terms and place them as an appendix item


# https://notebook.community/oditorium/blog/iPython/Reportlab2-FromMarkdown

# TODO get data from Transcripts/Prose and write SRT Transcripts/Captions
# write odt and pdf files to Transcripts/Prose
def write_output_files(markdown, srt, template_path, markdown_path, srt_path, docx_path):
    with open(markdown_path, 'w') as md_file:
        md_file.writelines(markdown)

    with open(srt_path, 'w') as srt_file:
        srt_file.writelines(srt)

    # Create at docx file from a template
    tpl = DocxTemplate(template_path)

    rt = markdown_to_richtext('\n'.join(markdown))

    # Convert the markdown to 
    context = {
        'title': 'Test Title',
        'date': '12/16/2023',
        'markdowntext': rt,
        'version': '1.0',
        'doi': 'https://doi.org/10.5281/zenodo.1234567',
        'terms': [
            {'term': 'yellow', 'definition': 'color of a banana'},
            {'term': 'red', 'definition': 'color of an apple'},
        ]
    }
    tpl.render(context)
    tpl.save(docx_path)
