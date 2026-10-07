#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f rg-th.tgz ]; then
  docker cp "$ROOT/rg-th.tgz" swccg_wiki:/tmp/rg-th.tgz
  docker exec swccg_wiki bash -lc 'rm -rf /tmp/rg-th; mkdir -p /tmp/rg-th; tar xzf /tmp/rg-th.tgz -C /tmp/rg-th; ls /tmp/rg-th | wc -l'
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Rotated landscape Talaga Enhanced / credit cards" \
    /tmp/rg-th || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Talaga landscape Enhanced cards shown horizontal" \
  "Reflections Gold" < pages/Reflections_Gold.wiki
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Layout test: LS/DS by type, original scan + Enhanced, OCR text" \
  "Reflections Gold (card list)" < pages/Reflections_Gold_\(card_list\).wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold (card list)"
echo DONE rg-card-list
