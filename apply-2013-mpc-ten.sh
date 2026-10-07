#!/bin/bash
# Apply 2013 MPC Day 1 Fink Kinser Tuan Le Mack Nelson Nguyen O'Hara Paragano Richards Sharer leftover.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-mpc-ten.tgz" ]; then
  tar xzf "$ROOT/y2013-mpc-ten.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-mpc-ten-titles.tsv}"
SUMMARY="${2:-2013 MPC Day 1 Fink Kinser TuanLe Mack Nelson Nguyen OHara Paragano Richards Sharer}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
if [ -d "$ROOT/y2013-mpc-ten-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-mpc-ten-media
  docker cp "$ROOT/y2013-mpc-ten-media/." swccg_wiki:/tmp/y2013-mpc-ten-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Match Play Championship Fink Kinser Tuan Le Mack Nelson Nguyen OHara Paragano Richards Sharer scans" \
    --extensions=png \
    /tmp/y2013-mpc-ten-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
cut -f1 "$TSV" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo APPLY-2013-MPC-TEN-DONE
