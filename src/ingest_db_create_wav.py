"""
This module processes and stores MP4 files in SurrealDB.
"""

import os
import asyncio
import shutil
import re
import logging
import csv
import json
import datetime
from surrealdb import AsyncSurreal
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
    async with AsyncSurreal(os.getenv("DB_URL")) as db:
        await db.signin({
            'username': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAMESPACE'), os.getenv('DB_NAME'))

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
    async with AsyncSurreal(os.getenv("DB_URL")) as db:
        print("checking")
        await db.signin({
            'username': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAMESPACE'), os.getenv('DB_NAME'))

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
                if not result or len(result) == 0:
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
                    for session in result:
                        session_id = session["id"]
                        update_result = await db.query(f"""UPDATE {session_id} MERGE {{
                            filename: '{filename}',
                            transcribed: false
                        }};""")
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

    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)

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
                    if not result or len(result) == 0:
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

def is_video_private(youtube_id):
    """Check if a YouTube video ID is marked as private"""
    private_videos_file = os.path.join(os.path.dirname(__file__), 'private_videos.json')
    if os.path.exists(private_videos_file):
        with open(private_videos_file, 'r') as f:
            private_data = json.load(f)
            return youtube_id in private_data.get('private_video_ids', [])
    return False

async def insert_missing_sessions_from_json(coda_json, db_url, db_user, db_password, db_name, db_namespace):
    """
    Read through Coda JSON export and create new sessions by session_name
    with full audit trail tracking

    Args:
        coda_json (str): Full path to JSON file
        db_url (str): Database URL
        db_user (str): Database username
        db_password (str): Database password
        db_name (str): Database name
        db_namespace (str): Database namespace
    """

    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)

        # Generate unique import run ID
        import_run_id = f"import_{datetime.datetime.now().isoformat()}_{os.path.basename(coda_json)}"
        stats = {"total": 0, "inserted": 0, "skipped": 0, "failed": 0, "errors": []}

        logging.info(f"Starting import run: {import_run_id}")

        # Read JSON file
        try:
            with open(coda_json, 'r') as jsonfile:
                data = json.load(jsonfile)
        except Exception as e:
            logging.error(f"Failed to read JSON file {coda_json}: {e}")
            await db.create('import_audit', {
                'import_run_id': import_run_id,
                'timestamp': datetime.datetime.now().isoformat(),
                'source_file': coda_json,
                'operation': 'read_file',
                'status': 'failed',
                'error_message': str(e)
            })
            return

        # Get the items array from the root object
        items = data.get('items', data if isinstance(data, list) else [])

        # Process each row in the JSON
        for row in items:
            stats["total"] += 1
            values = row.get('values', {})
            youtube_url = values.get('YouTube', '')

            if youtube_url:
                # Extract YouTube ID from URL
                youtube_id_pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|live\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
                match = youtube_id_pattern.search(youtube_url)
                if match:
                    youtube_id = match.group(1)
                else:
                    print(f"No valid YouTube ID found: {youtube_url}")
                    await db.create('import_audit', {
                        'import_run_id': import_run_id,
                        'timestamp': datetime.datetime.now().isoformat(),
                        'source_file': coda_json,
                        'operation': 'parse_youtube_id',
                        'status': 'failed',
                        'error_message': f'Invalid YouTube URL: {youtube_url}',
                        'data_attempted': {'youtube_url': youtube_url}
                    })
                    stats["failed"] += 1
                    continue

                try:
                    # Check if session already exists
                    result = await db.query(f"SELECT * FROM session WHERE session_name = '{youtube_id}'")
                    if len(result) == 0:
                        unique_event_name = values.get('Unique event name', '')

                        # Parse date if available
                        date_str = values.get('Date', '')
                        scheduled_date = None
                        if date_str:
                            try:
                                # Parse ISO format date: "2024-10-29T00:00:00.000-07:00"
                                scheduled_date = datetime.datetime.fromisoformat(date_str).isoformat()
                            except (ValueError, TypeError):
                                logging.warning(f"Could not parse date: {date_str}")

                        # Categorize the event
                        category, series, episode = categorize_name(unique_event_name, True)

                        # Create new session
                        new_session = {
                            'category': category,
                            'episode': episode,
                            'series': series,
                            'session_name': youtube_id,
                            'is_private': is_video_private(youtube_id),  # Check if video is private
                            'transcribed': False,
                            'wav_extracted': False,
                            'guests': values.get('Guests', ''),
                            'github': values.get('Github', ''),
                            'other_participants': values.get('Other Participants', ''),
                            'slides_url': values.get('Slides', '') or values.get('Slides URL', ''),
                            'paper_link': values.get('Paper link', ''),
                            'from_coda_json': True
                        }

                        # Add scheduled_date if available
                        if scheduled_date:
                            new_session['scheduled_date'] = f"d'{scheduled_date}'"

                        record = await db.create('session', new_session)
                        print(f"Inserted new session from JSON: {youtube_id}")

                        # Log successful insertion to audit table
                        await db.create('import_audit', {
                            'import_run_id': import_run_id,
                            'timestamp': datetime.datetime.now().isoformat(),
                            'source_file': coda_json,
                            'operation': 'insert',
                            'session_name': youtube_id,
                            'status': 'success',
                            'data_attempted': new_session,
                            'result_data': record
                        })
                        stats["inserted"] += 1
                    else:
                        print(f"Session already exists: {youtube_id}")

                        # Log skipped session to audit table
                        await db.create('import_audit', {
                            'import_run_id': import_run_id,
                            'timestamp': datetime.datetime.now().isoformat(),
                            'source_file': coda_json,
                            'operation': 'skip',
                            'session_name': youtube_id,
                            'status': 'skipped',
                            'error_message': 'Session already exists',
                            'data_attempted': {'youtube_id': youtube_id}
                        })
                        stats["skipped"] += 1

                except Exception as e:
                    logging.error(f"Failed to process session {youtube_id}: {e}")
                    await db.create('import_audit', {
                        'import_run_id': import_run_id,
                        'timestamp': datetime.datetime.now().isoformat(),
                        'source_file': coda_json,
                        'operation': 'insert',
                        'session_name': youtube_id if 'youtube_id' in locals() else 'unknown',
                        'status': 'failed',
                        'error_message': str(e),
                        'data_attempted': values
                    })
                    stats["failed"] += 1
                    stats["errors"].append({
                        'youtube_id': youtube_id if 'youtube_id' in locals() else 'unknown',
                        'error': str(e)
                    })

        # Create summary audit record
        await db.create('import_audit', {
            'import_run_id': import_run_id,
            'timestamp': datetime.datetime.now().isoformat(),
            'source_file': coda_json,
            'operation': 'import_summary',
            'status': 'completed',
            'result_data': stats
        })

        logging.info(f"Import run {import_run_id} completed: {stats}")
        print(f"\nImport Summary:")
        print(f"  Total processed: {stats['total']}")
        print(f"  Inserted: {stats['inserted']}")
        print(f"  Skipped: {stats['skipped']}")
        print(f"  Failed: {stats['failed']}")
        if stats['errors']:
            print(f"  Errors: {stats['errors']}")

async def rollback_import(import_run_id, db_url, db_user, db_password, db_name, db_namespace):
    """
    Rollback all sessions created during a specific import run

    Args:
        import_run_id (str): The import run ID to rollback
        db_url (str): Database URL
        db_user (str): Database username
        db_password (str): Database password
        db_name (str): Database name
        db_namespace (str): Database namespace

    Returns:
        dict: Summary of rollback operations
    """
    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)

        # Get all successful inserts from this import run
        result = await db.query(f"""
            SELECT * FROM import_audit
            WHERE import_run_id = '{import_run_id}'
            AND operation = 'insert'
            AND status = 'success'
        """)

        rollback_count = 0
        errors = []

        if result and len(result) > 0:
            for audit_record in result:
                session_name = audit_record.get('session_name')
                if session_name:
                    try:
                        # Delete the session - need to get the ID first then delete by ID
                        sessions_to_delete = await db.query(f"SELECT * FROM session WHERE session_name = '{session_name}'")
                        if sessions_to_delete and len(sessions_to_delete) > 0:
                            for session in sessions_to_delete:
                                delete_result = await db.query(f"DELETE {session['id']}")

                        # Mark the audit record as rolled back
                        await db.query(f"""UPDATE {audit_record['id']} MERGE {{
                            status: 'rolled_back',
                            rollback_timestamp: '{datetime.datetime.now().isoformat()}'
                        }};""")

                        rollback_count += 1
                        logging.info(f"Rolled back session: {session_name}")
                    except Exception as e:
                        errors.append({'session_name': session_name, 'error': str(e)})
                        logging.error(f"Failed to rollback session {session_name}: {e}")

        # Create rollback summary audit record
        summary = {
            'rollback_count': rollback_count,
            'errors': errors
        }

        await db.create('import_audit', {
            'import_run_id': import_run_id,
            'timestamp': datetime.datetime.now().isoformat(),
            'operation': 'rollback_summary',
            'status': 'completed',
            'result_data': summary
        })

        print(f"\nRollback Summary for {import_run_id}:")
        print(f"  Sessions rolled back: {rollback_count}")
        if errors:
            print(f"  Errors: {len(errors)}")
            for error in errors:
                print(f"    - {error['session_name']}: {error['error']}")

        return summary

async def get_import_summary(import_run_id, db_url, db_user, db_password, db_name, db_namespace):
    """
    Get summary statistics for an import run

    Args:
        import_run_id (str): The import run ID to get summary for

    Returns:
        dict: Summary of the import run
    """
    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)

        # Get the import summary record
        result = await db.query(f"""
            SELECT * FROM import_audit
            WHERE import_run_id = '{import_run_id}'
            AND operation = 'import_summary'
        """)

        if result and len(result) > 0:
            return result[0].get('result_data', {})

        # If no summary record, calculate from individual records
        all_records = await db.query(f"""
            SELECT operation, status FROM import_audit
            WHERE import_run_id = '{import_run_id}'
        """)

        stats = {"total": 0, "inserted": 0, "skipped": 0, "failed": 0}
        for record in all_records:
            if record['operation'] in ['insert', 'skip', 'parse_youtube_id']:
                stats["total"] += 1
                if record['status'] == 'success':
                    stats["inserted"] += 1
                elif record['status'] == 'skipped':
                    stats["skipped"] += 1
                elif record['status'] == 'failed':
                    stats["failed"] += 1

        return stats

