#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
# Preserve Bardez originals for /preserved/bardez/
mkdir -p "$ROOT/encyclopedia/preserved/bardez"
if [ -d "$ROOT/encyclopedia/bardez-templates" ]; then
  cp -a "$ROOT/encyclopedia/bardez-templates/." "$ROOT/encyclopedia/preserved/bardez/" || true
fi
# Images
docker exec swccg_wiki mkdir -p /tmp/tourney-custom
for f in \
  1998-worlds-p1.png \
  1998-worlds-p4.png \
  1998-commandcard-p1.png \
  decipher-decklist-p1.png \
  pc-decklist-2015-p1.png \
  2008-worlds-d1-p1.png \
  pc-tg-22-p1.png \
  decipher-scorecard-constructed-p1.png
do
  if [ -f "$ROOT/encyclopedia/upload/$f" ]; then
    docker cp "$ROOT/encyclopedia/upload/$f" swccg_wiki:/tmp/tourney-custom/
  fi
done
shopt -s nullglob
for f in "$ROOT"/encyclopedia/upload/Bardez-*.png "$ROOT"/encyclopedia/upload/Bardez-*.PNG; do
  docker cp "$f" swccg_wiki:/tmp/tourney-custom/ || true
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Tournament history scans and Bardez template previews" \
  /tmp/tourney-custom || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit() {
  local title="$1"
  local file="$2"
  local sum="$3"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$sum" "$title" < "$file"
}

edit "Tournaments" "$ROOT/pages/Tournaments.wiki" "Tournaments history: Decipher Swiss, Elo, Worlds 1998, decklists"
edit "Making Custom SWCCG Cards" "$ROOT/pages/Making_Custom_SWCCG_Cards.wiki" "Bardez GIMP templates preservation page"
edit "Bardez" "$ROOT/pages/Bardez.wiki" "Bardez template author stub"
edit "Tournament Guidelines" "$ROOT/pages/Tournament_Guidelines.wiki" "Pointer to Guide 2.2 and Tournaments history"
edit "Category:Card production" "$ROOT/pages/Category_Card_production.wiki" "Card production category"
edit "Championships" "$ROOT/pages/Championships.wiki" "Link Tournaments hub"
edit "Main Page" "$ROOT/pages/Main_Page.wiki" "Tournaments section; Making Custom Cards"
edit "MediaWiki:Sidebar" "$ROOT/pages/MediaWiki_Sidebar.wiki" "Sidebar: Tournaments, Making custom cards"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
for p in "Tournaments" "Making Custom SWCCG Cards" "Bardez" "Tournament Guidelines" "Championships" "Main Page" "MediaWiki:Sidebar"; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$p" || true
done
echo DONE tournaments-custom
