#!/bin/bash
set -euo pipefail
PAGES=/opt/swccg-wiki/pages
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="no fostered p/br gap under portrait" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="hide stray p in card-rail" "MediaWiki:Common.css" < "$PAGES/MediaWiki_Common.css.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Template:Card' 'MediaWiki:Common.css' 'Tatooine: Cantina' 'Caller' 'Sense' 'Luke Skywalker' '2X-3KPR (Tooex)' 'Millennium Falcon' 'Alderaan' 'Hydroponics Station' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo rail-gap done
