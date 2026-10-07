#!/bin/bash
# Apply 2013 MPC Smith last-name collision leftover.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-mpc-smith.tgz" ]; then
  tar xzf "$ROOT/y2013-mpc-smith.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-mpc-smith-titles.tsv}"
SUMMARY="${2:-2013 MPC Smith last-name collision retarget}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
cut -f1 "$TSV" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo APPLY-2013-MPC-SMITH-DONE
