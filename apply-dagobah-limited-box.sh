#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Dagobah Limited owner booster box as set image"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/dag-box; mkdir -p /tmp/dag-box'
docker cp "$ROOT/encyclopedia/upload/Dagobah-Limited-box.png" swccg_wiki:/tmp/dag-box/Dagobah-Limited-box.png
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" /tmp/dag-box

echo "== edit Dagobah Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Dagobah Limited' \
  < "$ROOT/pages/Dagobah_Limited.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'Dagobah Limited' 'Dagobah' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE Dagobah Limited box"
