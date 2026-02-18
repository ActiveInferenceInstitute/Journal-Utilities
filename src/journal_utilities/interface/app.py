"""
FastAPI web application for the Active Inference Institute interface.

Serves the SPA frontend and provides API endpoints for videos,
transcripts, audio streaming, search, and LLM chat.
"""

import logging
import mimetypes
import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Optional

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from journal_utilities.interface.chat_engine import ChatEngine
from journal_utilities.interface.data_loader import DataLoader

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------

STATIC_DIR = Path(__file__).parent / "static"


def create_app(data_dir: Optional[Path] = None) -> FastAPI:
    """Create and configure the FastAPI application."""
    # Initialize data loader and chat engine
    loader = DataLoader(data_dir=data_dir)
    chat_engine = ChatEngine()

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        """Load data on startup, cleanup on shutdown."""
        loader.load()
        chat_engine.search_index = loader.search_index
        logger.info("Application ready — %d videos loaded", len(loader.videos))
        yield
        logger.info("Application shutting down")

    app = FastAPI(
        title="Active Inference Institute",
        description="Transcript library and research chat for the Active Inference channel",
        version="1.0.0",
        lifespan=lifespan,
    )

    # CORS for development
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ------------------------------------------------------------------
    # API routes
    # ------------------------------------------------------------------

    @app.get("/api/stats")
    async def get_stats() -> dict[str, Any]:
        """Get aggregate channel statistics."""
        return loader.get_stats()

    @app.get("/api/videos")
    async def get_videos(
        category: Optional[str] = None,
        has_transcript: Optional[bool] = None,
        sort_by: str = "upload_date",
        reverse: bool = True,
        offset: int = 0,
        limit: int = Query(default=50, le=200),
        q: Optional[str] = None,
    ) -> dict[str, Any]:
        """Get paginated, filterable list of videos."""
        if q:
            # Search mode
            results = loader.search_index.search(q, limit=limit)
            video_dicts = []
            for r in results:
                video = loader.get_video(r.video_id)
                if video:
                    d = video.to_dict()
                    d["search_score"] = r.score
                    d["search_snippet"] = r.snippet
                    video_dicts.append(d)
            return {"videos": video_dicts, "total": len(video_dicts), "query": q}

        # Normal listing
        records, total = loader.get_all_videos(
            category=category,
            has_transcript=has_transcript,
            sort_by=sort_by,
            reverse=reverse,
            offset=offset,
            limit=limit,
        )
        return {
            "videos": [r.to_dict() for r in records],
            "total": total,
            "offset": offset,
            "limit": limit,
        }

    @app.get("/api/videos/{video_id}")
    async def get_video(video_id: str) -> dict[str, Any]:
        """Get detailed info for a single video."""
        record = loader.get_video(video_id)
        if not record:
            raise HTTPException(status_code=404, detail="Video not found")
        return record.to_dict()

    @app.get("/api/transcripts/{video_id}")
    async def get_transcript(video_id: str) -> dict[str, Any]:
        """Get transcript text for a video."""
        record = loader.get_video(video_id)
        if not record or not record.has_transcript:
            raise HTTPException(status_code=404, detail="Transcript not found")

        text = loader.search_index.get_transcript(video_id)
        if not text and record.transcript_path:
            try:
                text = Path(record.transcript_path).read_text(encoding="utf-8")
            except OSError:
                raise HTTPException(status_code=500, detail="Failed to read transcript")

        return {
            "video_id": video_id,
            "text": text or "",
            "size": record.transcript_size,
            "title": record.title,
        }

    @app.get("/api/audio/{video_id}")
    async def stream_audio(video_id: str, request: Request) -> StreamingResponse:
        """Stream audio file with Range header support."""
        record = loader.get_video(video_id)
        if not record or not record.has_audio or not record.audio_path:
            raise HTTPException(status_code=404, detail="Audio not found")

        audio_path = Path(record.audio_path)
        if not audio_path.exists():
            raise HTTPException(status_code=404, detail="Audio file missing")

        file_size = audio_path.stat().st_size
        content_type = mimetypes.guess_type(str(audio_path))[0] or "audio/mpeg"

        # Handle Range requests for seeking
        range_header = request.headers.get("range")
        if range_header:
            ranges = range_header.replace("bytes=", "").split("-")
            start = int(ranges[0]) if ranges[0] else 0
            end = int(ranges[1]) if ranges[1] else file_size - 1
            end = min(end, file_size - 1)
            content_length = end - start + 1

            def iter_range() -> Any:
                with open(audio_path, "rb") as f:
                    f.seek(start)
                    remaining = content_length
                    while remaining > 0:
                        chunk_size = min(8192, remaining)
                        data = f.read(chunk_size)
                        if not data:
                            break
                        remaining -= len(data)
                        yield data

            return StreamingResponse(
                iter_range(),
                status_code=206,
                media_type=content_type,
                headers={
                    "Content-Range": f"bytes {start}-{end}/{file_size}",
                    "Accept-Ranges": "bytes",
                    "Content-Length": str(content_length),
                },
            )

        # Full file
        def iter_file() -> Any:
            with open(audio_path, "rb") as f:
                while True:
                    data = f.read(8192)
                    if not data:
                        break
                    yield data

        return StreamingResponse(
            iter_file(),
            media_type=content_type,
            headers={
                "Accept-Ranges": "bytes",
                "Content-Length": str(file_size),
            },
        )

    @app.get("/api/categories")
    async def get_categories() -> dict[str, Any]:
        """Get all categories with video counts."""
        return {
            "categories": {
                cat: len(vids) for cat, vids in sorted(loader.categories.items())
            }
        }

    @app.get("/api/search")
    async def search(
        q: str = Query(..., min_length=2),
        limit: int = Query(default=20, le=100),
    ) -> dict[str, Any]:
        """Full-text search across all transcripts."""
        results = loader.search_index.search(q, limit=limit)
        items = []
        for r in results:
            video = loader.get_video(r.video_id)
            items.append(
                {
                    "video_id": r.video_id,
                    "title": video.title if video else "",
                    "category": video.category if video else None,
                    "score": r.score,
                    "snippet": r.snippet,
                    "thumbnail_url": video.thumbnail_url if video else "",
                }
            )
        return {"results": items, "total": len(items), "query": q}

    # ------------------------------------------------------------------
    # Chat API
    # ------------------------------------------------------------------

    @app.get("/api/chat/status")
    async def chat_status() -> dict[str, Any]:
        """Check LLM availability."""
        return await chat_engine.check_ollama()

    @app.post("/api/chat")
    async def chat_message(request: Request) -> dict[str, Any]:
        """Send a chat message (non-streaming)."""
        body = await request.json()
        session_id = body.get("session_id", "default")
        message = body.get("message", "")
        use_rag = body.get("use_rag", True)

        if not message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        return await chat_engine.chat(session_id, message, use_rag=use_rag)

    @app.post("/api/chat/stream")
    async def chat_stream(request: Request) -> StreamingResponse:
        """Send a chat message with streaming response (SSE)."""
        body = await request.json()
        session_id = body.get("session_id", "default")
        message = body.get("message", "")
        use_rag = body.get("use_rag", True)

        if not message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        return StreamingResponse(
            chat_engine.chat_stream(session_id, message, use_rag=use_rag),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
            },
        )

    @app.post("/api/chat/clear")
    async def chat_clear(request: Request) -> dict[str, str]:
        """Clear a chat session."""
        body = await request.json()
        session_id = body.get("session_id", "default")
        chat_engine.clear_session(session_id)
        return {"status": "cleared"}

    # ------------------------------------------------------------------
    # Static files + SPA fallback
    # ------------------------------------------------------------------

    if STATIC_DIR.is_dir():
        app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

    @app.get("/")
    async def index() -> HTMLResponse:
        """Serve the SPA."""
        index_path = STATIC_DIR / "index.html"
        if index_path.exists():
            return HTMLResponse(content=index_path.read_text(encoding="utf-8"))
        return HTMLResponse(
            content="<h1>Active Inference Institute</h1><p>Static files not found.</p>"
        )

    return app


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the development server."""
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logger.info("Starting Active Inference Institute interface on %s:%d", host, port)

    app = create_app()
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
