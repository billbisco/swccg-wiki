#!/bin/bash
# Apply 2014 World Championship hub, PDF scans, and first transcription slice.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-worlds.tgz" ]; then
  tar xzf "$ROOT/y2014-worlds.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-worlds-titles.tsv}"
SUMMARY="${2:-2014 World Championship hub and published decks}"

echo "== importImages PDFs =="
if [ -d "$ROOT/y2014-worlds-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2014-worlds-media
  docker cp "$ROOT/y2014-worlds-media/." swccg_wiki:/tmp/y2014-worlds-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2014 World Championship decklist scans" \
    --extensions=pdf \
    /tmp/y2014-worlds-media || true
  echo "== importImages PNG scans =="
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2014 World Championship decklist page scans" \
    --extensions=png \
    /tmp/y2014-worlds-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
Formats
Championships
2014 World Championship
Legacy Open
Category:2014
Emil Wallin
Brian Terwilliger
Chris Terwilliger
Matthew Harrison-Trainor
Greg Shaw
Matt Sokol
Angelo Consoli
Aaron Kingery
Brian Twigg
Chris Twigg
EOF
echo APPLY-2014-WORLDS-DONE