async def get_failed_imports(import_run_id, db_url, db_user, db_password, db_name, db_namespace):
    """
    Get all failed operations from an import run

    Args:
        import_run_id (str): The import run ID to check

    Returns:
        list: List of failed operations with details
    """
    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)

        result = await db.query(f"""
            SELECT * FROM import_audit
            WHERE import_run_id = '{import_run_id}'
            AND status = 'failed'
        """)

        failed_imports = []
        if result and len(result) > 0:
            for record in result:
                failed_imports.append({
                    'session_name': record.get('session_name', 'unknown'),
                    'operation': record.get('operation'),
                    'error': record.get('error_message'),
                    'timestamp': record.get('timestamp'),
                    'data_attempted': record.get('data_attempted', {})
                })

        return failed_imports

async def get_recent_import_runs(db_url, db_user, db_password, db_name, db_namespace, limit=10):
    """
    Get list of recent import runs

    Args:
        limit (int): Number of recent runs to return

    Returns:
        list: List of recent import run IDs with their summaries
    """
    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)

        result = await db.query(f"""
            SELECT import_run_id, timestamp, source_file, result_data
            FROM import_audit
            WHERE operation = 'import_summary'
            ORDER BY timestamp DESC
            LIMIT {limit}
        """)

        import_runs = []
        if result and len(result) > 0:
            for record in result:
                import_runs.append({
                    'import_run_id': record.get('import_run_id'),
                    'timestamp': record.get('timestamp'),
                    'source_file': record.get('source_file'),
                    'stats': record.get('result_data', {})
                })

        return import_runs

