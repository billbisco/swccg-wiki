#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
SRC=/tmp/virtual-pages
cp -f "$SRC/virtual-cards.xml" "$ROOT/virtual-cards.xml"
cp -f "$SRC/apply-virtual.sh" "$ROOT/apply-virtual.sh"
cp -f "$SRC/import_set_pages.py" "$ROOT/import_set_pages.py"
mkdir -p "$ROOT/pages/concepts"
cp -f "$SRC/Main_Page.wiki" "$ROOT/pages/Main_Page.wiki"
cp -f "$SRC/Sets.wiki" "$ROOT/pages/Sets.wiki"
cp -f "$SRC/MediaWiki_Sidebar.wiki" "$ROOT/pages/MediaWiki_Sidebar.wiki"
cp -f "$SRC/Cancelled_Expansions.wiki" "$ROOT/pages/Cancelled_Expansions.wiki"
cp -f "$SRC/Mission.wiki" "$ROOT/pages/concepts/Mission.wiki"

docker cp "$ROOT/virtual-cards.xml" swccg_wiki:/tmp/virtual-cards.xml
docker exec swccg_wiki php maintenance/run.php importDump /tmp/virtual-cards.xml

python3 - <<'PY'
import re
import subprocess
from pathlib import Path
import sys
sys.path.insert(0, "/opt/swccg-wiki")

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
edit("Current Virtual Sets", "#REDIRECT [[Main Page]]\n", "no hub; sets are on Main Page")
edit("Virtual Legacy", "#REDIRECT [[Main Page]]\n", "no hub; sets are on Main Page")

try:
    import import_set_pages as isp
    dates = isp.DATES
except Exception as e:
    print("dates import failed", e, flush=True)
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
Aayla Secura
Premiere Limited
Death Star II
MediaWiki:Sidebar
EOF
echo virtual pages apply done
