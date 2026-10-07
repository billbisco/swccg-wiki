#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec swccg_wiki mkdir -p /tmp/rg-prisoner
docker cp "$ROOT/encyclopedia/upload/RG-TH-We-Have-A-Prisoner.png" swccg_wiki:/tmp/rg-prisoner/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Rotated landscape Enhanced: We Have A Prisoner" \
  /tmp/rg-prisoner || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="We Have A Prisoner Enhanced card shown horizontal" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="We Have A Prisoner Enhanced card shown horizontal" \
  "Reflections Gold (card list)" < "$ROOT/pages/Reflections_Gold_(card_list).wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold (card list)"
echo DONE prisoner
