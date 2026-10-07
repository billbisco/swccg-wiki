#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/original-vc-packs
HUBS=$ROOT/pages/set-hubs
PAGES=$ROOT/pages
STAGE=/tmp/vc-packs-b3-import

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

echo "== importImages batch3 VS14+15+17 =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
for f in \
  VS14O-pack.png VS14O-set-symbol.png Set-VS14O-title.png \
  VS15O-pack.png VS15O-set-symbol.png Set-VS15O-title.png \
  VS17O-pack.png VS17O-set-symbol.png Set-VS17O-title.png
do
  cp -f "$IMG/$f" "$STAGE/"
done
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vc-packs-b3-import
docker exec swccg_wiki bash -c 'rm -rf /tmp/vc-packs-b3-import/*'
docker cp "$STAGE/." swccg_wiki:/tmp/vc-packs-b3-import/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Original Virtual VS14/15/17 cover pack+symbol from VirtualCards{N}.pdf (CDN legacyblocks)" \
  --overwrite \
  /tmp/vc-packs-b3-import
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

for n in 14 15 17; do
  edit "Virtual Set ${n} (Original)" "$HUBS/Virtual_Set_${n}_(Original).wiki" "VS${n} Original: cover pack+symbol from VirtualCards${n}.pdf (CDN legacyblocks)"
done
edit "Main Page" "$PAGES/Main_Page.wiki" "Original band: VS14/15/17 cover pack tiles"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -5

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 14 (Original)
Virtual Set 15 (Original)
Virtual Set 17 (Original)
Main Page
File:Set-VS14O-title.png
File:Set-VS15O-title.png
File:Set-VS17O-title.png
File:VS14O-pack.png
File:VS15O-pack.png
File:VS17O-pack.png
File:VS14O-set-symbol.png
File:VS15O-set-symbol.png
File:VS17O-set-symbol.png
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import subprocess, urllib.request
for n in [14,15,17]:
  title=f"Virtual Set {n} (Original)"
  t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],text=True,errors="replace")
  non=sum(1 for c in t if ord(c)>127)
  assert "VirtualCards" in t or "legacyblocks" in t or "Cover" in t or "pack" in t.lower()
  print(f"{title}: nonascii={non} ok")
for u in [
 "https://wiki.swccg.com/wiki/Virtual_Set_14_(Original)",
 "https://wiki.swccg.com/wiki/Virtual_Set_15_(Original)",
 "https://wiki.swccg.com/wiki/Virtual_Set_17_(Original)",
 "https://wiki.swccg.com/wiki/File:VS14O-pack.png",
 "https://wiki.swccg.com/wiki/File:Set-VS15O-title.png",
 "https://wiki.swccg.com/wiki/File:VS17O-set-symbol.png",
]:
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    print(u, r.status)
  except Exception as e:
    print(u, type(e).__name__, e)
print("VC ORIGINAL PACKS BATCH3 APPLY OK")
PY
