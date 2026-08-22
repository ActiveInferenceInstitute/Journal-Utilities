"""
YouTube video description and chapter formatter for Journal Utilities.

Combines:
- Paper citation & abstract information (already in video description)
- Formatted chapter timestamps (e.g. 00:00 Introduction) inserted between abstract and link block
- GitHub repository transcript & resource links
- Standard canonical Active Inference Institute link block

Generates clean, idempotent descriptions suitable for updating via YouTube Data API.
"""

import re
from dataclasses import dataclass
from typing import Any

CHAPTERS_MARKER_START = "--- TIMESTAMPS & CHAPTERS ---"
CHAPTERS_MARKER_END = "--- RESOURCES & TRANSCRIPT ---"
INSTITUTE_MARKER_START = "--- ACTIVE INFERENCE INSTITUTE ---"

DEFAULT_GITHUB_TRANSCRIPTS_BASE = "https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal/blob/main/transcripts"

STANDARD_INSTITUTE_LINKBLOCK = """Active Inference Institute information:
Website: https://www.activeinference.institute/
Activities: https://activities.activeinference.institute/
Discord: https://discord.activeinference.institute/
Donate: http://donate.activeinference.institute/
YouTube: https://www.youtube.com/c/ActiveInference/
X: https://x.com/InferenceActive
Active Inference Livestreams: https://video.activeinference.institute/""".strip()


def format_seconds_to_timestamp(seconds: float | int) -> str:
    """Convert duration in seconds to standard YouTube timestamp (MM:SS or HH:MM:SS)."""
    total_seconds = int(seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


@dataclass
class ChapterEntry:
    """Represents a single video chapter / timestamp entry."""
    start: float  # seconds
    title: str

    def to_youtube_line(self) -> str:
        ts = format_seconds_to_timestamp(self.start)
        return f"{ts} {self.title.strip()}"


def build_github_transcript_url(
    video_id: str,
    base_url: str = DEFAULT_GITHUB_TRANSCRIPTS_BASE,
) -> str:
    """Build the canonical GitHub URL for a video's transcript markdown."""
    return f"{base_url}/{video_id}.md"


def format_chapters_block(chapters: list[ChapterEntry | dict[str, Any]]) -> str:
    """Format a list of chapters into YouTube-compliant description lines."""
    if not chapters:
        return ""

    parsed: list[ChapterEntry] = []
    for c in chapters:
        if isinstance(c, ChapterEntry):
            parsed.append(c)
        elif isinstance(c, dict):
            start = float(c.get("start", c.get("start_time", 0.0)))
            title = str(c.get("title", "")).strip()
            if title:
                parsed.append(ChapterEntry(start=start, title=title))

    parsed.sort(key=lambda x: x.start)
    if parsed and parsed[0].start > 0:
        parsed.insert(0, ChapterEntry(start=0.0, title="Introduction"))

    lines = [c.to_youtube_line() for c in parsed]
    return "\n".join(lines)


_TIMESTAMP_LINE_RE = re.compile(r"^\s*(\d{1,2}:){1,2}\d{2}\s+")


def _strip_timestamp_runs(text: str, min_run: int = 3) -> str:
    """Remove runs of >= min_run consecutive legacy timestamp/chapter lines.

    Legacy descriptions sometimes embed a full chapter list (lines like
    '00:00 Introduction'). Stripping such runs keeps assemble_video_description
    idempotent: the freshly generated --- TIMESTAMPS & CHAPTERS --- block is the
    only timestamp list in the assembled description.
    """
    lines = text.split("\n")
    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        if _TIMESTAMP_LINE_RE.match(lines[i]):
            j = i
            while j < n and _TIMESTAMP_LINE_RE.match(lines[j]):
                j += 1
            if j - i >= min_run:
                i = j
                continue
            out.extend(lines[i:j])
            i = j
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


def split_base_description(description: str) -> tuple[str, str]:
    """Split existing YouTube description into (abstract_or_paper_info, links_or_footer).

    Finds where institute info / links block begins so timestamps can be inserted
    seamlessly between the paper's abstract/metadata and the link block.
    """
    if not description:
        return "", ""

    # Canonical assembly markers are checked first so re-assembly of an
    # already-assembled description cuts at the generated structure rather
    # than the trailing institute block (which would keep stale timestamps
    # and resource lines in paper_info and duplicate them).
    link_header_patterns = [
        r"(?i)\n*---\s*TIMESTAMPS",
        r"(?i)\n*---\s*RESOURCES",
        r"(?i)\n*---\s*ACTIVE INFERENCE",
        r"(?i)\n*(?:---+\s*)?(?:Active Inference Institute (?:information|links):?|Follow us:|Links & Resources:?)",
        r"(?i)\n*Website:\s*https?://",
    ]

    for pat in link_header_patterns:
        match = re.search(pat, description)
        if match:
            paper_info = _strip_timestamp_runs(description[:match.start()]).strip()
            link_block = description[match.start():].strip()
            return paper_info, link_block

    return _strip_timestamp_runs(description).strip(), ""


def assemble_video_description(
    *,
    base_description: str = "",
    chapters: list[ChapterEntry | dict[str, Any]] | None = None,
    video_id: str = "",
    github_transcript_url: str | None = None,
    slides_url: str | None = None,
    coda_url: str | None = None,
    category: str = "",
    series: str = "",
) -> str:
    """Assemble a complete, structured YouTube video description.

    Structure:
    1. Paper metadata / Abstract (preserved verbatim)
    2. Timestamps & Chapters (inserted right below abstract)
    3. Resources & GitHub Full Transcript links
    4. Canonical Active Inference Institute link block
    """
    sections: list[str] = []

    # 1. Paper metadata & abstract
    paper_info, _ = split_base_description(base_description)
    if paper_info:
        sections.append(paper_info)

    # 2. Timestamps & Chapters (inserted between abstract and links)
    if chapters:
        chapters_text = format_chapters_block(chapters)
        if chapters_text:
            sections.append(f"{CHAPTERS_MARKER_START}\n{chapters_text}")

    # 3. Resources & Transcript Links
    res_lines: list[str] = []
    transcript_url = github_transcript_url or (build_github_transcript_url(video_id) if video_id else None)
    if transcript_url:
        res_lines.append(f"📄 Full Transcript & Summary on GitHub:\n{transcript_url}")
    if slides_url:
        res_lines.append(f"📊 Presentation Slides:\n{slides_url}")
    if coda_url:
        res_lines.append(f"📋 Coda Workspace:\n{coda_url}")

    if res_lines:
        sections.append(f"{CHAPTERS_MARKER_END}\n" + "\n\n".join(res_lines))

    # 4. Standard updated Institute link block
    sections.append(STANDARD_INSTITUTE_LINKBLOCK)

    return "\n\n".join(sections)
