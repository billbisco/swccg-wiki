#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
edit() { docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin "$1" < "$2"; }

edit 'Reflections' "$ROOT/pages/Reflections.wiki"
edit 'Reflections II: Expanding the Galaxy' "$ROOT/pages/Reflections_II.wiki"
edit 'Reflections III: A Collector'\''s Bounty' "$ROOT/pages/Reflections_III.wiki"
edit 'Endor' "$ROOT/pages/Endor.wiki"
edit 'Promotional Foils' "$ROOT/pages/Promotional_Foils.wiki"
edit 'Skywalkers (expansion)' "$ROOT/pages/Skywalkers_(expansion).wiki"
edit 'Shadows of the Empire' "$ROOT/pages/Shadows_of_the_Empire.wiki"
edit 'Jedi Masters' "$ROOT/pages/Jedi_Masters.wiki"
edit 'Scoundrels' "$ROOT/pages/Scoundrels.wiki"
edit 'Lichtenstein' "$ROOT/pages/Lichtenstein.wiki"
edit 'Easter eggs' "$ROOT/pages/Easter_eggs.wiki"
edit 'Anagrams' "$ROOT/pages/Anagrams.wiki"
edit 'Unreleased cards' "$ROOT/pages/Unreleased_cards.wiki"
edit 'Reflections Gold' "$ROOT/pages/Reflections_Gold.wiki"
edit 'Cancelled Expansions' "$ROOT/pages/Cancelled_Expansions.wiki"
edit 'Main Page' "$ROOT/pages/Main_Page.wiki"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
for t in \
  'Reflections' \
  'Reflections II: Expanding the Galaxy' \
  "Reflections III: A Collector's Bounty" \
  'Endor' \
  'Promotional Foils' \
  'Skywalkers (expansion)' \
  'Shadows of the Empire' \
  'Jedi Masters' \
  'Scoundrels' \
  'Lichtenstein' \
  'Easter eggs' \
  'Anagrams' \
  'Unreleased cards' \
  'Reflections Gold' \
  'Cancelled Expansions' \
  'Main Page'
do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done
echo "DONE foils unreleased"
