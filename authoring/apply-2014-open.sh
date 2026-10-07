#!/bin/bash
# Apply 2014 post-reset Open hubs, decks, player tables, List rows.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-open.tgz" ]; then
  tar xzf "$ROOT/y2014-open.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-open-titles.tsv}"
SUMMARY="${2:-2014 Open tournament hubs and published decks}"
bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== FlaggedRevs ReviewTitles =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
European Championships
Formats
2014 Philadelphia Premiere Event
2014 European Championship Reset Beta
2014 World Championship Reset Beta
2014 World Championship
Category:2014
Chris Gogolen
Cedrik Vanderhaegen
Keith Brown
Casper Jørgensen
EOF
echo APPLY-2014-OPEN-DONE
