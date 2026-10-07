#!/bin/bash
# Apply 2015–2016 hubs, decks, player tables, List rows. edit + FlaggedRevs + purge.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2015-2016.tgz" ]; then
  tar xzf "$ROOT/y2015-2016.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2015-2016-titles.tsv}"
SUMMARY="${2:-2015-2016 tournament hubs and published decks}"
bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
European Championships
Formats
2016 Texas Mini Worlds
2016 European Championship
2016 World Championship
2016 Endor Grand Prix
2016 Match Play Championship
2015 Texas Mini Worlds
2015 European Championship
2015 World Championship
2015 Match Play Championship
2015 San Diego Grand Prix
Category:2015
Category:2016
Kevin Shannon
Joe Olson
Tom Haid
Brian Fred
Justin Desai
Emil Wallin
Ziemowit Skwara
Tom Kelly
Steve Baroni
EOF
echo APPLY-2015-2016-DONE
