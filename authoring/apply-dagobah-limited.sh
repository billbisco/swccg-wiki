#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Dagobah Limited collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/dagobah-limited; mkdir -p /tmp/dagobah-limited'
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/dag-all/
docker exec swccg_wiki sh -c 'mkdir -p /tmp/dagobah-limited; cp /tmp/dag-all/Dagobah-*.png /tmp/dagobah-limited/'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" --overwrite /tmp/dagobah-limited \
  || docker exec swccg_wiki php maintenance/run.php importImages \
       --user=Admin --comment="$COMMENT" /tmp/dagobah-limited

echo "== edit Dagobah Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Dagobah Limited' \
  < "$ROOT/pages/Dagobah_Limited.wiki"

echo "== redirect Dagobah =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Dagobah' \
  < "$ROOT/pages/Dagobah.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== edit Sets =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Sets' \
  < "$ROOT/pages/Sets.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'Dagobah Limited' 'Dagobah' 'Main Page' 'Sets'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE Dagobah Limited"
