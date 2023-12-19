import sys
# Append the src directory to sys.path
sys.path.append("/mnt/md0/projects/Journal-Utilities/5_markdown_to_final")
# import markdown_transcript_parser and write_output_files from parse_markdown
from markdown_transcript_parser import parse_markdown, write_output_files
import unittest
import os

class TestMarkdownParser(unittest.TestCase):
    def setUp(self):

        # Expected md output
        self.expected_output_md = '/mnt/md0/projects/Journal-Utilities/tests/expected_output.md'
        with open(self.expected_output_md, 'r') as file:
            self.expected_markdown = file.readlines()

        # Expected srt output
        self.expected_output_srt = '/mnt/md0/projects/Journal-Utilities/tests/expected_output.srt'
        with open(self.expected_output_srt, 'r') as file:
            self.expected_srt = file.readlines()

        # Input file
        self.path_sample_content_md = '/mnt/md0/projects/Journal-Utilities/tests/'
        self.input_sample_content_md = 'input_sample_content.md'

        # Output files
        self.output_markdown = '/mnt/md0/projects/Journal-Utilities/tests/sample_output.md'
        self.output_srt = '/mnt/md0/projects/Journal-Utilities/tests/sample_output.srt'

    def test_parse_markdown(self):
        markdown, srt = parse_markdown(self.path_sample_content_md, self.input_sample_content_md)
        
        self.assertEqual(markdown, self.expected_markdown)
        self.assertEqual(srt, self.expected_srt)

    def test_write_output_files(self):
        markdown, srt = parse_markdown(self.path_sample_content_md, self.input_sample_content_md)
        write_output_files(markdown, srt, self.output_markdown, self.output_srt)

    def test_lecture_1(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_1/Transcripts/Prose/'
        input_content_md = 'cFPIP-01L_Physics as Information Processing  ~ Chris Fields ~ Lecture 1.m4a.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_1/Transcripts/Prose/cFPIP-01L.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_1/Transcripts/Captions/cFPIP-01L.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

if __name__ == '__main__':
    unittest.main()
