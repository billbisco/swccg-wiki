#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
REST="$PAGES/ls-rest"

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="HTML infobox rows; location Dark/Light icons" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="infobox two-column cells" "MediaWiki:Common.css" < "$PAGES/MediaWiki_Common.css.wiki"

python3 - <<'PY'
import subprocess
from pathlib import Path

rest = Path("/opt/swccg-wiki/pages/ls-rest")
for line in (rest / "index.tsv").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    uid, title, fn = line.split("\t")
    n = int(uid.split("_")[1])
    if n < 121 or n > 139:
        continue
    path = rest / fn
    print("import", title)
    subprocess.run(
        [
            "docker",
            "exec",
            "-i",
            "swccg_wiki",
            "php",
            "maintenance/run.php",
            "edit",
            "--user=Admin",
            "--summary=split location icons; stacked infobox rows",
            title,
        ],
        input=path.read_bytes(),
        check=True,
    )
print("done locations")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
{
  echo 'Template:Card'
  echo 'MediaWiki:Common.css'
  echo '2X-3KPR (Tooex)'
  echo 'Luke Skywalker'
  echo 'Caller'
  echo 'Millennium Falcon'
  echo 'Tatooine: Cantina'
  echo 'Alderaan'
  echo 'Death Star: Detention Block Control Room'
  echo 'Death Star: Trash Compactor'
  echo 'Tatooine'
  echo 'Yavin 4'
  python3 - <<'PY'
from pathlib import Path
rest = Path("/opt/swccg-wiki/pages/ls-rest")
for line in (rest / "index.tsv").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    uid, title, fn = line.split("\t")
    n = int(uid.split("_")[1])
    if 121 <= n <= 139:
        print(title)
PY
} | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo location-icons done
