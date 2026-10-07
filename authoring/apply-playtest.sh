#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f playtest-imgs.tgz ]; then
  tar xzf playtest-imgs.tgz -C encyclopedia/upload
fi
docker exec swccg_wiki bash -lc 'rm -rf /tmp/playtest; mkdir -p /tmp/playtest'
shopt -s nullglob
for f in encyclopedia/upload/Playtest-*.png; do
  docker cp "$f" swccg_wiki:/tmp/playtest/
  echo "cp $(basename "$f")"
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Playtest scans from MPC Drive Playtest folder" \
  /tmp/playtest || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Playtest cards inventory from MPC Drive" \
  "Playtest cards" < pages/Playtest_cards.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Playtest cards"
echo DONE playtest
