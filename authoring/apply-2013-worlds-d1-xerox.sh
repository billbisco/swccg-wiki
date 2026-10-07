#!/bin/bash
# Apply 2013 Worlds Day 1 Xerox leftover: Cellucci DS, Gardner, Littauer, Way.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-worlds-d1-xerox.tgz" ]; then
  tar xzf "$ROOT/y2013-worlds-d1-xerox.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-worlds-d1-xerox-titles.tsv}"
SUMMARY="${2:-2013 Worlds Day 1 Xerox Cellucci DS Gardner Littauer Way}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
if [ -d "$ROOT/y2013-worlds-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-worlds-d1-xerox
  docker cp "$ROOT/y2013-worlds-media/." swccg_wiki:/tmp/y2013-worlds-d1-xerox/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 World Championship Day 1 Xerox page scans" \
    --extensions=png \
    /tmp/y2013-worlds-d1-xerox || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
cut -f1 "$TSV" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 World Championship
Category:2013
Stephen Cellucci
Jeremy Gardner
Ross Littauer
Nathan Way
Legacy Open
EOF
echo APPLY-2013-WORLDS-D1-XEROX-DONE
