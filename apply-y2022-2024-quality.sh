#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
tar -xf /tmp/y2022-2024-quality.tar
bash "$ROOT/apply-tsv.sh" "$ROOT/y2022-2024-quality.tsv" "2022-2024 player stubs and last-name redirects"
echo "== extra purge List + year categories =="
printf '%s\n' \
  "List of SWCCG tournaments" \
  "Category:2022" \
  "Category:2023" \
  "Category:2024" \
  "2024 Online Retro Event for Charity" \
  "Patrick Lima" \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo QUALITY_DONE
