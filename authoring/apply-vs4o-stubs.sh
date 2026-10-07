#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs4-original
STUBS=$ROOT/pages/vs4-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs4o-stubs-import

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

echo "== importImages VS4O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS4O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs4o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs4o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 4 (Original) Remaster slip faces from VirtualCards4.pdf" \
  --overwrite \
  /tmp/vs4o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 4 (Original)" "$HUBS/Virtual_Set_4_(Original).wiki" "VS4 Original: link all 50 Remaster slip stubs"
edit '2-1B (Too-Onebee) (V) (Virtual Set 4)' "$STUBS/2-1B_(Too-Onebee)_(V)_(Virtual_Set_4).wiki" "VS4O stub 01"
edit 'Attack Pattern Delta (V) (Virtual Set 4)' "$STUBS/Attack_Pattern_Delta_(V)_(Virtual_Set_4).wiki" "VS4O stub 02"
edit 'Commander Luke Skywalker (V) (Virtual Set 4)' "$STUBS/Commander_Luke_Skywalker_(V)_(Virtual_Set_4).wiki" "VS4O stub 03"
edit 'Dark Dissension (V) (Virtual Set 4)' "$STUBS/Dark_Dissension_(V)_(Virtual_Set_4).wiki" "VS4O stub 04"
edit 'Dual Laser Cannon (V) (Virtual Set 4)' "$STUBS/Dual_Laser_Cannon_(V)_(Virtual_Set_4).wiki" "VS4O stub 05"
edit 'Echo Base Trooper Officer (V) (Virtual Set 4)' "$STUBS/Echo_Base_Trooper_Officer_(V)_(Virtual_Set_4).wiki" "VS4O stub 06"
edit 'Frostbite (V) (Virtual Set 4)' "$STUBS/Frostbite_(V)_(Virtual_Set_4).wiki" "VS4O stub 07"
edit 'General Carlist Rieekan (V) (Virtual Set 4)' "$STUBS/General_Carlist_Rieekan_(V)_(Virtual_Set_4).wiki" "VS4O stub 08"
edit 'Heroic Sacrifice (V) (Virtual Set 4)' "$STUBS/Heroic_Sacrifice_(V)_(Virtual_Set_4).wiki" "VS4O stub 09"
edit 'Hoth: Echo Med Lab (V) (Virtual Set 4)' "$STUBS/Hoth:_Echo_Med_Lab_(V)_(Virtual_Set_4).wiki" "VS4O stub 10"
edit 'Local Uprising (V) / Liberation (V) (Virtual Set 4)' "$STUBS/Local_Uprising_(V)_-_Liberation_(V)_(Virtual_Set_4).wiki" "VS4O stub 11"
edit 'Maneuvering Flaps (V) (Virtual Set 4)' "$STUBS/Maneuvering_Flaps_(V)_(Virtual_Set_4).wiki" "VS4O stub 12"
edit 'Nice Of You Guys To Drop By (V) (Virtual Set 4)' "$STUBS/Nice_Of_You_Guys_To_Drop_By_(V)_(Virtual_Set_4).wiki" "VS4O stub 13"
edit 'Nick Of Time (V) (Virtual Set 4)' "$STUBS/Nick_Of_Time_(V)_(Virtual_Set_4).wiki" "VS4O stub 14"
edit 'R5-M2 (Arfive-Emmtoo) (V) (Virtual Set 4)' "$STUBS/R5-M2_(Arfive-Emmtoo)_(V)_(Virtual_Set_4).wiki" "VS4O stub 15"
edit 'Rebel Scout (V) (Virtual Set 4)' "$STUBS/Rebel_Scout_(V)_(Virtual_Set_4).wiki" "VS4O stub 16"
edit 'Romas "Lock" Navander (V) (Virtual Set 4)' "$STUBS/Romas_"Lock"_Navander_(V)_(Virtual_Set_4).wiki" "VS4O stub 17"
edit 'Tamizander Rey (V) (Virtual Set 4)' "$STUBS/Tamizander_Rey_(V)_(Virtual_Set_4).wiki" "VS4O stub 18"
edit 'Tauntaun Bones (V) (Virtual Set 4)' "$STUBS/Tauntaun_Bones_(V)_(Virtual_Set_4).wiki" "VS4O stub 19"
edit 'Tauntaun Handler (V) (Virtual Set 4)' "$STUBS/Tauntaun_Handler_(V)_(Virtual_Set_4).wiki" "VS4O stub 20"
edit 'Tigran Jamiro (V) (Virtual Set 4)' "$STUBS/Tigran_Jamiro_(V)_(Virtual_Set_4).wiki" "VS4O stub 21"
edit 'Toryn Farr (V) (Virtual Set 4)' "$STUBS/Toryn_Farr_(V)_(Virtual_Set_4).wiki" "VS4O stub 22"
edit 'Walker Sighting (V) (Virtual Set 4)' "$STUBS/Walker_Sighting_(V)_(Virtual_Set_4).wiki" "VS4O stub 23"
edit 'Wyron Serper (V) (Virtual Set 4)' "$STUBS/Wyron_Serper_(V)_(Virtual_Set_4).wiki" "VS4O stub 24"
edit 'You Will Go To The Dagobah System (V) (Virtual Set 4)' "$STUBS/You_Will_Go_To_The_Dagobah_System_(V)_(Virtual_Set_4).wiki" "VS4O stub 25"
edit 'A Dark Time For The Rebellion (V) (Virtual Set 4)' "$STUBS/A_Dark_Time_For_The_Rebellion_(V)_(Virtual_Set_4).wiki" "VS4O stub 26"
edit 'AT-AT Cannon (V) (Virtual Set 4)' "$STUBS/AT-AT_Cannon_(V)_(Virtual_Set_4).wiki" "VS4O stub 27"
edit 'Blizzard 1 (V) (Virtual Set 4)' "$STUBS/Blizzard_1_(V)_(Virtual_Set_4).wiki" "VS4O stub 28"
edit 'Blizzard 2 (V) (Virtual Set 4)' "$STUBS/Blizzard_2_(V)_(Virtual_Set_4).wiki" "VS4O stub 29"
edit 'Blizzard Scout 1 (V) (Virtual Set 4)' "$STUBS/Blizzard_Scout_1_(V)_(Virtual_Set_4).wiki" "VS4O stub 30"
edit 'Breached Defenses (V) (Virtual Set 4)' "$STUBS/Breached_Defenses_(V)_(Virtual_Set_4).wiki" "VS4O stub 31"
edit 'Captain Lennox (V) (Virtual Set 4)' "$STUBS/Captain_Lennox_(V)_(Virtual_Set_4).wiki" "VS4O stub 32"
edit 'Captain Piett (V) (Virtual Set 4)' "$STUBS/Captain_Piett_(V)_(Virtual_Set_4).wiki" "VS4O stub 33"
edit 'Death Squadron (V) (Virtual Set 4)' "$STUBS/Death_Squadron_(V)_(Virtual_Set_4).wiki" "VS4O stub 34"
edit 'Debris Zone (V) (Virtual Set 4)' "$STUBS/Debris_Zone_(V)_(Virtual_Set_4).wiki" "VS4O stub 35"
edit 'Deflector Shield Generators (V) (Virtual Set 4)' "$STUBS/Deflector_Shield_Generators_(V)_(Virtual_Set_4).wiki" "VS4O stub 36"
edit 'General Veers (V) (Virtual Set 4)' "$STUBS/General_Veers_(V)_(Virtual_Set_4).wiki" "VS4O stub 37"
edit 'Image Of The Dark Lord (V) (Virtual Set 4)' "$STUBS/Image_Of_The_Dark_Lord_(V)_(Virtual_Set_4).wiki" "VS4O stub 38"
edit 'Imperial Domination (V) (Virtual Set 4)' "$STUBS/Imperial_Domination_(V)_(Virtual_Set_4).wiki" "VS4O stub 39"
edit 'Imperial Occupation (V) / Imperial Control (V) (Virtual Set 4)' "$STUBS/Imperial_Occupation_(V)_-_Imperial_Control_(V)_(Virtual_Set_4).wiki" "VS4O stub 40"
edit 'Krayt Dragon Bones (V) (Virtual Set 4)' "$STUBS/Krayt_Dragon_Bones_(V)_(Virtual_Set_4).wiki" "VS4O stub 41"
edit 'One-Arm (V) (Virtual Set 4)' "$STUBS/One-Arm_(V)_(Virtual_Set_4).wiki" "VS4O stub 42"
edit 'Probe Droid (V) (Virtual Set 4)' "$STUBS/Probe_Droid_(V)_(Virtual_Set_4).wiki" "VS4O stub 43"
edit 'Probe Telemetry (V) (Virtual Set 4)' "$STUBS/Probe_Telemetry_(V)_(Virtual_Set_4).wiki" "VS4O stub 44"
edit 'Security Precautions (V) (Virtual Set 4)' "$STUBS/Security_Precautions_(V)_(Virtual_Set_4).wiki" "VS4O stub 45"
edit 'Self-Destruct Mechanism (V) (Virtual Set 4)' "$STUBS/Self-Destruct_Mechanism_(V)_(Virtual_Set_4).wiki" "VS4O stub 46"
edit 'Sergeant Major Bursk (V) (Virtual Set 4)' "$STUBS/Sergeant_Major_Bursk_(V)_(Virtual_Set_4).wiki" "VS4O stub 47"
edit 'Stalker (V) (Virtual Set 4)' "$STUBS/Stalker_(V)_(Virtual_Set_4).wiki" "VS4O stub 48"
edit 'Stop Motion (V) (Virtual Set 4)' "$STUBS/Stop_Motion_(V)_(Virtual_Set_4).wiki" "VS4O stub 49"
edit 'Wampa (V) (Virtual Set 4)' "$STUBS/Wampa_(V)_(Virtual_Set_4).wiki" "VS4O stub 50"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 4 (Original)
2-1B (Too-Onebee) (V) (Virtual Set 4)
Attack Pattern Delta (V) (Virtual Set 4)
Commander Luke Skywalker (V) (Virtual Set 4)
Dark Dissension (V) (Virtual Set 4)
Dual Laser Cannon (V) (Virtual Set 4)
Echo Base Trooper Officer (V) (Virtual Set 4)
Frostbite (V) (Virtual Set 4)
General Carlist Rieekan (V) (Virtual Set 4)
Heroic Sacrifice (V) (Virtual Set 4)
Hoth: Echo Med Lab (V) (Virtual Set 4)
Local Uprising (V) / Liberation (V) (Virtual Set 4)
Maneuvering Flaps (V) (Virtual Set 4)
Nice Of You Guys To Drop By (V) (Virtual Set 4)
Nick Of Time (V) (Virtual Set 4)
R5-M2 (Arfive-Emmtoo) (V) (Virtual Set 4)
Rebel Scout (V) (Virtual Set 4)
Romas "Lock" Navander (V) (Virtual Set 4)
Tamizander Rey (V) (Virtual Set 4)
Tauntaun Bones (V) (Virtual Set 4)
Tauntaun Handler (V) (Virtual Set 4)
Tigran Jamiro (V) (Virtual Set 4)
Toryn Farr (V) (Virtual Set 4)
Walker Sighting (V) (Virtual Set 4)
Wyron Serper (V) (Virtual Set 4)
You Will Go To The Dagobah System (V) (Virtual Set 4)
A Dark Time For The Rebellion (V) (Virtual Set 4)
AT-AT Cannon (V) (Virtual Set 4)
Blizzard 1 (V) (Virtual Set 4)
Blizzard 2 (V) (Virtual Set 4)
Blizzard Scout 1 (V) (Virtual Set 4)
Breached Defenses (V) (Virtual Set 4)
Captain Lennox (V) (Virtual Set 4)
Captain Piett (V) (Virtual Set 4)
Death Squadron (V) (Virtual Set 4)
Debris Zone (V) (Virtual Set 4)
Deflector Shield Generators (V) (Virtual Set 4)
General Veers (V) (Virtual Set 4)
Image Of The Dark Lord (V) (Virtual Set 4)
Imperial Domination (V) (Virtual Set 4)
Imperial Occupation (V) / Imperial Control (V) (Virtual Set 4)
Krayt Dragon Bones (V) (Virtual Set 4)
One-Arm (V) (Virtual Set 4)
Probe Droid (V) (Virtual Set 4)
Probe Telemetry (V) (Virtual Set 4)
Security Precautions (V) (Virtual Set 4)
Self-Destruct Mechanism (V) (Virtual Set 4)
Sergeant Major Bursk (V) (Virtual Set 4)
Stalker (V) (Virtual Set 4)
Stop Motion (V) (Virtual Set 4)
Wampa (V) (Virtual Set 4)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=['2-1B_(Too-Onebee)_(V)_(Virtual_Set_4)', 'Attack_Pattern_Delta_(V)_(Virtual_Set_4)', 'Commander_Luke_Skywalker_(V)_(Virtual_Set_4)', 'Dark_Dissension_(V)_(Virtual_Set_4)', 'Dual_Laser_Cannon_(V)_(Virtual_Set_4)', 'Echo_Base_Trooper_Officer_(V)_(Virtual_Set_4)', 'Frostbite_(V)_(Virtual_Set_4)', 'General_Carlist_Rieekan_(V)_(Virtual_Set_4)', 'Heroic_Sacrifice_(V)_(Virtual_Set_4)', 'Hoth:_Echo_Med_Lab_(V)_(Virtual_Set_4)', 'Local_Uprising_(V)_/_Liberation_(V)_(Virtual_Set_4)', 'Maneuvering_Flaps_(V)_(Virtual_Set_4)', 'Nice_Of_You_Guys_To_Drop_By_(V)_(Virtual_Set_4)', 'Nick_Of_Time_(V)_(Virtual_Set_4)', 'R5-M2_(Arfive-Emmtoo)_(V)_(Virtual_Set_4)', 'Rebel_Scout_(V)_(Virtual_Set_4)', 'Romas_"Lock"_Navander_(V)_(Virtual_Set_4)', 'Tamizander_Rey_(V)_(Virtual_Set_4)', 'Tauntaun_Bones_(V)_(Virtual_Set_4)', 'Tauntaun_Handler_(V)_(Virtual_Set_4)', 'Tigran_Jamiro_(V)_(Virtual_Set_4)', 'Toryn_Farr_(V)_(Virtual_Set_4)', 'Walker_Sighting_(V)_(Virtual_Set_4)', 'Wyron_Serper_(V)_(Virtual_Set_4)', 'You_Will_Go_To_The_Dagobah_System_(V)_(Virtual_Set_4)', 'A_Dark_Time_For_The_Rebellion_(V)_(Virtual_Set_4)', 'AT-AT_Cannon_(V)_(Virtual_Set_4)', 'Blizzard_1_(V)_(Virtual_Set_4)', 'Blizzard_2_(V)_(Virtual_Set_4)', 'Blizzard_Scout_1_(V)_(Virtual_Set_4)', 'Breached_Defenses_(V)_(Virtual_Set_4)', 'Captain_Lennox_(V)_(Virtual_Set_4)', 'Captain_Piett_(V)_(Virtual_Set_4)', 'Death_Squadron_(V)_(Virtual_Set_4)', 'Debris_Zone_(V)_(Virtual_Set_4)', 'Deflector_Shield_Generators_(V)_(Virtual_Set_4)', 'General_Veers_(V)_(Virtual_Set_4)', 'Image_Of_The_Dark_Lord_(V)_(Virtual_Set_4)', 'Imperial_Domination_(V)_(Virtual_Set_4)', 'Imperial_Occupation_(V)_/_Imperial_Control_(V)_(Virtual_Set_4)', 'Krayt_Dragon_Bones_(V)_(Virtual_Set_4)', 'One-Arm_(V)_(Virtual_Set_4)', 'Probe_Droid_(V)_(Virtual_Set_4)', 'Probe_Telemetry_(V)_(Virtual_Set_4)', 'Security_Precautions_(V)_(Virtual_Set_4)', 'Self-Destruct_Mechanism_(V)_(Virtual_Set_4)', 'Sergeant_Major_Bursk_(V)_(Virtual_Set_4)', 'Stalker_(V)_(Virtual_Set_4)', 'Stop_Motion_(V)_(Virtual_Set_4)', 'Wampa_(V)_(Virtual_Set_4)']
for slug in slugs:
  u="https://wiki.swccg.com/wiki/"+urllib.parse.quote(slug, safe="()_,!/:\"")
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    ok=(r.status==200)
  except Exception:
    ok=False
  print(("PASS" if ok else "FAIL"), u)
  if ok: pass_n+=1
  else: fail.append(u)
print("STUBS %d/50 PASS fail=%s" % (pass_n, fail[:10]))
u="https://wiki.swccg.com/wiki/Virtual_Set_4_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS4O STUBS APPLY OK")
PY
