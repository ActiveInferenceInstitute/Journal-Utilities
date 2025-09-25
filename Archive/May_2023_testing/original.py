import pytube
import moviepy.editor as mp
import numpy as np
import whisper
import time

video_url = "https://www.youtube.com/watch?v=oi8WMPI-JRQ"  # Replace with your desired YouTube video URL

def download_audio(video_url):
    data = pytube.YouTube(video_url)
    audio = data.streams.get_audio_only()
    downloaded_file = audio.download()
    return downloaded_file

def mp4_to_wav(input_file, output_file):
    audio = mp.AudioFileClip(input_file)
    audio.write_audiofile(output_file, codec="pcm_s16le")

tic = time.perf_counter()
input_file = download_audio(video_url)
output_file = "audio.wav"
mp4_to_wav(input_file, output_file)

whisper_model = whisper.load_model("base.en")  # Load the ASR model
result = whisper_model.transcribe("audio.wav")
with open('transcription.txt', 'w') as f:
    f.write(result["text"])

toc = time.perf_counter()
print("Total time taken: {}".format(toc - tic))
