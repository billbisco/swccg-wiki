#!/bin/bash
# Apply leftover dest: 2014 Worlds Day 2 Brian Billetta DS Gyriadan -> Garindan.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-billetta-garindan.tgz" ]; then
  tar xzf "$ROOT/y2014-billetta-garindan.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-billetta-garindan-titles.tsv}"
SUMMARY="${2:-2014 Worlds Billetta DS Gyriadan dested Garindan}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" apply-2014-billetta-garindan.sh || true
chmod +x apply-tsv.sh apply-2014-billetta-garindan.sh

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
cut -f1 "$TSV" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo APPLY-2014-BILLETTA-GARINDAN-DONE
