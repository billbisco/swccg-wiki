#!/bin/bash
# Premiere Limited collecting hub from Encyclopedia 3.2.
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Premiere Limited collecting: box, pack, starter, poster, sheets, printings"

echo "== importImages =="
docker exec swccg_wiki mkdir -p /tmp/premiere-collecting
docker exec swccg_wiki sh -c 'rm -rf /tmp/premiere-collecting; mkdir -p /tmp/premiere-collecting'
# Only Premiere-*.png from the upload dir on the host
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/premiere-collecting-all/
docker exec swccg_wiki sh -c 'mkdir -p /tmp/premiere-collecting; cp /tmp/premiere-collecting-all/Premiere-*.png /tmp/premiere-collecting/ 2>/dev/null || true'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" --overwrite /tmp/premiere-collecting \
  || docker exec swccg_wiki php maintenance/run.php importImages \
       --user=Admin --comment="$COMMENT" /tmp/premiere-collecting

echo "== edit Premiere Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Premiere Limited' \
  < "$ROOT/pages/Premiere_Limited.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
docker exec swccg_wiki php maintenance/run.php purgePage 'Premiere Limited' || true

echo "DONE Premiere Limited collecting"
