#!/bin/bash
set -euo pipefail
f=/opt/swccg-wiki/pages/2026_Retro_GEMPC_Kevin_Bing_LS_Profit.wiki
python3 - "$f" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print("stripped", p.name, len(text))
PY
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Dynamic two-column decklist balance (Profit alias)" \
  "2026 Retro GEMPC Kevin Bing LS Profit" < "$f"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -3
printf '%s\n' "2026 Retro GEMPC Kevin Bing LS Profit" | docker exec -i swccg_wiki php maintenance/run.php purgePage
echo DONE_PROFIT
