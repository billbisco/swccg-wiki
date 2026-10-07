#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
HUB="$ROOT/pages/set-hubs/Virtual_Set_1_(Original).wiki"

# ASCII check
python3 - <<PY
from pathlib import Path
p=Path("$HUB")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"):
  b=b[3:]; p.write_bytes(b)
assert sum(1 for c in b.decode("utf-8") if ord(c)>127)==0, "non-ascii in hub"
assert b"Set-VS1O-title.png|260px" not in b, "hero still in infobox"
assert b"decipher.com/starwars/cardlists" in b
print("hub ascii ok, hero gone, decipher cite present")
PY

STAGE=/tmp/vs1o-versions
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -f "$ROOT/images/original-vs1/vs1a-crops/"VS1A-*.png "$STAGE/"
cp -f "$ROOT/images/original-vs1/vs1-later/"VS1-Later-*.gif "$STAGE/"
ls "$STAGE" | wc -l

docker exec swccg_wiki mkdir -p /tmp/vs1o-versions
docker cp "$STAGE/." swccg_wiki:/tmp/vs1o-versions/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="VS1 Original slip version comparison: 1A crops + later Block1-pre proxies" \
  --overwrite \
  /tmp/vs1o-versions
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo "edit hub"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="VS1O hub: remove hero banner; Decipher cardlists provenance; 1A/Premium/Later slip comparison gallery" \
  "Virtual Set 1 (Original)" < "$HUB"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -3
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Virtual Set 1 (Original)
File:VS1A-01-Luke-Skywalker.png
File:VS1-Later-Luke-Skywalker.gif
File:VS1P-05-Luke-Skywalker.png
Main Page
EOF

python3 - <<'PY'
import subprocess, urllib.request
t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText","Virtual Set 1 (Original)"],text=True,errors="replace")
print("live nonascii", sum(1 for c in t if ord(c)>127))
print("hero260", "Set-VS1O-title.png|260px" in t)
print("decipher", "decipher.com/starwars/cardlists" in t)
print("provenance", "Provenance" in t)
print("gallery", "VS1A-01-Luke-Skywalker" in t and "VS1-Later-Luke-Skywalker" in t)
print("quote_snip", "Tournament-legal 03-09-02" in t or "tournament-legal 03-09-02" in t)
# Main Page still small thumb?
mp=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText","Main Page"],text=True,errors="replace")
import re
m=re.search(r"Set-VS1O-title[^\]]*\]", mp)
print("main_tile", m.group(0) if m else "NO_TITLE_FILE")
for u in [
 "https://wiki.swccg.com/wiki/Virtual_Set_1_(Original)",
 "https://wiki.swccg.com/wiki/Special:FilePath/VS1A-01-Luke-Skywalker.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/VS1-Later-Luke-Skywalker.gif",
]:
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=25)
    print(u, r.status, (r.headers.get("Content-Type") or "")[:50])
  except Exception as e:
    print(u, type(e).__name__, e)
print("APPLY DONE")
PY
