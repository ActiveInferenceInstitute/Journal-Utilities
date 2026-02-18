# Web Interface (FastAPI + Vanilla JS)

The Journal Utilities **Web Interface** (`src/journal_utilities/interface/`) is a lightweight, responsive Single Page Application (SPA) for browsing the Active Inference video library.

## Features

- **Video Library**: List all videos with thumbnails, durations, and metadata.
- **Search**: Full-text search over video titles, descriptions, and transcripts (BM25 + TF-IDF).
- **Video Detail**: Embedded YouTube player, transcript viewer with synchronized highlighting, and metadata panel.
- **Chat (RAG)**: Interactive Q&A powered by Ollama and local transcript retrieval.
- **Categories**: Browse videos by series (e.g., "Math Group", "Morphology", "Livestreams") or type.
- **Knowledge Graph**: Visualize relationships between speakers, concepts, and entities (future integration with SurrealDB).

## Architecture

The interface is built with a **backend-heavy** approach using FastAPI and HTMX principles (though implemented via vanilla JS fetching for dynamic components):

### Backend (`app.py`)

- **Framework**: FastAPI (async Python)
- **Data Loader**: `src/journal_utilities/interface/data_loader.py` loads the JSON manifest and builds the in-memory search index on startup.
- **API Endpoints**:
  - `GET /api/stats`: Library statistics
  - `GET /api/videos`: List all videos (paginated, filterable by category)
  - `GET /api/videos/{id}`: Detailed info for a single video
  - `GET /api/transcripts/{id}`: Transcript text for a video
  - `GET /api/audio/{id}`: Stream audio with Range header support
  - `GET /api/categories`: All categories with video counts
  - `GET /api/search`: Full-text search across transcripts
  - `GET /api/chat/status`: Check LLM (Ollama) availability
  - `POST /api/chat`: Send a chat message (non-streaming)
  - `POST /api/chat/stream`: Send a chat message with SSE streaming response
  - `POST /api/chat/clear`: Clear a chat session

### Frontend (`static/`)

- **HTML**: `index.html` (single entry point)
- **CSS**: `styles.css` (custom CSS variables, dark mode default)
- **JavaScript**: `app.js` (client-side router, state management, API calls)
  - **Router**: Hash-based routing (`#library`, `#video/ID`, `#chat`)
  - **Components**: Dynamic DOM creation for video cards, chat bubbles, etc.
  - **State**: Central `state` object for current view, search query, and pagination.

### Source Structure

```text
src/journal_utilities/interface/
├── app.py             # FastAPI application entry point
├── chat_engine.py     # RAG logic and Ollama integration
├── data_loader.py     # Loads metrics and search index
└── static/            # Frontend assets (served directly)
    ├── index.html     # Single Page App entry
    ├── styles.css     # CSS variables and dark mode
    └── app.js         # Client-side router and logic
```

### Setup & Running

1. **Install Interface Dependencies**:

    ```bash
    uv pip install -e ".[interface]"
    ```

2. **Start the Server**:

    ```bash
    uv run python run.py serve
    ```

    Or directly:

    ```bash
    uv run uvicorn journal_utilities.interface.app:create_app --factory --reload
    ```

3. **Access**: Open `http://localhost:8000` in your browser.

## Development

The frontend files are served directly from `src/journal_utilities/interface/static/`. Changes to HTML/CSS/JS are reflected immediately on refresh (if running with `--reload` or similar dev server).

**Key Files:**

- `src/journal_utilities/interface/app.py`: Main application logic.
- `src/journal_utilities/interface/static/app.js`: Core frontend logic (routing, rendering).
- `src/journal_utilities/interface/static/index.html`: Base layout.
