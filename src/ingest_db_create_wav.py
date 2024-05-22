"""
This module processes and stores MP4 files in SurrealDB.
"""

import os
import asyncio
import csv
import subprocess
import re
from surrealdb import Surreal
from dotenv import load_dotenv
load_dotenv('../.env')

async def process_and_store_files(directory):
    """
    Read a list of MP4 files from a directory into SurrealDB.

    Args:
        directory (str): The directory containing the MP4 files to process.

    Returns:
        None
    """
    async with Surreal(os.getenv("DB_URL")) as db:
        await db.signin({
            'user': os.getenv('DB_USER'),
            'pass': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAME'), os.getenv('DB_NAMESPACE'))

        # Process mp4 files
        for filename in os.listdir(directory):
            processed_name = ""
            if filename.endswith(".mp4") and filename.startswith("youtube_"):
                # Process filename: remove "youtube_" prefix and ".mp4" suffix
                processed_name = filename.replace("youtube_", "").replace(".mp4", "")
            elif filename.endswith("].mp4"):
                # Get the last 15 characters of filename and remove ""].mp4" suffix
                processed_name = filename[-16:].replace("].mp4", "")

            # Insert the processed filename into the sessions table
            if processed_name != "":
                record = await db.create(f'session:{processed_name}', {
                    'session_name': processed_name,
                    'filename': filename,
                    'wav_extracted': False,
                    'transcribed': False
                })
                print(f"Inserted: {processed_name} with result: {record}")

async def check_missing_mp4(directory):
    """
    Read a list of MP4 files and add them to SurrealDB if not found,
    otherwise update the filename and transcribed values

    Args:
        directory (str): The directory containing the MP4 files to process.

    Returns:
        None
    """
    async with Surreal(os.getenv("DB_URL")) as db:
        print("checking")
        await db.signin({
            'user': os.getenv('DB_USER'),
            'pass': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAME'), os.getenv('DB_NAMESPACE'))

        # Process mp4 files
        youtube_pattern = re.compile(r'^youtube_(.*).mp4$')
        bracket_pattern = re.compile(r'.*\[(.{15})\].mp4$')

        for filename in os.listdir(directory):
            processed_name = ""
            youtube_match = youtube_pattern.match(filename)
            bracket_match = bracket_pattern.match(filename)
            if youtube_match:
                processed_name = youtube_match.group(1)
            elif bracket_match:
                processed_name = bracket_match.group(1)
            if processed_name:
                print(processed_name)
                result = await db.query(f"SELECT * FROM session WHERE id = \
                                        'session:{processed_name}'")
                if len(result[0]["result"]) == 0:
                    print(processed_name)
                    record = await db.create('session', {
                        'session_name': processed_name,
                        'filename': filename,
                        'wav_extracted': False,
                        'transcribed': False
                    })
                    print(f"Inserted: {processed_name} with result: {record}")
                else:
                    print(processed_name)
                    for session in result[0]["result"]:
                        session_id = session["id"]
                        update_result = await db.query(f"UPDATE session SET filename='{filename}', \
                                                       transcribed=False WHERE id='{session_id}'")
                        print(f"Merge result for session {session_id}: {update_result}")


async def extract_audio_and_update(db, video_path, session_id):
    """
    Extract audio and update database

    Args:
        db (Surreal): database
        video_path (str): MP4 path
        session_id (str): session id for MP4 file

    Returns:
        None
    """
    output_audio_path = f"{video_path.replace('.mp4', '.wav')}"

    # Execute ffmpeg command to extract audio
    command = ['ffmpeg', '-i', video_path, '-ac', '1', '-ar', '16000', '-vn', output_audio_path]
    try:
        subprocess.run(command, check=True)
        # Merge the database record to indicate wav extraction is complete
        update_result = await db.query(f"UPDATE session SET wav_extracted=True \
                                       WHERE id='{session_id}'")
        print(f"Merge result for session {session_id}: {update_result}")
        print(f"Audio extracted and database updated for session {session_id}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to extract audio for session {session_id}: {str(e)}")

async def create_wavfiles(directory):
    """
    Read in unprocessed MP4 files from the database and create WAV files

    Args:
        directory (str): The directory containing the MP4 files to process.

    Returns:
        None
    """
    async with Surreal(os.getenv("DB_URL")) as db:
        await db.signin({
            'user': os.getenv('DB_USER'),
            'pass': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAME'), os.getenv('DB_NAMESPACE'))

        result = await db.query("SELECT * FROM session WHERE wav_extracted IS NULL \
                                OR wav_extracted = false")
        for session in result[0]["result"]:
            filename = session["filename"]
            video_path = f"{directory}/{filename}"  # Adjust path as necessary
            print(f"{video_path}")
            await extract_audio_and_update(db, video_path, session['id'])

async def update_session_name():
    """
    Read in all the session records where session_name = NONE, set session_name = id without
    "session:"

    Returns:
        None
    """
    async with Surreal(os.getenv("DB_URL")) as db:
        await db.signin({
            'user': os.getenv('DB_USER'),
            'pass': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAME'), os.getenv('DB_NAMESPACE'))

        result = await db.query("SELECT * FROM session WHERE session_name is NONE")
        for session in result[0]["result"]:
            session_id = session['id']
            session_name = session_id.replace("session:", "")
            update_result = await db.query(f"UPDATE session SET session_name='{session_name}' \
                                           WHERE id='{session_id}'")
            print(f"Update session_name for {session_id}: {update_result}")

async def insert_metadata(metadata_csv):
    """
    Read in all the session records where session_name = NONE, set session_name = id without
    "session:"

    Returns:
        None
    """
    async with Surreal(os.getenv("DB_URL")) as db:
        await db.signin({
            'user': os.getenv('DB_USER'),
            'pass': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAME'), os.getenv('DB_NAMESPACE'))

        # read in metadata_csv
        with open(metadata_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                session_id = row['id']
                title = row['title']
                description = row['description']
                thumbnails = row['thumbnails']
                published_at = row['publishedAt']
                url = row['_URL']

                if session_id == "hOto96Q8sYQ":
                    # Check if the session exists
                    result = await db.query(f"SELECT * FROM session WHERE id = 'session:{session_id}'")
                    if len(result[0]["result"]) > 0:
                        # Update the existing session
                        existing_session_id = result[0]["result"][0]["id"]
                        update_result = await db.query(f"UPDATE session SET title='{title}', \
                                                    description='{description}', thumbnails='{thumbnails}', \
                                                    published_at='{published_at}', url='{url}' \
                                                    WHERE id='{existing_session_id}'")
                        print(f"Updated metadata for session {session_id}: {update_result}")
                    else:
                        # Create a new session
                        record = await db.create(f'session:{session_id}', {
                            'session_name': id,
                            'title': title,
                            'description': description,
                            'thumbnails': thumbnails,
                            'published_at': published_at,
                            'url': url,
                            'wav_extracted': False,
                            'transcribed': False
                        })
                        print(f"Inserted new session {id} with result: {record}")

if __name__ == "__main__":
    file_directory = os.getenv('FILE_DIRECTORY')

    # asyncio.run(process_and_store_files(directory=file_directory))
    # asyncio.run(create_wavfiles(directory=file_directory))
    # asyncio.run(check_missing_mp4(directory=file_directory))
    # asyncio.run(update_session_name())
    asyncio.run(insert_metadata("/mnt/md0/projects/Journal-Utilities/data/input/video_metadata_2024-05-17.csv"))
