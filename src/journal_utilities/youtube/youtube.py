"""
YouTube-related utilities for Journal Utilities.

This module provides:
- YouTube ID extraction from URLs
- Private video detection
- Metadata fetching via YouTube API
"""

import json
import logging
import os
import re
from pathlib import Path
from typing import Optional

from pyytdata import get_video_info


# YouTube ID regex pattern
YOUTUBE_ID_PATTERN = re.compile(
    r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|live/)|youtu\.be/)([a-zA-Z0-9_-]{11})'
)


def build_channel_url(channel_id: str) -> str:
    """Build a YouTube channel URL from a channel ID.

    Args:
        channel_id: YouTube channel ID (e.g. ``UCbPq2w41ZaJSWtpCq4BE6Dg``).

    Returns:
        Full channel URL.
    """
    return f"https://www.youtube.com/channel/{channel_id}"


def build_video_url(video_id: str) -> str:
    """Build a YouTube video URL from a video ID.

    Args:
        video_id: YouTube video ID (11-character string).

    Returns:
        Full video watch URL.
    """
    return f"https://www.youtube.com/watch?v={video_id}"


def extract_youtube_id(url: str) -> Optional[str]:
    """
    Extract YouTube video ID from a URL.
    
    Args:
        url: YouTube URL in various formats
        
    Returns:
        11-character YouTube video ID, or None if not found
    """
    if not url:
        return None
        
    match = YOUTUBE_ID_PATTERN.search(url)
    return match.group(1) if match else None


def is_video_private(youtube_id: str) -> bool:
    """
    Check if a YouTube video ID is marked as private.
    
    Args:
        youtube_id: 11-character YouTube video ID
        
    Returns:
        True if the video is marked as private in the local list
    """
    private_videos_file = Path(__file__).parent / 'private_videos.json'
    
    if private_videos_file.exists():
        try:
            with open(private_videos_file, 'r') as f:
                private_data = json.load(f)
                return youtube_id in private_data.get('private_video_ids', [])
        except (json.JSONDecodeError, IOError) as e:
            logging.warning(f"Error reading private videos file: {e}")
    
    return False


def mark_video_private(youtube_id: str) -> None:
    """
    Mark a YouTube video as private in the local list.
    
    Args:
        youtube_id: 11-character YouTube video ID
    """
    private_videos_file = Path(__file__).parent / 'private_videos.json'
    
    private_data = {'private_video_ids': []}
    
    if private_videos_file.exists():
        try:
            with open(private_videos_file, 'r') as f:
                private_data = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    
    if youtube_id not in private_data.get('private_video_ids', []):
        private_data.setdefault('private_video_ids', []).append(youtube_id)
        
        with open(private_videos_file, 'w') as f:
            json.dump(private_data, f, indent=2)
        
        logging.info(f"Marked video {youtube_id} as private")


async def fetch_video_metadata(session_name: str, db_client) -> Optional[dict]:
    """
    Fetch metadata for a YouTube video and update the database.
    
    Args:
        session_name: YouTube video ID
        db_client: Database client instance
        
    Returns:
        Metadata dictionary if successful, None otherwise
    """
    try:
        info = get_video_info(session_name)
        
        # Escape quotes for database storage
        title = info.title.replace("'", "\\'") if info.title else ""
        description = info.description.replace("'", "\\'") if info.description else ""
        
        metadata = {
            'title': title,
            'description': description,
            'thumbnails': info.image_url,
            'published_at': info.publisheddate,
            'url': info.link,
            'channel_title': info.channel_title
        }
        
        logging.info(f"Fetched metadata for {session_name}")
        return metadata
        
    except Exception as e:
        logging.error(f"Failed to fetch metadata for {session_name}: {e}")
        return None


async def insert_metadata_youtube_api(db_client) -> int:
    """
    Fetch and insert metadata for all sessions missing titles.
    
    Args:
        db_client: Database client instance
        
    Returns:
        Number of sessions updated
    """
    result = await db_client.query(
        "SELECT * FROM session WHERE title is NONE AND is_private != true"
    )
    
    updated_count = 0
    
    for session in result:
        session_id = session['id']
        session_name = session['session_name']
        
        logging.info(f"Fetching metadata for {session_name}")
        
        try:
            info = get_video_info(session_name)
            
            # Escape title and description
            title = info.title.replace("'", "\\'") if info.title else ""
            description = info.description.replace("'", "\\'") if info.description else ""
            
            # Update the session
            await db_client.query(f"""UPDATE {session_id} MERGE {{
                title: '{title}',
                description: '{description}',
                thumbnails: '{info.image_url}',
                published_at: '{info.publisheddate}',
                url: '{info.link}',
                channel_title: '{info.channel_title}'
            }};""")
            
            logging.info(f"Updated metadata for {session_id}")
            updated_count += 1
            
        except Exception as e:
            logging.error(f"Failed to fetch metadata for {session_name}: {e}")
            # Mark as private if we can't access it
            mark_video_private(session_name)
    
    return updated_count
