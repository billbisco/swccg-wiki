#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs5-original
STUBS=$ROOT/pages/vs5-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs5o-stubs-import

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

echo "== importImages VS5O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS5O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs5o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs5o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 5 (Original) Remaster slip faces from VirtualCards5.pdf" \
  --overwrite \
  /tmp/vs5o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true


edit "Virtual Set 5 (Original)" "$HUBS/Virtual_Set_5_(Original).wiki" "VS5 Original: link all 50 Remaster slip stubs"

edit 'Asteroids Do Not Concern Me (V) (Virtual Set 5)' "$STUBS/Asteroids_Do_Not_Concern_Me_(V)_(Virtual_Set_5).wiki" "VS5O stub 01"
edit 'Away Put Your Weapon (V) (Virtual Set 5)' "$STUBS/Away_Put_Your_Weapon_(V)_(Virtual_Set_5).wiki" "VS5O stub 02"
edit 'Bron Burs (V) (Virtual Set 5)' "$STUBS/Bron_Burs_(V)_(Virtual_Set_5).wiki" "VS5O stub 03"
edit 'Descent Into The Dark (V) (Virtual Set 5)' "$STUBS/Descent_Into_The_Dark_(V)_(Virtual_Set_5).wiki" "VS5O stub 04"
edit 'Encampment (V) (Virtual Set 5)' "$STUBS/Encampment_(V)_(Virtual_Set_5).wiki" "VS5O stub 05"
edit 'Flash Of Insight (V) (Virtual Set 5)' "$STUBS/Flash_Of_Insight_(V)_(Virtual_Set_5).wiki" "VS5O stub 06"
edit 'Found Someone You Have (V) (Virtual Set 5)' "$STUBS/Found_Someone_You_Have_(V)_(Virtual_Set_5).wiki" "VS5O stub 07"
edit 'Harc Seff (V) (Virtual Set 5)' "$STUBS/Harc_Seff_(V)_(Virtual_Set_5).wiki" "VS5O stub 08"
edit 'Hiding In The Garbage (V) (Virtual Set 5)' "$STUBS/Hiding_In_The_Garbage_(V)_(Virtual_Set_5).wiki" "VS5O stub 09"
edit 'Ineffective Maneuver (V) (Virtual Set 5)' "$STUBS/Ineffective_Maneuver_(V)_(Virtual_Set_5).wiki" "VS5O stub 10"
edit 'Jedi Levitation (V) (Virtual Set 5)' "$STUBS/Jedi_Levitation_(V)_(Virtual_Set_5).wiki" "VS5O stub 11"
edit 'Levitation (V) (Virtual Set 5)' "$STUBS/Levitation_(V)_(Virtual_Set_5).wiki" "VS5O stub 12"
edit 'Neb Dulo (V) (Virtual Set 5)' "$STUBS/Neb_Dulo_(V)_(Virtual_Set_5).wiki" "VS5O stub 13"
edit 'No Disintegrations! (V) (Virtual Set 5)' "$STUBS/No_Disintegrations_(V)_(Virtual_Set_5).wiki" "VS5O stub 14"
edit 'Obi-Wan'\''s Apparition (V) (Virtual Set 5)' "$STUBS/ObiWans_Apparition_(V)_(Virtual_Set_5).wiki" "VS5O stub 15"
edit 'Polarized Negative Power Coupling (V) (Virtual Set 5)' "$STUBS/Polarized_Negative_Power_Coupling_(V)_(Virtual_Set_5).wiki" "VS5O stub 16"
edit 'Rayc Ryjerd (V) (Virtual Set 5)' "$STUBS/Rayc_Ryjerd_(V)_(Virtual_Set_5).wiki" "VS5O stub 17"
edit 'Scrambled Transmission (V) (Virtual Set 5)' "$STUBS/Scrambled_Transmission_(V)_(Virtual_Set_5).wiki" "VS5O stub 18"
edit 'Secure Route (V) (Virtual Set 5)' "$STUBS/Secure_Route_(V)_(Virtual_Set_5).wiki" "VS5O stub 19"
edit 'Shoo! Shoo! (V) (Virtual Set 5)' "$STUBS/Shoo_Shoo_(V)_(Virtual_Set_5).wiki" "VS5O stub 20"
edit 'Son Of Skywalker (V) (Virtual Set 5)' "$STUBS/Son_Of_Skywalker_(V)_(Virtual_Set_5).wiki" "VS5O stub 21"
edit 'Starship Levitation (V) (Virtual Set 5)' "$STUBS/Starship_Levitation_(V)_(Virtual_Set_5).wiki" "VS5O stub 22"
edit 'Visored Vision (V) (Virtual Set 5)' "$STUBS/Visored_Vision_(V)_(Virtual_Set_5).wiki" "VS5O stub 23"
edit 'Wars Not Make One Great (V) (Virtual Set 5)' "$STUBS/Wars_Not_Make_One_Great_(V)_(Virtual_Set_5).wiki" "VS5O stub 24"
edit 'Yoda (V) (Virtual Set 5)' "$STUBS/Yoda_(V)_(Virtual_Set_5).wiki" "VS5O stub 25"
edit 'Alert My Star Destroyer! (V) (Virtual Set 5)' "$STUBS/Alert_My_Star_Destroyer_(V)_(Virtual_Set_5).wiki" "VS5O stub 26"
edit 'Awwww, Cannot Get Your Ship Out (V) (Virtual Set 5)' "$STUBS/Awwww_Cannot_Get_Your_Ship_Out_(V)_(Virtual_Set_5).wiki" "VS5O stub 27"
edit 'Bad Feeling Have I (V) (Virtual Set 5)' "$STUBS/Bad_Feeling_Have_I_(V)_(Virtual_Set_5).wiki" "VS5O stub 28"
edit 'Bossk (V) (Virtual Set 5)' "$STUBS/Bossk_(V)_(Virtual_Set_5).wiki" "VS5O stub 29"
edit 'Close Call (V) (Virtual Set 5)' "$STUBS/Close_Call_(V)_(Virtual_Set_5).wiki" "VS5O stub 30"
edit 'Corporal Derdram (V) (Virtual Set 5)' "$STUBS/Corporal_Derdram_(V)_(Virtual_Set_5).wiki" "VS5O stub 31"
edit 'Corporal Vandolay (V) (Virtual Set 5)' "$STUBS/Corporal_Vandolay_(V)_(Virtual_Set_5).wiki" "VS5O stub 32"
edit 'Defensive Fire (V) (Virtual Set 5)' "$STUBS/Defensive_Fire_(V)_(Virtual_Set_5).wiki" "VS5O stub 33"
edit 'Dengar (V) (Virtual Set 5)' "$STUBS/Dengar_(V)_(Virtual_Set_5).wiki" "VS5O stub 34"
edit 'Desilijic Tattoo (V) (Virtual Set 5)' "$STUBS/Desilijic_Tattoo_(V)_(Virtual_Set_5).wiki" "VS5O stub 35"
edit 'Fear (V) (Virtual Set 5)' "$STUBS/Fear_(V)_(Virtual_Set_5).wiki" "VS5O stub 36"
edit 'Field Promotion (V) (Virtual Set 5)' "$STUBS/Field_Promotion_(V)_(Virtual_Set_5).wiki" "VS5O stub 37"
edit 'Flagship (V) (Virtual Set 5)' "$STUBS/Flagship_(V)_(Virtual_Set_5).wiki" "VS5O stub 38"
edit 'Hound'\''s Tooth (V) (Virtual Set 5)' "$STUBS/Hounds_Tooth_(V)_(Virtual_Set_5).wiki" "VS5O stub 39"
edit 'IG-88 (V) (Virtual Set 5)' "$STUBS/IG88_(V)_(Virtual_Set_5).wiki" "VS5O stub 40"
edit 'IG-88'\''s Neural Inhibitor (V) (Virtual Set 5)' "$STUBS/IG88s_Neural_Inhibitor_(V)_(Virtual_Set_5).wiki" "VS5O stub 41"
edit 'Lando System? (V) (Virtual Set 5)' "$STUBS/Lando_System_(V)_(Virtual_Set_5).wiki" "VS5O stub 42"
edit 'Location, Location, Location (V) (Virtual Set 5)' "$STUBS/Location_Location_Location_(V)_(Virtual_Set_5).wiki" "VS5O stub 43"
edit 'Mist Hunter (V) (Virtual Set 5)' "$STUBS/Mist_Hunter_(V)_(Virtual_Set_5).wiki" "VS5O stub 44"
edit 'Precision Targeting (V) (Virtual Set 5)' "$STUBS/Precision_Targeting_(V)_(Virtual_Set_5).wiki" "VS5O stub 45"
edit 'Punishing One (V) (Virtual Set 5)' "$STUBS/Punishing_One_(V)_(Virtual_Set_5).wiki" "VS5O stub 46"
edit 'Sudden Impact (V) (Virtual Set 5)' "$STUBS/Sudden_Impact_(V)_(Virtual_Set_5).wiki" "VS5O stub 47"
edit 'Take Evasive Action (V) (Virtual Set 5)' "$STUBS/Take_Evasive_Action_(V)_(Virtual_Set_5).wiki" "VS5O stub 48"
edit 'The Dark Path (V) (Virtual Set 5)' "$STUBS/The_Dark_Path_(V)_(Virtual_Set_5).wiki" "VS5O stub 49"
edit 'Voyeur (V) (Virtual Set 5)' "$STUBS/Voyeur_(V)_(Virtual_Set_5).wiki" "VS5O stub 50"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 5 (Original)
Asteroids Do Not Concern Me (V) (Virtual Set 5)
Away Put Your Weapon (V) (Virtual Set 5)
Bron Burs (V) (Virtual Set 5)
Descent Into The Dark (V) (Virtual Set 5)
Encampment (V) (Virtual Set 5)
Flash Of Insight (V) (Virtual Set 5)
Found Someone You Have (V) (Virtual Set 5)
Harc Seff (V) (Virtual Set 5)
Hiding In The Garbage (V) (Virtual Set 5)
Ineffective Maneuver (V) (Virtual Set 5)
Jedi Levitation (V) (Virtual Set 5)
Levitation (V) (Virtual Set 5)
Neb Dulo (V) (Virtual Set 5)
No Disintegrations! (V) (Virtual Set 5)
Obi-Wan's Apparition (V) (Virtual Set 5)
Polarized Negative Power Coupling (V) (Virtual Set 5)
Rayc Ryjerd (V) (Virtual Set 5)
Scrambled Transmission (V) (Virtual Set 5)
Secure Route (V) (Virtual Set 5)
Shoo! Shoo! (V) (Virtual Set 5)
Son Of Skywalker (V) (Virtual Set 5)
Starship Levitation (V) (Virtual Set 5)
Visored Vision (V) (Virtual Set 5)
Wars Not Make One Great (V) (Virtual Set 5)
Yoda (V) (Virtual Set 5)
Alert My Star Destroyer! (V) (Virtual Set 5)
Awwww, Cannot Get Your Ship Out (V) (Virtual Set 5)
Bad Feeling Have I (V) (Virtual Set 5)
Bossk (V) (Virtual Set 5)
Close Call (V) (Virtual Set 5)
Corporal Derdram (V) (Virtual Set 5)
Corporal Vandolay (V) (Virtual Set 5)
Defensive Fire (V) (Virtual Set 5)
Dengar (V) (Virtual Set 5)
Desilijic Tattoo (V) (Virtual Set 5)
Fear (V) (Virtual Set 5)
Field Promotion (V) (Virtual Set 5)
Flagship (V) (Virtual Set 5)
Hound's Tooth (V) (Virtual Set 5)
IG-88 (V) (Virtual Set 5)
IG-88's Neural Inhibitor (V) (Virtual Set 5)
Lando System? (V) (Virtual Set 5)
Location, Location, Location (V) (Virtual Set 5)
Mist Hunter (V) (Virtual Set 5)
Precision Targeting (V) (Virtual Set 5)
Punishing One (V) (Virtual Set 5)
Sudden Impact (V) (Virtual Set 5)
Take Evasive Action (V) (Virtual Set 5)
The Dark Path (V) (Virtual Set 5)
Voyeur (V) (Virtual Set 5)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=['Asteroids_Do_Not_Concern_Me_(V)_(Virtual_Set_5)', 'Away_Put_Your_Weapon_(V)_(Virtual_Set_5)', 'Bron_Burs_(V)_(Virtual_Set_5)', 'Descent_Into_The_Dark_(V)_(Virtual_Set_5)', 'Encampment_(V)_(Virtual_Set_5)', 'Flash_Of_Insight_(V)_(Virtual_Set_5)', 'Found_Someone_You_Have_(V)_(Virtual_Set_5)', 'Harc_Seff_(V)_(Virtual_Set_5)', 'Hiding_In_The_Garbage_(V)_(Virtual_Set_5)', 'Ineffective_Maneuver_(V)_(Virtual_Set_5)', 'Jedi_Levitation_(V)_(Virtual_Set_5)', 'Levitation_(V)_(Virtual_Set_5)', 'Neb_Dulo_(V)_(Virtual_Set_5)', 'No_Disintegrations!_(V)_(Virtual_Set_5)', "Obi-Wan's_Apparition_(V)_(Virtual_Set_5)", 'Polarized_Negative_Power_Coupling_(V)_(Virtual_Set_5)', 'Rayc_Ryjerd_(V)_(Virtual_Set_5)', 'Scrambled_Transmission_(V)_(Virtual_Set_5)', 'Secure_Route_(V)_(Virtual_Set_5)', 'Shoo!_Shoo!_(V)_(Virtual_Set_5)', 'Son_Of_Skywalker_(V)_(Virtual_Set_5)', 'Starship_Levitation_(V)_(Virtual_Set_5)', 'Visored_Vision_(V)_(Virtual_Set_5)', 'Wars_Not_Make_One_Great_(V)_(Virtual_Set_5)', 'Yoda_(V)_(Virtual_Set_5)', 'Alert_My_Star_Destroyer!_(V)_(Virtual_Set_5)', 'Awwww,_Cannot_Get_Your_Ship_Out_(V)_(Virtual_Set_5)', 'Bad_Feeling_Have_I_(V)_(Virtual_Set_5)', 'Bossk_(V)_(Virtual_Set_5)', 'Close_Call_(V)_(Virtual_Set_5)', 'Corporal_Derdram_(V)_(Virtual_Set_5)', 'Corporal_Vandolay_(V)_(Virtual_Set_5)', 'Defensive_Fire_(V)_(Virtual_Set_5)', 'Dengar_(V)_(Virtual_Set_5)', 'Desilijic_Tattoo_(V)_(Virtual_Set_5)', 'Fear_(V)_(Virtual_Set_5)', 'Field_Promotion_(V)_(Virtual_Set_5)', 'Flagship_(V)_(Virtual_Set_5)', "Hound's_Tooth_(V)_(Virtual_Set_5)", 'IG-88_(V)_(Virtual_Set_5)', "IG-88's_Neural_Inhibitor_(V)_(Virtual_Set_5)", 'Lando_System?_(V)_(Virtual_Set_5)', 'Location,_Location,_Location_(V)_(Virtual_Set_5)', 'Mist_Hunter_(V)_(Virtual_Set_5)', 'Precision_Targeting_(V)_(Virtual_Set_5)', 'Punishing_One_(V)_(Virtual_Set_5)', 'Sudden_Impact_(V)_(Virtual_Set_5)', 'Take_Evasive_Action_(V)_(Virtual_Set_5)', 'The_Dark_Path_(V)_(Virtual_Set_5)', 'Voyeur_(V)_(Virtual_Set_5)']
for slug in slugs:
  u="https://wiki.swccg.com/wiki/"+urllib.parse.quote(slug, safe="()_,!'?")
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    ok=(r.status==200)
  except Exception as e:
    ok=False
  print(("PASS" if ok else "FAIL"), u)
  if ok: pass_n+=1
  else: fail.append(u)
print("STUBS %d/50 PASS fail=%s" % (pass_n, fail[:10]))
u="https://wiki.swccg.com/wiki/Virtual_Set_5_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS5O STUBS APPLY OK")

PY
