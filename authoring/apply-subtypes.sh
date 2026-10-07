#!/bin/bash
set -euo pipefail
PAGES=/opt/swccg-wiki/pages

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="subtype_link for weapon/vehicle subtypes" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="subtype_link" "2X-3KPR (Tooex)" < "$PAGES/Card_2X-3KPR.wiki"

python3 - <<'PY'
import subprocess
from pathlib import Path

def edit(title, data, summary):
    print("edit", title)
    subprocess.run(
        [
            "docker", "exec", "-i", "swccg_wiki",
            "php", "maintenance/run.php", "edit",
            "--user=Admin", f"--summary={summary}", title,
        ],
        input=data if isinstance(data, bytes) else data.encode("utf-8"),
        check=True,
    )

for path in sorted(Path("/opt/swccg-wiki/pages/concepts").glob("*.wiki")):
    edit(path.stem.replace("_", " "), path.read_bytes(), "card type/subtype stub")

for folder, summary in (
    (Path("/opt/swccg-wiki/pages/ls-chars"), "character subtype_link"),
    (Path("/opt/swccg-wiki/pages/ls-rest"), "subtype_link"),
    (Path("/opt/swccg-wiki/pages/ds-cards"), "subtype_link"),
):
    for line in (folder / "index.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        uid, title, fn = line.split("\t")
        edit(title, (folder / fn).read_bytes(), summary)
print("done")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Template:Card' '2X-3KPR (Tooex)' 'Alter' "Vader's Lightsaber" 'Jedi Lightsaber' 'Character Weapon' 'Starship Weapon' 'Automated Weapon' 'Artillery Weapon' 'Bantha' 'Creature Vehicle' 'Character' 'Weapon' 'Luke Skywalker' 'Millennium Falcon' 'Proton Torpedoes' 'Timer Mine' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo subtypes done
