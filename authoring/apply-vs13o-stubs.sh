#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs13-original
STUBS=$ROOT/pages/vs13-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs13o-stubs-import

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

echo "== importImages VS13O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS13O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs13o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs13o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 13 (Original) Remaster slip faces from VirtualCards13.pdf" \
  --overwrite \
  /tmp/vs13o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 13 (Original)" "$HUBS/Virtual_Set_13_(Original).wiki" "VS13 Original: link all 25 Remaster slip stubs"

edit 'Asteroid Field (Light) (V) (Virtual Set 13)' "$STUBS/Asteroid_Field_(Light)_(V)_(Virtual_Set_13).wiki" "VS13O stub 01"
edit 'Chasm (V) (Virtual Set 13)' "$STUBS/Chasm_(V)_(Virtual_Set_13).wiki" "VS13O stub 02"
edit 'Coruscant: Docking Bay (Light) (V) (Virtual Set 13)' "$STUBS/Coruscant__Docking_Bay_(Light)_(V)_(Virtual_Set_13).wiki" "VS13O stub 03"
edit 'Yavin 4: Docking Bay (Light) (V) (Virtual Set 13)' "$STUBS/Yavin_4__Docking_Bay_(Light)_(V)_(Virtual_Set_13).wiki" "VS13O stub 04"
edit 'Darklighter Spin (V) (Virtual Set 13)' "$STUBS/Darklighter_Spin_(V)_(Virtual_Set_13).wiki" "VS13O stub 05"
edit 'Eyes In The Dark (V) (Virtual Set 13)' "$STUBS/Eyes_In_The_Dark_(V)_(Virtual_Set_13).wiki" "VS13O stub 06"
edit 'Jek Porkins (V) (Virtual Set 13)' "$STUBS/Jek_Porkins_(V)_(Virtual_Set_13).wiki" "VS13O stub 07"
edit 'Lieutenant Williams (V) (Virtual Set 13)' "$STUBS/Lieutenant_Williams_(V)_(Virtual_Set_13).wiki" "VS13O stub 08"
edit 'Endor: Back Door (Light) (V) (Virtual Set 13)' "$STUBS/Endor__Back_Door_(Light)_(V)_(Virtual_Set_13).wiki" "VS13O stub 09"
edit 'Perimeter Scan (V) (Virtual Set 13)' "$STUBS/Perimeter_Scan_(V)_(Virtual_Set_13).wiki" "VS13O stub 10"
edit 'Yavin 4: Briefing Room (V) (Virtual Set 13)' "$STUBS/Yavin_4__Briefing_Room_(V)_(Virtual_Set_13).wiki" "VS13O stub 11"
edit 'Through The Force Things You Will See (V) (Virtual Set 13)' "$STUBS/Through_The_Force_Things_You_Will_See_(V)_(Virtual_Set_13).wiki" "VS13O stub 12"
edit 'Abyss (V) (Virtual Set 13)' "$STUBS/Abyss_(V)_(Virtual_Set_13).wiki" "VS13O stub 13"
edit 'Executor: Comm Station (V) (Virtual Set 13)' "$STUBS/Executor__Comm_Station_(V)_(Virtual_Set_13).wiki" "VS13O stub 14"
edit 'Spaceport Street (Dark) (V) (Virtual Set 13)' "$STUBS/Spaceport_Street_(Dark)_(V)_(Virtual_Set_13).wiki" "VS13O stub 15"
edit 'ComScan Detection (V) (Virtual Set 13)' "$STUBS/ComScan_Detection_(V)_(Virtual_Set_13).wiki" "VS13O stub 16"
edit 'Naboo: Theed Palace Hallway (Dark) (V) (Virtual Set 13)' "$STUBS/Naboo__Theed_Palace_Hallway_(Dark)_(V)_(Virtual_Set_13).wiki" "VS13O stub 17"
edit "Jabba's Palace: Dungeon (V) (Virtual Set 13)" "$STUBS/Jabbas_Palace__Dungeon_(V)_(Virtual_Set_13).wiki" "VS13O stub 18"
edit "Spaceport Prefect's Office (V) (Virtual Set 13)" "$STUBS/Spaceport_Prefects_Office_(V)_(Virtual_Set_13).wiki" "VS13O stub 19"
edit 'Hoth: Echo Command Center (War Room) (Dark) (V) (Virtual Set 13)' "$STUBS/Hoth__Echo_Command_Center_(War_Room)_(Dark)_(V)_(Virtual_Set_13).wiki" "VS13O stub 20"
edit 'Tatooine: Desert Landing Site (V) (Virtual Set 13)' "$STUBS/Tatooine__Desert_Landing_Site_(V)_(Virtual_Set_13).wiki" "VS13O stub 21"
edit 'Big One: Asteroid Cave or Space Slug Belly (Dark) (V) (Virtual Set 13)' "$STUBS/Big_One__Asteroid_Cave_or_Space_Slug_Belly_(Dark)_(V)_(Virtual_Set_13).wiki" "VS13O stub 22"
edit 'Quietly Observing (V) (Virtual Set 13)' "$STUBS/Quietly_Observing_(V)_(Virtual_Set_13).wiki" "VS13O stub 23"
edit 'Tatooine: Jawa Canyon (Dark) (V) (Virtual Set 13)' "$STUBS/Tatooine__Jawa_Canyon_(Dark)_(V)_(Virtual_Set_13).wiki" "VS13O stub 24"
edit 'Watch Your Back! (V) (Virtual Set 13)' "$STUBS/Watch_Your_Back!_(V)_(Virtual_Set_13).wiki" "VS13O stub 25"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "== purgePage hub + stubs + samples =="
docker exec swccg_wiki php maintenance/run.php purgePage 'Virtual Set 13 (Original)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Main Page' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Category:Virtual Original sets' || true

docker exec swccg_wiki php maintenance/run.php purgePage 'Asteroid Field (Light) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Chasm (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Coruscant: Docking Bay (Light) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Yavin 4: Docking Bay (Light) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Darklighter Spin (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Eyes In The Dark (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Jek Porkins (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Lieutenant Williams (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Endor: Back Door (Light) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Perimeter Scan (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Yavin 4: Briefing Room (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Through The Force Things You Will See (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Abyss (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Executor: Comm Station (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Spaceport Street (Dark) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'ComScan Detection (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Naboo: Theed Palace Hallway (Dark) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage "Jabba's Palace: Dungeon (V) (Virtual Set 13)" || true
docker exec swccg_wiki php maintenance/run.php purgePage "Spaceport Prefect's Office (V) (Virtual Set 13)" || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Hoth: Echo Command Center (War Room) (Dark) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Tatooine: Desert Landing Site (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Big One: Asteroid Cave or Space Slug Belly (Dark) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Quietly Observing (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Tatooine: Jawa Canyon (Dark) (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Watch Your Back! (V) (Virtual Set 13)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS13O-01-Asteroid_Field_Light.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS13O-07-Jek_Porkins.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS13O-12-Through_The_Force_Things_You_Will_See.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS13O-18-Jabbas_Palace_Dungeon.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS13O-25-Watch_Your_Back.png' || true
echo VS13O_APPLY_DONE
