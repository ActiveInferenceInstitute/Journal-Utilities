import re

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

def write_output_files(clean_markdown, srt_entries, markdown_path, srt_path):
    with open(markdown_path, 'w') as md_file:
        md_file.writelines(clean_markdown)

    with open(srt_path, 'w') as srt_file:
        srt_file.writelines(srt_entries)

