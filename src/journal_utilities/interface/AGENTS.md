# AGENTS.md - Web Interface

## Module Purpose

FastAPI SPA for browsing the Active Inference video library with Ollama-powered RAG chat.

## Key Files

| File | Purpose |
| --- | --- |
| `app.py` | FastAPI server, REST API, static file serving |
| `data_loader.py` | Builds video manifest from `data/output/` directory |
| `chat_engine.py` | Ollama RAG chat with transcript context retrieval |
| `static/index.html` | HTML shell for the single-page application |
| `static/styles.css` | Design system — monochrome + red theme |
| `static/app.js` | Client-side router, search, filter, pagination, chat |

## Entry Points

```bash
# Launch the interface
uv run python -m journal_utilities.interface.app  # http://localhost:8000
# Or: journal-ui

# Requires interface deps
uv pip install -e ".[interface]"
```

## API Routes

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/api/videos` | Paginated video list (search, filter, sort) |
| `GET` | `/api/videos/{id}` | Video detail with transcript |
| `GET` | `/api/categories` | Category list with counts |
| `GET` | `/api/stats` | Library statistics |
| `POST` | `/api/chat` | Chat message to Ollama |
| `GET` | `/api/chat/status` | Ollama health check |

## Data Flow

```
data/output/
├── transcripts/  → data_loader.py scans for .txt files
├── audio/        → data_loader.py scans for .mp3/.m4a files
└── video/        → data_loader.py scans for .mp4 files
                  ↓
              VideoManifest (in-memory)
                  ↓
              FastAPI REST API → static/app.js (client)
```

## Theme

Monochrome (black/white/gray) + red (`#e63946`) highlights. No blue or green.

## Dependencies

Requires `interface` optional group: `fastapi`, `uvicorn`, `httpx`.
Chat requires Ollama running locally (`ollama serve`).
