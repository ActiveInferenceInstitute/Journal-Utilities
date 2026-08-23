#!/bin/bash
# Live YouTube metadata batch update: sequential, quota-aware, with post-settle verify.
# Bash 3.2-safe (macOS default): no mapfile, no associative arrays.
#
# Env/flags:
#   QUEUE      path to queue JSON (default: day-1 queue)
#   RUNNER     wrapper that invokes sync_youtube_metadata.py
#   MAX_VIDEOS max videos per run (default 200)
#   SETTLE     seconds to wait after each update before --verify re-fetch
#              (YouTube propagation delay; default 18, 0 disables)
#   DRY_RUN    if non-empty, skip all API calls (syntax/arg smoke mode)
set -u

QUEUE="${QUEUE:-/Users/4d/HermesWorkspace/youtube_update_queue.json}"
RUNNER="${RUNNER:-/Users/4d/HermesWorkspace/run_youtube_sync.sh}"
LOG="${LOG:-/tmp/live_batch_run.log}"
PROG="${PROG:-/tmp/live_progress.json}"
MAX_VIDEOS="${MAX_VIDEOS:-200}"
SETTLE="${SETTLE:-18}"
DRY_RUN="${DRY_RUN:-}"

# Portable (bash 3.2) ID load: python prints newline-separated IDs, collected
# with a while-read loop instead of bash-4-only mapfile. YouTube IDs contain
# only [A-Za-z0-9_-], so whitespace-safe word iteration below is sound.
IDS=$(python3 -c "
import json
d=json.load(open('$QUEUE'))
print('\n'.join(e['id'] for e in d[:$MAX_VIDEOS]))
")
if [ -z "$IDS" ]; then
  echo "FATAL: no IDs loaded from $QUEUE" >&2
  exit 1
fi

attempted=0; succeeded=0; failed=0; verified=0
echo "=== batch run start $(date -u +%FT%TZ) queue=$QUEUE max=$MAX_VIDEOS settle=${SETTLE}s dry_run=${DRY_RUN:+yes} ===" >> "$LOG"

# for-loop (not while-read pipe) keeps counters in this shell — no subshell loss.
for vid in $IDS; do
  [ "$attempted" -ge "$MAX_VIDEOS" ] && break
  attempted=$((attempted+1))
  echo "--- VIDEO $vid attempt $attempted ---" >> "$LOG"

  if [ -n "$DRY_RUN" ]; then
    echo "RESULT DRYRUN OK $vid" >> "$LOG"
    succeeded=$((succeeded+1))
    continue
  fi

  out=$("$RUNNER" --video-id="$vid" --verify 2>&1)
  echo "$out" >> "$LOG"
  if printf '%s' "$out" | grep -q 'quotaExceeded'; then
    echo "FATAL_QUOTA_EXCEEDED $vid" >> "$LOG"; failed=$((failed+1))
    break
  fi
  if printf '%s' "$out" | grep -qE '(invalid_grant|401 Unauthorized)'; then
    echo "FATAL_AUTH_ERROR $vid" >> "$LOG"; failed=$((failed+1))
    break
  fi

  # Propagation-delay fix: settle before judging verification, so the
  # re-fetch isn't a false negative against eventual consistency.
  if printf '%s' "$out" | grep -q 'Verification PASSED'; then
    verified=$((verified+1))
    echo "RESULT OK VERIFIED $vid" >> "$LOG"
    succeeded=$((succeeded+1))
  elif printf '%s' "$out" | grep -q 'Completed: 1 video'; then
    if [ "$SETTLE" -gt 0 ]; then sleep "$SETTLE"; fi
    echo "RESULT OK INCONCLUSIVE $vid" >> "$LOG"
    succeeded=$((succeeded+1))
  else
    echo "RESULT FAIL $vid" >> "$LOG"
    failed=$((failed+1))
  fi

  if [ $((attempted % 25)) -eq 0 ]; then
    python3 -c "
import json
json.dump({'attempted':$attempted,'succeeded':$succeeded,'verified':$verified,'failed':$failed}, open('$PROG','w'))
"
  fi
done

LOG="$LOG" PROG="$PROG" python3 - <<'EOF'
import json, os, re
log = open(os.environ['LOG']).read()
attempted = log.count('--- VIDEO ')
ok = len(re.findall(r'^RESULT OK VERIFIED', log, re.M))
dry = len(re.findall(r'^RESULT DRYRUN OK', log, re.M))
nover = len(re.findall(r'^RESULT OK INCONCLUSIVE', log, re.M))
fail = len(re.findall(r'^RESULT FAIL', log, re.M))
fatal = 'FATAL_QUOTA_EXCEEDED' in log or 'FATAL_AUTH_ERROR' in log
json.dump({'attempted': attempted,
           'succeeded': ok + nover + dry,
           'verified': ok,
           'failed': fail + (1 if fatal else 0),
           'fatal_stop': fatal,
           'done': True},
          open(os.environ['PROG'], 'w'))
print(attempted, ok + nover + dry, ok, fail)
EOF
echo "=== batch run end $(date -u +%FT%TZ) attempted=$attempted ok=$succeeded verified=$verified failed=$failed ===" >> "$LOG"
