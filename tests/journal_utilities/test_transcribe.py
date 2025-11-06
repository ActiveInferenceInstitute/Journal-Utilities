"""Test suite for transcription service in journal_utilities."""

from unittest.mock import MagicMock, patch

import pytest

from journal_utilities.transcribe import TranscriptionService


@pytest.fixture
def transcription_service() -> TranscriptionService:
    """Set up a TranscriptionService instance with mocked models for testing."""
    # Mock the model loading functions to avoid needing actual models
    with (
        patch("whisperx.load_model") as mock_load_model,
        patch("whisperx.load_align_model") as mock_align_model,
        patch("journal_utilities.transcribe.DiarizationPipeline") as mock_diarize,
    ):
        # Configure mocks
        mock_load_model.return_value = MagicMock()
        mock_align_model.return_value = (MagicMock(), MagicMock())
        mock_diarize.return_value = MagicMock()

        # Create the service instance
        service = TranscriptionService(
            hf_token="test_token", device="cpu", batch_size=1, compute_type="int8"
        )

    return service


def test_output_text_single_speaker(transcription_service: TranscriptionService) -> None:
    """Test output_text with a single speaker."""
    input_data = [
        {
            "start": 7.622,
            "end": 23.423,
            "text": " all right i think we are live hello everyone and welcome to the active inference live stream this is active inference live stream 11 it is december 16 2020 and there's a lot to get to today so thanks for tuning in",
            "speaker": "SPEAKER_00",
        }
    ]
    expected_output = "SPEAKER_00:\nall right i think we are live hello everyone and welcome to the active inference live stream this is active inference live stream 11 it is december 16 2020 and there's a lot to get to today so thanks for tuning in"
    output_result = transcription_service.output_text(input_data)
    assert output_result == expected_output


def test_output_text_multiple_speakers(
    transcription_service: TranscriptionService,
) -> None:
    """Test output_text with multiple speakers."""
    input_data = [
        {
            "start": 7.622,
            "end": 23.423,
            "text": " all right i think we are live hello everyone and welcome to the active inference live stream this is active inference live stream 11 it is december 16 2020 and there's a lot to get to today so thanks for tuning in",
            "speaker": "SPEAKER_00",
        },
        {
            "start": 24.67,
            "end": 27.091,
            "text": " Welcome to the Active Inference Lab, everyone.",
            "speaker": "SPEAKER_00",
        },
        {
            "start": 27.912,
            "end": 33.675,
            "text": "We are an experiment in online team communication, learning, and practice related to Active Inference.",
            "speaker": "SPEAKER_01",
        },
    ]
    expected_output = "SPEAKER_00:\nall right i think we are live hello everyone and welcome to the active inference live stream this is active inference live stream 11 it is december 16 2020 and there's a lot to get to today so thanks for tuning in\n\nWelcome to the Active Inference Lab, everyone.\n\n\nSPEAKER_01:\nWe are an experiment in online team communication, learning, and practice related to Active Inference."
    output_result = transcription_service.output_text(input_data)
    assert output_result == expected_output


def test_output_text_empty_input(transcription_service: TranscriptionService) -> None:
    """Test output_text with empty input."""
    input_data = []
    expected_output = ""
    assert transcription_service.output_text(input_data) == expected_output
