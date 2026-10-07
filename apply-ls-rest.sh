#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
REST="$PAGES/ls-rest"

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="optional infobox stats; armor/maneuver/hyperspeed" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="next Caller" "Wioslea" < "$PAGES/ls-chars/1_33.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="redirect to Sense" "Sense (Premiere)" < "$PAGES/Sense_Premiere_redirect.wiki"

python3 - <<'PY'
import subprocess
from pathlib import Path

rest = Path("/opt/swccg-wiki/pages/ls-rest")
index = rest / "index.tsv"
for line in index.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    uid, title, fn = line.split("\t")
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
            "--summary=Premiere LS card",
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

alias_file = rest / "aliases.tsv"
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
print("done rest")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
{
  echo 'Template:Card'
  echo 'Wioslea'
  echo 'Sense'
  echo 'Sense (Premiere)'
  echo '2X-3KPR (Tooex)'
  echo 'Luke Skywalker'
  cut -f2 "$REST/index.tsv"
} | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo ls-rest done
