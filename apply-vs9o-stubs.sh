#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs9-original
STUBS=$ROOT/pages/vs9-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs9o-stubs-import

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

echo "== importImages VS9O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS9O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs9o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs9o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 9 (Original) Remaster slip faces from VirtualCards9.pdf" \
  --overwrite \
  /tmp/vs9o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 9 (Original)" "$HUBS/Virtual_Set_9_(Original).wiki" "VS9 Original: link all 50 Remaster slip stubs"
edit 'A280 Sharpshooter Rifle (V) (Virtual Set 9)' "$STUBS/A280_Sharpshooter_Rifle_(V)_(Virtual_Set_9).wiki" "VS9O stub 01"
edit 'Chewie'"'"'s AT-ST (V) (Virtual Set 9)' "$STUBS/Chewies_AT-ST_(V)_(Virtual_Set_9).wiki" "VS9O stub 02"
edit 'Chief Chirpa (V) (Virtual Set 9)' "$STUBS/Chief_Chirpa_(V)_(Virtual_Set_9).wiki" "VS9O stub 03"
edit 'Corellian Retort (V) (Virtual Set 9)' "$STUBS/Corellian_Retort_(V)_(Virtual_Set_9).wiki" "VS9O stub 04"
edit 'Count Me In (V) (Virtual Set 9)' "$STUBS/Count_Me_In_(V)_(Virtual_Set_9).wiki" "VS9O stub 05"
edit 'Covert Landing (V) (Virtual Set 9)' "$STUBS/Covert_Landing_(V)_(Virtual_Set_9).wiki" "VS9O stub 06"
edit 'Endor Celebration (V) (Virtual Set 9)' "$STUBS/Endor_Celebration_(V)_(Virtual_Set_9).wiki" "VS9O stub 07"
edit 'Entrenchment (V) (Virtual Set 9)' "$STUBS/Entrenchment_(V)_(Virtual_Set_9).wiki" "VS9O stub 08"
edit 'General Solo (V) (Virtual Set 9)' "$STUBS/General_Solo_(V)_(Virtual_Set_9).wiki" "VS9O stub 09"
edit 'I'"'"'m With You Too (V) (Virtual Set 9)' "$STUBS/Im_With_You_Too_(V)_(Virtual_Set_9).wiki" "VS9O stub 10"
edit 'I Wonder Who They Found (V) (Virtual Set 9)' "$STUBS/I_Wonder_Who_They_Found_(V)_(Virtual_Set_9).wiki" "VS9O stub 11"
edit 'Jedi Lightsaber (V) (Virtual Set 9)' "$STUBS/Jedi_Lightsaber_(V)_(Virtual_Set_9).wiki" "VS9O stub 12"
edit 'Luke Skywalker, Rebel Scout (V) (Virtual Set 9)' "$STUBS/Luke_Skywalker,_Rebel_Scout_(V)_(Virtual_Set_9).wiki" "VS9O stub 13"
edit 'Mace Windu (V) (Virtual Set 9)' "$STUBS/Mace_Windu_(V)_(Virtual_Set_9).wiki" "VS9O stub 14"
edit 'Mon Mothma (V) (Virtual Set 9)' "$STUBS/Mon_Mothma_(V)_(Virtual_Set_9).wiki" "VS9O stub 15"
edit 'No Questions Asked (V) (Virtual Set 9)' "$STUBS/No_Questions_Asked_(V)_(Virtual_Set_9).wiki" "VS9O stub 16"
edit 'Quick Draw (V) (Virtual Set 9)' "$STUBS/Quick_Draw_(V)_(Virtual_Set_9).wiki" "VS9O stub 17"
edit 'Rapid Deployment (V) (Virtual Set 9)' "$STUBS/Rapid_Deployment_(V)_(Virtual_Set_9).wiki" "VS9O stub 18"
edit 'Superficial Damage (V) (Virtual Set 9)' "$STUBS/Superficial_Damage_(V)_(Virtual_Set_9).wiki" "VS9O stub 19"
edit 'That'"'"'s One (V) (Virtual Set 9)' "$STUBS/Thats_One_(V)_(Virtual_Set_9).wiki" "VS9O stub 20"
edit 'The Planet That It'"'"'s Farthest From (V) (Virtual Set 9)' "$STUBS/The_Planet_That_Its_Farthest_From_(V)_(Virtual_Set_9).wiki" "VS9O stub 21"
edit 'The Professor (V) (Virtual Set 9)' "$STUBS/The_Professor_(V)_(Virtual_Set_9).wiki" "VS9O stub 22"
edit 'Tydirium (V) (Virtual Set 9)' "$STUBS/Tydirium_(V)_(Virtual_Set_9).wiki" "VS9O stub 23"
edit 'Watch Your Step (V) / This Place Can Be A Little Rough (V) (Virtual Set 9)' "$STUBS/Watch_Your_Step_(V)_-_This_Place_Can_Be_A_Little_Rough_(V)_(Virtual_Set_9).wiki" "VS9O stub 24"
edit 'Wicket (V) (Virtual Set 9)' "$STUBS/Wicket_(V)_(Virtual_Set_9).wiki" "VS9O stub 25"
edit 'A Bright Center To The Universe (V) (Virtual Set 9)' "$STUBS/A_Bright_Center_To_The_Universe_(V)_(Virtual_Set_9).wiki" "VS9O stub 26"
edit 'Aratech Corporation (V) (Virtual Set 9)' "$STUBS/Aratech_Corporation_(V)_(Virtual_Set_9).wiki" "VS9O stub 27"
edit 'AT-ST Dual Cannon (V) (Virtual Set 9)' "$STUBS/AT-ST_Dual_Cannon_(V)_(Virtual_Set_9).wiki" "VS9O stub 28"
edit 'Commander Igar (V) (Virtual Set 9)' "$STUBS/Commander_Igar_(V)_(Virtual_Set_9).wiki" "VS9O stub 29"
edit 'Crossfire (V) (Virtual Set 9)' "$STUBS/Crossfire_(V)_(Virtual_Set_9).wiki" "VS9O stub 30"
edit 'Dead Ewok (V) (Virtual Set 9)' "$STUBS/Dead_Ewok_(V)_(Virtual_Set_9).wiki" "VS9O stub 31"
edit 'Dreaded Imperial Starfleet (V) (Virtual Set 9)' "$STUBS/Dreaded_Imperial_Starfleet_(V)_(Virtual_Set_9).wiki" "VS9O stub 32"
edit 'Empire'"'"'s New Order (V) (Virtual Set 9)' "$STUBS/Empires_New_Order_(V)_(Virtual_Set_9).wiki" "VS9O stub 33"
edit 'Establish Secret Base (V) (Virtual Set 9)' "$STUBS/Establish_Secret_Base_(V)_(Virtual_Set_9).wiki" "VS9O stub 34"
edit 'Feltipern Trevagg'"'"'s Stun Rifle (V) (Virtual Set 9)' "$STUBS/Feltipern_Trevaggs_Stun_Rifle_(V)_(Virtual_Set_9).wiki" "VS9O stub 35"
edit 'Freeze! (V) (Virtual Set 9)' "$STUBS/Freeze!_(V)_(Virtual_Set_9).wiki" "VS9O stub 36"
edit 'Imperial Academy Training (V) (Virtual Set 9)' "$STUBS/Imperial_Academy_Training_(V)_(Virtual_Set_9).wiki" "VS9O stub 37"
edit 'Imperial Tyranny (V) (Virtual Set 9)' "$STUBS/Imperial_Tyranny_(V)_(Virtual_Set_9).wiki" "VS9O stub 38"
edit 'Inconsequential Losses (V) (Virtual Set 9)' "$STUBS/Inconsequential_Losses_(V)_(Virtual_Set_9).wiki" "VS9O stub 39"
edit 'Lieutenant Grond (V) (Virtual Set 9)' "$STUBS/Lieutenant_Grond_(V)_(Virtual_Set_9).wiki" "VS9O stub 40"
edit 'Lieutenant Renz (V) (Virtual Set 9)' "$STUBS/Lieutenant_Renz_(V)_(Virtual_Set_9).wiki" "VS9O stub 41"
edit 'Lieutenant Watts (V) (Virtual Set 9)' "$STUBS/Lieutenant_Watts_(V)_(Virtual_Set_9).wiki" "VS9O stub 42"
edit 'Major Hewex (V) (Virtual Set 9)' "$STUBS/Major_Hewex_(V)_(Virtual_Set_9).wiki" "VS9O stub 43"
edit 'Outflank (V) (Virtual Set 9)' "$STUBS/Outflank_(V)_(Virtual_Set_9).wiki" "VS9O stub 44"
edit 'Pinned Down (V) (Virtual Set 9)' "$STUBS/Pinned_Down_(V)_(Virtual_Set_9).wiki" "VS9O stub 45"
edit 'Scout Recon (V) (Virtual Set 9)' "$STUBS/Scout_Recon_(V)_(Virtual_Set_9).wiki" "VS9O stub 46"
edit 'Sergeant Wallen (V) (Virtual Set 9)' "$STUBS/Sergeant_Wallen_(V)_(Virtual_Set_9).wiki" "VS9O stub 47"
edit 'Sneak Attack (V) (Virtual Set 9)' "$STUBS/Sneak_Attack_(V)_(Virtual_Set_9).wiki" "VS9O stub 48"
edit 'Well-earned Command (V) (Virtual Set 9)' "$STUBS/Well-earned_Command_(V)_(Virtual_Set_9).wiki" "VS9O stub 49"
edit 'Wipe Them Out, All Of Them (V) (Virtual Set 9)' "$STUBS/Wipe_Them_Out,_All_Of_Them_(V)_(Virtual_Set_9).wiki" "VS9O stub 50"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 9 (Original)
A280 Sharpshooter Rifle (V) (Virtual Set 9)
Chewie's AT-ST (V) (Virtual Set 9)
Chief Chirpa (V) (Virtual Set 9)
Corellian Retort (V) (Virtual Set 9)
Count Me In (V) (Virtual Set 9)
Covert Landing (V) (Virtual Set 9)
Endor Celebration (V) (Virtual Set 9)
Entrenchment (V) (Virtual Set 9)
General Solo (V) (Virtual Set 9)
I'm With You Too (V) (Virtual Set 9)
I Wonder Who They Found (V) (Virtual Set 9)
Jedi Lightsaber (V) (Virtual Set 9)
Luke Skywalker, Rebel Scout (V) (Virtual Set 9)
Mace Windu (V) (Virtual Set 9)
Mon Mothma (V) (Virtual Set 9)
No Questions Asked (V) (Virtual Set 9)
Quick Draw (V) (Virtual Set 9)
Rapid Deployment (V) (Virtual Set 9)
Superficial Damage (V) (Virtual Set 9)
That's One (V) (Virtual Set 9)
The Planet That It's Farthest From (V) (Virtual Set 9)
The Professor (V) (Virtual Set 9)
Tydirium (V) (Virtual Set 9)
Watch Your Step (V) / This Place Can Be A Little Rough (V) (Virtual Set 9)
Wicket (V) (Virtual Set 9)
A Bright Center To The Universe (V) (Virtual Set 9)
Aratech Corporation (V) (Virtual Set 9)
AT-ST Dual Cannon (V) (Virtual Set 9)
Commander Igar (V) (Virtual Set 9)
Crossfire (V) (Virtual Set 9)
Dead Ewok (V) (Virtual Set 9)
Dreaded Imperial Starfleet (V) (Virtual Set 9)
Empire's New Order (V) (Virtual Set 9)
Establish Secret Base (V) (Virtual Set 9)
Feltipern Trevagg's Stun Rifle (V) (Virtual Set 9)
Freeze! (V) (Virtual Set 9)
Imperial Academy Training (V) (Virtual Set 9)
Imperial Tyranny (V) (Virtual Set 9)
Inconsequential Losses (V) (Virtual Set 9)
Lieutenant Grond (V) (Virtual Set 9)
Lieutenant Renz (V) (Virtual Set 9)
Lieutenant Watts (V) (Virtual Set 9)
Major Hewex (V) (Virtual Set 9)
Outflank (V) (Virtual Set 9)
Pinned Down (V) (Virtual Set 9)
Scout Recon (V) (Virtual Set 9)
Sergeant Wallen (V) (Virtual Set 9)
Sneak Attack (V) (Virtual Set 9)
Well-earned Command (V) (Virtual Set 9)
Wipe Them Out, All Of Them (V) (Virtual Set 9)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=[
  'A280_Sharpshooter_Rifle_(V)_(Virtual_Set_9)',
  "Chewie's_AT-ST_(V)_(Virtual_Set_9)",
  'Chief_Chirpa_(V)_(Virtual_Set_9)',
  'Corellian_Retort_(V)_(Virtual_Set_9)',
  'Count_Me_In_(V)_(Virtual_Set_9)',
  'Covert_Landing_(V)_(Virtual_Set_9)',
  'Endor_Celebration_(V)_(Virtual_Set_9)',
  'Entrenchment_(V)_(Virtual_Set_9)',
  'General_Solo_(V)_(Virtual_Set_9)',
  "I'm_With_You_Too_(V)_(Virtual_Set_9)",
  'I_Wonder_Who_They_Found_(V)_(Virtual_Set_9)',
  'Jedi_Lightsaber_(V)_(Virtual_Set_9)',
  'Luke_Skywalker,_Rebel_Scout_(V)_(Virtual_Set_9)',
  'Mace_Windu_(V)_(Virtual_Set_9)',
  'Mon_Mothma_(V)_(Virtual_Set_9)',
  'No_Questions_Asked_(V)_(Virtual_Set_9)',
  'Quick_Draw_(V)_(Virtual_Set_9)',
  'Rapid_Deployment_(V)_(Virtual_Set_9)',
  'Superficial_Damage_(V)_(Virtual_Set_9)',
  "That's_One_(V)_(Virtual_Set_9)",
  "The_Planet_That_It's_Farthest_From_(V)_(Virtual_Set_9)",
  'The_Professor_(V)_(Virtual_Set_9)',
  'Tydirium_(V)_(Virtual_Set_9)',
  'Watch_Your_Step_(V)_/_This_Place_Can_Be_A_Little_Rough_(V)_(Virtual_Set_9)',
  'Wicket_(V)_(Virtual_Set_9)',
  'A_Bright_Center_To_The_Universe_(V)_(Virtual_Set_9)',
  'Aratech_Corporation_(V)_(Virtual_Set_9)',
  'AT-ST_Dual_Cannon_(V)_(Virtual_Set_9)',
  'Commander_Igar_(V)_(Virtual_Set_9)',
  'Crossfire_(V)_(Virtual_Set_9)',
  'Dead_Ewok_(V)_(Virtual_Set_9)',
  'Dreaded_Imperial_Starfleet_(V)_(Virtual_Set_9)',
  "Empire's_New_Order_(V)_(Virtual_Set_9)",
  'Establish_Secret_Base_(V)_(Virtual_Set_9)',
  "Feltipern_Trevagg's_Stun_Rifle_(V)_(Virtual_Set_9)",
  'Freeze!_(V)_(Virtual_Set_9)',
  'Imperial_Academy_Training_(V)_(Virtual_Set_9)',
  'Imperial_Tyranny_(V)_(Virtual_Set_9)',
  'Inconsequential_Losses_(V)_(Virtual_Set_9)',
  'Lieutenant_Grond_(V)_(Virtual_Set_9)',
  'Lieutenant_Renz_(V)_(Virtual_Set_9)',
  'Lieutenant_Watts_(V)_(Virtual_Set_9)',
  'Major_Hewex_(V)_(Virtual_Set_9)',
  'Outflank_(V)_(Virtual_Set_9)',
  'Pinned_Down_(V)_(Virtual_Set_9)',
  'Scout_Recon_(V)_(Virtual_Set_9)',
  'Sergeant_Wallen_(V)_(Virtual_Set_9)',
  'Sneak_Attack_(V)_(Virtual_Set_9)',
  'Well-earned_Command_(V)_(Virtual_Set_9)',
  'Wipe_Them_Out,_All_Of_Them_(V)_(Virtual_Set_9)',
]
for slug in slugs:
  u="https://wiki.swccg.com/wiki/"+urllib.parse.quote(slug, safe="()_,!'?/")
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    ok=(r.status==200)
  except Exception:
    ok=False
  print(("PASS" if ok else "FAIL"), u)
  if ok: pass_n+=1
  else: fail.append(u)
print("STUBS %d/50 PASS fail=%s" % (pass_n, fail[:10]))
u="https://wiki.swccg.com/wiki/Virtual_Set_9_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS9O STUBS APPLY OK")
PY
