#!/bin/bash
set -euo pipefail
PAGES=/opt/swccg-wiki/pages

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Rulings and Strategy sections" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Scomp rulings" "2X-3KPR (Tooex)" < "$PAGES/Card_2X-3KPR.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="add Dark Side Decipher card list" "Premiere Limited" < /opt/swccg-wiki/premiere-limited-raw.wiki

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

for folder in (
    Path("/opt/swccg-wiki/pages/ls-chars"),
    Path("/opt/swccg-wiki/pages/ls-rest"),
    Path("/opt/swccg-wiki/pages/ds-cards"),
):
    for line in (folder / "index.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        uid, title, fn = line.split("\t")
        edit(title, (folder / fn).read_bytes(), "Scomp rulings; Decipher strategy if starred")
print("done")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Template:Card' 'Premiere Limited' '2X-3KPR (Tooex)' 'Alter' 'A Few Maneuvers' 'Darth Vader' 'Luke Skywalker' 'Sense' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo rulings done
