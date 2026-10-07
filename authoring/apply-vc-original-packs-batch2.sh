#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/original-vc-packs
HUBS=$ROOT/pages/set-hubs
PAGES=$ROOT/pages
STAGE=/tmp/vc-packs-b2-import

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

echo "== importImages batch2 VS7-13+16 =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
for f in \
  VS7O-pack.png VS7O-set-symbol.png Set-VS7O-title.png \
  VS8O-pack.png VS8O-set-symbol.png Set-VS8O-title.png \
  VS9O-pack.png VS9O-set-symbol.png Set-VS9O-title.png \
  VS10O-pack.png VS10O-set-symbol.png Set-VS10O-title.png \
  VS11O-pack.png VS11O-set-symbol.png Set-VS11O-title.png \
  VS12O-pack.png VS12O-set-symbol.png Set-VS12O-title.png \
  VS13O-pack.png VS13O-set-symbol.png Set-VS13O-title.png \
  VS16O-pack.png VS16O-set-symbol.png Set-VS16O-title.png
do
  cp -f "$IMG/$f" "$STAGE/"
done
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vc-packs-b2-import
docker exec swccg_wiki bash -c 'rm -rf /tmp/vc-packs-b2-import/*'
docker cp "$STAGE/." swccg_wiki:/tmp/vc-packs-b2-import/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Original Virtual VS7-13+16 Remaster pack+symbol from VirtualCards{N}.pdf (IA Wayback)" \
  --overwrite \
  /tmp/vc-packs-b2-import
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

for n in 7 8 9 10 11 12 13 16; do
  edit "Virtual Set ${n} (Original)" "$HUBS/Virtual_Set_${n}_(Original).wiki" "VS${n} Original: Remaster pack+symbol from VirtualCards${n}.pdf (IA)"
done
edit "Main Page" "$PAGES/Main_Page.wiki" "Original band: VS7-13+16 Remaster pack tiles"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -5

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 7 (Original)
Virtual Set 8 (Original)
Virtual Set 9 (Original)
Virtual Set 10 (Original)
Virtual Set 11 (Original)
Virtual Set 12 (Original)
Virtual Set 13 (Original)
Virtual Set 16 (Original)
Main Page
File:Set-VS7O-title.png
File:Set-VS10O-title.png
File:Set-VS16O-title.png
File:VS7O-pack.png
File:VS10O-pack.png
File:VS16O-set-symbol.png
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import subprocess, urllib.request
for n in [7,8,9,10,11,12,13,16]:
  title=f"Virtual Set {n} (Original)"
  t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],text=True,errors="replace")
  non=sum(1 for c in t if ord(c)>127)
  assert "Remaster" in t or "VirtualCards" in t
  print(f"{title}: nonascii={non} ok")
for u in [
 "https://wiki.swccg.com/wiki/Virtual_Set_7_(Original)",
 "https://wiki.swccg.com/wiki/Virtual_Set_10_(Original)",
 "https://wiki.swccg.com/wiki/Virtual_Set_16_(Original)",
 "https://wiki.swccg.com/wiki/File:VS10O-pack.png",
 "https://wiki.swccg.com/wiki/File:Set-VS16O-title.png",
]:
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    print(u, r.status)
  except Exception as e:
    print(u, type(e).__name__, e)
print("VC ORIGINAL PACKS BATCH2 APPLY OK")
PY