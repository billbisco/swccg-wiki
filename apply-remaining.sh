#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Remaining CardGuide collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/rem; mkdir -p /tmp/rem'
for f in \
  ECC-box.png ECC-pack.png ECC-premiums.png \
  EJP-display.png EJP-pack.png EJP-premiums.png \
  Reflections-display.png Reflections-pack.png Reflections-box-toppers.png \
  Third-Anthology-box.png Third-Anthology-checklist.png Third-Anthology-premiums.png \
  DS2-Limited-display.png DS2-Limited-pack.png DS2-Limited-starters.png DS2-Limited-rulebook.png \
  DS2-Limited-four-panel-poster.png DS2-Limited-four-panel-poster-back.png \
  JP-OTSD-box.png JP-OTSD-covers.png \
  Tatooine-Limited-box.png Tatooine-Limited-pack.png \
  Coruscant-Limited-box.png Coruscant-Limited-pack.png \
  Theed-Limited-box.png Theed-Limited-pack.png \
  Reflections-II-display.png Reflections-II-pack.png \
  Reflections-II-rules-supplement-front.png Reflections-II-rules-supplement-back.png \
  Reflections-III-display.png Reflections-III-pack.png \
  Reflections-III-rules-supplement-front.png Reflections-III-rules-supplement-back.png
do
  docker cp "$ROOT/encyclopedia/upload/$f" "swccg_wiki:/tmp/rem/$f"
done
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/rem

edit() { docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin "$1" < "$2"; }

echo "== edit pages =="
edit 'Enhanced Cloud City' "$ROOT/pages/Enhanced_Cloud_City.wiki"
edit "Enhanced Jabba's Palace" "$ROOT/pages/Enhanced_Jabbas_Palace.wiki"
edit 'Reflections' "$ROOT/pages/Reflections.wiki"
edit 'Third Anthology' "$ROOT/pages/Third_Anthology.wiki"
edit 'Death Star II' "$ROOT/pages/Death_Star_II.wiki"
edit 'Death Star II Starter Decks' "$ROOT/pages/Death_Star_II_Starter_Decks.wiki"
edit "Jabba's Palace Sealed Deck" "$ROOT/pages/Jabbas_Palace_Sealed_Deck.wiki"
edit 'Reflections II: Expanding the Galaxy' "$ROOT/pages/Reflections_II.wiki"
edit 'Tatooine' "$ROOT/pages/Tatooine.wiki"
edit 'Coruscant' "$ROOT/pages/Coruscant.wiki"
edit "Reflections III: A Collector's Bounty" "$ROOT/pages/Reflections_III.wiki"
edit 'Theed Palace' "$ROOT/pages/Theed_Palace.wiki"
edit 'Main Page' "$ROOT/pages/Main_Page.wiki"

echo "== FlaggedRevs + purge =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
for t in \
  'Enhanced Cloud City' \
  "Enhanced Jabba's Palace" \
  'Reflections' \
  'Third Anthology' \
  'Death Star II' \
  'Death Star II Starter Decks' \
  "Jabba's Palace Sealed Deck" \
  'Reflections II: Expanding the Galaxy' \
  'Tatooine' \
  'Coruscant' \
  "Reflections III: A Collector's Bounty" \
  'Theed Palace' \
  'Main Page'
do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done
echo "DONE remaining CardGuide hubs"
