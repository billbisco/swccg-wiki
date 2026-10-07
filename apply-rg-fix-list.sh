#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Swap Scum And Villainy Enhanced files (standalone vs combo)" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Card list: original type/destiny/text, combo types, Credits, Scum swap" \
  "Reflections Gold (card list)" < "$ROOT/pages/Reflections_Gold_(card_list).wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold (card list)"
echo DONE rg-fix-list
