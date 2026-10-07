#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="hatnote for other-side cards" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="card-hatnote style" "MediaWiki:Common.css" < "$PAGES/MediaWiki_Common.css.wiki"

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

concepts = Path("/opt/swccg-wiki/pages/concepts")
for path in sorted(concepts.glob("*.wiki")):
    title = path.stem.replace("_", " ")
    edit(title, path.read_bytes(), "game concept stub")

# Light rest
rest = Path("/opt/swccg-wiki/pages/ls-rest")
for line in (rest / "index.tsv").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    uid, title, fn = line.split("\t")
    edit(title, (rest / fn).read_bytes(), "link Effect/Utinni Effect/Interrupt")

# Jawa hatnote
jawa = Path("/opt/swccg-wiki/pages/ls-chars/1_12.wiki")
edit("Jawa", jawa.read_bytes(), "hatnote Dark Jawa")

ds = Path("/opt/swccg-wiki/pages/ds-cards")
for line in (ds / "index.tsv").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    uid, title, fn = line.split("\t")
    edit(title, (ds / fn).read_bytes(), "Premiere Dark Side card")
    edit(f"Card:{uid}", f"#REDIRECT [[{title}]]\n", "redirect")

alias_file = ds / "aliases.tsv"
if alias_file.exists():
    for line in alias_file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        alias, dest = line.split("\t", 1)
        edit(alias, f"#REDIRECT [[{dest}]]\n", "name redirect")
print("done import")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
{
  echo Template:Card
  echo Interrupt
  echo Effect
  echo 'Utinni Effect'
  echo 'Used Interrupt'
  echo Alter
  echo 'Alter (Dark)'
  echo 'Darth Vader'
  echo Jawa
  echo 'Jawa (Dark)'
  echo Sense
  echo 'Death Star Plans'
  echo 'Timer Mine (Dark)'
} | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo ds-and-concepts done
