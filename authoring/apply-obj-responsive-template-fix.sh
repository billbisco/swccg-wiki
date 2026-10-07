#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

python3 - "$PAGES/Template_Card.wiki" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PY

echo "edit Template:Card"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Fix image2_layout responsive nesting: #if concat for right|responsive side-by-side" "Template:Card" < "$PAGES/Template_Card.wiki"

echo "FlaggedRevs"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -5

for t in "Template:Card" "Set Your Course For Alderaan / The Ultimate Power In The Universe" "HoloNet Transmission" "Attack Run"; do
  echo "purge $t"
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done
echo DONE
