#!/bin/bash
# Apply 2013 MPC Day 1 Joe Pinto Xerox leftover.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-mpc-pinto.tgz" ]; then
  tar xzf "$ROOT/y2013-mpc-pinto.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-mpc-pinto-titles.tsv}"
SUMMARY="${2:-2013 MPC Day 1 Joe Pinto Xerox}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
if [ -d "$ROOT/y2013-mpc-pinto-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-mpc-pinto-media
  docker cp "$ROOT/y2013-mpc-pinto-media/." swccg_wiki:/tmp/y2013-mpc-pinto-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Match Play Championship Joe Pinto scans" \
    --extensions=png \
    /tmp/y2013-mpc-pinto-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
2013 Match Play Championship
2013 Match Play Championship Day 1 Joe Pinto LS Plead My Case To The Senate
2013 Match Play Championship Day 1 Joe Pinto DS Carbon Chamber Testing
Joe Pinto
EOF
echo APPLY-2013-MPC-PINTO-DONE
