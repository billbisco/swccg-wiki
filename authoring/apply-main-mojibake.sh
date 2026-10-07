#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
FILE="$ROOT/pages/Main_Page.wiki"
python3 - <<'PY'
from pathlib import Path
p=Path("/opt/swccg-wiki/pages/Main_Page.wiki")
b=p.read_bytes()
assert b"\xc3\xa2\xe2\x82\xac" not in b, "mojibake dash still present"
assert b"\xc3\x82\xc2\xb7" not in b, "mojibake middot still present"
assert b"2014&ndash;" in b
print("precheck ok", len(b))
PY
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Main Page: fix UTF-8 mojibake; HTML entities for dashes/middots" "Main Page" < "$FILE"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec swccg_wiki php maintenance/run.php purgePage "Main Page" 2>/dev/null || true
echo "--- verify ---"
docker exec swccg_wiki php maintenance/run.php getText "Main Page" 2>/dev/null | grep -nE "Current Virtual|Labeled virtual|printed 1995|Rulebooks" | head -10
echo DONE