def escape_string(value):
    """Escape single quotes in a string, or return None if the value is None."""
    return value.replace("'", "\\'") if value is not None else None

async def insert_missing_session_data_from_csv(coda_csv, db_url, db_user, db_password, db_name, db_namespace):
    """
    read through coda_csv and update sessions by session_name

    Args:
        coda_csv (str): Full path to CSV
        db_url (str): Database URL
        db_user (str): Database username
        db_password (str): Database password
        db_name (str): Database name
        db_namespace (str): Database namespace
    """

    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)

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
                    result = await db.query(f"SELECT * FROM session where from_coda_csv is None and session_name = '{youtube_id}'")

                    # for each record in result update slides_url, other_participants, guests, from_coda_csv, github
                    for record in result:
                        session_id = record['id']

                        # TODO: add scheduledDate here
                        guests = escape_string(row.get('Guests', None))
                        github = escape_string(row.get('Github', None))
                        other_participants = escape_string(row.get('Other Participants', None))
                        slides_url = escape_string(row.get('Slides URL', None))

                        # Execute the UPDATE query
                        update_result = await db.query(f"""UPDATE {session_id} MERGE {{
                            guests: '{guests}',
                            github: '{github}',
                            other_participants: '{other_participants}',
                            slides_url: '{slides_url}',
                            from_coda_csv: true
                        }};""")
                        print(f"Updated session {session_id}: {update_result}")

