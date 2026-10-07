#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
echo "== import RG-F and RG-C1 =="
docker exec swccg_wiki mkdir -p /tmp/rg-src
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/rg-src/
docker exec swccg_wiki bash -lc 'mkdir -p /tmp/rg-src-only; cp /tmp/rg-src/RG-F-* /tmp/rg-src/RG-C1-* /tmp/rg-src-only/ 2>/dev/null || true; ls /tmp/rg-src-only | wc -l'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Reflections Gold source photos: forum Photobucket full-size and Category One buylist" \
  /tmp/rg-src-only || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
echo "== edit hub =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Label image columns by source: Forum post, Category One, Remastered" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold" || true
echo DONE refgold-sources
