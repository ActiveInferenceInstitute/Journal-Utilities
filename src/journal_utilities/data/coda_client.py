"""
Coda (Superhuman Docs) API client for fetching table rows.

Coda was renamed Superhuman Docs on 2026-07-08; the v1 endpoints at
``coda.io/apis/v1`` continue to work and ``docs.superhuman.com`` is accepted
as an alternative base. Base URL is configurable via ``CODA_API_BASE``.
Uses stdlib ``urllib`` only — no new dependencies.
"""

import json
import logging
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_BASE = "https://coda.io/apis/v1"
DOC_ID = "TwB_SP81yq"
TABLE_ID = "grid-cjvFiXp3a3"
PAGE_LIMIT = 200
MAX_RETRIES = 3


class CodaAuthError(RuntimeError):
    """Raised when no API token is available."""


def fetch_table_rows(
    doc_id: str = DOC_ID,
    table_id: str = TABLE_ID,
    token: Optional[str] = None,
    base_url: Optional[str] = None,
    limit: int = PAGE_LIMIT,
) -> list[dict]:
    """Fetch all rows of a table, following nextPageLink pagination."""
    token = token or os.environ.get("CODA_API_TOKEN", "")
    if not token:
        raise CodaAuthError("CODA_API_TOKEN is not set")
    base = (base_url or os.environ.get("CODA_API_BASE", DEFAULT_BASE)).rstrip("/")
    url = f"{base}/docs/{doc_id}/tables/{table_id}/rows?limit={limit}&useColumnNames=true"

    items: list[dict] = []
    page = 0
    while url:
        page += 1
        data = _get_json(url, token)
        batch = data.get("items", [])
        items.extend(batch)
        logger.info("coda: page %d -> %d rows (total %d)", page, len(batch), len(items))
        url = data.get("nextPageLink")
    return items


def _get_json(url: str, token: str) -> dict:
    for attempt in range(MAX_RETRIES + 1):
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < MAX_RETRIES:
                wait = 2 ** (attempt + 1)
                logger.warning("coda: 429 rate-limited, retrying in %ds", wait)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("unreachable")


def load_rows(
    snapshot_path: Path,
    cache_path: Path,
    fetch: bool = True,
) -> tuple[list[dict], str]:
    """
    Return (rows, source_label).

    Tries a live API fetch (cached to ``cache_path``) when ``fetch`` is true;
    falls back to an existing cache, then to the checked-in snapshot.
    """
    if fetch:
        try:
            items = fetch_table_rows()
            cache_path.write_text(
                json.dumps({"items": items}, ensure_ascii=False), encoding="utf-8"
            )
            return items, f"api ({len(items)} rows, cached to {cache_path.name})"
        except CodaAuthError as exc:
            logger.warning("coda fetch skipped: %s", exc)
        except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
            logger.warning("coda fetch failed: %s", exc)
    if cache_path.exists():
        items = json.loads(cache_path.read_text(encoding="utf-8")).get("items", [])
        return items, f"cache {cache_path.name} ({len(items)} rows)"
    items = json.loads(snapshot_path.read_text(encoding="utf-8")).get("items", [])
    return items, f"snapshot {snapshot_path.name} ({len(items)} rows — one page, coverage reduced)"
