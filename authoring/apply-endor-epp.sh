#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Endor and Enhanced Premiere collecting from Encyclopedia 3.2"
docker exec swccg_wiki sh -c 'rm -rf /tmp/ee; mkdir -p /tmp/ee'
for f in Endor-Limited-box.png Endor-Limited-pack.png Endor-Limited-four-panel-poster.png Endor-Limited-four-panel-poster-back.png Endor-Limited-rules-supplement-front.png Endor-Limited-rules-supplement-back.png EPP-display.png EPP-pack.png EPP-insert.png EPP-premiums.png; do
  docker cp "$ROOT/encyclopedia/upload/$f" "swccg_wiki:/tmp/ee/$f"
done
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/ee
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Endor' < "$ROOT/pages/Endor.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Enhanced Premiere' < "$ROOT/pages/Enhanced_Premiere.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' < "$ROOT/pages/Main_Page.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
for t in 'Endor' 'Enhanced Premiere' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done
echo "DONE Endor EPP"
