#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec swccg_wiki mkdir -p /tmp/rg-circle
docker cp "$ROOT/encyclopedia/upload/RG-T-The-Circle-Is-Now-Complete-Vader-s-Obsession.png" swccg_wiki:/tmp/rg-circle/
docker cp "$ROOT/encyclopedia/upload/RG-T-The-Circle-Is-Now-Complete-v2.png" swccg_wiki:/tmp/rg-circle/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Circle combo reconstruction (Drive corrected.png); standalone Circle from Drive (1).png" \
  /tmp/rg-circle || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Talaga: combo Circle/Vader Obsession from corrected.png; standalone Circle from Drive (1)" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
echo DONE circle-combo
