#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
tar -xf /tmp/y2022-canon-players.tar
bash "$ROOT/apply-tsv.sh" "$ROOT/y2022-canon-players.tsv" "canonical player names 2022-2024 hubs and dest stubs"
echo "== extra purge =="
printf '%s\n' \
  "List of SWCCG tournaments" \
  "Bill Kafer" \
  "Pär Birgander" \
  "Ben Butterworth" \
  "2023 Seventh Annual GEMPC" \
  "2023 U.S. National Championship" \
  "2024 World Championship" \
  "2024 Eclipse Major" \
  "2024 Supreme Southern Showdown" \
  "2022 PC20 Tournament" \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo CANON_PLAYERS_DONE
