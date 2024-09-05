"""
This module processes and stores MP4 files in SurrealDB.
"""

import os
import asyncio
import shutil
import re
import logging
import csv
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

async def insert_missing_sessions_from_csv(coda_csv, db_url, db_user, db_password, db_name, db_namespace):
    """
    read through coda_csv and create new sessions by session_name
    CSV format:
    Category,Unique event name,Guests,YouTube,Slides URL,Github,Title or name of stream,Other Participants
    Livestream,Livestream #058.0,,https://www.youtube.com/live/_zW1BrLwACY,https://docs.google.com/presentation/d/1y7vOH6fRd71xedf95x-blBAM3E_UKJw7XIXKzU_7cO4/edit#slide=id.gc77d90b7ef_1_17,,From pixels to planning: scale-free active inference,,

    Args:
        coda_csv (str): Full path to CSV
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

        # read in CSV line by line
        with open(coda_csv, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile, quotechar="`")
            for row in csvreader:
                youtube_url = row.get('YouTube', '')
                if youtube_url:
                    # Extract YouTube ID from URL, it can be in one of four formats:
                    # https://www.youtube.com/live/L6dhr5hUu8o https://www.youtube.com/watch?v=L6dhr5hUu8o https://youtu.be/L6dhr5hUu8o
                    # https://youtube.com/live/L6dhr5hUu8o
                    youtube_id_pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|live\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
                    match = youtube_id_pattern.search(youtube_url)
                    if match:
                        youtube_id = match.group(1)
                    else:
                        print(f"No valid YouTube ID found: {youtube_url}")
                    
                    # Check if session already exists
                    result = await db.query(f"SELECT * FROM session WHERE session_name = '{youtube_id}'")
                    if len(result[0]["result"]) == 0:
                        unique_event_name = row.get('Unique event name', '')
                        # if categorization fails, enter None for category, series, and episode to be filled in later
                        category, series, episode = categorize_name(unique_event_name, True)
                        # Create new session
                        new_session = {
                            'category': category,
                            'episode': episode,
                            'series': series,
                            'session_name': youtube_id,
                            'transcribed': False,
                            'wav_extracted': False,
                            'guests': row.get('Guests', ''),
                            'github': row.get('Github', ''),
                            'other_participants': row.get('Other Participants', ''),
                            'slides_url': row.get('Slides URL', ''),
                            'from_coda_csv': True
                        }
                        record = await db.create('session', new_session)
                        print(f"Inserted new session: {youtube_id}")

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

def categorize_name(name, is_unique_event_name):
    """
    set is_unique_event_name is true if using the unique event name from the coda table,
    otherwise, if using title from youtube video, set to false
    """
    if is_unique_event_name:
        livestream_pattern = r'(Livestream) #?(\d+)\.(\d+)' #Livestream #057.2
        modelstream_pattern = r'(ModelStream) #?(\d+)\.(\d+)'
        gueststream_pattern = r'(GuestStream) #?(\d+)\.(\d+)'
        insights_pattern = r'Insights #(\d+)'
        roundtable_pattern = r'(Roundtable) ?(\d+)\.(\d+)'
        mathstream_pattern = r'MathStream #(\d+)\.(\d+)'
        orgstream_pattern = r'OrgStream #?(\d+)\.(\d+)'
        morphstream_pattern = r'MorphStream #?(\d+)\.(\d+)'
        artstream_pattern = r'ArtStream #?(\d+)\.(\d+)'
        mathartstream_pattern = r'MathArtStream (\d+)'
        activeinferantstream_pattern = r'Active InferAnt Stream #?(\d+)\.(\d+)'

        # probably won't work with the event name in the coda table
        textbookgroup_pattern = r'ActInf Textbook Group ~ Cohort (\d+) ~ Meeting (\d+)'
        symposium_2021_pattern = r'Prof\. Karl Friston ~ Applied Active Inference Symposium'
        symposium_2022_pattern = r'2nd Applied Active Inference Symposium'
        bookstream_pattern = r'(Active Inference)? ?(?:~.*~)? ?BookStream #?(\d+)\.(\d+)'
        social_sciences_pattern = r'(Active Inference for (?:the )?Social Sciences 2023|ActInf Social Sciences 2023)'
        physics_info_pattern = r'Physics as Information Processing'
        reviewstream_pattern = r'(ReviewStream|Active Inference Livestream Review)'
        twitterspaces_pattern = r'Active Inference ~ Twitter spaces #(\d+)'
    else:
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
        textbookgroup_pattern = r'ActInf Textbook Group ~ Cohort (\d+) ~ (?:Meeting|Session) (\d+)'
        twitterspaces_pattern = r'Active Inference ~ Twitter spaces #(\d+)'
        
        # might need to add ActInf to the beginning of these patterns
        morphstream_pattern = r'MorphStream #?(\d+)\.(\d+)'
        artstream_pattern = r'ArtStream #?(\d+)\.(\d+)'
        mathartstream_pattern = r'MathArtStream (\d+)'
        activeinferantstream_pattern = r'Active InferAnt Stream #?(\d+)\.(\d+)'
    
    symposium_2021_match = re.search(symposium_2021_pattern, name)
    symposium_2022_match = re.search(symposium_2022_pattern, name)
    bookstream_match = re.search(bookstream_pattern, name)
    social_sciences_match = re.search(social_sciences_pattern, name)
    physics_info_match = re.search(physics_info_pattern, name)
    gueststream_match = re.search(gueststream_pattern, name)
    insights_match = re.search(insights_pattern, name)
    livestream_match = re.search(livestream_pattern, name)
    mathstream_match = re.search(mathstream_pattern, name)
    modelstream_match = re.search(modelstream_pattern, name)
    morphstream_match = re.search(morphstream_pattern, name)
    artstream_match = re.search(artstream_pattern, name)
    mathartstream_match = re.search(mathartstream_pattern, name)
    activeinferantstream_match = re.search(activeinferantstream_pattern, name)
    orgstream_match = re.search(orgstream_pattern, name)
    reviewstream_match = re.search(reviewstream_pattern, name)
    roundtable_match = re.search(roundtable_pattern, name)
    textbookgroup_match = re.search(textbookgroup_pattern, name)
    twitterspaces_match = re.search(twitterspaces_pattern, name)

    category = None
    series = None
    episode = None

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
    elif morphstream_match:
        category = "MorphStream"
        series = f"MorphStream_{morphstream_match.group(1).zfill(3)}"
        episode = morphstream_match.group(2)
    elif artstream_match:
        category = "ArtStream"
        series = f"ArtStream_{artstream_match.group(1).zfill(3)}"
        episode = artstream_match.group(2)
    elif mathartstream_match:
        category = "MathArtStream"
        series = f"MathArtStream_{mathartstream_match.group(1).zfill(3)}"
        episode = None
    elif activeinferantstream_match:
        category = "ActiveInferAntStream"
        series = f"ActiveInferAntStream_{activeinferantstream_match.group(1).zfill(3)}"
        episode = activeinferantstream_match.group(2)
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
        print(f"match not found for {name}")
    return category, series, episode

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
    async with Surreal(db_url) as db:
        await db.signin({
            'user': db_user,
            'pass': db_password
        })
        await db.use(db_name, db_namespace)
        result = await db.query("SELECT * FROM session where category is null;")

        for session in result[0]["result"]:
            session_id = session['id']
            title = session.get('title', '')

            if title:
                category, series, episode = categorize_name(title, False)
                if category is None:
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
        result = await db.query("SELECT * FROM session where category is 'Projects/General'")
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

async def insert_processed_files(journal_repo_dir, db_url, db_user, db_password, db_name, db_namespace):
    # async with Surreal(db_url) as db:
    #     await db.signin({
    #         'user': db_user,
    #         'pass': db_password
    #     })
    #     await db.use(db_name, db_namespace)
        for root, dirs, _ in os.walk(journal_repo_dir):
            if 'Transcripts' in dirs:
                transcript_prose_dir = os.path.join(root, 'Transcripts', 'Prose')
                if os.path.exists(transcript_prose_dir):
                    for file in os.listdir(transcript_prose_dir):
                        if file != "blank_document.txt":
                            full_path = os.path.join(transcript_prose_dir, file)
                            print(full_path)
                            # TODO: add to list of files for a session
                    # TODO: insert the best file format for a session md > txt > odt > pdf


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
    asyncio.run(update_category_series_episode_by_title(DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    # asyncio.run(copy_files_to_journal(OUTPUT_DIR, JOURNAL_REPO_DIR, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))

    # CODA_CSV = "/mnt/md0/projects/Journal-Utilities/data/input/livestream_fulldata_2024-09-05.csv"
    # asyncio.run(insert_missing_sessions_from_csv(CODA_CSV, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    # asyncio.run(insert_processed_files(JOURNAL_REPO_DIR, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    