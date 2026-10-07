#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
CARDS=$ROOT/pages/original-vs1
HUBS=$ROOT/pages/set-hubs
PAGES=$ROOT/pages
strip() {
  python3 - <<PY
from pathlib import Path
p=Path("$1")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"): b=b[3:]
p.write_bytes(b)
assert sum(1 for c in b.decode("utf-8") if ord(c)>127)==0
PY
}
edit() {
  strip "$2"
  echo "edit: $1"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$3" "$1" < "$2"
}
# retry import without failing the script
STAGE=/tmp/vs1o-import
mkdir -p "$STAGE"
cp -f $ROOT/images/original-vs1/*.png "$STAGE/"
docker exec swccg_wiki mkdir -p /tmp/vs1o-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs1o-import/
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="VS1 Original slips" --overwrite /tmp/vs1o-import || echo "importImages had failures (may already exist)"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 1 (Original)" "$HUBS/Virtual_Set_1_(Original).wiki" "VS1 Original hub: Premium 12-slip list + Sources"
edit "Main Page" "$PAGES/Main_Page.wiki" "Original band: VS1 Premium pack placeholder tile"
edit "Bo Shek (V) (Virtual Set 1 Original)" "$CARDS/Bo_Shek_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 01"
edit "Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)" "$CARDS/Fusion_Generator_Supply_Tanks_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 02"
edit "Gold 1 (V) (Virtual Set 1 Original)" "$CARDS/Gold_1_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 03"
edit "Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)" "$CARDS/Hans_Heavy_Blaster_Pistol_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 04"
edit "Luke Skywalker (V) (Virtual Set 1 Original)" "$CARDS/Luke_Skywalker_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 05"
edit "Sai'torr Kal Fas (V) (Virtual Set 1 Original)" "$CARDS/Saitorr_Kal_Fas_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 06"
edit "Assault Rifle (V) (Virtual Set 1 Original)" "$CARDS/Assault_Rifle_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 07"
edit "Black 2 (V) (Virtual Set 1 Original)" "$CARDS/Black_2_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 08"
edit "Blaster Rack (V) (Virtual Set 1 Original)" "$CARDS/Blaster_Rack_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 09"
edit "Darth Vader (V) (Virtual Set 1 Original)" "$CARDS/Darth_Vader_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 10"
edit "Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)" "$CARDS/Fusion_Generator_Supply_Tanks_(V)_(Dark)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 11"
edit "Prophetess (V) (Virtual Set 1 Original)" "$CARDS/Prophetess_(V)_(Virtual_Set_1_Original).wiki" "VS1 Original slip 12"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -3
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Main Page
Virtual Set 1 (Original)
Bo Shek (V) (Virtual Set 1 Original)
Luke Skywalker (V) (Virtual Set 1 Original)
Darth Vader (V) (Virtual Set 1 Original)
Sai'torr Kal Fas (V) (Virtual Set 1 Original)
Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)
Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)
Category:Virtual Original sets
EOF
python3 - <<'PY'
import subprocess
for title in ["Virtual Set 1 (Original)","Bo Shek (V) (Virtual Set 1 Original)","Luke Skywalker (V) (Virtual Set 1 Original)","Darth Vader (V) (Virtual Set 1 Original)","Main Page"]:
  t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],text=True,errors="replace")
  print(title, "nonascii", sum(1 for c in t if ord(c)>127), "moj", any(x in t for x in ["â€","Â·","Ã¢"]))
print("OK")
PY