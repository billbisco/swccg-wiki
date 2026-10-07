#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Easter egg encyclopedia crops, LS Mara Jade, Reflections Gold original scans"

docker exec swccg_wiki sh -c 'rm -rf /tmp/er; mkdir -p /tmp/er'
for f in "$ROOT"/encyclopedia/upload/EE-*.png "$ROOT"/encyclopedia/upload/Mara-Jade-Light-Side-unreleased.png "$ROOT"/encyclopedia/upload/RG-*.jpg; do
  bn=$(basename "$f")
  docker cp "$f" "swccg_wiki:/tmp/er/$bn"
done
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/er

edit() { docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin "$1" < "$2"; }
edit 'Easter eggs' "$ROOT/pages/Easter_eggs.wiki"
edit 'Unreleased cards' "$ROOT/pages/Unreleased_cards.wiki"
edit 'Reflections Gold' "$ROOT/pages/Reflections_Gold.wiki"
edit 'Main Page' "$ROOT/pages/Main_Page.wiki"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
for t in 'Easter eggs' 'Unreleased cards' 'Reflections Gold' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done
echo "DONE easter refgold"
