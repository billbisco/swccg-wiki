#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
edit() {
  echo "edit $1"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$3" "$1" < "$2"
}
edit "Light Side" "$ROOT/pages/Light_Side.wiki" "Archive copies of Drive and Reddit sources"
edit "Dark Side" "$ROOT/pages/Dark_Side.wiki" "Archive copies of Drive and Reddit sources"
edit "Playtest cards" "$ROOT/pages/Playtest_cards.wiki" "Playtest notes plus archived Drive/Reddit sources"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Light Side"
docker exec swccg_wiki php maintenance/run.php purgePage "Dark Side"
docker exec swccg_wiki php maintenance/run.php purgePage "Playtest cards"
echo DONE card-sides-archives
