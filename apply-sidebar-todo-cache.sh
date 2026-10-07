#!/bin/bash
set -euo pipefail
cd /opt/swccg-wiki
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import re
p = Path("/opt/swccg-wiki/extra-settings.php")
t = p.read_text()
new = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
pat = re.compile(r"\$wgCacheEpoch\s*=\s*'[^']*';")
if not pat.search(t):
    raise SystemExit("no wgCacheEpoch")
p.write_text(pat.sub(f"$wgCacheEpoch = '{new}';", t, count=1))
print("epoch bumped to", new)
PY
docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d wiki
sleep 5
docker exec swccg_wiki php maintenance/run.php purgePage "MediaWiki:Sidebar" || true
docker exec swccg_wiki php maintenance/run.php purgePage "Main Page" || true
docker exec swccg_wiki php maintenance/run.php purgePage "To-Do List" || true
echo DONE sidebar-cache
