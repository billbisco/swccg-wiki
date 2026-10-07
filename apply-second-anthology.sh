#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Second Anthology collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/sa2; mkdir -p /tmp/sa2'
docker cp "$ROOT/encyclopedia/upload/Second-Anthology-box.png" swccg_wiki:/tmp/sa2/
docker cp "$ROOT/encyclopedia/upload/Second-Anthology-checklist.png" swccg_wiki:/tmp/sa2/
docker cp "$ROOT/encyclopedia/upload/Second-Anthology-preview-cards.png" swccg_wiki:/tmp/sa2/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" /tmp/sa2

echo "== edit Second Anthology =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Second Anthology' \
  < "$ROOT/pages/Second_Anthology.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'Second Anthology' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE Second Anthology"
