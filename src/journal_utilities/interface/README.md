# Web Interface

FastAPI-based single-page application for browsing and interacting with the Active Inference video library.

## Quick Start

```bash
# Install interface dependencies
uv pip install -e ".[interface]"

# Launch (http://localhost:8000)
uv run python -m journal_utilities.interface.app
# Or via CLI entry point:
journal-ui
```

## Architecture

| File | Purpose |
| --- | --- |
| `app.py` | FastAPI server, REST API routes, static file serving |
| `data_loader.py` | Scans `data/output/` to build a video manifest (transcripts, audio, categories) |
| `chat_engine.py` | Ollama-powered RAG chat engine with transcript context retrieval |
| `static/index.html` | Single-page HTML shell |
| `static/styles.css` | Full design system — monochrome + red theme, responsive layout |
| `static/app.js` | Client-side SPA logic (routing, search, filtering, pagination, chat) |

## Features

### Library Tab

- Searchable, filterable video grid with pagination (25 per page)
- Filter by category (25 categories across Livestream, GuestStream, TextbookGroup, etc.)
- Stats dashboard: total videos, categories, transcripts, audio files

### Video Detail

- Embedded YouTube player
- Audio playback with download
- Full transcript viewer with formatted text
- Metadata sidebar (category, date, video ID)

### Chat Tab

- Ollama-powered conversational AI (llama3.2)
- RAG toggle for transcript-grounded responses
- Context chunks from transcript corpus
- Typing indicators and auto-scroll

### Knowledge Tab

- Category cards with video counts and progress bars
- Click-through to filtered library view

## API Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/api/stats` | Library statistics |
| `GET` | `/api/videos` | Paginated video list with search/filter |
| `GET` | `/api/videos/{id}` | Single video detail |
| `GET` | `/api/transcripts/{id}` | Transcript text for a video |
| `GET` | `/api/audio/{id}` | Stream audio file (supports Range) |
| `GET` | `/api/search` | Full-text transcript search |
| `GET` | `/api/categories` | Category list with counts |
| `POST` | `/api/chat` | Send message to Ollama chat engine |
| `POST` | `/api/chat/stream` | Streaming chat response |
| `POST` | `/api/chat/clear` | Clear chat session history |
| `GET` | `/api/chat/status` | Check Ollama connectivity |

## Theme

Monochrome (black, white, gray) with red (`#e63946`) highlights. Design tokens defined as CSS custom properties in `styles.css`:

```css
--accent-primary: #e63946;    /* Red — links, buttons, highlights */
--bg-primary: #0a0a0a;        /* Near-black background */
--text-primary: #f1f1f1;      /* Off-white text */
--surface-primary: #141414;   /* Card backgrounds */
```

## Dependencies

Requires the `interface` optional dependency group:

- `fastapi >= 0.115.0`
- `uvicorn[standard] >= 0.34.0`
- `httpx >= 0.28.0`

Ollama must be running locally for chat functionality (`ollama serve`).
