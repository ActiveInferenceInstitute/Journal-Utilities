import sys
# Append the src directory to sys.path
sys.path.append("/mnt/md0/projects/Journal-Utilities/5_markdown_to_final")
from markdown_transcript_parser import parse_markdown
import unittest
import os

class TestMarkdownParser(unittest.TestCase):
    def setUp(self):

        # Expected md output
        self.final_md = '/mnt/md0/projects/Journal-Utilities/tests/final.md'
        with open(self.final_md, 'r') as file:
            self.expected_clean_markdown = file.readlines()

        # Expected srt output
        self.final_srt = '/mnt/md0/projects/Journal-Utilities/tests/final.srt'
        with open(self.final_srt, 'r') as file:
            self.expected_srt = file.readlines()

        # Input markdown file
        self.temp_markdown_file = '/mnt/md0/projects/Journal-Utilities/tests/sample_content.md'

    def test_parse_markdown(self):
        clean_markdown, srt_entries = parse_markdown(self.temp_markdown_file)
        
        self.assertEqual(clean_markdown, self.expected_clean_markdown)
        self.assertEqual(srt_entries, self.expected_srt)

if __name__ == '__main__':
    unittest.main()
