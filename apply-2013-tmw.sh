#!/bin/bash
# Apply 2013 Texas Mini Worlds hub and Day 1 typed Reisch lists.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-tmw.tgz" ]; then
  tar xzf "$ROOT/y2013-tmw.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-tmw-titles.tsv}"
SUMMARY="${2:-2013 Texas Mini Worlds Day 1 typed leftover}"

echo "== importImages =="
if [ -d "$ROOT/y2013-tmw-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-tmw-media
  docker cp "$ROOT/y2013-tmw-media/." swccg_wiki:/tmp/y2013-tmw-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Texas Mini Worlds decklist scans" \
    --extensions=pdf \
    /tmp/y2013-tmw-media || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Texas Mini Worlds decklist page scans" \
    --extensions=png \
    /tmp/y2013-tmw-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 Texas Mini Worlds
Category:2013
Nick Reisch
Aaron Nelson
Robbie Hendon
Greg Shaw
Mike Richards
Evan Kirkpatrick
James Barnes
Bobby Hilbun
JW Millet
Steve Skilton
Steve Izzo
Brian Herold
Blake Huffman
John Anderson
Barry Alperstein
Amar Banger
Allen Gamble
Olaf Schroeder
Matt Wehner
Legacy Open
EOF
echo APPLY-2013-TMW-DONE
