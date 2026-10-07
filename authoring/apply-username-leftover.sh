#!/bin/bash
# Apply leftover: Username on Xerox decklists + Reid Smith retarget.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y-username-leftover.tgz" ]; then
  tar xzf "$ROOT/y-username-leftover.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y-username-leftover-titles.tsv}"
SUMMARY="${2:-Username on Xerox decklists; 3MW0J8 is Reid Smith}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" apply-username-leftover.sh || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
cut -f1 "$TSV" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo APPLY-USERNAME-LEFTOVER-DONE
