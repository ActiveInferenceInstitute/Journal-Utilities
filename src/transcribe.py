"""
This module handles the transcription of audio files using WhisperX,
and updates the transcription status in the database.
"""
import asyncio
import os
import json
import logging
import whisperx
from whisperx.diarize import DiarizationPipeline
import subprocess
from surrealdb import AsyncSurreal
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('../.env')

# Set up logging
logging.basicConfig(
    filename='transcription.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class TranscriptionService:
    """
    A service for transcribing audio files using WhisperX, including alignment and diarization.
    
    Attributes:
        hf_token (str): Hugging Face token for authentication.
        device (str): Device to use for computation (e.g., 'cuda').
        batch_size (int): Batch size for transcription.
        compute_type (str): Compute type (e.g., 'float16', 'int8').
    """
    def __init__(self, hf_token, device, batch_size, compute_type):
        self.device = device
        self.batch_size = batch_size
        self.hf_token = hf_token
        self.compute_type = compute_type
        self.model = whisperx.load_model("large-v3", device, compute_type=compute_type,
                                         language="en")

        # Load alignment model and diarization pipeline during initialization
        self.align_model, self.metadata = whisperx.load_align_model(language_code="en",
                                                                    device=device)
        self.diarize_model = DiarizationPipeline(use_auth_token=hf_token, device=device)

    def download_audio(self, video_url, output_wav_file, ffmpeg_location='/usr/bin'):
        """Function to download and prepare the audio file"""
        subprocess.run(['yt-dlp', '-xv', '--ffmpeg-location', ffmpeg_location, '--audio-format', 'wav', '-o', output_wav_file, '--', video_url], check=True)

    async def extract_audio_and_update(self, db, video_path, session_id):
        output_audio_path = f"{video_path.replace('.mp4', '.wav')}"  # Modify as needed based on your directory structure
        
        # Execute ffmpeg command to extract audio
        command = ['ffmpeg', '-i', video_path, '-ac', '1', '-ar', '16000', '-vn', output_audio_path]
        try:
            subprocess.run(command, check=True)
            # Merge the database record to indicate wav extraction is complete
            update_result = await db.query(f"""UPDATE {session_id} MERGE {{
                wav_extracted: true
            }};""")
            print(f"Merge result for session {session_id}: {update_result}")
            print(f"Audio extracted and database updated for session {session_id}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to extract audio for session {session_id}: {str(e)}")

    async def create_wavfiles(self, mp4_directory, db_url, db_user, db_password, db_name, db_namespace):
        """
        Read in unprocessed MP4 files from the database and create WAV files

        Args:
            mp4_directory (str): The directory containing the MP4 files to process.
            db_url (str): Database URL
            db_user (str): Database username
            db_password (str): Database password
            db_name (str): Database name
            db_namespace (str): Database namespace

        Returns:
            None
        """
        async with AsyncSurreal(db_url) as db:
            await db.signin({
                'username': db_user,
                'password': db_password
            })
            await db.use(db_namespace, db_name)

            result = await db.query("SELECT * FROM session WHERE (wav_extracted IS NULL OR wav_extracted = false) AND is_private != true")
            for session in result:
                filename = session["filename"]
                video_path = f"{mp4_directory}/{filename}"  # Adjust path as necessary
                print(f"{video_path}")
                await self.extract_audio_and_update(db, video_path, session['id'])

    def remove_words(self, obj):
        """
        Recursively remove 'words' key from dictionaries and lists.
        
        Args:
            obj (dict or list): The object to process.
        
        Returns:
            dict or list: The processed object with 'words' key removed.
        """
        if isinstance(obj, dict):
            obj = {k: self.remove_words(v) for k, v in obj.items() if k != "words"}
        elif isinstance(obj, list):
            obj = [self.remove_words(item) for item in obj]
        return obj

    def simplify_transcript(self, detailed_transcript):
        """
        Simplify the transcript by removing 'words' arrays.
        
        Args:
            detailed_transcript (dict): The detailed transcript.
        
        Returns:
            dict: The simplified transcript.
        """
        return self.remove_words(detailed_transcript)

    def output_text(self, simple_transcript):
        """
        Convert simplified transcript to a formatted text string.
        
        Args:
            simple_transcript (list): The simplified transcript.
        
        Returns:
            str: The formatted text string.
        """
        output = ""
        prev_speaker = None

        for segment in simple_transcript:
            speaker = segment.get("speaker", "UNKNOWN")
            text = segment.get("text", "").strip()

            if text:
                if speaker != prev_speaker:
                    output += f"\n{speaker}:\n"
                    prev_speaker = speaker

                output += text + "\n\n"

        return output.strip()

    def transcribe(self, output_dir, audio_file):
        """
        Transcribe an audio file and save the results in various formats.
        
        Args:
            output_dir (str): Path to folder to store the json and txt files
            audio_file (str): Path to the audio file.
        
        Returns:
            None
        """
        try:
            # 1. Transcribe with original whisper (batched)
            audio = whisperx.load_audio(audio_file)
            result = self.model.transcribe(audio, batch_size=self.batch_size)

            # 2. Align whisper output
            result = whisperx.align(result["segments"], self.align_model, self.metadata, audio,
                                    self.device, return_char_alignments=False)

            # 3. Assign speaker labels
            diarize_segments = self.diarize_model(audio)
            result = whisperx.assign_word_speakers(diarize_segments, result)

            # 4. Write to JSON file
            result_segments = result["segments"]
            base_filename = os.path.splitext(os.path.basename(audio_file))[0]
            output_file = os.path.join(output_dir, f"{base_filename}.json")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(result_segments, f, indent=2)
            logging.info("Transcription saved to %s", output_file)

            # 5. Write simplified JSON file without the 'words' list
            output_simple_file = os.path.join(output_dir, f"{base_filename}.simple.json")
            result_simple = self.simplify_transcript(result_segments)
            with open(output_simple_file, "w", encoding="utf-8") as f:
                json.dump(result_simple, f, indent=2)

            # 6. Write simplified TXT file
            output_simple_txt_file = os.path.join(output_dir, f"{base_filename}.simple.txt")
            result_simple_txt = self.output_text(result_simple)
            with open(output_simple_txt_file, "w", encoding="utf-8") as f:
                f.write(result_simple_txt)
        except Exception as e:
            logging.error("An error occurred during transcription of %s: %s", audio_file, e)
            raise  # Re-raise the exception to propagate it

async def transcribe_and_update(transcription_service, db, session, wav_directory, output_dir):
    """
    Transcribe an audio file and update the database.
    
    Args:
        transcription_service (TranscriptionService): The transcription service instance.
        db (Surreal): The database connection.
        session (dict): The session information.
        wav_directory (str): The directory containing the WAV files.
        output_dir (str): Path to folder to store the json and txt files
    
    Returns:
        None
    """
    try:
        audio_file = f"{wav_directory}/{session['filename']}"
        session_id = session["id"]
        logging.info("Transcription started for session %s", session_id)
        transcription_service.transcribe(output_dir, audio_file)
        update_result = await db.query(f"""UPDATE {session_id} MERGE {{
            transcribed: true
        }};""")
        logging.info("Transcription and update complete for session  %s: %s",
                     session_id, update_result)
    except (IOError, RuntimeError) as e:
        logging.error("An error occurred during transcribe and db update of %s record: %s",
                      session['filename'], e)

async def process_untranscribed_sessions(db_url, db_user, db_password, db_name, db_namespace, wav_directory,
                          output_dir, hf_token, device, batch_size, compute_type):
    """
    Read in all the sessions in the database that haven't been transcribed and run
    transcribe
    
    Args:
        db_url (str): Database URL
        db_user (str): Database username
        db_password (str): Database password
        db_name (str): Database name
        db_namespace (str): Database namespace
        wav_directory (str): The directory containing the WAV files to process.
        output_dir (str): Path to folder to store the json and txt files
        hf_token (str): Hugging Face token for authentication.
        device (str): Device to use for computation (e.g., 'cuda').
        batch_size (int): Batch size for transcription.
        compute_type (str): Compute type (e.g., 'float16', 'int8').
    
    Returns:
        None
    """
    try:
        transcription_service = TranscriptionService(hf_token, device, batch_size, compute_type)

        async with AsyncSurreal(db_url) as db:
            await db.signin({'username': db_user, 'password': db_password})
            await db.use(db_namespace, db_name)

            result = await db.query("SELECT * FROM session WHERE transcribed = false AND is_private != true")

            if result and len(result) > 0:
                for session in result:
                    await transcribe_and_update(transcription_service, db, session,
                                                wav_directory, output_dir)
            else:
                logging.info("No unprocessed sessions found.")
    except (Exception) as e: # pylint: disable=broad-except
        logging.error("An error occurred during query and transcription: %s", e)

async def download_and_transcribe(video_url, db_url, db_user, db_password, db_name, db_namespace,
                                  wav_directory, output_dir, hf_token, device, batch_size, compute_type):
    """
    Downloads an audio file to the wav_directory, creates a session in the database,
    transcribes the wav file, and saves the transcript to the output_dir

    Args:
        video_url: youtube video path in the format https://www.youtube.com/watch?v=v4sAeY06ngs
        transcription_service (TranscriptionService): The transcription service instance.
        db (Surreal): The database connection.
        wav_directory (str): The directory containing the WAV files.
        output_dir (str): Path to folder to store the json and txt files

    Returns:
        None
    """
    # Extract YouTube video ID from the URL
    video_id = video_url.split("v=")[-1]
    
    # Construct the output WAV filename
    output_wav_file = os.path.join(wav_directory, f"{video_id}.wav")
    
    try:
        async with AsyncSurreal(db_url) as db:
            await db.signin({'username': db_user, 'password': db_password})
            await db.use(db_namespace, db_name)

            transcription_service = TranscriptionService(hf_token, device, batch_size, compute_type)

            result = await db.query(f"SELECT * FROM session WHERE session_name = '{video_id}'")
            if result and len(result) > 0:
                logging.error("Video ID %s already downloaded", video_id)
                return

            transcription_service.download_audio(video_url, output_wav_file)
            logging.info("Successfully downloaded audio for video ID: %s", video_id)

            # Create a new session in the database
            session = {
                "session_name": video_id,
                "filename": f"{video_id}.wav",
                "wav_extracted": True,
                "transcribed": False
            }
            create_result = await db.create("session", session)
            logging.info("Created new session in database: %s", create_result)

            # Transcribe the audio and update the database
            await transcribe_and_update(transcription_service, db, session, wav_directory, output_dir)
    except subprocess.CalledProcessError as e:
        logging.error("Failed to download audio for video ID %s: %s", video_id, str(e))
        return
    except Exception as e:
        logging.error("Failed to create session in database: %s", str(e))
        return


if __name__ == '__main__':
    HF_TOKEN = os.getenv('HF_TOKEN')
    DEVICE = "cuda"
    BATCH_SIZE = 48  # reduce if low on GPU mem
    COMPUTE_TYPE = "float16"  # change to "int8" if low on GPU mem (may reduce accuracy)
    WAV_DIRECTORY = os.getenv('WAV_DIRECTORY')
    OUTPUT_DIR = os.getenv('OUTPUT_DIR')
    DB_URL = os.getenv("DB_URL")
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_NAMESPACE = os.getenv('DB_NAMESPACE')

    # asyncio.run(process_untranscribed_sessions(DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE, WAV_DIRECTORY,
    #                             OUTPUT_DIR, HF_TOKEN, DEVICE, BATCH_SIZE, COMPUTE_TYPE))

    VIDEO_URL = "https://www.youtube.com/watch?v=v4sAeY06ngs"
    # TODO: Test
    asyncio.run(download_and_transcribe(VIDEO_URL, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE, WAV_DIRECTORY,
                                OUTPUT_DIR, HF_TOKEN, DEVICE, BATCH_SIZE, COMPUTE_TYPE))
