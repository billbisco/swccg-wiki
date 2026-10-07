#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
python3 - "$PAGES/Errata.wiki" <<'PYINNER'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PYINNER
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Errata hub: add Reason column (source-stated only; HoloNet + Great Warrior filled)" \
  "Errata" < "$PAGES/Errata.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8
docker exec swccg_wiki php maintenance/run.php purgePage "Errata" 2>/dev/null || true
echo "== DONE errata-reason-col =="
