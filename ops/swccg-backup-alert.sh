#!/bin/bash
# OnFailure helper for swccg-backup.service. No AI, no tokens in logs.
# Notify Bill only when the nightly job failed to do useful work.
# A non-zero exit that still completed backup tasks (the known source-inventory
# failures, swccg-guild/work#625) is logged and not pushed to the phone.
set -euo pipefail
LOG=/var/log/swccg-backup-alert.log
STATE=/var/lib/swccg-ops/backup-state.json
NOTIFY=/usr/local/sbin/swccg-ntfy-send
umask 077
mkdir -p "$(dirname "$LOG")"
result=$(systemctl show swccg-backup.service --value --property=Result --no-pager || true)
status=$(systemctl show swccg-backup.service --value --property=ExecMainStatus --no-pager || true)
started=$(systemctl show swccg-backup.service --value --property=ExecMainStartTimestamp --no-pager || true)
exited=$(systemctl show swccg-backup.service --value --property=ExecMainExitTimestamp --no-pager || true)
completed=""
inventory=""
if [ -f "$STATE" ]; then
  completed=$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("completed_tasks") or d.get("completed") or 0)' "$STATE" 2>/dev/null || true)
  inventory=$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("source_inventory_failures") or 0)' "$STATE" 2>/dev/null || true)
fi
# Do not print state contents beyond these counters.
msg="swccg-backup result=${result} exit=${status} start=${started} end=${exited} completed_tasks=${completed:-?} source_inventory_failures=${inventory:-?}"
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $msg" >> "$LOG"
# Useful work happened if some tasks completed. Known #625 exits 1 in that case.
if [ "${status:-1}" != "0" ] && [ "${completed:-0}" != "0" ] && [ "${completed:-0}" != "?" ]; then
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) no phone alert (completed work; non-zero exit, see work#625/#1323)" >> "$LOG"
  exit 0
fi
if [ "${status:-1}" = "0" ]; then
  exit 0
fi
body=$(printf '%s\n\nSee journalctl -u swccg-backup.service and work#1323.\n' "$msg")
if [ -x "$NOTIFY" ]; then
  # Subject is $1; body on stdin. The helper reads the topic itself.
  printf '%s' "$body" | "$NOTIFY" "swccg-backup failed" || echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) notify command failed" >> "$LOG"
else
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) notify helper missing; logged only" >> "$LOG"
fi
