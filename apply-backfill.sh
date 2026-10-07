#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="CardGuide backfill collecting from Encyclopedia 3.2"

echo "== importImages =="
docker exec swccg_wiki sh -c 'rm -rf /tmp/bf; mkdir -p /tmp/bf'
for f in \
  First-Anthology-box.png First-Anthology-rules.png First-Anthology-preview-cards.png \
  Premiere-2P-box.png Premiere-2P-rules.png Premiere-2P-premiums.png \
  ESB-2P-box.png ESB-2P-rules.png ESB-2P-sample-game.png ESB-2P-premiums.png \
  Jedi-Pack-pack.png Jedi-Pack-booklet.png Jedi-Pack-cards.png \
  Rebel-Leader-cards.png
do
  docker cp "$ROOT/encyclopedia/upload/$f" "swccg_wiki:/tmp/bf/$f"
done
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/bf

edit() { docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin "$1" < "$2"; }

edit 'First Anthology' "$ROOT/pages/First_Anthology.wiki"
edit 'Jedi Pack' "$ROOT/pages/Jedi_Pack.wiki"
edit 'Rebel Leader Packs' "$ROOT/pages/Rebel_Leader_Packs.wiki"
edit 'Premiere Two-Player Introductory Game' "$ROOT/pages/Premiere_Two-Player_Introductory_Game.wiki"
edit 'The Empire Strikes Back Introductory Two-Player Game' "$ROOT/pages/ESB_Two_Player.wiki"
edit 'Main Page' "$ROOT/pages/Main_Page.wiki"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
for t in 'First Anthology' 'Jedi Pack' 'Rebel Leader Packs' 'Premiere Two-Player Introductory Game' 'The Empire Strikes Back Introductory Two-Player Game' 'Main Page'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done
echo "DONE backfill"
