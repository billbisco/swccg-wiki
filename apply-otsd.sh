#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Official Tournament Sealed Deck collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/otsd; mkdir -p /tmp/otsd'
docker cp "$ROOT/encyclopedia/upload/OTSD-storage-box.png" swccg_wiki:/tmp/otsd/
docker cp "$ROOT/encyclopedia/upload/OTSD-storage-boxes-six.png" swccg_wiki:/tmp/otsd/
docker cp "$ROOT/encyclopedia/upload/OTSD-rulebook.png" swccg_wiki:/tmp/otsd/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" /tmp/otsd

echo "== edit Official Tournament Sealed Deck =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Official Tournament Sealed Deck' \
  < "$ROOT/pages/Official_Tournament_Sealed_Deck.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'Official Tournament Sealed Deck' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE OTSD"
