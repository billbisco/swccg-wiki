#!/bin/bash
set -euo pipefail
PAGES=/opt/swccg-wiki/pages
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="drop type-list disclaimer; link card-type stubs" "Premiere Limited" < /opt/swccg-wiki/premiere-limited-raw.wiki

python3 - <<'PY'
import subprocess
from pathlib import Path

def edit(title, path):
    print("stub", title, flush=True)
    subprocess.run(
        [
            "docker", "exec", "-i", "swccg_wiki",
            "php", "maintenance/run.php", "edit",
            "--user=Admin", "--summary=card type stub", title,
        ],
        input=Path(path).read_bytes(),
        check=True,
    )

c = Path("/opt/swccg-wiki/pages/concepts")
pairs = [
    ("Character", "Character.wiki"),
    ("Device", "Device.wiki"),
    ("Effect", "Effect.wiki"),
    ("Interrupt", "Interrupt.wiki"),
    ("Location", "Location.wiki"),
    ("Starship", "Starship.wiki"),
    ("Vehicle", "Vehicle.wiki"),
    ("Weapon", "Weapon.wiki"),
    ("Creature", "Creature.wiki"),
    ("Objective", "Objective.wiki"),
    ("Admiral's Order", "Admirals_Order.wiki"),
    ("Epic Event", "Epic_Event.wiki"),
    ("Jedi Test", "Jedi_Test.wiki"),
    ("Podracer", "Podracer.wiki"),
    ("Defensive Shield", "Defensive_Shield.wiki"),
]
for title, fn in pairs:
    edit(title, c / fn)
print("stubs done")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Premiere Limited' 'Character' 'Device' 'Effect' 'Interrupt' 'Location' 'Starship' 'Vehicle' 'Weapon' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo premiere hub done
