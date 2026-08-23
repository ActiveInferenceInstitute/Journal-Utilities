#!/usr/bin/env python3
# Closed-Loop YouTube Metadata Synchronizer

import argparse
import json
import os
import logging
import sys
from pathlib import Path

# Repo paths
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
CHANNEL_VIDEOS = DATA_DIR / "output/channel_videos.json"
CHAPTERS_FILE = DATA_DIR / "input/video_chapters.json"
TRANSCRIPTS_DIR = DATA_DIR / "output/transcripts"

# Add InstituteOS source to sys.path if not installed in current venv
INSTITUTEOS_SRC = REPO_ROOT.parent.parent / "src"
if INSTITUTEOS_SRC.exists() and str(INSTITUTEOS_SRC) not in sys.path:
    sys.path.insert(0, str(INSTITUTEOS_SRC))

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("sync_youtube_metadata")


def derive_video_tags(raw_title: str, existing_tags: list[str] | None = None) -> list[str]:
    tags_set = set(existing_tags or [])
    tags_set.update(["Active Inference", "Active Inference Institute", "Neuroscience", "Free Energy Principle"])
    title_lower = raw_title.lower()
    if "livestream" in title_lower:
        tags_set.add("Active Inference Livestream")
    if "gueststream" in title_lower:
        tags_set.add("GuestStream")
    if "modelstream" in title_lower:
        tags_set.add("ModelStream")
    if "mathstream" in title_lower:
        tags_set.add("MathStream")
    if "symposium" in title_lower:
        tags_set.add("Symposium")
    if "textbook" in title_lower:
        tags_set.add("Textbook Group")

    sorted_tags = sorted(tags_set)
    final_tags = []
    total_len = 0
    for t in sorted_tags:
        if total_len + len(t) + 1 <= 480:
            final_tags.append(t)
            total_len += len(t) + 1
    return final_tags


