#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"

if [ -d "$ROOT/y2022-2024-media" ]; then
  echo "== import GEMP media =="
  docker exec swccg_wiki mkdir -p /tmp/y2022-2024-media
  docker cp "$ROOT/y2022-2024-media/." swccg_wiki:/tmp/y2022-2024-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="GEMP import 2022-2024 recovered decks" \
    /tmp/y2022-2024-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$ROOT/y2022-2024-regen.tsv" "2022-2024 tournament hubs, decks, player stubs, and retitle redirects"
