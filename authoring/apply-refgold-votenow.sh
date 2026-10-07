#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
echo "== import Vote Now C1 + any new RG-C1 =="
docker exec swccg_wiki mkdir -p /tmp/rg-vn
docker cp "$ROOT/encyclopedia/upload/RG-C1-Vote-Now-Light.jpg" swccg_wiki:/tmp/rg-vn/
docker cp "$ROOT/encyclopedia/upload/RG-C1-Vote-Now-Dark.jpg" swccg_wiki:/tmp/rg-vn/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Category One buylist photos: Vote Now! Light and Dark" \
  /tmp/rg-vn || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
echo "== edit hub =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Forum post vs Category One vs Remastered; Vote Now C1 sides; YouTube and forum page sources" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold" || true
echo DONE refgold-votenow