def parse_date(date_str):
    try:
        # Try parsing with time
        return datetime.datetime.strptime(date_str, '%m/%d/%Y %I:%M %p').strftime('%Y-%m-%dT%H:%M:%S-08:00')
    except ValueError:
        try:
            # Try parsing without time
            return datetime.datetime.strptime(date_str, '%m/%d/%Y').strftime('%Y-%m-%dT%H:%M:%S-08:00')
        except ValueError:
            logging.error("Failed to parse date: %s", date_str)
            return None

async def insert_session_date_from_csv(coda_csv, db_url, db_user, db_password, db_name, db_namespace):
    """
    read through coda_csv and update session date by session_name

    Args:
        coda_csv (str): Full path to CSV
        db_url (str): Database URL
        db_user (str): Database username
        db_password (str): Database password
        db_name (str): Database name
        db_namespace (str): Database namespace
    """

    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)

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
                    result = await db.query(f"SELECT * FROM session where session_name = '{youtube_id}'")

                    # for each record in result update date
                    for record in result:
                        session_id = record['id']

                        date_str = row.get('Date', None)
                        if date_str:
                            date = parse_date(date_str)
                            if date:
                                date = f"d'{date}'"
                            else:
                                date = None
                        else:
                            date = None

                        # Execute the UPDATE query
                        update_result = await db.query(f"""UPDATE {session_id} MERGE {{
                            scheduled_date: {date}
                        }};""")
                        print(f"Updated session {session_id}: {update_result}")

