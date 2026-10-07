#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
ART="$ROOT/set-card-art"
BACKS="$ROOT/obj-backs"
HUB="$ROOT/pages/set-hubs"

import_art() {
  local src="$1"
  local dest="$2"
  local comment="$3"
  if [[ -d "$src" ]]; then
    docker exec swccg_wiki mkdir -p "$dest"
    docker cp "$src/." "swccg_wiki:$dest/"
    docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$comment" --overwrite "$dest" || true
  fi
}

if [[ -d "$BACKS" ]]; then
  import_art "$BACKS" /tmp/obj-backs "Objective 7-side art"
elif [[ -d "$ART" ]]; then
  import_art "$ART" /tmp/set-card-art "Decipher set card art"
fi

python3 - <<'PY'
import subprocess
from pathlib import Path

hub = Path("/opt/swccg-wiki/pages/set-hubs")
# filename -> wiki title
names = {
    "A_New_Hope.wiki": "A New Hope",
    "Hoth.wiki": "Hoth",
    "Dagobah.wiki": "Dagobah",
    "Cloud_City.wiki": "Cloud City",
    "Jabba_s_Palace.wiki": "Jabba's Palace",
    "Special_Edition.wiki": "Special Edition",
    "Endor.wiki": "Endor",
    "Death_Star_II.wiki": "Death Star II",
    "Tatooine.wiki": "Tatooine",
    "Coruscant.wiki": "Coruscant",
    "Theed_Palace.wiki": "Theed Palace",
    "Premiere_Two_Player_Introductory_Game.wiki": "Premiere Two-Player Introductory Game",
    "The_Empire_Strikes_Back_Introductory_Two_Player_Game.wiki": "The Empire Strikes Back Introductory Two-Player Game",
    "Rebel_Leader_Packs.wiki": "Rebel Leader Packs",
    "Jedi_Pack.wiki": "Jedi Pack",
    "Official_Tournament_Sealed_Deck.wiki": "Official Tournament Sealed Deck",
    "Enhanced_Premiere.wiki": "Enhanced Premiere",
    "Enhanced_Cloud_City.wiki": "Enhanced Cloud City",
    "Enhanced_Jabba_s_Palace.wiki": "Enhanced Jabba's Palace",
    "Third_Anthology.wiki": "Third Anthology",
    "Jabba_s_Palace_Sealed_Deck.wiki": "Jabba's Palace Sealed Deck",
    "Reflections_II_Expanding_the_Galaxy.wiki": "Reflections II: Expanding the Galaxy",
    "Reflections_III_A_Collector_s_Bounty.wiki": "Reflections III: A Collector's Bounty",
    "Death_Star_II_Starter_Decks.wiki": "Death Star II Starter Decks",
    "First_Anthology.wiki": "First Anthology",
    "Second_Anthology.wiki": "Second Anthology",
}
for fn, title in names.items():
    path = hub / fn
    if not path.exists():
        print("skip", fn)
        continue
    print("edit", title, flush=True)
    subprocess.run(
        [
            "docker", "exec", "-i", "swccg_wiki",
            "php", "maintenance/run.php", "edit",
            "--user=Admin", "--summary=unique card list thumbs",
            title,
        ],
        input=path.read_bytes(),
        check=True,
    )
print("hubs done")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
A New Hope
Hoth
Dagobah
Cloud City
Jabba's Palace
Special Edition
Endor
Death Star II
Tatooine
Coruscant
Theed Palace
Enhanced Premiere
Enhanced Cloud City
Enhanced Jabba's Palace
Death Star II Starter Decks
Official Tournament Sealed Deck
Jabba's Palace Sealed Deck
Third Anthology
Reflections II: Expanding the Galaxy
Reflections III: A Collector's Bounty
Main Page
EOF
echo set lists done
