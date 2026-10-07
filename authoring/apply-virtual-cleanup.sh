#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

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

if [[ -d "$ROOT/set-art-virtual-cropped" ]]; then
  import_art "$ROOT/set-art-virtual-cropped" /tmp/set-art-virtual-cropped "Cropped virtual set banners"
fi

if [[ -d "$ROOT/legacy-card-art" ]]; then
  import_art "$ROOT/legacy-card-art" /tmp/legacy-card-art "Legacy virtual card art (pre-reset)"
fi

if [[ -f "$ROOT/legacy-reuse-notes.xml" ]]; then
  docker cp "$ROOT/legacy-reuse-notes.xml" swccg_wiki:/tmp/legacy-reuse-notes.xml
  docker exec swccg_wiki php maintenance/run.php importDump /tmp/legacy-reuse-notes.xml
fi

python3 - <<'PY'
import subprocess
from pathlib import Path

def edit(title, data, summary):
    print("edit", title, flush=True)
    subprocess.run(
        [
            "docker", "exec", "-i", "swccg_wiki",
            "php", "maintenance/run.php", "edit",
            "--user=Admin", f"--summary={summary}",
            title,
        ],
        input=data if isinstance(data, bytes) else data.encode("utf-8"),
        check=True,
    )

pages = Path("/opt/swccg-wiki/pages")
edit("Main Page", (pages / "Main_Page.wiki").read_bytes(), "Set D after Set 0; Set P after Set 5; cropped banners")
edit("Sets", (pages / "Sets.wiki").read_bytes(), "Set D / Set P chronological order")
edit("Cancelled Expansions", (pages / "Cancelled_Expansions.wiki").read_bytes(), "fix infobox; one ad image")
edit("MediaWiki:Common.css", (pages / "MediaWiki_Common.css.wiki").read_bytes(), "set-tile object-fit cover")
edit("Virtual Set D", (pages / "set-hubs" / "Virtual_Set_D.wiki").read_bytes(), "launched with Set 0")
edit("Virtual Set P", (pages / "set-hubs" / "Virtual_Set_P.wiki").read_bytes(), "first release February 2017")
print("edits done")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Main Page
Sets
Cancelled Expansions
Virtual Set 0
Virtual Set D
Virtual Set P
Virtual Block 9
Anakin Skywalker, Padawan Learner (Virtual Block 9)
MediaWiki:Common.css
EOF
echo virtual cleanup done