async def update_session_name():
    """
    Read in all the session records where session_name = NONE, set session_name = id without
    "session:"

    Returns:
        None
    """
    async with AsyncSurreal(os.getenv("DB_URL")) as db:
        await db.signin({
            'username': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAMESPACE'), os.getenv('DB_NAME'))

        result = await db.query("SELECT * FROM session WHERE session_name is NONE")
        for session in result:
            session_id = session['id']
            session_name = session_id.replace("session:", "")
            update_result = await db.query(f"""UPDATE {session_id} MERGE {{
                session_name: '{session_name}'
            }};""")
            print(f"Update session_name for {session_id}: {update_result}")

async def insert_metadata_youtube_api():
    """
    Looks up metadata for all the sessions where title is none, and updates the metadata in the database

    Returns:
        None
    """
    async with AsyncSurreal(os.getenv("DB_URL")) as db:
        await db.signin({
            'username': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        })
        await db.use(os.getenv('DB_NAMESPACE'), os.getenv('DB_NAME'))

        result = await db.query("SELECT * FROM session WHERE title is NONE AND is_private != true")

        for session in result:
            session_id = session['id']
            session_name = session['session_name']

            print(f"Fetching metadata for {session_name}")

            info = get_video_info(session_name)

            # escape title and description
            title = info.title.replace("'", "\\'")
            description = info.description.replace("'", "\\'")

            # Update the existing session using SurrealDB MERGE syntax
            update_result = await db.query(f"""UPDATE {session_id} MERGE {{
                title: '{title}',
                description: '{description}',
                thumbnails: '{info.image_url}',
                published_at: '{info.publisheddate}',
                url: '{info.link}',
                channel_title: '{info.channel_title}'
            }};""")
            
            # print the query
            print(f"Updated metadata for {session_id}")

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
        textbook_parr_pattern = r'Parr, Pezzulo, Friston 2022 Textbook Cohort (\d+), Session (\d+)'
        symposium_2021_pattern = r'Prof\. Karl Friston ~ Applied Active Inference Symposium'
        symposium_2022_pattern = r'2nd Applied Active Inference Symposium'
        symposium_pattern = r'Applied Active Inference Symposium (\d{4}) part (\d+)'
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
    symposium_match = re.search(symposium_pattern, name)
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
    textbook_parr_match = re.search(textbook_parr_pattern, name)
    twitterspaces_match = re.search(twitterspaces_pattern, name)

    category = None


    series = None
    episode = None

    if symposium_match:
        category = "Applied Active Inference Symposium/" + symposium_match.group(1)
        series = f"part {symposium_match.group(2)}"
        episode = None
    elif symposium_2021_match:
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
    elif textbook_parr_match:
        # For patterns like "Parr, Pezzulo, Friston 2022 Textbook Cohort 7, Session 1"
        category = f"TextbookGroup/ParrPezzuloFriston2022/Cohort_{textbook_parr_match.group(1)}"
        series = f"Meeting_{textbook_parr_match.group(2).zfill(3)}"
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
    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)
        result = await db.query("SELECT * FROM session where category is null;")

        for session in result:
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
    
    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)
        result = await db.query("SELECT * FROM session where category is 'Projects/General'")
        for session in result:
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
    # Choose the best prose file where md > txt > odt > pdf
    prose_file_priority = {'md': 3, 'txt': 2, 'odt': 1, 'pdf': 0}

    async with AsyncSurreal(db_url) as db:
        await db.signin({
            'username': db_user,
            'password': db_password
        })
        await db.use(db_namespace, db_name)
        result = await db.query("SELECT * FROM session where metadata_filename is None;")

        for session in result:
            session_id = session['id']
            category = session.get('category')
            series = session.get('series')
            # TODO: how to deal with multiple episodes in the Metadata folder
            episode = session.get('episode', '')

            logging.info("%s %s %s", category, series, episode)

            if not category or not series or category is None or series is None:
                logging.info("Category or Series missing for session %s", session_id)
                continue

            repo_path = os.path.join(journal_repo_dir, category, series, 'Metadata')
            if os.path.exists(repo_path):
                # check if a file exists that matches repo_path/*.sentences.csv
                metadata_files = [f for f in os.listdir(repo_path) if f.endswith('.sentences.csv')]
            
                if metadata_files:
                    # If there are matching files, use the first one
                    metadata_filename = metadata_files[0]
                    transcript_method = "AssemblyAI"
                else:
                    metadata_files = [f for f in os.listdir(repo_path) if f.endswith('.simple.txt')]
                    if metadata_files:
                        # If there are matching files, use the first one
                        metadata_filename = metadata_files[0]
                        transcript_method = "WhisperX"
                    else:
                        # no files ended with .sentences.csv or .simple.txt
                        # look for any files in metadata_files that are not blank_document.txt
                        # Look for any files that are not blank_document.txt
                        metadata_files = [f for f in os.listdir(repo_path) if f != 'blank_document.txt']
                        
                        if metadata_files:
                            # If there are non-blank files, use the first one
                            # TODO: assumes AssemblyAI transcript method currently
                            metadata_filename = metadata_files[0]
                            transcript_method = "AssemblyAI"
                        else:
                            metadata_filename = None
                    
                if metadata_filename:
                    # Update the session record with the metadata filename
                    update_result = await db.query(f"""
                        UPDATE session 
                        SET 
                            metadata_filename = '{metadata_filename}',
                            transcript_method = '{transcript_method}',
                            transcribed = True
                        WHERE id = '{session_id}'
                    """)
                    logging.info("Updated metadata_filename for session %s: %s", session_id, metadata_filename)
                else:
                    logging.warning("Metadata file not found for session %s: %s", session_id, repo_path)
            else:
                logging.warning("Metadata directory not found for session %s: %s", session_id, repo_path)

            # Check for WorkingCopy file
            workingcopy_path = os.path.join(journal_repo_dir, category, series, 'Transcripts', 'WorkingCopy')
            if os.path.exists(workingcopy_path):
                workingcopy_files = [f for f in os.listdir(workingcopy_path) if f != 'blank_document.txt']
                if workingcopy_files:
                    workingcopy_filename = workingcopy_files[0]
                    update_result = await db.query(f"""
                        UPDATE session 
                        SET 
                            workingcopy_filename = '{workingcopy_filename}'
                        WHERE id = '{session_id}'
                    """)
                    logging.info("Updated workingcopy_filename for session %s: %s", session_id, workingcopy_filename)

            # Check for Prose file
            prose_path = os.path.join(journal_repo_dir, category, series, 'Transcripts', 'Prose')
            if os.path.exists(prose_path):
                prose_files = [f for f in os.listdir(prose_path) if f != 'blank_document.txt']
                if prose_files:
                    prose_filename = max(prose_files, key=lambda f: prose_file_priority.get(f.split('.')[-1].lower(), -1))

                    update_result = await db.query(f"""
                        UPDATE session 
                        SET 
                            prose_filename = '{prose_filename}'
                        WHERE id = '{session_id}'
                    """)
                    logging.info("Updated prose_filename for session %s: %s", session_id, prose_filename)


