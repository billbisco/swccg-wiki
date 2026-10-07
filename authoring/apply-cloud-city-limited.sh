#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Cloud City Limited collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/cc-limited /tmp/cc-all; mkdir -p /tmp/cc-limited'
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/cc-all/
docker exec swccg_wiki sh -c 'cp /tmp/cc-all/Cloud-City-*.png /tmp/cc-limited/'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" /tmp/cc-limited

echo "== edit Cloud City Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Cloud City Limited' \
  < "$ROOT/pages/Cloud_City_Limited.wiki"

echo "== redirect Cloud City =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Cloud City' \
  < "$ROOT/pages/Cloud_City.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== edit Sets =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Sets' \
  < "$ROOT/pages/Sets.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'Cloud City Limited' 'Cloud City' 'Main Page' 'Sets'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE Cloud City Limited"
