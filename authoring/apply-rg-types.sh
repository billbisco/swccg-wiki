#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec swccg_wiki mkdir -p /tmp/rg-types
for f in RG-T-Vote-Now-Dark-v2.png RG-TH-Vote-Now-Dark-v2.png; do
  docker cp "$ROOT/encyclopedia/upload/$f" swccg_wiki:/tmp/rg-types/
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Dark Side Vote Now! Talaga Enhanced (Drive Darkside vote now.png)" \
  /tmp/rg-types || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Swap Imperial Command Enhanced files; Dark Vote Now! Talaga" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="RG types, Anakin character, Imperial Command swap, Dark Vote Now!" \
  "Reflections Gold (card list)" < "$ROOT/pages/Reflections_Gold_(card_list).wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Create To-Do List (Reflections Gold proofing)" \
  "To-Do List" < "$ROOT/pages/To-Do_List.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Card versions section: add To-Do List" \
  "MediaWiki:Sidebar" < "$ROOT/pages/MediaWiki_Sidebar.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Dark Side Vote Now! Talaga Enhanced" \
  "File:RG-TH-Vote-Now-Dark-v2.png" < "$ROOT/pages/File_RG-TH-Vote-Now-Dark-v2.png.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold (card list)"
docker exec swccg_wiki php maintenance/run.php purgePage "To-Do List"
docker exec swccg_wiki php maintenance/run.php purgePage "MediaWiki:Sidebar"
docker exec swccg_wiki php maintenance/run.php purgePage "Main Page"
echo DONE rg-types
