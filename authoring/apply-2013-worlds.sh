#!/bin/bash
# Apply 2013 World Championship hub and Day 1 typed Cellucci Light list.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-worlds.tgz" ]; then
  tar xzf "$ROOT/y2013-worlds.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-worlds-titles.tsv}"
SUMMARY="${2:-2013 World Championship Day 1 typed Cellucci Light}"

echo "== importImages =="
if [ -d "$ROOT/y2013-worlds-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-worlds-media
  docker cp "$ROOT/y2013-worlds-media/." swccg_wiki:/tmp/y2013-worlds-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 World Championship decklist scans" \
    --extensions=pdf \
    /tmp/y2013-worlds-media || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 World Championship decklist page scans" \
    --extensions=png \
    /tmp/y2013-worlds-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 World Championship
Category:2013
Stephen Cellucci
Jeremy Gardner
Ross Littauer
Drew Powers
Nathan Way
Steve Baroni
Vikram Bali
Jonny Chu
Kevin Shannon
Reid Smith
Emil Wallin
Seth Acree
Matthew Harrison-Trainor
John Anderson
Casey Anis
Legacy Open
EOF
echo APPLY-2013-WORLDS-DONE
