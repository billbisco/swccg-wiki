#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec swccg_wiki mkdir -p /tmp/rg-h2
for f in \
  RG-TH-Tactical-Support.png \
  RG-TH-Security-Precautions.png \
  RG-TH-Our-First-Catch-Of-The-Day.png \
  RG-TH-You-Will-Take-Me-To-Jabba-Now.png \
  RG-TH-Traffic-Control.png \
  RG-TH-Nice-Of-You-Guys-To-Drop-By.png \
  RG-TH-Neck-And-Neck.png \
  RG-TH-Attack-Pattern-Delta.png \
  RG-TH-Aim-High.png \
  RG-C1-Naboo-Ceremonial-Chamber-h.jpg \
  RG-TH-Naboo-Ceremonial-Chamber-v2.jpg
do
  docker cp "$ROOT/encyclopedia/upload/$f" swccg_wiki:/tmp/rg-h2/
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Rotated landscape Enhanced (and original Naboo: Ceremonial Chamber)" \
  /tmp/rg-h2 || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="More Enhanced credit cards shown horizontal; Naboo Ceremonial Chamber original + Enhanced" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="More Enhanced credit cards shown horizontal; Naboo Ceremonial Chamber original + Enhanced" \
  "Reflections Gold (card list)" < "$ROOT/pages/Reflections_Gold_(card_list).wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold (card list)"
echo DONE rg-h2
