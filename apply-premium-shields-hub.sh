#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/premium-shields
HUBS=$ROOT/pages/set-hubs
PAGES=$ROOT/pages
ICONS=$ROOT/pages/icons
STAGE=/tmp/ps1-import

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

echo "== importImages =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/*.png "$STAGE/"
ls -la "$STAGE"
docker exec swccg_wiki mkdir -p /tmp/ps1-import
docker cp "$STAGE/." swccg_wiki:/tmp/ps1-import/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Premium Set 1 Defensive Shields: pack/symbol/icon-key/slips from DefensiveShields.pdf (IA)" \
  --overwrite \
  /tmp/ps1-import
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Premium Set 1: Defensive Shields" "$HUBS/Premium_Set_1_Defensive_Shields.wiki" "Premium Set 1: Defensive Shields hub from DefensiveShields.pdf (IA Dec 2006)"
edit "Virtual Shields (Original)" "$HUBS/Virtual_Shields_(Original).wiki" "Redirect to Premium Set 1: Defensive Shields (Bill naming lock)"
edit "Virtual card icons" "$ICONS/Virtual_card_icons.wiki" "Cite DefensiveShields.pdf ICON KEY (Premium Set 1)"
edit "Main Page" "$PAGES/Main_Page.wiki" "Original band tile: Premium Set 1: Defensive Shields"
edit "Virtual Sets (2002-2009)" "$PAGES/Virtual_Sets_(2002-2009).wiki" "Premium row: DefensiveShields.pdf + Premium Set 1 hub"
edit "Virtual Shields" "$HUBS/Virtual_Shields.wiki" "Point Original-era note to Premium Set 1: Defensive Shields"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -5

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Premium Set 1: Defensive Shields
Virtual Shields (Original)
Virtual card icons
Main Page
Virtual Sets (2002-2009)
Virtual Shields
File:Set-PS1-title.png
File:PS1-DefensiveShields-set-symbol.png
File:PS1-DefensiveShields-pack.png
File:PS1-DefensiveShields-icon-key.png
File:PS1-DefensiveShields-slips-sheet.png
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import subprocess, urllib.request
titles = [
 "Premium Set 1: Defensive Shields",
 "Virtual Shields (Original)",
 "Virtual card icons",
 "Main Page",
]
for title in titles:
  t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],text=True,errors="replace")
  non=sum(1 for c in t if ord(c)>127)
  print(f"{title}: nonascii={non} len={len(t)}")
  if title.startswith("Premium"):
    assert "DefensiveShields.pdf" in t
    assert "Premium Set 1" in t
  if title == "Virtual Shields (Original)":
    assert "REDIRECT" in t and "Premium Set 1: Defensive Shields" in t
for u in [
 "https://wiki.swccg.com/wiki/Premium_Set_1:_Defensive_Shields",
 "https://wiki.swccg.com/wiki/Virtual_Shields_(Original)",
 "https://wiki.swccg.com/wiki/Special:FilePath/Set-PS1-title.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/PS1-DefensiveShields-set-symbol.png",
]:
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    print(u, r.status)
  except Exception as e:
    print(u, type(e).__name__, e)
print("PREMIUM SHIELDS HUB APPLY OK")
PY
