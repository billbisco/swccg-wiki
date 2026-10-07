#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
FILE_WIKI="$PAGES/File_ANH-L-attackrun-wb-decipher.gif.wiki"
HT_EXPECTED=3a3ee5afcd96a081a9ae73b683a4001c93ad862c

ht_hex() {
  docker exec swccg_wiki sha1sum /var/www/html/images/5/58/ANH-L-attackrun.gif | awk '{print $1}'
}

echo "== Holotable BEFORE (page-edit only; no importImages) =="
HT_BEFORE=$(ht_hex)
echo "ht_before=$HT_BEFORE"
test "$HT_BEFORE" = "$HT_EXPECTED"

python3 - "$FILE_WIKI" <<'PY'
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

echo "== edit File:ANH-L-attackrun-wb-decipher.gif =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="WB File summary: white-border crop 348x488 + BR bleach; baseline on Attack Run/Errata; Holotable on PC Errata only" \
  "File:ANH-L-attackrun-wb-decipher.gif" < "$FILE_WIKI"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

echo "purge File:ANH-L-attackrun-wb-decipher.gif"
docker exec swccg_wiki php maintenance/run.php purgePage "File:ANH-L-attackrun-wb-decipher.gif" 2>/dev/null \
  || docker exec swccg_wiki php maintenance/purgePage.php "File:ANH-L-attackrun-wb-decipher.gif" 2>/dev/null \
  || true

echo "== Holotable AFTER =="
HT_AFTER=$(ht_hex)
echo "ht_after=$HT_AFTER"
test "$HT_AFTER" = "$HT_EXPECTED"
echo "DONE_FILE_DESC"
