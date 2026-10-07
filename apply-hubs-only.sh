#!/bin/bash
set -euo pipefail
python3 - <<'PY'
import subprocess
from pathlib import Path

hub = Path("/opt/swccg-wiki/pages/set-hubs")
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
            "--user=Admin", "--summary=Light/Dark links; DS2 starters; anthology previews",
            title,
        ],
        input=path.read_bytes(),
        check=True,
    )
print("hubs done")
PY
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="link Light/Dark; type stubs" "Premiere Limited" < /opt/swccg-wiki/premiere-limited-raw.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Premiere Limited' 'Death Star II Starter Decks' 'Death Star II' 'First Anthology' 'Second Anthology' 'A New Hope' 'Light' 'Dark' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo hubs-only done
