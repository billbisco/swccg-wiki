#!/bin/bash
# Recropped easy encyclopedia photos (ANH + Dagobah Revised box).
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Easy crop recrop: drop encyclopedia chrome"

echo "== importImages v2 =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/recrop-v2 /tmp/recrop-all; mkdir -p /tmp/recrop-v2'
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/recrop-all/
docker exec swccg_wiki sh -c 'cp /tmp/recrop-all/*-v2.png /tmp/recrop-v2/'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" /tmp/recrop-v2

echo "== edit A New Hope Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'A New Hope Limited' \
  < "$ROOT/pages/A_New_Hope_Limited.wiki"

echo "== edit Dagobah Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Dagobah Limited' \
  < "$ROOT/pages/Dagobah_Limited.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'A New Hope Limited' 'Dagobah Limited' 'Dagobah' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE recrop easy v2"
