"""
LLM-based chapter and timestamp generator for Active Inference video transcripts.

Supports:
- Local Ollama (e.g. gemma3:4b, qwen2.5:7b)
- Hosted OpenRouter / OpenAI compatible endpoints

Processes timestamped transcript segments (from WhisperX/transcript JSON),
identifies semantic shifts, and outputs properly formatted, high-resolution
chronological YouTube chapters starting at 00:00 (10-30 chapters based on video duration).
"""

from __future__ import annotations

import json
import logging
import os
import re
import urllib.error
import urllib.request
from typing import Any

from journal_utilities.youtube.metadata_formatter import (
    ChapterEntry,
    format_seconds_to_timestamp,
)

logger = logging.getLogger(__name__)

DEFAULT_OLLAMA_URL = "http://localhost:11434"
DEFAULT_OPENROUTER_URL = "https://openrouter.ai/api/v1"
DEFAULT_OLLAMA_MODEL = "gemma3:4b"
DEFAULT_OPENROUTER_MODEL = "openai/gpt-4o-mini"

CHAPTER_LINE_PATTERN = re.compile(
    r"(?:^\s*(?:\d+[\.\)]\s*)?)(?:\[?(\d{1,2}:\d{2}(?::\d{2})?)\]?)\s*[-–—:]?\s*(.+)$"
)


def parse_timestamp_to_seconds(ts_str: str) -> float | None:
    """Parse MM:SS or HH:MM:SS string to seconds."""
    parts = ts_str.strip().split(":")
    try:
        if len(parts) == 2:
            return float(parts[0]) * 60 + float(parts[1])
        elif len(parts) == 3:
            return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
    except (ValueError, IndexError):
        return None
    return None


def parse_llm_chapters_text(text: str) -> list[ChapterEntry]:
    """Extract and sanitize chapter entries from LLM generated response."""
    chapters: list[ChapterEntry] = []

    for line in text.splitlines():
        line_str = line.strip()
        if not line_str:
            continue
        match = CHAPTER_LINE_PATTERN.search(line_str)
        if match:
            ts_str = match.group(1).strip()
            title = match.group(2).strip()
            title = re.sub(r"[\*\_]", "", title).strip()

            secs = parse_timestamp_to_seconds(ts_str)
            if secs is not None and title:
                chapters.append(ChapterEntry(start=secs, title=title))

    if not chapters:
        return []

    # Deduplicate and sort chronologically
    chapters.sort(key=lambda c: c.start)
    unique_chapters: list[ChapterEntry] = []
    seen_times: set[float] = set()
    for c in chapters:
        if c.start not in seen_times:
            unique_chapters.append(c)
            seen_times.add(c.start)

    # Ensure starts at 00:00 (YouTube requirement)
    if unique_chapters and unique_chapters[0].start > 0:
        unique_chapters.insert(0, ChapterEntry(start=0.0, title="Introduction"))

    # Enforce chapter-count contract (10-30 chapters per video)
    if len(unique_chapters) > 30:
        logger.warning(
            "LLM produced %d chapters; downsampling to 30 via evenly spaced selection.",
            len(unique_chapters),
        )
        indices = sorted({round(i * (len(unique_chapters) - 1) / 29) for i in range(30)})
        indices[0] = 0  # Always keep the first (00:00) entry
        unique_chapters = [unique_chapters[i] for i in indices]
    elif 0 < len(unique_chapters) < 10:
        logger.warning(
            "LLM produced only %d chapters; below the 10-chapter minimum but kept as-is.",
            len(unique_chapters),
        )

    return unique_chapters


