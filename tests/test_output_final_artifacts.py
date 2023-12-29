import sys
# Append the src directory to sys.path
sys.path.append("/mnt/md0/projects/Journal-Utilities/5_markdown_to_final")
# import markdown_transcript_parser and write_output_files from parse_markdown
from markdown_transcript_parser import parse_markdown, write_output_files, concatenate_markdown_files
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

    def test_lecture_2(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_2/Transcripts/Prose/'
        input_content_md = 'cFPIP-02L_Physics as Information Processing  ~ Chris Fields ~ Lecture 2.m4a.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_2/Transcripts/Prose/cFPIP-02L.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_2/Transcripts/Captions/cFPIP-02L.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_lecture_3(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_3/Transcripts/Prose/'
        input_content_md = 'cFPIP-03L_Physics as Information Processing  ~ Chris Fields ~ Lecture 3.m4a.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_3/Transcripts/Prose/cFPIP-03L.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_3/Transcripts/Captions/cFPIP-03L.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_lecture_4(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_4/Transcripts/Prose/'
        input_content_md = 'cFPIP-04L_Physics as Information Processing  ~ Chris Fields ~ Lecture 4.m4a.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_4/Transcripts/Prose/cFPIP-04L.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_4/Transcripts/Captions/cFPIP-04L.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_lecture_5(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_5/Transcripts/Prose/'
        input_content_md = 'cFPIP-05L_lGCSOxLTx0ADSPqI-qbiYtzaJGLqansa5nZ51Z2fXVE.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_5/Transcripts/Prose/cFPIP-05L.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_5/Transcripts/Captions/cFPIP-05L.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_lecture_6(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_6/Transcripts/Prose/'
        input_content_md = 'cFPIP-01L_Physics as Information Processing ~ Chris Fields ~ Lecture 6.m4a.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_6/Transcripts/Prose/cFPIP-06L.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_6/Transcripts/Captions/cFPIP-06L.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_discussion_1(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_1/Transcripts/Prose/'
        input_content_md = 'cFPIP-01W Physics as Information Processing ~ Ander Aguirre ~ Discussion 1.wav.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_1/Transcripts/Prose/cFPIP-01W.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_1/Transcripts/Captions/cFPIP-01W.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)
    
    def test_discussion_2(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_2/Transcripts/Prose/'
        input_content_md = 'cFPIP-02W_Physics as Information Processing  ~ Ander Aguirre ~ Discussion 2.m4a.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_2/Transcripts/Prose/cFPIP-02W.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_2/Transcripts/Captions/cFPIP-02W.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_discussion_3(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_3/Transcripts/Prose/'
        input_content_md = 'cFPIP-03W_Physics as Information Processing  ~ Ander Aguirre ~ Discussion 3.m4a.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_3/Transcripts/Prose/cFPIP-03W.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_3/Transcripts/Captions/cFPIP-03W.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_discussion_4(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_4/Transcripts/Prose/'
        input_content_md = 'cFPIP-04W_Physics as Information Processing  ~ Ander Aguirre ~ Discussion 4.wav.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_4/Transcripts/Prose/cFPIP-04W.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_4/Transcripts/Captions/cFPIP-04W.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_discussion_5(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_5/Transcripts/Prose/'
        input_content_md = 'cFPIP-05W__jw7UOQnkPAQImExl_1b8wyN9FlAVTJNtVW73dqAqvM.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_5/Transcripts/Prose/cFPIP-05W.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_5/Transcripts/Captions/cFPIP-05W.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_discussion_6(self):
        path_content_md = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Transcripts/Prose/'
        input_content_md = 'cFPIP-06W_4WKy_TVLReB2KAN6cGr5zk-GvfzfsRAihgK7Kc_Equw.sentences.csv_transcript.md'
        output_markdown_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Transcripts/Prose/cFPIP-06W.md'
        output_srt_path = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Transcripts/Captions/cFPIP-06W.srt'

        markdown, srt = parse_markdown(path_content_md, input_content_md)
        write_output_files(markdown, srt, output_markdown_path, output_srt_path)

    def test_concatenate_markdown_files(self):
        md_file_path = ['/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_1/Transcripts/Prose/cFPIP-01L.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_1/Transcripts/Prose/cFPIP-01W.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_2/Transcripts/Prose/cFPIP-02L.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_2/Transcripts/Prose/cFPIP-02W.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_3/Transcripts/Prose/cFPIP-03L.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_3/Transcripts/Prose/cFPIP-03W.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_4/Transcripts/Prose/cFPIP-04L.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_4/Transcripts/Prose/cFPIP-04W.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_5/Transcripts/Prose/cFPIP-05L.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_5/Transcripts/Prose/cFPIP-05W.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Lecture_6/Transcripts/Prose/cFPIP-06L.md',
                        '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/Discussion_6/Transcripts/Prose/cFPIP-06W.md']
        md_output_file_name = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/all_transcripts.md'
        metadata_file_name = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/metadata.md'
        acknowledgments_file_name = '/mnt/md0/projects/ActiveInferenceJournal/Courses/PhysicsAsInformationProcessing_ChrisFields/acknowledgments.md'

        concatenate_markdown_files(md_file_path, md_output_file_name, metadata_file_name, acknowledgments_file_name)

        # run pandoc
        # pandoc --pdf-engine xelatex -f markdown-implicit_figures all_transcripts.md --lua-filter=images/scholarly-metadata.lua --lua-filter=images/author-info-blocks.lua -o all_transcripts.pdf
if __name__ == '__main__':
    unittest.main()
