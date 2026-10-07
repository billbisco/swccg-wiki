#!/bin/bash
# A New Hope Limited collecting hub + rename from A New Hope.
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="A New Hope Limited collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/anh-limited; mkdir -p /tmp/anh-limited'
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/anh-all/
docker exec swccg_wiki sh -c 'mkdir -p /tmp/anh-limited; cp /tmp/anh-all/ANH-*.png /tmp/anh-limited/'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" --overwrite /tmp/anh-limited \
  || docker exec swccg_wiki php maintenance/run.php importImages \
       --user=Admin --comment="$COMMENT" /tmp/anh-limited

echo "== edit A New Hope Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'A New Hope Limited' \
  < "$ROOT/pages/A_New_Hope_Limited.wiki"

echo "== redirect A New Hope =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'A New Hope' \
  < "$ROOT/pages/A_New_Hope.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== edit Sets =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Sets' \
  < "$ROOT/pages/Sets.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'A New Hope Limited' 'A New Hope' 'Main Page' 'Sets'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE A New Hope Limited"
