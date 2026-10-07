#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
tar -xf /tmp/y2022-remaining-players.tar
bash "$ROOT/apply-tsv.sh" "$ROOT/y2022-remaining-players.tsv" "2022 Nationals full names, missing Day 1 lists, and player stubs"
echo "== extra purge List + new players =="
printf '%s\n' \
  "List of SWCCG tournaments" \
  "Patrick Lima" \
  "Stephen Fulner" \
  "Category:2022" \
  "Category:2023" \
  "Category:2024" \
  "2022 U.S. National Championship" \
  "2022 Endor Grand Prix" \
  "2022 Sixth Annual GEMPC" \
  "2024 European Championship" \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo REMAINING_PLAYERS_DONE
