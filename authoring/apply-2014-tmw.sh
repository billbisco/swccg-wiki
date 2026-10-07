#!/bin/bash
# Apply 2014 Texas Mini Worlds hub and Day 2 typed lists.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-tmw.tgz" ]; then
  tar xzf "$ROOT/y2014-tmw.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-tmw-titles.tsv}"
SUMMARY="${2:-2014 Texas Mini Worlds typed lists}"

echo "== importImages =="
if [ -d "$ROOT/y2014-tmw-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2014-tmw-media
  docker cp "$ROOT/y2014-tmw-media/." swccg_wiki:/tmp/y2014-tmw-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2014 Texas Mini Worlds decklist scans" \
    --extensions=pdf \
    /tmp/y2014-tmw-media || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2014 Texas Mini Worlds decklist page scans" \
    --extensions=png \
    /tmp/y2014-tmw-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2014 Texas Mini Worlds
Category:2014
Nick Reisch
Paul Bonsall
Greg Shaw
Ganden Yanaga
Steve Skilton
Chris Schoenthal
Amar Banger
John Anderson
Mike Richards
James Barnes
Olaf Schroeder
Thomas Whaley
Legacy Open
EOF
echo APPLY-2014-TMW-DONE
