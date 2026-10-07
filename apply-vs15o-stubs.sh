#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs15-original
STUBS=$ROOT/pages/vs15-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs15o-stubs-import

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

echo "== importImages VS15O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS15O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs15o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs15o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 15 (Original) slip faces from VirtualCards15.pdf" \
  --overwrite \
  /tmp/vs15o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

# APCu gotcha after importImages — clear + graceful if needed
docker exec -u root swccg_wiki bash -c 'php -r "if(function_exists(\"apcu_clear_cache\")){apcu_clear_cache(); echo \"APCu cleared\n\";} else {echo \"no apcu\n\";}"' || true
docker exec -u root swccg_wiki bash -c 'apachectl graceful 2>/dev/null || apache2ctl graceful 2>/dev/null || true'

edit "Virtual Set 15 (Original)" "$HUBS/Virtual_Set_15_(Original).wiki" "VS15 Original: link all 67 slip stubs"

edit 'Anger, Fear, Aggression (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Anger,_Fear,_Aggression_(V)_(Virtual_Set_15).wiki' "VS15O stub 01"
edit 'Alderaan Consular Ship (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Alderaan_Consular_Ship_(V)_(Virtual_Set_15).wiki' "VS15O stub 02"
edit 'Artillery Remote (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Artillery_Remote_(V)_(Virtual_Set_15).wiki' "VS15O stub 03"
edit 'Artoo (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Artoo_(V)_(Virtual_Set_15).wiki' "VS15O stub 04"
edit 'Beru Lars (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Beru_Lars_(V)_(Virtual_Set_15).wiki' "VS15O stub 05"
edit 'Beru Stew (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Beru_Stew_(V)_(Virtual_Set_15).wiki' "VS15O stub 06"
edit 'Booster In Pulsar Skate (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Booster_In_Pulsar_Skate_(V)_(Virtual_Set_15).wiki' "VS15O stub 07"
edit 'Brainiac (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Brainiac_(V)_(Virtual_Set_15).wiki' "VS15O stub 08"
edit 'Dantooine: Base - Operations Center (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Dantooine:_Base_-_Operations_Center_(V)_(Virtual_Set_15).wiki' "VS15O stub 09"
edit 'Fixer (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Fixer_(V)_(Virtual_Set_15).wiki' "VS15O stub 10"
edit 'Harvest (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Harvest_(V)_(Virtual_Set_15).wiki' "VS15O stub 11"
edit 'Hidden Base (V) / Systems Will Slip Through Your Fingers (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Hidden_Base_(V)_-_Systems_Will_Slip_Through_Your_Fingers_(V)_(Virtual_Set_15).wiki' "VS15O stub 12"
edit 'IL-19 (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/IL-19_(V)_(Virtual_Set_15).wiki' "VS15O stub 13"
edit 'Insurrection (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Insurrection_(V)_(Virtual_Set_15).wiki' "VS15O stub 14"
edit 'Lando Calrissian (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Lando_Calrissian_(V)_(Virtual_Set_15).wiki' "VS15O stub 15"
edit 'Lars'\'' Hydroponics Station (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Lars_Hydroponics_Station_(V)_(Virtual_Set_15).wiki' "VS15O stub 16"
edit 'Lars'\'' Vaporator (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Lars_Vaporator_(V)_(Virtual_Set_15).wiki' "VS15O stub 17"
edit 'Learn About The Force, Luke (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Learn_About_The_Force,_Luke_(V)_(Virtual_Set_15).wiki' "VS15O stub 18"
edit 'Luke'\''s Hunting Rifle (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Lukes_Hunting_Rifle_(V)_(Virtual_Set_15).wiki' "VS15O stub 19"
edit 'Melas (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Melas_(V)_(Virtual_Set_15).wiki' "VS15O stub 20"
edit 'Owen Lars (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Owen_Lars_(V)_(Virtual_Set_15).wiki' "VS15O stub 21"
edit 'Rebel Cell - Hidden Landing Site (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Rebel_Cell_-_Hidden_Landing_Site_(V)_(Virtual_Set_15).wiki' "VS15O stub 22"
edit 'Rebel Cell - Monitoring Station (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Rebel_Cell_-_Monitoring_Station_(V)_(Virtual_Set_15).wiki' "VS15O stub 23"
edit 'Rebel Cell - Perimeter (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Rebel_Cell_-_Perimeter_(V)_(Virtual_Set_15).wiki' "VS15O stub 24"
edit 'Rebel Cell - Situation Room (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Rebel_Cell_-_Situation_Room_(V)_(Virtual_Set_15).wiki' "VS15O stub 25"
edit 'Republic Corvette (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Republic_Corvette_(V)_(Virtual_Set_15).wiki' "VS15O stub 26"
edit 'Republic Trooper with Blaster Rifle (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Republic_Trooper_with_Blaster_Rifle_(V)_(Virtual_Set_15).wiki' "VS15O stub 27"
edit 'Skull (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Skull_(V)_(Virtual_Set_15).wiki' "VS15O stub 28"
edit 'Talon Karrde (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Talon_Karrde_(V)_(Virtual_Set_15).wiki' "VS15O stub 29"
edit 'Tatooine: Lars'\'' Moisture Farm (Light) (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Tatooine:_Lars_Moisture_Farm_(Light)_(V)_(Virtual_Set_15).wiki' "VS15O stub 30"
edit 'Tatooine Utility Belt (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Tatooine_Utility_Belt_(V)_(Virtual_Set_15).wiki' "VS15O stub 31"
edit 'Theron Nett (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Theron_Nett_(V)_(Virtual_Set_15).wiki' "VS15O stub 32"
edit 'Uncharted Settlements (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Uncharted_Settlements_(V)_(Virtual_Set_15).wiki' "VS15O stub 33"
edit 'Wedge Antilles (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Wedge_Antilles_(V)_(Virtual_Set_15).wiki' "VS15O stub 34"
edit 'Wes Janson (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Wes_Janson_(V)_(Virtual_Set_15).wiki' "VS15O stub 35"
edit 'YT-1300 Transport (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/YT-1300_Transport_(V)_(Virtual_Set_15).wiki' "VS15O stub 36"
edit 'Abyssin Ornament & Wounded Wookiee (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Abyssin_Ornament_and_Wounded_Wookiee_(V)_(Virtual_Set_15).wiki' "VS15O stub 37"
edit 'Arica (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Arica_(V)_(Virtual_Set_15).wiki' "VS15O stub 38"
edit 'Bib Fortuna (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Bib_Fortuna_(V)_(Virtual_Set_15).wiki' "VS15O stub 39"
edit 'Chokk (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Chokk_(V)_(Virtual_Set_15).wiki' "VS15O stub 40"
edit 'Collateral Damage (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Collateral_Damage_(V)_(Virtual_Set_15).wiki' "VS15O stub 41"
edit 'Cyclone 1 (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Cyclone_1_(V)_(Virtual_Set_15).wiki' "VS15O stub 42"
edit 'Danz Borin (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Danz_Borin_(V)_(Virtual_Set_15).wiki' "VS15O stub 43"
edit 'Dark Reconnaissance (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Dark_Reconnaissance_(V)_(Virtual_Set_15).wiki' "VS15O stub 44"
edit 'Devastator (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Devastator_(V)_(Virtual_Set_15).wiki' "VS15O stub 45"
edit 'Dewback (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Dewback_(V)_(Virtual_Set_15).wiki' "VS15O stub 46"
edit 'Force Push (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Force_Push_(V)_(Virtual_Set_15).wiki' "VS15O stub 47"
edit 'Gravel Storm (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Gravel_Storm_(V)_(Virtual_Set_15).wiki' "VS15O stub 48"
edit 'Imperial Detainment (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Imperial_Detainment_(V)_(Virtual_Set_15).wiki' "VS15O stub 49"
edit 'Imperial Entanglements (V) / No One To Stop Us This Time (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Imperial_Entanglements_(V)_-_No_One_To_Stop_Us_This_Time_(V)_(Virtual_Set_15).wiki' "VS15O stub 50"
edit 'Imperial Pilot (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Imperial_Pilot_(V)_(Virtual_Set_15).wiki' "VS15O stub 51"
edit 'Knowledge And Defense (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Knowledge_And_Defense_(V)_(Virtual_Set_15).wiki' "VS15O stub 52"
edit 'Let'\''s Pass On That (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Lets_Pass_On_That_(V)_(Virtual_Set_15).wiki' "VS15O stub 53"
edit 'Look Sir, Droids (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Look_Sir,_Droids_(V)_(Virtual_Set_15).wiki' "VS15O stub 54"
edit 'Maul'\''s Sith Speeder (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Mauls_Sith_Speeder_(V)_(Virtual_Set_15).wiki' "VS15O stub 55"
edit 'No Bargain (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/No_Bargain_(V)_(Virtual_Set_15).wiki' "VS15O stub 56"
edit 'Raider Craft (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Raider_Craft_(V)_(Virtual_Set_15).wiki' "VS15O stub 57"
edit 'Sandtrooper (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Sandtrooper_(V)_(Virtual_Set_15).wiki' "VS15O stub 58"
edit 'Scout Mercenary (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Scout_Mercenary_(V)_(Virtual_Set_15).wiki' "VS15O stub 59"
edit 'SD-17 Homing Missile (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/SD-17_Homing_Missile_(V)_(Virtual_Set_15).wiki' "VS15O stub 60"
edit 'Sebulba (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Sebulba_(V)_(Virtual_Set_15).wiki' "VS15O stub 61"
edit 'Shada (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Shada_(V)_(Virtual_Set_15).wiki' "VS15O stub 62"
edit 'Sith Probe Droid (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Sith_Probe_Droid_(V)_(Virtual_Set_15).wiki' "VS15O stub 63"
edit 'Stunning Leader (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Stunning_Leader_(V)_(Virtual_Set_15).wiki' "VS15O stub 64"
edit 'Tatooine: Mos Eisley (Dark) (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Tatooine:_Mos_Eisley_(Dark)_(V)_(Virtual_Set_15).wiki' "VS15O stub 65"
edit 'The Mandalorian (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/The_Mandalorian_(V)_(Virtual_Set_15).wiki' "VS15O stub 66"
edit 'Trained In The Jedi Arts (V) (Virtual Set 15)' '/opt/swccg-wiki/pages/vs15-original/Trained_In_The_Jedi_Arts_(V)_(Virtual_Set_15).wiki' "VS15O stub 67"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 15 (Original)
Anger, Fear, Aggression (V) (Virtual Set 15)
Alderaan Consular Ship (V) (Virtual Set 15)
Artillery Remote (V) (Virtual Set 15)
Artoo (V) (Virtual Set 15)
Beru Lars (V) (Virtual Set 15)
Beru Stew (V) (Virtual Set 15)
Booster In Pulsar Skate (V) (Virtual Set 15)
Brainiac (V) (Virtual Set 15)
Dantooine: Base - Operations Center (V) (Virtual Set 15)
Fixer (V) (Virtual Set 15)
Harvest (V) (Virtual Set 15)
Hidden Base (V) / Systems Will Slip Through Your Fingers (V) (Virtual Set 15)
IL-19 (V) (Virtual Set 15)
Insurrection (V) (Virtual Set 15)
Lando Calrissian (V) (Virtual Set 15)
Lars' Hydroponics Station (V) (Virtual Set 15)
Lars' Vaporator (V) (Virtual Set 15)
Learn About The Force, Luke (V) (Virtual Set 15)
Luke's Hunting Rifle (V) (Virtual Set 15)
Melas (V) (Virtual Set 15)
Owen Lars (V) (Virtual Set 15)
Rebel Cell - Hidden Landing Site (V) (Virtual Set 15)
Rebel Cell - Monitoring Station (V) (Virtual Set 15)
Rebel Cell - Perimeter (V) (Virtual Set 15)
Rebel Cell - Situation Room (V) (Virtual Set 15)
Republic Corvette (V) (Virtual Set 15)
Republic Trooper with Blaster Rifle (V) (Virtual Set 15)
Skull (V) (Virtual Set 15)
Talon Karrde (V) (Virtual Set 15)
Tatooine: Lars' Moisture Farm (Light) (V) (Virtual Set 15)
Tatooine Utility Belt (V) (Virtual Set 15)
Theron Nett (V) (Virtual Set 15)
Uncharted Settlements (V) (Virtual Set 15)
Wedge Antilles (V) (Virtual Set 15)
Wes Janson (V) (Virtual Set 15)
YT-1300 Transport (V) (Virtual Set 15)
Abyssin Ornament & Wounded Wookiee (V) (Virtual Set 15)
Arica (V) (Virtual Set 15)
Bib Fortuna (V) (Virtual Set 15)
Chokk (V) (Virtual Set 15)
Collateral Damage (V) (Virtual Set 15)
Cyclone 1 (V) (Virtual Set 15)
Danz Borin (V) (Virtual Set 15)
Dark Reconnaissance (V) (Virtual Set 15)
Devastator (V) (Virtual Set 15)
Dewback (V) (Virtual Set 15)
Force Push (V) (Virtual Set 15)
Gravel Storm (V) (Virtual Set 15)
Imperial Detainment (V) (Virtual Set 15)
Imperial Entanglements (V) / No One To Stop Us This Time (V) (Virtual Set 15)
Imperial Pilot (V) (Virtual Set 15)
Knowledge And Defense (V) (Virtual Set 15)
Let's Pass On That (V) (Virtual Set 15)
Look Sir, Droids (V) (Virtual Set 15)
Maul's Sith Speeder (V) (Virtual Set 15)
No Bargain (V) (Virtual Set 15)
Raider Craft (V) (Virtual Set 15)
Sandtrooper (V) (Virtual Set 15)
Scout Mercenary (V) (Virtual Set 15)
SD-17 Homing Missile (V) (Virtual Set 15)
Sebulba (V) (Virtual Set 15)
Shada (V) (Virtual Set 15)
Sith Probe Droid (V) (Virtual Set 15)
Stunning Leader (V) (Virtual Set 15)
Tatooine: Mos Eisley (Dark) (V) (Virtual Set 15)
The Mandalorian (V) (Virtual Set 15)
Trained In The Jedi Arts (V) (Virtual Set 15)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=['Anger,_Fear,_Aggression_(V)_(Virtual_Set_15)', 'Alderaan_Consular_Ship_(V)_(Virtual_Set_15)', 'Artillery_Remote_(V)_(Virtual_Set_15)', 'Artoo_(V)_(Virtual_Set_15)', 'Beru_Lars_(V)_(Virtual_Set_15)', 'Beru_Stew_(V)_(Virtual_Set_15)', 'Booster_In_Pulsar_Skate_(V)_(Virtual_Set_15)', 'Brainiac_(V)_(Virtual_Set_15)', 'Dantooine:_Base_-_Operations_Center_(V)_(Virtual_Set_15)', 'Fixer_(V)_(Virtual_Set_15)', 'Harvest_(V)_(Virtual_Set_15)', 'Hidden_Base_(V)_-_Systems_Will_Slip_Through_Your_Fingers_(V)_(Virtual_Set_15)', 'IL-19_(V)_(Virtual_Set_15)', 'Insurrection_(V)_(Virtual_Set_15)', 'Lando_Calrissian_(V)_(Virtual_Set_15)', 'Lars_Hydroponics_Station_(V)_(Virtual_Set_15)', 'Lars_Vaporator_(V)_(Virtual_Set_15)', 'Learn_About_The_Force,_Luke_(V)_(Virtual_Set_15)', 'Lukes_Hunting_Rifle_(V)_(Virtual_Set_15)', 'Melas_(V)_(Virtual_Set_15)', 'Owen_Lars_(V)_(Virtual_Set_15)', 'Rebel_Cell_-_Hidden_Landing_Site_(V)_(Virtual_Set_15)', 'Rebel_Cell_-_Monitoring_Station_(V)_(Virtual_Set_15)', 'Rebel_Cell_-_Perimeter_(V)_(Virtual_Set_15)', 'Rebel_Cell_-_Situation_Room_(V)_(Virtual_Set_15)', 'Republic_Corvette_(V)_(Virtual_Set_15)', 'Republic_Trooper_with_Blaster_Rifle_(V)_(Virtual_Set_15)', 'Skull_(V)_(Virtual_Set_15)', 'Talon_Karrde_(V)_(Virtual_Set_15)', 'Tatooine:_Lars_Moisture_Farm_(Light)_(V)_(Virtual_Set_15)', 'Tatooine_Utility_Belt_(V)_(Virtual_Set_15)', 'Theron_Nett_(V)_(Virtual_Set_15)', 'Uncharted_Settlements_(V)_(Virtual_Set_15)', 'Wedge_Antilles_(V)_(Virtual_Set_15)', 'Wes_Janson_(V)_(Virtual_Set_15)', 'YT-1300_Transport_(V)_(Virtual_Set_15)', 'Abyssin_Ornament_and_Wounded_Wookiee_(V)_(Virtual_Set_15)', 'Arica_(V)_(Virtual_Set_15)', 'Bib_Fortuna_(V)_(Virtual_Set_15)', 'Chokk_(V)_(Virtual_Set_15)', 'Collateral_Damage_(V)_(Virtual_Set_15)', 'Cyclone_1_(V)_(Virtual_Set_15)', 'Danz_Borin_(V)_(Virtual_Set_15)', 'Dark_Reconnaissance_(V)_(Virtual_Set_15)', 'Devastator_(V)_(Virtual_Set_15)', 'Dewback_(V)_(Virtual_Set_15)', 'Force_Push_(V)_(Virtual_Set_15)', 'Gravel_Storm_(V)_(Virtual_Set_15)', 'Imperial_Detainment_(V)_(Virtual_Set_15)', 'Imperial_Entanglements_(V)_-_No_One_To_Stop_Us_This_Time_(V)_(Virtual_Set_15)', 'Imperial_Pilot_(V)_(Virtual_Set_15)', 'Knowledge_And_Defense_(V)_(Virtual_Set_15)', 'Lets_Pass_On_That_(V)_(Virtual_Set_15)', 'Look_Sir,_Droids_(V)_(Virtual_Set_15)', 'Mauls_Sith_Speeder_(V)_(Virtual_Set_15)', 'No_Bargain_(V)_(Virtual_Set_15)', 'Raider_Craft_(V)_(Virtual_Set_15)', 'Sandtrooper_(V)_(Virtual_Set_15)', 'Scout_Mercenary_(V)_(Virtual_Set_15)', 'SD-17_Homing_Missile_(V)_(Virtual_Set_15)', 'Sebulba_(V)_(Virtual_Set_15)', 'Shada_(V)_(Virtual_Set_15)', 'Sith_Probe_Droid_(V)_(Virtual_Set_15)', 'Stunning_Leader_(V)_(Virtual_Set_15)', 'Tatooine:_Mos_Eisley_(Dark)_(V)_(Virtual_Set_15)', 'The_Mandalorian_(V)_(Virtual_Set_15)', 'Trained_In_The_Jedi_Arts_(V)_(Virtual_Set_15)']
for slug in slugs:
  u="https://wiki.swccg.com/wiki/"+urllib.parse.quote(slug, safe="()_,!'?")
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    ok=(r.status==200)
  except Exception:
    ok=False
  print(("PASS" if ok else "FAIL"), u)
  if ok: pass_n+=1
  else: fail.append(u)
print("STUBS %d/67 PASS fail=%s" % (pass_n, fail[:10]))
u="https://wiki.swccg.com/wiki/Virtual_Set_15_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS15O STUBS APPLY OK")

PY
