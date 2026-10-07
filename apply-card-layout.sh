#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
edit() {
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="card layout" "$1" < "$2"
}
edit "Template:Card" "$PAGES/Template_Card.wiki"
edit "2X-3KPR (Tooex)" "$PAGES/Card_2X-3KPR.wiki"
edit "Rarity" "$PAGES/Rarity.wiki"
edit "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '2X-3KPR (Tooex)\nTemplate:Card\nRarity\n' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo card-layout done
