#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/original-vc-packs
HUBS=$ROOT/pages/set-hubs
PAGES=$ROOT/pages
STAGE=/tmp/vc-packs-b1-import

strip() {
  python3 - <<PY
from pathlib import Path
p=Path("$1")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"): b=b[3:]
p.write_bytes(b)
n=sum(1 for c in b.decode("utf-8") if ord(c)>127)
print(f"  {p.name} nonascii={n}")
assert n==0, p
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip "$file"
  echo "edit: $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

echo "== importImages batch1 VS2-6 =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
# Only the File: assets (avoid raw duplicates if any)
for f in \
  VS2O-pack.png VS2O-set-symbol.png Set-VS2O-title.png \
  VS3O-pack.png VS3O-set-symbol.png Set-VS3O-title.png \
  VS4O-pack.png VS4O-set-symbol.png Set-VS4O-title.png \
  VS5O-pack.png VS5O-set-symbol.png Set-VS5O-title.png \
  VS6O-pack.png VS6O-set-symbol.png Set-VS6O-title.png
do
  cp -f "$IMG/$f" "$STAGE/"
done
ls -la "$STAGE"
docker exec swccg_wiki mkdir -p /tmp/vc-packs-b1-import
docker exec swccg_wiki rm -rf /tmp/vc-packs-b1-import/*
docker cp "$STAGE/." swccg_wiki:/tmp/vc-packs-b1-import/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Original Virtual VS2-6 Remaster pack+symbol from VirtualCards{N}.pdf (IA Wayback)" \
  --overwrite \
  /tmp/vc-packs-b1-import
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 2 (Original)" "$HUBS/Virtual_Set_2_(Original).wiki" "VS2 Original: Remaster pack+symbol from VirtualCards2.pdf (IA)"
edit "Virtual Set 3 (Original)" "$HUBS/Virtual_Set_3_(Original).wiki" "VS3 Original: Remaster pack+symbol from VirtualCards3.pdf (IA)"
edit "Virtual Set 4 (Original)" "$HUBS/Virtual_Set_4_(Original).wiki" "VS4 Original: Remaster pack+symbol from VirtualCards4.pdf (IA)"
edit "Virtual Set 5 (Original)" "$HUBS/Virtual_Set_5_(Original).wiki" "VS5 Original: Remaster pack+symbol from VirtualCards5.pdf (IA)"
edit "Virtual Set 6 (Original)" "$HUBS/Virtual_Set_6_(Original).wiki" "VS6 Original: Remaster pack+symbol from VirtualCards6.pdf (IA)"
edit "Main Page" "$PAGES/Main_Page.wiki" "Original band: VS2-6 Remaster pack tiles"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 2 (Original)
Virtual Set 3 (Original)
Virtual Set 4 (Original)
Virtual Set 5 (Original)
Virtual Set 6 (Original)
Main Page
File:Set-VS2O-title.png
File:Set-VS3O-title.png
File:Set-VS4O-title.png
File:Set-VS5O-title.png
File:Set-VS6O-title.png
File:VS2O-pack.png
File:VS2O-set-symbol.png
File:VS3O-pack.png
File:VS3O-set-symbol.png
File:VS4O-pack.png
File:VS4O-set-symbol.png
File:VS5O-pack.png
File:VS5O-set-symbol.png
File:VS6O-pack.png
File:VS6O-set-symbol.png
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import subprocess, urllib.request
titles = [
 "Virtual Set 2 (Original)",
 "Virtual Set 3 (Original)",
 "Virtual Set 4 (Original)",
 "Virtual Set 5 (Original)",
 "Virtual Set 6 (Original)",
 "Main Page",
]
for title in titles:
  t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],text=True,errors="replace")
  non=sum(1 for c in t if ord(c)>127)
  print(f"{title}: nonascii={non} len={len(t)}")
  if title.startswith("Virtual Set"):
    assert "Remaster" in t or "VirtualCards" in t
    assert "set-symbol" in t or "VS" in t
for u in [
 "https://wiki.swccg.com/wiki/Virtual_Set_2_(Original)",
 "https://wiki.swccg.com/wiki/Virtual_Set_3_(Original)",
 "https://wiki.swccg.com/wiki/Virtual_Set_6_(Original)",
 "https://wiki.swccg.com/wiki/Special:FilePath/Set-VS2O-title.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/VS2O-set-symbol.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/VS6O-pack.png",
]:
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    print(u, r.status)
  except Exception as e:
    print(u, type(e).__name__, e)
print("VC ORIGINAL PACKS BATCH1 (VS2-6) APPLY OK")
PY