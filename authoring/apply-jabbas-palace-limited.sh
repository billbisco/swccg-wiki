#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Jabba's Palace Limited collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/jp-limited /tmp/jp-all; mkdir -p /tmp/jp-limited'
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/jp-all/
docker exec swccg_wiki sh -c 'cp /tmp/jp-all/Jabbas-Palace-*.png /tmp/jp-limited/'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" /tmp/jp-limited

echo "== edit Jabba's Palace Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin "Jabba's Palace Limited" \
  < "$ROOT/pages/Jabbas_Palace_Limited.wiki"

echo "== redirect Jabba's Palace =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin "Jabba's Palace" \
  < "$ROOT/pages/Jabbas_Palace.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== edit Sets =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Sets' \
  < "$ROOT/pages/Sets.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in "Jabba's Palace Limited" "Jabba's Palace" "Main Page" "Sets"; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE Jabba's Palace Limited"
