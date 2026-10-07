#!/bin/bash
set -euo pipefail
PAGES=/opt/swccg-wiki/pages

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="left-rail option; refs list padding" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="references list flush with Sources; left rail" "MediaWiki:Common.css" < "$PAGES/MediaWiki_Common.css.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Scomp/Decipher extras; link card names" "2X-3KPR (Tooex)" < "$PAGES/Card_2X-3KPR.wiki"

python3 - <<'PY'
import subprocess
from pathlib import Path

def edit(title, data, summary):
    print("edit", title, flush=True)
    subprocess.run(
        [
            "docker", "exec", "-i", "swccg_wiki",
            "php", "maintenance/run.php", "edit",
            "--user=Admin", f"--summary={summary}", title,
        ],
        input=data if isinstance(data, bytes) else data.encode("utf-8"),
        check=True,
    )

summary = "Scomp sections; Decipher strategy; wiki-link card names"
for folder in (
    Path("/opt/swccg-wiki/pages/ls-chars"),
    Path("/opt/swccg-wiki/pages/ls-rest"),
    Path("/opt/swccg-wiki/pages/ds-cards"),
):
    for line in (folder / "index.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        uid, title, fn = line.split("\t")
        edit(title, (folder / fn).read_bytes(), summary)
print("pages done")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Template:Card' 'MediaWiki:Common.css' '2X-3KPR (Tooex)' 'Darth Vader' 'Djas Puhr' 'Luke Skywalker' 'Grand Moff Tarkin' 'Alter' 'Sense' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo premiere extras mass import done
