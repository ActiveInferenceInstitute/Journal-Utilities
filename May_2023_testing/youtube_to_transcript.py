# python -m pip install -r requirements.txt

# Import necessary libraries
import pytube
import moviepy.editor as mp
import numpy as np
import whisper
import time

# Set your YouTube video URL
video_url = "https://www.youtube.com/watch?v=ChO1u1mJRGE"

def download_audio(video_url):
    """
    Function to download the audio from a YouTube video.

    Parameters:
    video_url (str): The URL of the YouTube video.

    Returns:
    str: The path to the downloaded file.
    """
    # Initialize a YouTube object with the video URL
    data = pytube.YouTube(video_url)

    # Get the audio only stream
    audio = data.streams.get_audio_only()

    # Download the audio file and return the path to the file
    downloaded_file = audio.download()
    return downloaded_file

def mp4_to_wav(input_file, output_file):
    """
    Function to convert an MP4 file to WAV format.

    Parameters:
    input_file (str): The path to the input MP4 file.
    output_file (str): The path to the output WAV file.
    """
    # Load the audio file
    audio = mp.AudioFileClip(input_file)

    # Write the audio file in WAV format
    audio.write_audiofile(output_file, codec="pcm_s16le")

# Start the timer
tic = time.perf_counter()

# Download the audio from the YouTube video
input_file = download_audio(video_url)

# Convert the downloaded MP4 file to WAV format
output_file = "audio.wav"
mp4_to_wav(input_file, output_file)

# Load the Automatic Speech Recognition (ASR) model
whisper_model = whisper.load_model("base.en")

# Transcribe the audio file
result = whisper_model.transcribe("audio.wav")

# Write the transcription to a text file
with open('transcription.txt', 'w') as f:
    f.write(result["text"])

# Stop the timer and calculate the total time taken
toc = time.perf_counter()
print("Total time taken: {}".format(toc - tic))

