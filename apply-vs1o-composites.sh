#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
HUB="$ROOT/pages/set-hubs/Virtual_Set_1_(Original).wiki"
CARDS="$ROOT/pages/original-vs1"

python3 - <<PY
from pathlib import Path
p=Path("$HUB")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"):
  b=b[3:]; p.write_bytes(b)
assert sum(1 for c in b.decode("utf-8") if ord(c)>127)==0
assert b"VS1O-05-Luke-Skywalker-composite" in b
assert b"VS1A-gal-05" in b and b"VS1P-gal-05" in b and b"VS1L-gal-05" in b
print("hub ok")
for f in Path("$CARDS").glob("*.wiki"):
  t=f.read_bytes()
  if t.startswith(b"\xef\xbb\xbf"):
    t=t[3:]; f.write_bytes(t)
  assert sum(1 for c in t.decode("utf-8") if ord(c)>127)==0, f
  assert b"VS1O-" in t and b"composite.png" in t, f
print("cards ok", len(list(Path("$CARDS").glob("*.wiki"))))
PY

STAGE=/tmp/vs1o-composites
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -f "$ROOT/images/original-vs1/vs1-composites/"VS1O-*-composite.png "$STAGE/"
cp -f "$ROOT/images/original-vs1/vs1-composites/gallery-thumbs/"*.png "$STAGE/"
echo "stage count $(ls "$STAGE" | wc -l)"

docker exec swccg_wiki mkdir -p /tmp/vs1o-composites
docker cp "$STAGE/." swccg_wiki:/tmp/vs1o-composites/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="VS1 Original: Premium+Decipher composites + equal-size slip gallery thumbs" \
  --overwrite \
  /tmp/vs1o-composites
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit() {
  echo "edit: $1"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$3" "$1" < "$2"
}

edit "Virtual Set 1 (Original)" "$HUB" "VS1O: equal slip gallery thumbs; card list composites; Premium+Decipher amalgamates"
edit "Bo Shek (V) (Virtual Set 1 Original)" "$CARDS/Bo_Shek_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)" "$CARDS/Fusion_Generator_Supply_Tanks_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Gold 1 (V) (Virtual Set 1 Original)" "$CARDS/Gold_1_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)" "$CARDS/Hans_Heavy_Blaster_Pistol_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Luke Skywalker (V) (Virtual Set 1 Original)" "$CARDS/Luke_Skywalker_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Sai'torr Kal Fas (V) (Virtual Set 1 Original)" "$CARDS/Saitorr_Kal_Fas_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Assault Rifle (V) (Virtual Set 1 Original)" "$CARDS/Assault_Rifle_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Black 2 (V) (Virtual Set 1 Original)" "$CARDS/Black_2_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Blaster Rack (V) (Virtual Set 1 Original)" "$CARDS/Blaster_Rack_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Darth Vader (V) (Virtual Set 1 Original)" "$CARDS/Darth_Vader_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)" "$CARDS/Fusion_Generator_Supply_Tanks_(V)_(Dark)_(Virtual_Set_1_Original).wiki" "VS1O composite face"
edit "Prophetess (V) (Virtual Set 1 Original)" "$CARDS/Prophetess_(V)_(Virtual_Set_1_Original).wiki" "VS1O composite face"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -3
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Virtual Set 1 (Original)
Bo Shek (V) (Virtual Set 1 Original)
Luke Skywalker (V) (Virtual Set 1 Original)
Darth Vader (V) (Virtual Set 1 Original)
Gold 1 (V) (Virtual Set 1 Original)
Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)
Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)
Prophetess (V) (Virtual Set 1 Original)
File:VS1O-05-Luke-Skywalker-composite.png
File:VS1A-gal-05-Luke-Skywalker.png
File:VS1P-gal-05-Luke-Skywalker.png
Main Page
EOF

python3 - <<'PY'
import subprocess, urllib.request, re
for title in [
 "Virtual Set 1 (Original)",
 "Luke Skywalker (V) (Virtual Set 1 Original)",
 "Bo Shek (V) (Virtual Set 1 Original)",
 "Darth Vader (V) (Virtual Set 1 Original)",
]:
  t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],text=True,errors="replace")
  print(title, "nonascii", sum(1 for c in t if ord(c)>127), "composite", "composite.png" in t or "VS1O-" in t, "gal_equal", "VS1A-gal-" in t and "VS1P-gal-" in t if "Virtual Set 1"==title[:14] else "n/a")
urls=[
 "https://wiki.swccg.com/wiki/Luke_Skywalker_(V)_(Virtual_Set_1_Original)",
 "https://wiki.swccg.com/wiki/Bo_Shek_(V)_(Virtual_Set_1_Original)",
 "https://wiki.swccg.com/wiki/Darth_Vader_(V)_(Virtual_Set_1_Original)",
 "https://wiki.swccg.com/wiki/Special:FilePath/VS1O-05-Luke-Skywalker-composite.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/VS1A-gal-05-Luke-Skywalker.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/VS1P-gal-05-Luke-Skywalker.png",
 "https://wiki.swccg.com/wiki/Virtual_Set_1_(Original)",
]
for u in urls:
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=25)
    print(u, r.status, (r.headers.get("Content-Type") or "")[:40])
  except Exception as e:
    print(u, type(e).__name__, e)
print("APPLY DONE")
PY
