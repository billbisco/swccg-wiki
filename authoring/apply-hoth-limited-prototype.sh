#!/bin/bash
# Prototype set-hub packaging + memorabilia on Hoth Limited.
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Hoth Limited packaging prototype: box, pack, encyclopedia memorabilia"

echo "== importImages =="
docker exec swccg_wiki mkdir -p /tmp/hoth-limited-proto
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/hoth-limited-proto/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" --overwrite /tmp/hoth-limited-proto \
  || docker exec swccg_wiki php maintenance/run.php importImages \
       --user=Admin --comment="$COMMENT" /tmp/hoth-limited-proto

echo "== edit Hoth Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Hoth Limited' \
  < "$ROOT/pages/set-hubs/Hoth.wiki"

echo "== edit Main Page tile =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'Hoth Limited' 'Hoth' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE Hoth Limited prototype"
