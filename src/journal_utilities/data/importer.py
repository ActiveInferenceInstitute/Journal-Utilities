"""
Session import functionality for Journal Utilities.

This module handles importing sessions from Coda JSON exports
into the SurrealDB database with full audit trail tracking.
"""

import datetime
import json
import logging
import os
import re
from pathlib import Path
from typing import Any, Optional

from ..youtube.categorizer import categorize_name
from .database import DatabaseClient, DatabaseConfig
from ..youtube.youtube import extract_youtube_id, is_video_private


async def insert_missing_sessions_from_json(
    coda_json: str,
    db_url: str,
    db_user: str,
    db_password: str,
    db_name: str,
    db_namespace: str
) -> dict:
    """
    Read through Coda JSON export and create new sessions with audit trail.

    Args:
        coda_json: Full path to JSON file
        db_url: Database URL
        db_user: Database username
        db_password: Database password
        db_name: Database name
        db_namespace: Database namespace

    Returns:
        Import statistics dictionary
    """
    config = DatabaseConfig(
        url=db_url,
        user=db_user,
        password=db_password,
        name=db_name,
        namespace=db_namespace
    )
    
    async with DatabaseClient(config) as db:
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
            return stats

        # Get the items array from the root object
        if isinstance(data, list):
            items = data
        else:
            items = data.get('items', [])

        # Process each row in the JSON
        for row in items:
            stats["total"] += 1
            values = row.get('values', {})
            youtube_url = values.get('YouTube', '')

            if youtube_url:
                youtube_id = extract_youtube_id(youtube_url)
                
                if not youtube_id:
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
                                scheduled_date = datetime.datetime.fromisoformat(date_str)
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
                            'is_private': is_video_private(youtube_id),
                            'transcribed': False,
                            'wav_extracted': False,
                            'guests': values.get('Guests', ''),
                            'github': values.get('Github', ''),
                            'other_participants': values.get('Other Participants', ''),
                            'slides_url': values.get('Slides', '') or values.get('Slides URL', ''),
                            'paper_link': values.get('Paper link', ''),
                            'from_coda_json': True
                        }

                        if scheduled_date:
                            new_session['scheduled_date'] = scheduled_date

                        record = await db.create('session', new_session)
                        print(f"Inserted new session from JSON: {youtube_id}")

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

        return stats
