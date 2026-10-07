#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

edit() {
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="card POC" "$1" < "$2"
}

edit "Template:Card" "$PAGES/Template_Card.wiki"
edit "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki"
edit "MediaWiki:Common.js" "$PAGES/MediaWiki_Common.js.wiki"
edit "2X-3KPR (Tooex)" "$PAGES/Card_2X-3KPR.wiki"

printf '%s\n' '#REDIRECT [[2X-3KPR (Tooex)]]' | docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="redirect" "Card:1_1"
printf '%s\n' '#REDIRECT [[2X-3KPR (Tooex)]]' | docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="redirect" "2X-3KPR"
printf '%s\n' '#REDIRECT [[2X-3KPR (Tooex)]]' | docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="redirect" "Tooex"
printf '%s\n' "Dark Side Special Edition counterpart of [[2X-3KPR (Tooex)]]. Common droid: where present under nighttime conditions, your Imperials and aliens at the same planet site are power +2 and immune to attrition < 3. Construction stub." | docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="stub" "2X-7KPR (Tooex)"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '2X-3KPR (Tooex)\nCard:1_1\nTemplate:Card\nPremiere Limited\n' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo card-poc done
curl -sL -m 12 "https://wiki.swccg.com/wiki/2X-3KPR_(Tooex)" | python3 -c "import sys; t=sys.stdin.read(); print('title', '2X-3KPR' in t); print('lore', 'Lerrimore' in t); print('image', '2x3kpr' in t.lower()); print('gemp', '1_1' in t); print('hydro', 'Hydroponics' in t)"
