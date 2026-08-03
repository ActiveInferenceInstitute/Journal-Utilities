#!/usr/bin/env bash
# Resumable watchdog for a long-running journal series translation run.
# Safe to invoke repeatedly: it takes a portable atomic mkdir lock so concurrent
# invocations never double-translate the same file, runs the idempotent
# translator (which skips existing <lang>.srt files), prints a concise status.
set -u

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
JOURNAL="${JOURNAL_DIR:-$REPO/../ActiveInferenceJournal}"
SERIES="${SERIES:-TextbookGroup}"
LOCKDIR="$REPO/.translate_tb_watchdog.lock.d"

# Take an exclusive lock via atomic mkdir; release it on exit.
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  echo "[watchdog] another run in progress, skipping this tick"
  exit 0
fi
trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT

cd "$REPO" || exit 1

before=$(find "$JOURNAL/data/video/activeinferenceinstitute/$SERIES" -path '*/translations/*.srt' 2>/dev/null | wc -l | tr -d ' ')

out=$(python3 scripts/translate_subtitles.py --journal "$JOURNAL" --series "$SERIES" 2>&1)
code=$?

after=$(find "$JOURNAL/data/video/activeinferenceinstitute/$SERIES" -path '*/translations/*.srt' 2>/dev/null | wc -l | tr -d ' ')

echo "[watchdog] exit=$code before=$before after=$after"
printf '%s\n' "$out" | grep -E '^Done\.|skipped [0-9]+ duplicate' | tail -2
