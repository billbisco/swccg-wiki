#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
SRC=/tmp/legacy-sources-72-91
python3 - <<'PY'
import subprocess
from pathlib import Path
SRC = Path("/tmp/legacy-sources-72-91")
NAMES = {
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
summary = "Legacy Virtual Sources: fold Alpha1 7.2 (13/29 Dec 2010) + 9.1 (10 Jan 2014) primaries; VB8/Shields strengthen (Dates unchanged)"
for fn, title in NAMES.items():
    path = SRC / fn
    if not path.exists():
        raise SystemExit(f"missing {path}")
    edit(title, path.read_bytes(), summary)
print("edits done", flush=True)
PY
mkdir -p "$ROOT/pages/set-hubs"
cp -f "$SRC"/Virtual_Block_{7,8,9}.wiki "$SRC"/Virtual_Shields.wiki "$ROOT/pages/set-hubs/" || true
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Virtual Shields
Virtual Block 7
Virtual Block 8
Virtual Block 9
EOF
echo "legacy virtual sources 7.2/9.1 apply done"
