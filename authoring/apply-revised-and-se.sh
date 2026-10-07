#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="CardGuide 15-18 collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/cg1518; mkdir -p /tmp/cg1518'
for f in \
  SE-Limited-display.png SE-Limited-pack.png SE-Limited-starters.png \
  SE-Limited-rulebook.png SE-Limited-glossary.png \
  SE-Limited-four-panel-poster.png SE-Limited-four-panel-poster-back.png \
  SE-Limited-ls-rare-sheet.png \
  ANH-Revised-rules-supplement.png Hoth-Revised-rules-supplement.png \
  Dagobah-Revised-rules-supplement.png
do
  docker cp "$ROOT/encyclopedia/upload/$f" "swccg_wiki:/tmp/cg1518/$f"
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin --comment="$COMMENT" /tmp/cg1518

echo "== edit Revised hubs =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Revised A New Hope' \
  < "$ROOT/pages/Revised_A_New_Hope.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Revised Hoth' \
  < "$ROOT/pages/Revised_Hoth.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Revised Dagobah' \
  < "$ROOT/pages/Revised_Dagobah.wiki"

echo "== edit Special Edition =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Special Edition' \
  < "$ROOT/pages/Special_Edition.wiki"

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Main Page' \
  < "$ROOT/pages/Main_Page.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'Revised A New Hope' 'Revised Hoth' 'Revised Dagobah' 'Special Edition' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE CardGuide 15-18"
