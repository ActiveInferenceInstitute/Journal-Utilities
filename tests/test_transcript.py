import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from src.transcribe import output_text

class TestOutputText(unittest.TestCase):
    def test_output_text(self):
        # Test case 1: Single speaker
        input_data = [
            {
                "start": 7.622,
                "end": 23.423,
                "text": " all right i think we are live hello everyone and welcome to the active inference live stream this is active inference live stream 11 it is december 16 2020 and there's a lot to get to today so thanks for tuning in",
                "speaker": "SPEAKER_00"
            }
        ]
        expected_output = "SPEAKER_00:\nall right i think we are live hello everyone and welcome to the active inference live stream this is active inference live stream 11 it is december 16 2020 and there's a lot to get to today so thanks for tuning in"
        output_result = output_text(input_data)
        self.assertEqual(output_result, expected_output)

        # Test case 2: Multiple speakers
        input_data = [
            {
                "start": 7.622,
                "end": 23.423,
                "text": " all right i think we are live hello everyone and welcome to the active inference live stream this is active inference live stream 11 it is december 16 2020 and there's a lot to get to today so thanks for tuning in",
                "speaker": "SPEAKER_00"
            },
            {
                "start": 24.67,
                "end": 27.091,
                "text": " Welcome to the Active Inference Lab, everyone.",
                "speaker": "SPEAKER_00"
            },
            {
                "start": 27.912,
                "end": 33.675,
                "text": "We are an experiment in online team communication, learning, and practice related to Active Inference.",
                "speaker": "SPEAKER_01"
            }
        ]
        expected_output = "SPEAKER_00:\nall right i think we are live hello everyone and welcome to the active inference live stream this is active inference live stream 11 it is december 16 2020 and there's a lot to get to today so thanks for tuning in\n\nWelcome to the Active Inference Lab, everyone.\n\n\nSPEAKER_01:\nWe are an experiment in online team communication, learning, and practice related to Active Inference."
        output_result = output_text(input_data)
        self.assertEqual(output_result, expected_output)

        # Test case 3: Empty input
        input_data = []
        expected_output = ""
        self.assertEqual(output_text(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()