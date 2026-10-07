#!/bin/bash
# Embed 2014 Worlds PDF page rasters on first-slice decks; fix VB dests + Jawa counterparts.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-deck-fix.tgz" ]; then
  tar xzf "$ROOT/y2014-deck-fix.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-deck-fix-titles.tsv}"
SUMMARY="${2:-2014 Worlds PDF page scans, Virtual Block dests, Coruscant Jawa counterparts}"

echo "== importImages PNG scans =="
if [ -d "$ROOT/y2014-worlds-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2014-deck-scans
  docker exec swccg_wiki sh -c 'rm -rf /tmp/y2014-deck-scans; mkdir -p /tmp/y2014-deck-scans'
  docker cp "$ROOT/y2014-worlds-media/." swccg_wiki:/tmp/y2014-deck-scans/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2014 World Championship decklist page scans" \
    --extensions=png \
    /tmp/y2014-deck-scans || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo APPLY-2014-DECK-FIX-DONE
