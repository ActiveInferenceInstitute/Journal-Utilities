"""
This module processes and stores MP4 files in SurrealDB.
"""

import os
import asyncio
import shutil
import re
import logging
from surrealdb import Surreal
from pyytdata import get_video_info
from dotenv import load_dotenv
load_dotenv('../.env')

# TODO: change all print statements to logging.* and pass in SURREALDB as arguments

# Set up logging
logging.basicConfig(
    filename='transcription.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

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

async def insert_metadata_youtube_api():
    """
    Looks up metadata for all the sessions where title is none, and updates the metadata in the database

    Returns:
        None
    """
    async with Surreal(os.getenv("DB_URL")) as db:
        await db.signin({
            'user': os.getenv('DB_USER'),
            'pass': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAME'), os.getenv('DB_NAMESPACE'))

        result = await db.query("SELECT * FROM session WHERE title is NONE")

        for session in result[0]["result"]:
            session_id = session['id']
            session_name = session['session_name']

            info = get_video_info(session_name)

            # escape title and description
            title = info.title.replace("'", "\\'")
            description = info.description.replace("'", "\\'")

            # Update the existing session
            update_result = await db.query(f"UPDATE session SET title='{title}', \
                                        description='{description}', thumbnails='{info.image_url}', \
                                        published_at='{info.publisheddate}', url='{info.link}', \
                                        channel_title='{info.channel_title}' \
                                        WHERE id='{session_id}'")
            print(f"Updated metadata for session {session_id}: {update_result}")


async def update_category_series_episode_by_title(db_url, db_user, db_password, db_name, db_namespace):
    """
    select all the sessions, using the title, figure out category, series, and episode
    
    Args:
        db_url (str): Database URL
        db_user (str): Database username
        db_password (str): Database password
        db_name (str): Database name
        db_namespace (str): Database namespace
    """
    
    # if the title matches 'ActInf GuestStream \d+\.\d+', 'ActInf GuestStream #\d+\.\d+', or 'Active Inference GuestStream #\d+\.\d+'
    # set the category to "GuestStream"
    # if the title is 'ActInf GuestStream 067.1'
    # set the series to the first matching number with "GuestStream_" prefix e.g. will be "GuestStream_067"
    # set the episode to the second matching number "1"
    async with Surreal(db_url) as db:
        await db.signin({
            'user': db_user,
            'pass': db_password
        })
        await db.use(db_name, db_namespace)
        result = await db.query("SELECT * FROM session")

        for session in result[0]["result"]:
            session_id = session['id']
            title = session.get('title', '')

            if title:
                symposium_2021_pattern = r'Prof\. Karl Friston ~ Applied Active Inference Symposium'
                symposium_2022_pattern = r'2nd Applied Active Inference Symposium'
                bookstream_pattern = r'(Active Inference)? ?(?:~.*~)? ?BookStream #?(\d+)\.(\d+)'
                social_sciences_pattern = r'(Active Inference for (?:the )?Social Sciences 2023|ActInf Social Sciences 2023)'
                physics_info_pattern = r'Physics as Information Processing'
                gueststream_pattern = r'(ActInf|Active Inference) GuestStream #?(\d+)\.(\d+)'
                insights_pattern = r'Active Inference Insights (\d+)'
                livestream_pattern = r'(ActInf|Active Inference) (?:Livestream|LiveStream) #?(\d+)\.(\d+)'
                mathstream_pattern = r'ActInf MathStream (\d+)\.(\d+)'
                modelstream_pattern = r'(ActInf|Active Inference) ModelStream #?(\d+)\.(\d+)'
                orgstream_pattern = r'ActInf OrgStream #?(\d+)\.(\d+)'
                reviewstream_pattern = r'(ReviewStream|Active Inference Livestream Review)'
                roundtable_pattern = r'(ActInfLab|Active Inference Institute).*?(\d{4}).*?Quarterly Roundtable #(\d+)'
                textbookgroup_pattern = r'ActInf Textbook Group ~ Cohort (\d+) ~ Meeting (\d+)'
                twitterspaces_pattern = r'Active Inference ~ Twitter spaces #(\d+)'
                
                symposium_2021_match = re.search(symposium_2021_pattern, title)
                symposium_2022_match = re.search(symposium_2022_pattern, title)
                bookstream_match = re.search(bookstream_pattern, title)
                social_sciences_match = re.search(social_sciences_pattern, title)
                physics_info_match = re.search(physics_info_pattern, title)
                gueststream_match = re.search(gueststream_pattern, title)
                insights_match = re.search(insights_pattern, title)
                livestream_match = re.search(livestream_pattern, title)
                mathstream_match = re.search(mathstream_pattern, title)
                modelstream_match = re.search(modelstream_pattern, title)
                orgstream_match = re.search(orgstream_pattern, title)
                reviewstream_match = re.search(reviewstream_pattern, title)
                roundtable_match = re.search(roundtable_pattern, title)
                textbookgroup_match = re.search(textbookgroup_pattern, title)
                twitterspaces_match = re.search(twitterspaces_pattern, title)

                if symposium_2021_match:
                    category = "Applied Active Inference Symposium"
                    series = "2021 Symposium with Karl Friston"
                    episode = None
                elif symposium_2022_match:
                    category = "Applied Active Inference Symposium"
                    series = "2022 Symposium on Robotics"
                    episode = None
                elif bookstream_match:
                    category = "BookStream"
                    series = f"BookStream_{bookstream_match.group(2).zfill(3)}"
                    episode = bookstream_match.group(3)
                elif social_sciences_match:
                    category = "Courses/ActiveInferenceForTheSocialSciences"
                    series = None
                    episode = None
                elif physics_info_match:
                    category = "Courses/PhysicsAsInformationProcessing_ChrisFields"
                    series = None
                    episode = None
                elif gueststream_match:
                    category = "GuestStream"
                    series = f"GuestStream_{gueststream_match.group(2).zfill(3)}"
                    episode = gueststream_match.group(3)
                elif insights_match:
                    category = "Insights"
                    series = f"Insights_{insights_match.group(1).zfill(3)}"
                    episode = None
                elif livestream_match:
                    category = "Livestream"
                    series = f"LiveStream_{livestream_match.group(2).zfill(3)}"
                    episode = livestream_match.group(3)
                elif mathstream_match:
                    category = "MathStream"
                    series = f"MathStream_{mathstream_match.group(1).zfill(3)}"
                    episode = mathstream_match.group(2)
                elif modelstream_match:
                    category = "ModelStream"
                    series = f"ModelStream_{modelstream_match.group(2).zfill(3)}"
                    episode = modelstream_match.group(3)
                elif orgstream_match:
                    category = "OrgStream"
                    series = f"OrgStream_{orgstream_match.group(1).zfill(3)}"
                    episode = orgstream_match.group(2)
                elif reviewstream_match:
                    category = "ReviewStream"
                    series = None
                    episode = None
                elif roundtable_match:
                    category = "Roundtable"
                    series = f"Roundtable_{roundtable_match.group(2)}.{roundtable_match.group(3)}"
                    episode = None
                elif textbookgroup_match:
                    category = f"TextbookGroup/ParrPezzuloFriston2022/Cohort_{textbookgroup_match.group(1)}"
                    series = f"Meeting_{textbookgroup_match.group(2).zfill(3)}"
                    episode = None
                elif twitterspaces_match:
                    category = "Twitter Spaces"
                    series = f"TwitterSpaces_{twitterspaces_match.group(1).zfill(3)}"
                    episode = None
                else:
                    continue  # Skip if no match

                update_result = await db.query(f"""
                    UPDATE session 
                    SET 
                        category = '{category}',
                        series = {f"'{series}'" if series is not None else 'NONE'},
                        episode = {f"'{episode}'" if episode is not None else 'NONE'}
                    WHERE id = '{session_id}'
                """)
                print(f"Updated category, series, and episode for session {session_id}: {update_result}")

async def copy_files_to_journal(output_dir, journal_repo_dir, db_url, db_user, db_password, db_name, db_namespace):
    """
    copy files from output_dir to journal_repo_dir based on category, series, and episode
    
    Args:
        output_dir (str): Path to transcripts
        journal_repo_path (str): Full Journal Repo path
        db_url (str): Database URL
        db_user (str): Database username
        db_password (str): Database password
        db_name (str): Database name
        db_namespace (str): Database namespace
    """
    
    async with Surreal(db_url) as db:
        await db.signin({
            'user': db_user,
            'pass': db_password
        })
        await db.use(db_name, db_namespace)
        result = await db.query("SELECT * FROM session where category is 'OrgStream'")
        for session in result[0]["result"]:
            session_id = session['id']
            filename = session.get('filename', '')
            category = session.get('category', '')
            series = session.get('series', '')
            episode = session.get('episode', '')

            # root_filename, remove .mp4 from filename youtube_gx9yAF607ko.mp4
            root_filename = os.path.splitext(filename)[0]

            # create full path by journal_repo_dir + '/' + category + '/' + series + '/Metadata'
            print(f"journal_repo_dir: {journal_repo_dir}, category: {category}, series: {series}")

            repo_path = os.path.join(journal_repo_dir, category, series, 'Metadata')
            
            # Create the directory if it doesn't exist
            os.makedirs(repo_path, exist_ok=True)

            source_files = [
                f"{root_filename}.json",    
                f"{root_filename}.simple.json",
                f"{root_filename}.simple.txt"
            ]

            # new prefix: LiveStream_052.1_ with episode number Meeting_8_ without episode number
            new_filename_prefix = series
            if episode and episode != 'NONE':
                new_filename_prefix += f".{episode}"
            new_filename_prefix += "_"

            for source_file in source_files:
                source_path = os.path.join(output_dir, source_file)

                # Create the new filename
                file_parts = source_file.split('.')
                if len(file_parts) > 2 and file_parts[-2] == 'simple':
                    # Handle .simple.json and .simple.txt files
                    new_filename = f"{new_filename_prefix}{root_filename}.simple.{file_parts[-1]}"
                else:
                    # Handle regular .json files
                    new_filename = f"{new_filename_prefix}{root_filename}.{file_parts[-1]}"
                
                dest_path = os.path.join(repo_path, new_filename)

                if os.path.exists(source_path):
                    shutil.copy2(source_path, dest_path)
                    logging.info("Copied %s to %s", source_file, dest_path)
                else:
                    logging.error("Source file not found: %s", source_path)

            update_result = await db.query(f"""
                UPDATE session 
                SET 
                    journal_filename = '{new_filename_prefix}{root_filename}.simple.txt'
                WHERE id = '{session_id}'
            """)
            logging.info("Updated journal_filename %s: %s", session_id, update_result)


if __name__ == "__main__":
    WAV_DIRECTORY = os.getenv('WAV_DIRECTORY')
    OUTPUT_DIR = os.getenv('OUTPUT_DIR')
    JOURNAL_REPO_DIR = os.getenv('JOURNAL_REPO_DIR')

    DB_URL = os.getenv("DB_URL")
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_NAMESPACE = os.getenv('DB_NAMESPACE')

    # asyncio.run(process_and_store_files(directory=WAV_DIRECTORY))
    # asyncio.run(create_wavfiles(directory=WAV_DIRECTORY))
    # asyncio.run(check_missing_mp4(directory=WAV_DIRECTORY))
    # asyncio.run(update_session_name())
    # asyncio.run(insert_metadata_youtube_api())
    # asyncio.run(update_category_series_episode_by_title(DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    asyncio.run(copy_files_to_journal(OUTPUT_DIR, JOURNAL_REPO_DIR, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))