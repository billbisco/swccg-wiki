#!/bin/bash
# Apply Cite-beside-scan decks + Virtual Legacy hub + import Final Master PDFs.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"

echo "== extra-settings MaxUploadSize =="
grep -n 'wgMaxUploadSize\|wgCacheEpoch' "$ROOT/extra-settings.php"

echo "== reload PHP (graceful) =="
if docker exec swccg_wiki apachectl graceful; then
  echo "apachectl graceful ok"
elif docker exec swccg_wiki apache2ctl graceful; then
  echo "apache2ctl graceful ok"
else
  echo "graceful failed; docker restart swccg_wiki"
  docker restart swccg_wiki
  sleep 3
fi

echo "== live MaxUploadSize =="
echo 'echo "MaxUploadSize="; var_export( $wgMaxUploadSize ); echo "\n";' \
  | docker exec -i swccg_wiki php maintenance/run.php eval

echo "== importImages Virtual Legacy Final Master PDFs =="
docker exec swccg_wiki rm -rf /tmp/vl-pdfs || true
docker cp /tmp/vl-pdfs swccg_wiki:/tmp/vl-pdfs
ls -l /tmp/vl-pdfs
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Host Virtual Legacy Final Master printable slips (DS/LS)" \
  /tmp/vl-pdfs \
  || docker exec swccg_wiki php maintenance/importImages.php \
    --user=Admin \
    --comment="Host Virtual Legacy Final Master printable slips (DS/LS)" \
    /tmp/vl-pdfs
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo "== ReviewTitles.php into maintenance =="
docker cp "$ROOT/ReviewTitles.php" swccg_wiki:/var/www/html/maintenance/ReviewTitles.php

echo "== apply TSV =="
bash "$ROOT/apply-tsv.sh" "$ROOT/_vl_scan_cite.tsv" "Cite-beside-scan Day 3 decks; Virtual Legacy era hub + Final Master PDFs"

echo "== force FlaggedRevs stable =="
# File: namespace is not FlaggedRevs; skip those titles.
# Pipe stdin into the maintenance script directly (run.php would consume it).
grep -v '^File:' "$ROOT/_vl_scan_cite.tsv" | cut -f1 \
  | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php

echo "== purge again =="
cut -f1 "$ROOT/_vl_scan_cite.tsv" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true

echo "APPLY_VL_DONE"
