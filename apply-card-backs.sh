#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec swccg_wiki mkdir -p /tmp/card-backs
docker cp "$ROOT/encyclopedia/upload/Card-Back-Light-Side.png" swccg_wiki:/tmp/card-backs/
docker cp "$ROOT/encyclopedia/upload/Card-Back-Dark-Side.png" swccg_wiki:/tmp/card-backs/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="MPC print-ready Drive card backs (no-text templates)" \
  /tmp/card-backs || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
edit() {
  echo "edit $1"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$3" "$1" < "$2"
}
edit "File:Card-Back-Light-Side.png" "$ROOT/pages/File_Card-Back-Light-Side.png.wiki" "Source: MPC print-ready Drive LS no-text back"
edit "File:Card-Back-Dark-Side.png" "$ROOT/pages/File_Card-Back-Dark-Side.png.wiki" "Source: MPC print-ready Drive DS no-text back"
edit "Light Side" "$ROOT/pages/Light_Side.wiki" "Light Side article with card back from MPC Drive"
edit "Dark Side" "$ROOT/pages/Dark_Side.wiki" "Dark Side article with card back from MPC Drive"
edit "Light" "$ROOT/pages/Light.wiki" "Redirect Light to Light Side"
edit "Dark" "$ROOT/pages/Dark.wiki" "Redirect Dark (game concept) to Dark Side; player is Timo Dusel"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Light Side"
docker exec swccg_wiki php maintenance/run.php purgePage "Dark Side"
docker exec swccg_wiki php maintenance/run.php purgePage "Light"
docker exec swccg_wiki php maintenance/run.php purgePage "Dark"
echo DONE card-backs
