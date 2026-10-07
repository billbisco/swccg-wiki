#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/original-vc-packs
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vo-pack-recenter-import

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

echo "== importImages VO pack recenter =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
FILES=(
  VS2O-pack.png VS3O-pack.png VS4O-pack.png VS5O-pack.png VS6O-pack.png
  VS7O-pack.png VS8O-pack.png VS9O-pack.png VS11O-pack.png VS12O-pack.png
  VS13O-pack.png VS15O-pack.png VS16O-pack.png
)
for f in "${FILES[@]}"; do
  cp -f "$IMG/$f" "$STAGE/"
done
ls -la "$STAGE"
docker exec swccg_wiki mkdir -p /tmp/vo-pack-recenter-import
docker exec swccg_wiki bash -c 'rm -rf /tmp/vo-pack-recenter-import/*'
docker cp "$STAGE/." swccg_wiki:/tmp/vo-pack-recenter-import/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="VO Main Page pack thumbs: recenter/re-extract full pack face (even padding; no left gutter / right clip)" \
  --overwrite \
  /tmp/vo-pack-recenter-import
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

docker exec swccg_wiki php -r 'if(function_exists("apcu_clear_cache")){apcu_clear_cache(); echo "apcu cleared\n";} else {echo "no apcu\n";}'

for n in 2 3 4 5 6 7 8 9 11 12 13 15 16; do
  edit "Virtual Set ${n} (Original)" "$HUBS/Virtual_Set_${n}_(Original).wiki" "VS${n} Original: infobox primary = recentered VS${n}O-pack.png (same File as Main Page)"
done

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Main Page
Virtual Set 2 (Original)
Virtual Set 3 (Original)
Virtual Set 4 (Original)
Virtual Set 5 (Original)
Virtual Set 6 (Original)
Virtual Set 7 (Original)
Virtual Set 8 (Original)
Virtual Set 9 (Original)
Virtual Set 11 (Original)
Virtual Set 12 (Original)
Virtual Set 13 (Original)
Virtual Set 15 (Original)
Virtual Set 16 (Original)
File:VS2O-pack.png
File:VS3O-pack.png
File:VS4O-pack.png
File:VS5O-pack.png
File:VS6O-pack.png
File:VS7O-pack.png
File:VS8O-pack.png
File:VS9O-pack.png
File:VS11O-pack.png
File:VS12O-pack.png
File:VS13O-pack.png
File:VS15O-pack.png
File:VS16O-pack.png
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import subprocess, urllib.request, re
for n in [2,5,8,12,15,16]:
  title=f"Virtual Set {n} (Original)"
  t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],text=True,errors="replace")
  assert f"VS{n}O-pack.png" in t, title
  m=re.search(r'expansion-infobox.*?File:(VS\d+O-pack\.png|Set-VS\d+O-title\.png)', t, re.S)
  print(title, 'primary=', m.group(1) if m else 'NONE')
for u in [
 "https://wiki.swccg.com/wiki/Main_Page",
 "https://wiki.swccg.com/wiki/File:VS2O-pack.png",
 "https://wiki.swccg.com/wiki/File:VS15O-pack.png",
 "https://wiki.swccg.com/wiki/Virtual_Set_2_(Original)",
 "https://wiki.swccg.com/wiki/Virtual_Set_15_(Original)",
]:
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    print(u, r.status)
  except Exception as e:
    print(u, type(e).__name__, e)
print("VO PACK RECENTER APPLY OK")
PY
