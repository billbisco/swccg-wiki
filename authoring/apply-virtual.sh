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

if [[ -d "$ROOT/set-art-virtual" ]]; then
  import_art "$ROOT/set-art-virtual" /tmp/set-art-virtual "Virtual set title banners"
fi
if [[ -d "$ROOT/cancelled-art" ]]; then
  import_art "$ROOT/cancelled-art" /tmp/cancelled-art "Death Star II starter rulebook ad"
fi

# Virtual card GIFs named V0- / V1- / VB / VD / VP / VSh
if [[ -d "$ROOT/set-card-art" ]]; then
  docker exec swccg_wiki mkdir -p /tmp/virtual-card-art
  python3 - <<'PY'
import shutil
from pathlib import Path
src = Path("/opt/swccg-wiki/set-card-art")
dest = Path("/tmp/virtual-card-art-host")
dest.mkdir(parents=True, exist_ok=True)
n = 0
for p in src.iterdir():
    if not p.is_file():
        continue
    if p.name.startswith("V") and p.suffix.lower() in {".gif", ".jpg", ".png", ".jpeg"}:
        shutil.copy2(p, dest / p.name)
        n += 1
print("staged", n)
PY
  docker cp /tmp/virtual-card-art-host/. swccg_wiki:/tmp/virtual-card-art/ || true
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="Players Committee virtual card art" --overwrite /tmp/virtual-card-art || true
fi

if [[ -f "$ROOT/virtual-cards.xml" ]]; then
  docker cp "$ROOT/virtual-cards.xml" swccg_wiki:/tmp/virtual-cards.xml
  docker exec swccg_wiki php maintenance/run.php importDump /tmp/virtual-cards.xml
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
edit("Main Page", (pages / "Main_Page.wiki").read_bytes(), "virtual sets; Decipher month+year dates; cancelled expansions")
edit("Sets", (pages / "Sets.wiki").read_bytes(), "virtual sets and Decipher dates")
edit("MediaWiki:Sidebar", (pages / "MediaWiki_Sidebar.wiki").read_bytes(), "drop virtual hubs; link cancelled expansions")
edit("Cancelled Expansions", (pages / "Cancelled_Expansions.wiki").read_bytes(), "cancelled Decipher expansions")
edit("Mission", (pages / "concepts" / "Mission.wiki").read_bytes(), "card type stub")
edit("Current Virtual Sets", "#REDIRECT [[Main Page#Current Virtual Sets (2014–)]]\n", "no hub; sets are on Main Page")
edit("Virtual Legacy", "#REDIRECT [[Main Page#Virtual Legacy (2002–2014)]]\n", "no hub; sets are on Main Page")

# Patch infobox Date on existing Decipher hubs without rewriting thumbs.
import re, sys
sys.path.insert(0, "/opt/swccg-wiki")
try:
    import import_set_pages as isp
    dates = isp.DATES
except Exception:
    dates = {}

def get_text(title):
    r = subprocess.run(
        ["docker", "exec", "swccg_wiki", "php", "maintenance/run.php", "getText", title],
        capture_output=True,
    )
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else ""

for title, date in dates.items():
    text = get_text(title)
    if "! Date" not in text:
        print("skip date", title, flush=True)
        continue
    new, n = re.subn(r"(! Date\n\| )[^\n]+", r"\g<1>" + date, text, count=1)
    if n and new != text:
        edit(title, new, "month+year release date")
    else:
        print("date unchanged", title, flush=True)

print("pages done")
PY

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Main Page
Sets
Cancelled Expansions
Virtual Set 0
Virtual Block 1
Luke Skywalker (V)
Premiere Limited
Death Star II
MediaWiki:Sidebar
EOF
echo virtual import done
