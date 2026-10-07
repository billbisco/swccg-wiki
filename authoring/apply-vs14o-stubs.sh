#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs14-original
STUBS=$ROOT/pages/vs14-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs14o-stubs-import

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

echo "== importImages VS14O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS14O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs14o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs14o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 14 (Original) slip faces from VirtualCards14.pdf" \
  --overwrite \
  /tmp/vs14o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

# APCu gotcha after importImages — clear + graceful if needed
docker exec -u root swccg_wiki bash -c 'php -r "if(function_exists(\"apcu_clear_cache\")){apcu_clear_cache(); echo \"APCu cleared\n\";} else {echo \"no apcu\n\";}"' || true
docker exec -u root swccg_wiki bash -c 'apachectl graceful 2>/dev/null || apache2ctl graceful 2>/dev/null || true'

edit "Virtual Set 14 (Original)" "$HUBS/Virtual_Set_14_(Original).wiki" "VS14 Original: link all 33 slip stubs"

edit 'Admiral Ackbar (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Admiral_Ackbar_(V)_(Virtual_Set_14).wiki' "VS14O stub 01"
edit 'Antilles Maneuver (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Antilles_Maneuver_(V)_(Virtual_Set_14).wiki' "VS14O stub 02"
edit 'Balanced Attack (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Balanced_Attack_(V)_(Virtual_Set_14).wiki' "VS14O stub 03"
edit 'Capital Support (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Capital_Support_(V)_(Virtual_Set_14).wiki' "VS14O stub 04"
edit 'General Walex Blissex (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/General_Walex_Blissex_(V)_(Virtual_Set_14).wiki' "VS14O stub 05"
edit 'Lieutenant Blount (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Lieutenant_Blount_(V)_(Virtual_Set_14).wiki' "VS14O stub 06"
edit 'Millennium Falcon (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Millennium_Falcon_(V)_(Virtual_Set_14).wiki' "VS14O stub 07"
edit 'Mon Calamari Star Cruiser (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Mon_Calamari_Star_Cruiser_(V)_(Virtual_Set_14).wiki' "VS14O stub 08"
edit 'Our Only Hope (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Our_Only_Hope_(V)_(Virtual_Set_14).wiki' "VS14O stub 09"
edit 'Put That Down (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Put_That_Down_(V)_(Virtual_Set_14).wiki' "VS14O stub 10"
edit 'Radiant VII (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Radiant_VII_(V)_(Virtual_Set_14).wiki' "VS14O stub 11"
edit 'Red Leader (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Red_Leader_(V)_(Virtual_Set_14).wiki' "VS14O stub 12"
edit 'Taking Them With Us (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Taking_Them_With_Us_(V)_(Virtual_Set_14).wiki' "VS14O stub 13"
edit 'Wesa Ready To Do Our-sa Part (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Wesa_Ready_To_Do_Our-sa_Part_(V)_(Virtual_Set_14).wiki' "VS14O stub 14"
edit 'Yoda, Master of the Force (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Yoda,_Master_of_the_Force_(V)_(Virtual_Set_14).wiki' "VS14O stub 15"
edit 'Accuser (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Accuser_(V)_(Virtual_Set_14).wiki' "VS14O stub 16"
edit 'Admiral Ozzel (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Admiral_Ozzel_(V)_(Virtual_Set_14).wiki' "VS14O stub 17"
edit 'After Her! (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/After_Her!_(V)_(Virtual_Set_14).wiki' "VS14O stub 18"
edit 'Black 3 (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Black_3_(V)_(Virtual_Set_14).wiki' "VS14O stub 19"
edit 'Captain Yorr (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Captain_Yorr_(V)_(Virtual_Set_14).wiki' "VS14O stub 20"
edit 'Comlink (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Comlink_(V)_(Virtual_Set_14).wiki' "VS14O stub 21"
edit 'Commander Nemet (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Commander_Nemet_(V)_(Virtual_Set_14).wiki' "VS14O stub 22"
edit 'Conquest (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Conquest_(V)_(Virtual_Set_14).wiki' "VS14O stub 23"
edit 'Death Star Gunner (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Death_Star_Gunner_(V)_(Virtual_Set_14).wiki' "VS14O stub 24"
edit 'Dominator (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Dominator_(V)_(Virtual_Set_14).wiki' "VS14O stub 25"
edit 'Grand Admiral Thrawn (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Grand_Admiral_Thrawn_(V)_(Virtual_Set_14).wiki' "VS14O stub 26"
edit 'I Can'\''t Shake Him! (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/I_Can'\''t_Shake_Him!_(V)_(Virtual_Set_14).wiki' "VS14O stub 27"
edit 'Much Anger In Him (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Much_Anger_In_Him_(V)_(Virtual_Set_14).wiki' "VS14O stub 28"
edit 'Nothing Can Get Through Our Shield (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Nothing_Can_Get_Through_Our_Shield_(V)_(Virtual_Set_14).wiki' "VS14O stub 29"
edit 'Sith Fury (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Sith_Fury_(V)_(Virtual_Set_14).wiki' "VS14O stub 30"
edit 'Trade Federation Tactics (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Trade_Federation_Tactics_(V)_(Virtual_Set_14).wiki' "VS14O stub 31"
edit 'Warrant Officer M'\''Kae (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Warrant_Officer_M'\''Kae_(V)_(Virtual_Set_14).wiki' "VS14O stub 32"
edit 'Where Are Those Droidekas?! (V) (Virtual Set 14)' '/opt/swccg-wiki/pages/vs14-original/Where_Are_Those_Droidekas?!_(V)_(Virtual_Set_14).wiki' "VS14O stub 33"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 14 (Original)
Admiral Ackbar (V) (Virtual Set 14)
Antilles Maneuver (V) (Virtual Set 14)
Balanced Attack (V) (Virtual Set 14)
Capital Support (V) (Virtual Set 14)
General Walex Blissex (V) (Virtual Set 14)
Lieutenant Blount (V) (Virtual Set 14)
Millennium Falcon (V) (Virtual Set 14)
Mon Calamari Star Cruiser (V) (Virtual Set 14)
Our Only Hope (V) (Virtual Set 14)
Put That Down (V) (Virtual Set 14)
Radiant VII (V) (Virtual Set 14)
Red Leader (V) (Virtual Set 14)
Taking Them With Us (V) (Virtual Set 14)
Wesa Ready To Do Our-sa Part (V) (Virtual Set 14)
Yoda, Master of the Force (V) (Virtual Set 14)
Accuser (V) (Virtual Set 14)
Admiral Ozzel (V) (Virtual Set 14)
After Her! (V) (Virtual Set 14)
Black 3 (V) (Virtual Set 14)
Captain Yorr (V) (Virtual Set 14)
Comlink (V) (Virtual Set 14)
Commander Nemet (V) (Virtual Set 14)
Conquest (V) (Virtual Set 14)
Death Star Gunner (V) (Virtual Set 14)
Dominator (V) (Virtual Set 14)
Grand Admiral Thrawn (V) (Virtual Set 14)
I Can't Shake Him! (V) (Virtual Set 14)
Much Anger In Him (V) (Virtual Set 14)
Nothing Can Get Through Our Shield (V) (Virtual Set 14)
Sith Fury (V) (Virtual Set 14)
Trade Federation Tactics (V) (Virtual Set 14)
Warrant Officer M'Kae (V) (Virtual Set 14)
Where Are Those Droidekas?! (V) (Virtual Set 14)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=['Admiral_Ackbar_(V)_(Virtual_Set_14)', 'Antilles_Maneuver_(V)_(Virtual_Set_14)', 'Balanced_Attack_(V)_(Virtual_Set_14)', 'Capital_Support_(V)_(Virtual_Set_14)', 'General_Walex_Blissex_(V)_(Virtual_Set_14)', 'Lieutenant_Blount_(V)_(Virtual_Set_14)', 'Millennium_Falcon_(V)_(Virtual_Set_14)', 'Mon_Calamari_Star_Cruiser_(V)_(Virtual_Set_14)', 'Our_Only_Hope_(V)_(Virtual_Set_14)', 'Put_That_Down_(V)_(Virtual_Set_14)', 'Radiant_VII_(V)_(Virtual_Set_14)', 'Red_Leader_(V)_(Virtual_Set_14)', 'Taking_Them_With_Us_(V)_(Virtual_Set_14)', 'Wesa_Ready_To_Do_Our-sa_Part_(V)_(Virtual_Set_14)', 'Yoda,_Master_of_the_Force_(V)_(Virtual_Set_14)', 'Accuser_(V)_(Virtual_Set_14)', 'Admiral_Ozzel_(V)_(Virtual_Set_14)', 'After_Her!_(V)_(Virtual_Set_14)', 'Black_3_(V)_(Virtual_Set_14)', 'Captain_Yorr_(V)_(Virtual_Set_14)', 'Comlink_(V)_(Virtual_Set_14)', 'Commander_Nemet_(V)_(Virtual_Set_14)', 'Conquest_(V)_(Virtual_Set_14)', 'Death_Star_Gunner_(V)_(Virtual_Set_14)', 'Dominator_(V)_(Virtual_Set_14)', 'Grand_Admiral_Thrawn_(V)_(Virtual_Set_14)', "I_Can't_Shake_Him!_(V)_(Virtual_Set_14)", 'Much_Anger_In_Him_(V)_(Virtual_Set_14)', 'Nothing_Can_Get_Through_Our_Shield_(V)_(Virtual_Set_14)', 'Sith_Fury_(V)_(Virtual_Set_14)', 'Trade_Federation_Tactics_(V)_(Virtual_Set_14)', "Warrant_Officer_M'Kae_(V)_(Virtual_Set_14)", 'Where_Are_Those_Droidekas?!_(V)_(Virtual_Set_14)']
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
print("STUBS %d/33 PASS fail=%s" % (pass_n, fail[:10]))
u="https://wiki.swccg.com/wiki/Virtual_Set_14_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS14O STUBS APPLY OK")

PY
