#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
CHAR="$PAGES/ls-chars"

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Info caption; empty Notes default" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="drop GEMP disclaimer and Spanish Premiere" "2X-3KPR (Tooex)" < "$PAGES/Card_2X-3KPR.wiki"

python3 - <<'PY'
import subprocess
from pathlib import Path

char = Path("/opt/swccg-wiki/pages/ls-chars")
index = char / "index.tsv"
for line in index.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    uid, title, fn = line.split("\t")
    path = char / fn
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
            "--summary=drop GEMP disclaimer, Spanish Premiere, filler Notes",
            title,
        ],
        input=path.read_bytes(),
        check=True,
    )
    redir = f"#REDIRECT [[{title}]]\n"
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
            "--summary=redirect",
            f"Card:{uid}",
        ],
        input=redir.encode("utf-8"),
        check=True,
    )

alias_file = char / "aliases.tsv"
if alias_file.exists():
    for line in alias_file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        alias, dest = line.split("\t", 1)
        print("alias", alias, "->", dest)
        redir = f"#REDIRECT [[{dest}]]\n"
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
                "--summary=name redirect",
                alias,
            ],
            input=redir.encode("utf-8"),
            check=True,
        )
print("done chars")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
{
  echo 'Template:Card'
  echo '2X-3KPR (Tooex)'
  cut -f2 "$CHAR/index.tsv"
} | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo ls-chars done