if __name__ == "__main__":
    WAV_DIRECTORY = os.getenv('WAV_DIRECTORY')
    OUTPUT_DIR = os.getenv('OUTPUT_DIR')
    JOURNAL_REPO_DIR = os.getenv('JOURNAL_REPO_DIR')

    DB_URL = os.getenv("DB_URL")
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_NAMESPACE = os.getenv('DB_NAMESPACE')

    CODA_JSON = "/mnt/md0/projects/Journal-Utilities/data/input/livestream_fulldata_table.json"
    
    # STEP 1
    # asyncio.run(insert_missing_sessions_from_json(CODA_JSON, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))

    # STEP 2
    asyncio.run(insert_metadata_youtube_api())

    # STEP 3
    # run transcribe.py

    # STEP 4
    # asyncio.run(copy_files_to_journal(OUTPUT_DIR, JOURNAL_REPO_DIR, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))


    # Old utilities
    # CODA_CSV = "/mnt/md0/projects/Journal-Utilities/data/input/livestream_fulldata_2024-09-05.csv"
    # asyncio.run(insert_missing_sessions_from_csv(CODA_CSV, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    # asyncio.run(insert_missing_session_data_from_csv(CODA_CSV, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    # asyncio.run(insert_session_date_from_csv(CODA_CSV, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    # asyncio.run(insert_processed_files(JOURNAL_REPO_DIR, DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    # asyncio.run(update_category_series_episode_by_title(DB_URL, DB_USER, DB_PASSWORD, DB_NAME, DB_NAMESPACE))
    # asyncio.run(process_and_store_files(directory=WAV_DIRECTORY))
    # asyncio.run(check_missing_mp4(directory=WAV_DIRECTORY))
    # asyncio.run(update_session_name())
    