def main() -> int:
    parser = argparse.ArgumentParser(description="Synchronize YouTube video metadata")
    parser.add_argument("--video-id", type=str, help="Single YouTube video ID to process")
    parser.add_argument("--limit", type=int, default=0, help="Max videos to process (0 = all)")
    parser.add_argument("--dry-run", action="store_true", help="Preview metadata changes without applying API updates")
    parser.add_argument("--verify", action="store_true", help="Re-fetch metadata from YouTube after update to verify")
    parser.add_argument("--llm-backend", choices=["none", "ollama", "openrouter"], default="none",
                        help="LLM backend to generate chapters from transcript JSON if missing")
    parser.add_argument("--llm-model", type=str, default=None, help="Model override for LLM chapter generation")
    args = parser.parse_args()

    from journal_utilities.youtube.metadata_formatter import (
        assemble_video_description,
        build_github_transcript_url,
    )

    try:
        from instituteos.extensions.integrations.youtube import YouTubeClient, YouTubeVideoSnippet
    except ImportError:
        logger.error("Could not import InstituteOS YouTube integration. Ensure instituteos is in PYTHONPATH.")
        return 1

    videos = []
    if CHANNEL_VIDEOS.exists():
        try:
            data = json.loads(CHANNEL_VIDEOS.read_text(encoding="utf-8"))
            videos = data.get("videos", [])
        except Exception as e:
            logger.warning("Error loading channel_videos.json: %s", e)

    chapters_map = {}
    if CHAPTERS_FILE.exists():
        try:
            chapters_map = json.loads(CHAPTERS_FILE.read_text(encoding="utf-8"))
        except Exception as e:
            logger.warning("Error loading video_chapters.json: %s", e)

    if args.video_id:
        targets = [v for v in videos if v.get("id") == args.video_id]
        if not targets:
            targets = [{"id": args.video_id, "title": f"Video {args.video_id}", "description": ""}]
    else:
        targets = videos

    if args.limit > 0:
        targets = targets[: args.limit]

    logger.info("Found %d target video(s) to evaluate.", len(targets))
    # Build client from standard env-var credential locations (same contract as
    # the InstituteOS YouTubeAdapter.connect config).
    client = YouTubeClient(
        client_secrets_path=os.environ.get("YOUTUBE_CLIENT_SECRETS"),
        token_path=os.environ.get("YOUTUBE_TOKEN_PATH"),
        api_key=os.environ.get("YOUTUBE_API_KEY"),
    )

    chapter_gen = None
    if args.llm_backend != "none":
        from journal_utilities.youtube.chapter_generator import ChapterGenerator
        chapter_gen = ChapterGenerator(backend=args.llm_backend, model=args.llm_model)

    updated_count = 0
    for i, v in enumerate(targets, 1):
        vid = v.get("id")
        if not vid:
            continue

        raw_title = v.get("title", "")
        raw_desc = v.get("description", "")
        existing_tags = v.get("tags", [])

        # 1. PULL
        live_snippet = None
        try:
            live_snippet = client.get_video_snippet(vid)
            if live_snippet:
                raw_title = live_snippet.title or raw_title
                raw_desc = live_snippet.description or raw_desc
                existing_tags = live_snippet.tags or existing_tags
        except Exception as e:
            logger.debug("Could not fetch live snippet for %s: %s", vid, e)

        # If raw_desc is empty and channel_videos.json did not have it, scrape via yt-dlp fallback
        if not raw_desc:
            try:
                import yt_dlp
                with yt_dlp.YoutubeDL({"quiet": True, "skip_download": True}) as ydl:
                    info = ydl.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
                    raw_title = info.get("title") or raw_title
                    raw_desc = info.get("description") or raw_desc
                    existing_tags = info.get("tags") or existing_tags
            except Exception as e:
                logger.debug("yt-dlp fallback info fetch failed for %s: %s", vid, e)

        # 2. CHAPTERS & TRANSCRIPTS
        chapters = chapters_map.get(vid, [])
        transcript_json_path = TRANSCRIPTS_DIR / f"{vid}.json"
        has_transcript = (TRANSCRIPTS_DIR / f"{vid}.txt").exists() or transcript_json_path.exists()

        if not chapters and transcript_json_path.exists() and chapter_gen is not None:
            logger.info("[%d/%d] Generating LLM chapters for %s via %s...", i, len(targets), vid, args.llm_backend)
            try:
                segments = json.loads(transcript_json_path.read_text(encoding="utf-8"))
                chapters = chapter_gen.generate_chapters(title=raw_title, transcript_segments=segments)
                if chapters:
                    logger.info("Generated %d chapters for %s", len(chapters), vid)
                    chapters_map[vid] = [{"start": c.start, "title": c.title} for c in chapters]
                    CHAPTERS_FILE.parent.mkdir(parents=True, exist_ok=True)
                    CHAPTERS_FILE.write_text(json.dumps(chapters_map, indent=2), encoding="utf-8")
            except Exception as e:
                logger.warning("LLM chapter generation failed for %s: %s", vid, e)

        new_description = assemble_video_description(
            base_description=raw_desc,
            chapters=chapters,
            video_id=vid,
            github_transcript_url=build_github_transcript_url(vid) if has_transcript else None,
        )
        new_tags = derive_video_tags(raw_title, existing_tags)

        snippet = YouTubeVideoSnippet(
            video_id=vid,
            title=raw_title,
            description=new_description,
            category_id=live_snippet.category_id if live_snippet else "27",
            tags=new_tags,
        )

        logger.info("[%d/%d] Target %s - Chapters: %d, Tags: %d, Transcript: %s",
                    i, len(targets), vid, len(chapters), len(new_tags), has_transcript)

        # 3. PUSH
        if args.dry_run:
            print(f"\n=================== DRY RUN PREVIEW: {vid} ===================")
            print(f"Title: {snippet.title}")
            print(f"Tags ({len(snippet.tags)}): {", ".join(snippet.tags)}")
            print("Description:")
            print(snippet.description)
            print("==============================================================\n")
            result = client.update_video_snippet(snippet, dry_run=True)
        else:
            result = client.update_video_snippet(snippet, dry_run=False)

        if not result.success:
            logger.error("Failed update for %s: %s", vid, result.error)
            continue

        updated_count += 1

        # 4. VERIFY (short sleep for YouTube propagation)
        if args.verify and not args.dry_run:
            import time as _time
            _time.sleep(5)
            logger.info("Verifying update on YouTube for %s...", vid)
            try:
                verified = client.get_video_snippet(vid)
                if verified and "--- RESOURCES & TRANSCRIPT ---" in verified.description:
                    logger.info("✓ Verification PASSED for %s", vid)
                else:
                    logger.warning("✗ Verification check inconclusive for %s", vid)
            except Exception as e:
                logger.warning("Verification read failed for %s: %s", vid, e)

    logger.info("Completed: %d video(s) processed successfully.", updated_count)
    return 0


if __name__ == "__main__":
    sys.exit(main())