def downsample_transcript_segments(
    segments: list[dict[str, Any]],
    interval_seconds: float = 30.0,
    max_chars: int = 40000,
) -> str:
    """Downsample granular transcript segments into a concise time-stamped text block."""
    if not segments:
        return ""

    lines: list[str] = []
    last_time = -interval_seconds

    for seg in segments:
        start = float(seg.get("start", 0.0))
        text = str(seg.get("text", "")).strip()
        if not text:
            continue

        if start - last_time >= interval_seconds:
            ts_str = format_seconds_to_timestamp(start)
            lines.append(f"[{ts_str}] {text}")
            last_time = start

    text_block = "\n".join(lines)
    if len(text_block) > max_chars:
        text_block = text_block[:max_chars] + "\n[...remaining transcript omitted for brevity...]"
    return text_block


def calculate_optimal_chapter_count(total_duration_seconds: float | None) -> int:
    """Calculate optimal number of chapters (10-30) based on video length."""
    if not total_duration_seconds or total_duration_seconds <= 0:
        return 15  # Default balanced count

    minutes = total_duration_seconds / 60.0
    if minutes < 20:
        return 10
    elif minutes < 45:
        return 12
    elif minutes < 90:
        return 20
    else:
        return min(30, int(minutes // 4))


class ChapterGenerator:
    """Generates high-resolution video chapters from transcripts using local or hosted LLMs."""

    def __init__(
        self,
        backend: str = "ollama",
        model: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
    ) -> None:
        self.backend = backend.lower()
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if self.backend == "ollama":
            self.model = model or DEFAULT_OLLAMA_MODEL
            self.base_url = (base_url or os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_URL)).rstrip("/")
        else:
            self.model = model or DEFAULT_OPENROUTER_MODEL
            self.base_url = (base_url or os.getenv("OPENROUTER_BASE_URL", DEFAULT_OPENROUTER_URL)).rstrip("/")

    def generate_chapters(
        self,
        *,
        title: str,
        transcript_segments: list[dict[str, Any]],
        num_chapters: int | None = None,
    ) -> list[ChapterEntry]:
        """Generate timestamped chapters for a video (10-30 chapters by default)."""
        total_duration = 0.0
        if transcript_segments:
            last_seg = transcript_segments[-1]
            total_duration = float(last_seg.get("end", last_seg.get("start", 0.0)))

        target_count = num_chapters or calculate_optimal_chapter_count(total_duration)
        sample_text = downsample_transcript_segments(transcript_segments, interval_seconds=30.0)
        if not sample_text:
            logger.warning("No transcript text available to generate chapters.")
            return []

        prompt = (
            f"You are an expert technical editor for the Active Inference Institute.\n"
            f"Create {target_count} clear, high-resolution YouTube video chapters with timestamps for the session: \"{title}\".\n\n"
            f"GUIDELINES:\n"
            f"1. Must start with \"00:00 Introduction\" (or relevant title).\n"
            f"2. Provide between {max(8, target_count - 5)} and {target_count + 5} granular chapters marking every significant topic, speaker transition, model slide, or discussion question.\n"
            f"3. Timestamps must be strictly chronological and derived from the bracketed [MM:SS] timestamps in the transcript.\n"
            f"4. Format each line strictly as: MM:SS Chapter Title or HH:MM:SS Chapter Title.\n"
            f"5. Output ONLY the numbered or clean timestamp list, no introduction, markdown headers, or summary prose.\n\n"
            f"TRANSCRIPT EXCERPT WITH TIMESTAMPS:\n"
            f"{sample_text}\n"
        )

        if self.backend == "ollama":
            raw_response = self._call_ollama(prompt)
        else:
            raw_response = self._call_openrouter(prompt)

        return parse_llm_chapters_text(raw_response)

    def _call_ollama(self, prompt: str) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.2},
        }
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("response", "")
        except Exception as e:
            logger.error("Ollama chapter generation request failed: %s", e)
            raise

    def _call_openrouter(self, prompt: str) -> str:
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY required for OpenRouter backend")
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You generate high-resolution YouTube chapters with exact timestamps from transcripts."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=body,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "X-Title": "journal-youtube-chapters",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choices = data.get("choices", [])
                if choices:
                    return choices[0].get("message", {}).get("content", "")
                return ""
        except Exception as e:
            logger.error("OpenRouter chapter generation request failed: %s", e)
            raise
