#!/usr/bin/env python3
"""
CLI utility to compile ActiveInferenceJournal into a static GitHub Pages bundle.

Usage:
    python scripts/build_pages_site.py --journal ../ActiveInferenceJournal --output dist
"""

import argparse
import sys
from pathlib import Path

# Add src to path
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from journal_utilities.site.builder import build_site  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build static interactive website for ActiveInferenceJournal (GitHub Pages)."
    )
    parser.add_argument(
        "--journal",
        type=Path,
        default=REPO.parent / "ActiveInferenceJournal",
        help="Path to ActiveInferenceJournal repo root (default: ../ActiveInferenceJournal)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO / "dist",
        help="Output directory for generated static site (default: dist)",
    )
    parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Do not clean output directory before building",
    )

    args = parser.parse_args()

    if not args.journal.exists():
        print(f"Error: Journal directory not found at {args.journal}", file=sys.stderr)
        return 1

    print(f"Building static website from {args.journal} -> {args.output}...")
    result = build_site(
        journal_dir=args.journal,
        output_dir=args.output,
        clean=not args.no_clean,
    )
    print(f"✓ Static site build complete: {result['items_processed']} items generated in {result['output_dir']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
