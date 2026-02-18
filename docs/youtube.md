# YouTube Module

The YouTube module (`src/journal_utilities/youtube/`) handles the discovery and categorization of content from the Active Inference Institute channel.

## Architecture

This module does **not** use the YouTube Data API v3 for enumeration, avoiding quota limits. Instead, it uses `yt-dlp`'s flat-playlist extraction features.

## Components

### 1. Channel Enumeration (`channel.py`)

Enumerates all videos on the channel.

- **Method**: extract from the "Uploads" playlist (`UU...`) which contains every public video.
- **Output**: `ChannelManifest` containing `VideoInfo` objects.
- **Performance**: Can list 1000+ videos in seconds without downloading media.

```python
from journal_utilities.youtube.channel import enumerate_channel_videos

manifest = enumerate_channel_videos("UCbPq2w41ZaJSWtpCq4BE6Dg")
print(f"Found {manifest.total_videos} videos")
```

### 2. Playlist Enumeration (`playlist.py`)

Enumerates all playlists created by the channel.

- **Method**: Scrapes the `/playlists` tab via `yt-dlp`.
- **Output**: `PlaylistManifest` containing playlist metadata and video lists.

### 3. Categorizer (`categorizer.py`)

Heuristic engine to parse video titles into structured metadata (Category, Series, Episode).

- **Logic**: Regex pattern matching against known show formats.
- **Supported Formats**:
  - Livestreams (`Livestream #001.1`)
  - GuestStreams
  - OrgStreams
  - MathStreams
  - ModelStreams
  - Textbook Groups
  - Symposia

#### Example Parsing

| Input Title | Category | Series | Episode |
| :--- | :--- | :--- | :--- |
| `Active Inference Livestream #042.1` | `Livestream` | `Livestream_042` | `1` |
| `GuestStream #015.1: John Doe` | `GuestStream` | `GuestStream_015` | `1` |
| `OrgStream #003.1` | `OrgStream` | `OrgStream_003` | `1` |
| `MathStream #001.2: Category Theory` | `MathStream` | `MathStream_001` | `2` |
| `Applied Active Inference Symposium 2021 part 1` | `Symposium` | `2021` | `1` |
| `Textbook Group Cohort 3 Meeting 5` | `TextbookGroup` | `Cohort_3` | `Meeting_005` |

## Data Models

### `VideoInfo`

- `id`: YouTube ID (11 chars)
- `title`: Video title
- `upload_date`: YYYYMMDD
- `duration`: Seconds
- `view_count`: Approximate views

### `ChannelManifest`

- `channel_id`: Source channel
- `enumerated_at`: Timestamp
- `videos`: List of `VideoInfo`
