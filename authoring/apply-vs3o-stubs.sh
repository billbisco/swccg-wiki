#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs3-original
STUBS=$ROOT/pages/vs3-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs3o-stubs-import

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

echo "== importImages VS3O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS3O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs3o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs3o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 3 (Original) Remaster slip faces from VirtualCards3.pdf" \
  --overwrite \
  /tmp/vs3o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 3 (Original)" "$HUBS/Virtual_Set_3_(Original).wiki" "VS3 Original: link all 50 Remaster slip stubs"
edit 'A Tremor In The Force (V) (Virtual Set 3)' "$STUBS/A_Tremor_In_The_Force_(V)_(Virtual_Set_3).wiki" "VS3O stub 01"
edit 'Advanced Preparation (V) (Virtual Set 3)' "$STUBS/Advanced_Preparation_(V)_(Virtual_Set_3).wiki" "VS3O stub 02"
edit 'Cell 2187 (V) (Virtual Set 3)' "$STUBS/Cell_2187_(V)_(Virtual_Set_3).wiki" "VS3O stub 03"
edit 'Chewbacca (V) (Virtual Set 3)' "$STUBS/Chewbacca_(V)_(Virtual_Set_3).wiki" "VS3O stub 04"
edit 'Colonel Feyn Gospic (V) (Virtual Set 3)' "$STUBS/Colonel_Feyn_Gospic_(V)_(Virtual_Set_3).wiki" "VS3O stub 05"
edit 'Commander Evram Lajaie (V) (Virtual Set 3)' "$STUBS/Commander_Evram_Lajaie_(V)_(Virtual_Set_3).wiki" "VS3O stub 06"
edit 'Commander Vanden Willard (V) (Virtual Set 3)' "$STUBS/Commander_Vanden_Willard_(V)_(Virtual_Set_3).wiki" "VS3O stub 07"
edit 'Eject! Eject! (V) (Virtual Set 3)' "$STUBS/Eject_Eject_(V)_(Virtual_Set_3).wiki" "VS3O stub 08"
edit 'For Luck (V) (Virtual Set 3)' "$STUBS/For_Luck_(V)_(Virtual_Set_3).wiki" "VS3O stub 09"
edit 'Grappling Hook (V) (Virtual Set 3)' "$STUBS/Grappling_Hook_(V)_(Virtual_Set_3).wiki" "VS3O stub 10"
edit 'Han (V) (Virtual Set 3)' "$STUBS/Han_(V)_(Virtual_Set_3).wiki" "VS3O stub 11"
edit 'Leia (V) (Virtual Set 3)' "$STUBS/Leia_(V)_(Virtual_Set_3).wiki" "VS3O stub 12"
edit 'Leia'\''s Sporting Blaster (V) (Virtual Set 3)' "$STUBS/Leias_Sporting_Blaster_(V)_(Virtual_Set_3).wiki" "VS3O stub 13"
edit 'Logistical Delay (V) (Virtual Set 3)' "$STUBS/Logistical_Delay_(V)_(Virtual_Set_3).wiki" "VS3O stub 14"
edit 'Merc Sunlet (V) (Virtual Set 3)' "$STUBS/Merc_Sunlet_(V)_(Virtual_Set_3).wiki" "VS3O stub 15"
edit 'R2-D2 (Artoo-Detoo) (V) (Virtual Set 3)' "$STUBS/R2D2_(ArtooDetoo)_(V)_(Virtual_Set_3).wiki" "VS3O stub 16"
edit 'Rebel Tech (V) (Virtual Set 3)' "$STUBS/Rebel_Tech_(V)_(Virtual_Set_3).wiki" "VS3O stub 17"
edit 'Red 5 (V) (Virtual Set 3)' "$STUBS/Red_5_(V)_(Virtual_Set_3).wiki" "VS3O stub 18"
edit 'Sabotage (V) (Virtual Set 3)' "$STUBS/Sabotage_(V)_(Virtual_Set_3).wiki" "VS3O stub 19"
edit 'Scanner Techs (V) (Virtual Set 3)' "$STUBS/Scanner_Techs_(V)_(Virtual_Set_3).wiki" "VS3O stub 20"
edit 'Solomahal (V) (Virtual Set 3)' "$STUBS/Solomahal_(V)_(Virtual_Set_3).wiki" "VS3O stub 21"
edit 'They'\''re On Dantooine (V) (Virtual Set 3)' "$STUBS/Theyre_On_Dantooine_(V)_(Virtual_Set_3).wiki" "VS3O stub 22"
edit 'Traffic Control (V) (Virtual Set 3)' "$STUBS/Traffic_Control_(V)_(Virtual_Set_3).wiki" "VS3O stub 23"
edit 'Undercover (V) (Light) (Virtual Set 3)' "$STUBS/Undercover_(V)_(Light)_(Virtual_Set_3).wiki" "VS3O stub 24"
edit 'Wokling (V) (Virtual Set 3)' "$STUBS/Wokling_(V)_(Virtual_Set_3).wiki" "VS3O stub 25"
edit 'A Disturbance In The Force (V) (Virtual Set 3)' "$STUBS/A_Disturbance_In_The_Force_(V)_(Virtual_Set_3).wiki" "VS3O stub 26"
edit 'Astromech Shortage (V) (Virtual Set 3)' "$STUBS/Astromech_Shortage_(V)_(Virtual_Set_3).wiki" "VS3O stub 27"
edit 'Besieged (V) (Virtual Set 3)' "$STUBS/Besieged_(V)_(Virtual_Set_3).wiki" "VS3O stub 28"
edit 'Come With Me (V) (Virtual Set 3)' "$STUBS/Come_With_Me_(V)_(Virtual_Set_3).wiki" "VS3O stub 29"
edit 'Dannik Jerriko (V) (Virtual Set 3)' "$STUBS/Dannik_Jerriko_(V)_(Virtual_Set_3).wiki" "VS3O stub 30"
edit 'Dark Forces (V) (Virtual Set 3)' "$STUBS/Dark_Forces_(V)_(Virtual_Set_3).wiki" "VS3O stub 31"
edit 'Greedo (V) (Virtual Set 3)' "$STUBS/Greedo_(V)_(Virtual_Set_3).wiki" "VS3O stub 32"
edit 'Hem Dazon (V) (Virtual Set 3)' "$STUBS/Hem_Dazon_(V)_(Virtual_Set_3).wiki" "VS3O stub 33"
edit 'Hyperwave Scan (V) (Virtual Set 3)' "$STUBS/Hyperwave_Scan_(V)_(Virtual_Set_3).wiki" "VS3O stub 34"
edit 'I'\''m On The Leader (V) (Virtual Set 3)' "$STUBS/Im_On_The_Leader_(V)_(Virtual_Set_3).wiki" "VS3O stub 35"
edit 'Informant (V) (Virtual Set 3)' "$STUBS/Informant_(V)_(Virtual_Set_3).wiki" "VS3O stub 36"
edit 'IT-O (Eyetee-Oh) (V) (Virtual Set 3)' "$STUBS/ITO_(EyeteeOh)_(V)_(Virtual_Set_3).wiki" "VS3O stub 37"
edit 'Ket Maliss (V) (Virtual Set 3)' "$STUBS/Ket_Maliss_(V)_(Virtual_Set_3).wiki" "VS3O stub 38"
edit 'Leia Seeker (V) (Virtual Set 3)' "$STUBS/Leia_Seeker_(V)_(Virtual_Set_3).wiki" "VS3O stub 39"
edit 'Motti (V) (Virtual Set 3)' "$STUBS/Motti_(V)_(Virtual_Set_3).wiki" "VS3O stub 40"
edit 'Oo-ta Goo-ta, Solo? (V) (Virtual Set 3)' "$STUBS/Oota_Goota_Solo_(V)_(Virtual_Set_3).wiki" "VS3O stub 41"
edit 'Reactor Terminal (V) (Virtual Set 3)' "$STUBS/Reactor_Terminal_(V)_(Virtual_Set_3).wiki" "VS3O stub 42"
edit 'Reegesk (V) (Virtual Set 3)' "$STUBS/Reegesk_(V)_(Virtual_Set_3).wiki" "VS3O stub 43"
edit 'Reserve Pilot (V) (Virtual Set 3)' "$STUBS/Reserve_Pilot_(V)_(Virtual_Set_3).wiki" "VS3O stub 44"
edit 'Rodian (V) (Virtual Set 3)' "$STUBS/Rodian_(V)_(Virtual_Set_3).wiki" "VS3O stub 45"
edit 'Spice Mines Of Kessel (V) (Virtual Set 3)' "$STUBS/Spice_Mines_Of_Kessel_(V)_(Virtual_Set_3).wiki" "VS3O stub 46"
edit 'Tarkin (V) (Virtual Set 3)' "$STUBS/Tarkin_(V)_(Virtual_Set_3).wiki" "VS3O stub 47"
edit 'Tentacle (V) (Virtual Set 3)' "$STUBS/Tentacle_(V)_(Virtual_Set_3).wiki" "VS3O stub 48"
edit 'Trooper Davin Felth (V) (Virtual Set 3)' "$STUBS/Trooper_Davin_Felth_(V)_(Virtual_Set_3).wiki" "VS3O stub 49"
edit 'Undercover (V) (Dark) (Virtual Set 3)' "$STUBS/Undercover_(V)_(Dark)_(Virtual_Set_3).wiki" "VS3O stub 50"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 3 (Original)
A Tremor In The Force (V) (Virtual Set 3)
Advanced Preparation (V) (Virtual Set 3)
Cell 2187 (V) (Virtual Set 3)
Chewbacca (V) (Virtual Set 3)
Colonel Feyn Gospic (V) (Virtual Set 3)
Commander Evram Lajaie (V) (Virtual Set 3)
Commander Vanden Willard (V) (Virtual Set 3)
Eject! Eject! (V) (Virtual Set 3)
For Luck (V) (Virtual Set 3)
Grappling Hook (V) (Virtual Set 3)
Han (V) (Virtual Set 3)
Leia (V) (Virtual Set 3)
Leia's Sporting Blaster (V) (Virtual Set 3)
Logistical Delay (V) (Virtual Set 3)
Merc Sunlet (V) (Virtual Set 3)
R2-D2 (Artoo-Detoo) (V) (Virtual Set 3)
Rebel Tech (V) (Virtual Set 3)
Red 5 (V) (Virtual Set 3)
Sabotage (V) (Virtual Set 3)
Scanner Techs (V) (Virtual Set 3)
Solomahal (V) (Virtual Set 3)
They're On Dantooine (V) (Virtual Set 3)
Traffic Control (V) (Virtual Set 3)
Undercover (V) (Light) (Virtual Set 3)
Wokling (V) (Virtual Set 3)
A Disturbance In The Force (V) (Virtual Set 3)
Astromech Shortage (V) (Virtual Set 3)
Besieged (V) (Virtual Set 3)
Come With Me (V) (Virtual Set 3)
Dannik Jerriko (V) (Virtual Set 3)
Dark Forces (V) (Virtual Set 3)
Greedo (V) (Virtual Set 3)
Hem Dazon (V) (Virtual Set 3)
Hyperwave Scan (V) (Virtual Set 3)
I'm On The Leader (V) (Virtual Set 3)
Informant (V) (Virtual Set 3)
IT-O (Eyetee-Oh) (V) (Virtual Set 3)
Ket Maliss (V) (Virtual Set 3)
Leia Seeker (V) (Virtual Set 3)
Motti (V) (Virtual Set 3)
Oo-ta Goo-ta, Solo? (V) (Virtual Set 3)
Reactor Terminal (V) (Virtual Set 3)
Reegesk (V) (Virtual Set 3)
Reserve Pilot (V) (Virtual Set 3)
Rodian (V) (Virtual Set 3)
Spice Mines Of Kessel (V) (Virtual Set 3)
Tarkin (V) (Virtual Set 3)
Tentacle (V) (Virtual Set 3)
Trooper Davin Felth (V) (Virtual Set 3)
Undercover (V) (Dark) (Virtual Set 3)
Main Page
Category:Virtual Original sets
File:VS3O-01-A_Tremor_In_The_Force.png
File:VS3O-02-Advanced_Preparation.png
File:VS3O-03-Cell_2187.png
File:VS3O-04-Chewbacca.png
File:VS3O-05-Colonel_Feyn_Gospic.png
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
titles=["A Tremor In The Force (V) (Virtual Set 3)", "Advanced Preparation (V) (Virtual Set 3)", "Cell 2187 (V) (Virtual Set 3)", "Chewbacca (V) (Virtual Set 3)", "Colonel Feyn Gospic (V) (Virtual Set 3)", "Commander Evram Lajaie (V) (Virtual Set 3)", "Commander Vanden Willard (V) (Virtual Set 3)", "Eject! Eject! (V) (Virtual Set 3)", "For Luck (V) (Virtual Set 3)", "Grappling Hook (V) (Virtual Set 3)", "Han (V) (Virtual Set 3)", "Leia (V) (Virtual Set 3)", "Leia's Sporting Blaster (V) (Virtual Set 3)", "Logistical Delay (V) (Virtual Set 3)", "Merc Sunlet (V) (Virtual Set 3)", "R2-D2 (Artoo-Detoo) (V) (Virtual Set 3)", "Rebel Tech (V) (Virtual Set 3)", "Red 5 (V) (Virtual Set 3)", "Sabotage (V) (Virtual Set 3)", "Scanner Techs (V) (Virtual Set 3)", "Solomahal (V) (Virtual Set 3)", "They're On Dantooine (V) (Virtual Set 3)", "Traffic Control (V) (Virtual Set 3)", "Undercover (V) (Light) (Virtual Set 3)", "Wokling (V) (Virtual Set 3)", "A Disturbance In The Force (V) (Virtual Set 3)", "Astromech Shortage (V) (Virtual Set 3)", "Besieged (V) (Virtual Set 3)", "Come With Me (V) (Virtual Set 3)", "Dannik Jerriko (V) (Virtual Set 3)", "Dark Forces (V) (Virtual Set 3)", "Greedo (V) (Virtual Set 3)", "Hem Dazon (V) (Virtual Set 3)", "Hyperwave Scan (V) (Virtual Set 3)", "I'm On The Leader (V) (Virtual Set 3)", "Informant (V) (Virtual Set 3)", "IT-O (Eyetee-Oh) (V) (Virtual Set 3)", "Ket Maliss (V) (Virtual Set 3)", "Leia Seeker (V) (Virtual Set 3)", "Motti (V) (Virtual Set 3)", "Oo-ta Goo-ta, Solo? (V) (Virtual Set 3)", "Reactor Terminal (V) (Virtual Set 3)", "Reegesk (V) (Virtual Set 3)", "Reserve Pilot (V) (Virtual Set 3)", "Rodian (V) (Virtual Set 3)", "Spice Mines Of Kessel (V) (Virtual Set 3)", "Tarkin (V) (Virtual Set 3)", "Tentacle (V) (Virtual Set 3)", "Trooper Davin Felth (V) (Virtual Set 3)", "Undercover (V) (Dark) (Virtual Set 3)"]
for title in titles:
  slug=title.replace(' ', '_')
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
u="https://wiki.swccg.com/wiki/Virtual_Set_3_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS3O STUBS APPLY OK")
PY
