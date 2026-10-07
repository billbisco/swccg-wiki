#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2008-worlds.tgz" ]; then
  tar xzf "$ROOT/y2008-worlds.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2008-worlds-titles.tsv}"
SUMMARY="${2:-2008 World Championship Day 3 Frafjord DS + hub}"

mkdir -p "$ROOT/y2008-worlds-media"
cp -n /tmp/pc-pre2014-pdfs/2008_Worlds_D1.pdf "$ROOT/y2008-worlds-media/2008 Worlds Day 1.pdf" 2>/dev/null || true
cp -n /tmp/pc-pre2014-pdfs/2008_Worlds_D2.pdf "$ROOT/y2008-worlds-media/2008 Worlds Day 2.pdf" 2>/dev/null || true
cp -n /tmp/pc-pre2014-pdfs/2008_Worlds_D3.pdf "$ROOT/y2008-worlds-media/2008 Worlds Day 3.pdf" 2>/dev/null || true
cp -n /tmp/pc-pre2014-pdfs/2008_Worlds_Team.pdf "$ROOT/y2008-worlds-media/2008 Worlds Team.pdf" 2>/dev/null || true

echo "== importImages =="
docker exec swccg_wiki mkdir -p /tmp/y2008-worlds-media
docker cp "$ROOT/y2008-worlds-media/." swccg_wiki:/tmp/y2008-worlds-media/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="2008 World Championship PDFs" --extensions=pdf \
  /tmp/y2008-worlds-media || true
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="2008 World Championship page scans" --extensions=png \
  /tmp/y2008-worlds-media || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true
bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
cut -f1 "$TSV" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PEOF' || true
List of SWCCG tournaments
2008 World Championship
Category:2008
Tom Frafjord
Virtual Sets (2002-2009)
Legacy Open
PEOF
echo APPLY-2008-WORLDS-DONE