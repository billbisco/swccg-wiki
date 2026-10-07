#!/bin/bash
# Apply 2013 SoCal Grand Prix hub and typed lists.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-socal.tgz" ]; then
  tar xzf "$ROOT/y2013-socal.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-socal-titles.tsv}"
SUMMARY="${2:-2013 SoCal Grand Prix hub and typed dest}"

echo "== importImages =="
if [ -d "$ROOT/y2013-socal-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-socal-media
  docker cp "$ROOT/y2013-socal-media/." swccg_wiki:/tmp/y2013-socal-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 SoCal Grand Prix decklist scans" \
    --extensions=pdf \
    /tmp/y2013-socal-media || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 SoCal Grand Prix decklist page scans" \
    --extensions=png \
    /tmp/y2013-socal-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 SoCal Grand Prix
Category:2013
Phil Aasen
John Anderson
Clayton Atkin
Brian Herold
Matthew Harrison-Trainor
Anthony Massung
Joe Olson
Kevin Shannon
Greg Shaw
Steve Skilton
Reid Smith
Matt Thornton
Ganden Yanaga
Legacy Open
EOF
echo APPLY-2013-SOCAL-DONE
