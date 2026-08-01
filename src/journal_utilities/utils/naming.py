"""
Deterministic, filesystem-safe names derived from video titles.

Used for journal items that have no series numbering (Other/ one-offs):
the slug is generated once at item creation and recorded as the item name;
the video id in metadata.json parts[] stays authoritative for all lookups.
"""

import re
import unicodedata

MAX_SLUG_LEN = 60


def slugify_title(title: str, max_len: int = MAX_SLUG_LEN) -> str:
    """
    Turn a video title into a stable directory-safe slug.

    ASCII letters/digits/underscore only (checkout-safe on every platform),
    accents folded, '&' becomes 'and', capped at max_len on a word boundary.
    Returns '' for titles with no usable characters — callers fall back to
    the video id.
    """
    text = unicodedata.normalize("NFKD", title or "").replace("&", " and ")
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
    if len(text) > max_len:
        cut = text[:max_len]
        # Prefer cutting at a word boundary (the previous underscore); when the
        # slice has no underscore at all (one very long token), hard-truncate
        # instead of collapsing the entire slug to "".
        text = cut.rsplit("_", 1)[0] if "_" in cut else cut
    return text.strip("_")
