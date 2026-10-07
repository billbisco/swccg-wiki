#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
SRC=/tmp/legacy-dates
python3 - <<'PY'
import subprocess
from pathlib import Path
SRC = Path("/tmp/legacy-dates")
NAMES = {
    "Virtual_Block_1.wiki": "Virtual Block 1",
    "Virtual_Block_2.wiki": "Virtual Block 2",
    "Virtual_Block_3.wiki": "Virtual Block 3",
    "Virtual_Block_4.wiki": "Virtual Block 4",
    "Virtual_Block_5.wiki": "Virtual Block 5",
    "Virtual_Block_6.wiki": "Virtual Block 6",
    "Virtual_Block_7.wiki": "Virtual Block 7",
    "Virtual_Block_8.wiki": "Virtual Block 8",
    "Virtual_Block_9.wiki": "Virtual Block 9",
    "Virtual_Shields.wiki": "Virtual Shields",
}
def edit(title, data, summary):
    print("edit", title, flush=True)
    subprocess.run(
        ["docker", "exec", "-i", "swccg_wiki", "php", "maintenance/run.php", "edit",
         "--user=Admin", f"--summary={summary}", title],
        input=data, check=True,
    )
summary = "Legacy Virtual Dates: Sep 2009 reorg / subset dates; Shields ~2006-07; Sources cites"
for fn, title in NAMES.items():
    path = SRC / fn
    if not path.exists():
        raise SystemExit(f"missing {path}")
    edit(title, path.read_bytes(), summary)
edit("Main Page", (SRC / "Main_Page.wiki").read_bytes(),
     "Virtual Legacy: Shields before Block 1; set-meta dates match hubs")
print("edits done", flush=True)
PY
mkdir -p "$ROOT/pages/set-hubs"
cp -f "$SRC"/Virtual_Block_*.wiki "$SRC"/Virtual_Shields.wiki "$ROOT/pages/set-hubs/" || true
cp -f "$SRC/Main_Page.wiki" "$ROOT/pages/Main_Page.wiki"
cp -f "$SRC/main-virtual-legacy.wiki" "$ROOT/pages/main-virtual-legacy.wiki" 2>/dev/null || true
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Main Page
Virtual Shields
Virtual Block 1
Virtual Block 2
Virtual Block 3
Virtual Block 4
Virtual Block 5
Virtual Block 6
Virtual Block 7
Virtual Block 8
Virtual Block 9
EOF
echo "legacy virtual dates apply done"
