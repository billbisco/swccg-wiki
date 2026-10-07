#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs6-original
STUBS=$ROOT/pages/vs6-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs6o-stubs-import

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

echo "== importImages VS6O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS6O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs6o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs6o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 6 (Original) Remaster slip faces from VirtualCards6.pdf" \
  --overwrite \
  /tmp/vs6o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 6 (Original)" "$HUBS/Virtual_Set_6_(Original).wiki" "VS6 Original: link all 50 Remaster slip stubs"
edit 'Access Denied (V) (Virtual Set 6)' "$STUBS/Access_Denied_(V)_(Virtual_Set_6).wiki" "VS6O stub 01"
edit 'All My Urchins (V) (Virtual Set 6)' "$STUBS/All_My_Urchins_(V)_(Virtual_Set_6).wiki" "VS6O stub 02"
edit 'Beldon'\''s Eye (V) (Virtual Set 6)' "$STUBS/Beldons_Eye_(V)_(Virtual_Set_6).wiki" "VS6O stub 03"
edit 'Bionic Hand (V) (Virtual Set 6)' "$STUBS/Bionic_Hand_(V)_(Virtual_Set_6).wiki" "VS6O stub 04"
edit 'Bright Hope (V) (Virtual Set 6)' "$STUBS/Bright_Hope_(V)_(Virtual_Set_6).wiki" "VS6O stub 05"
edit 'Civil Disorder (V) (Virtual Set 6)' "$STUBS/Civil_Disorder_(V)_(Virtual_Set_6).wiki" "VS6O stub 06"
edit 'Computer Interface (V) (Virtual Set 6)' "$STUBS/Computer_Interface_(V)_(Virtual_Set_6).wiki" "VS6O stub 07"
edit 'Courage Of A Skywalker (V) (Virtual Set 6)' "$STUBS/Courage_Of_A_Skywalker_(V)_(Virtual_Set_6).wiki" "VS6O stub 08"
edit 'Down With The Emperor! (V) (Virtual Set 6)' "$STUBS/Down_With_The_Emperor!_(V)_(Virtual_Set_6).wiki" "VS6O stub 09"
edit 'Hopping Mad (V) (Virtual Set 6)' "$STUBS/Hopping_Mad_(V)_(Virtual_Set_6).wiki" "VS6O stub 10"
edit 'Imperial Atrocity (V) (Virtual Set 6)' "$STUBS/Imperial_Atrocity_(V)_(Virtual_Set_6).wiki" "VS6O stub 11"
edit 'Kebyc (V) (Virtual Set 6)' "$STUBS/Kebyc_(V)_(Virtual_Set_6).wiki" "VS6O stub 12"
edit 'Keep Your Eyes Open (V) (Virtual Set 6)' "$STUBS/Keep_Your_Eyes_Open_(V)_(Virtual_Set_6).wiki" "VS6O stub 13"
edit 'Leia Of Alderaan (V) (Virtual Set 6)' "$STUBS/Leia_Of_Alderaan_(V)_(Virtual_Set_6).wiki" "VS6O stub 14"
edit 'Lobot (V) (Virtual Set 6)' "$STUBS/Lobot_(V)_(Virtual_Set_6).wiki" "VS6O stub 15"
edit 'Luke'\''s Blaster Pistol (V) (Virtual Set 6)' "$STUBS/Lukes_Blaster_Pistol_(V)_(Virtual_Set_6).wiki" "VS6O stub 16"
edit 'Princess Leia (V) (Virtual Set 6)' "$STUBS/Princess_Leia_(V)_(Virtual_Set_6).wiki" "VS6O stub 17"
edit 'Rebel Planners (V) (Virtual Set 6)' "$STUBS/Rebel_Planners_(V)_(Virtual_Set_6).wiki" "VS6O stub 18"
edit 'Redemption (V) (Virtual Set 6)' "$STUBS/Redemption_(V)_(Virtual_Set_6).wiki" "VS6O stub 19"
edit 'Seeking An Audience (V) (Virtual Set 6)' "$STUBS/Seeking_An_Audience_(V)_(Virtual_Set_6).wiki" "VS6O stub 20"
edit 'Surreptitious Glance (V) (Virtual Set 6)' "$STUBS/Surreptitious_Glance_(V)_(Virtual_Set_6).wiki" "VS6O stub 21"
edit 'Weather Vane (V) (Light) (Virtual Set 6)' "$STUBS/Weather_Vane_(V)_(Light)_(Virtual_Set_6).wiki" "VS6O stub 22"
edit 'We'\''ll Find Han (V) (Virtual Set 6)' "$STUBS/Well_Find_Han_(V)_(Virtual_Set_6).wiki" "VS6O stub 23"
edit 'Weapons Display (V) (Virtual Set 6)' "$STUBS/Weapons_Display_(V)_(Virtual_Set_6).wiki" "VS6O stub 24"
edit 'Wookiee Strangle (V) (Virtual Set 6)' "$STUBS/Wookiee_Strangle_(V)_(Virtual_Set_6).wiki" "VS6O stub 25"
edit 'A Day Long Remembered (V) (Virtual Set 6)' "$STUBS/A_Day_Long_Remembered_(V)_(Virtual_Set_6).wiki" "VS6O stub 26"
edit 'Ability, Ability, Ability (V) (Virtual Set 6)' "$STUBS/Ability,_Ability,_Ability_(V)_(Virtual_Set_6).wiki" "VS6O stub 27"
edit 'Atmospheric Assault (V) (Virtual Set 6)' "$STUBS/Atmospheric_Assault_(V)_(Virtual_Set_6).wiki" "VS6O stub 28"
edit 'Boba Fett (V) (Virtual Set 6)' "$STUBS/Boba_Fett_(V)_(Virtual_Set_6).wiki" "VS6O stub 29"
edit 'Boba Fett'\''s Blaster Rifle (V) (Virtual Set 6)' "$STUBS/Boba_Fetts_Blaster_Rifle_(V)_(Virtual_Set_6).wiki" "VS6O stub 30"
edit 'Captain Bewil (V) (Virtual Set 6)' "$STUBS/Captain_Bewil_(V)_(Virtual_Set_6).wiki" "VS6O stub 31"
edit 'Despair (V) (Virtual Set 6)' "$STUBS/Despair_(V)_(Virtual_Set_6).wiki" "VS6O stub 32"
edit 'E-3PO (V) (Virtual Set 6)' "$STUBS/E-3PO_(V)_(Virtual_Set_6).wiki" "VS6O stub 33"
edit 'Firepower (V) (Virtual Set 6)' "$STUBS/Firepower_(V)_(Virtual_Set_6).wiki" "VS6O stub 34"
edit 'He'\''s All Yours, Bounty Hunter (V) (Virtual Set 6)' "$STUBS/Hes_All_Yours,_Bounty_Hunter_(V)_(Virtual_Set_6).wiki" "VS6O stub 35"
edit 'I Am Your Father (V) (Virtual Set 6)' "$STUBS/I_Am_Your_Father_(V)_(Virtual_Set_6).wiki" "VS6O stub 36"
edit 'I Had No Choice (V) (Virtual Set 6)' "$STUBS/I_Had_No_Choice_(V)_(Virtual_Set_6).wiki" "VS6O stub 37"
edit 'Imperial Decree (V) (Virtual Set 6)' "$STUBS/Imperial_Decree_(V)_(Virtual_Set_6).wiki" "VS6O stub 38"
edit 'Imperial Propaganda (V) (Virtual Set 6)' "$STUBS/Imperial_Propaganda_(V)_(Virtual_Set_6).wiki" "VS6O stub 39"
edit 'Jabba'\''s Influence (V) (Virtual Set 6)' "$STUBS/Jabbas_Influence_(V)_(Virtual_Set_6).wiki" "VS6O stub 40"
edit 'Kuat Drive Yards (V) (Virtual Set 6)' "$STUBS/Kuat_Drive_Yards_(V)_(Virtual_Set_6).wiki" "VS6O stub 41"
edit 'Lando Calrissian (V) (Virtual Set 6)' "$STUBS/Lando_Calrissian_(V)_(Virtual_Set_6).wiki" "VS6O stub 42"
edit 'Levitation Attack (V) (Virtual Set 6)' "$STUBS/Levitation_Attack_(V)_(Virtual_Set_6).wiki" "VS6O stub 43"
edit 'Slip Sliding Away (V) (Virtual Set 6)' "$STUBS/Slip_Sliding_Away_(V)_(Virtual_Set_6).wiki" "VS6O stub 44"
edit 'Special Delivery (V) (Virtual Set 6)' "$STUBS/Special_Delivery_(V)_(Virtual_Set_6).wiki" "VS6O stub 45"
edit 'The Emperor (V) (Virtual Set 6)' "$STUBS/The_Emperor_(V)_(Virtual_Set_6).wiki" "VS6O stub 46"
edit 'The Emperor'\''s Prize (V) (Virtual Set 6)' "$STUBS/The_Emperors_Prize_(V)_(Virtual_Set_6).wiki" "VS6O stub 47"
edit 'Vader'\''s Bounty (V) (Virtual Set 6)' "$STUBS/Vaders_Bounty_(V)_(Virtual_Set_6).wiki" "VS6O stub 48"
edit 'Weather Vane (V) (Dark) (Virtual Set 6)' "$STUBS/Weather_Vane_(V)_(Dark)_(Virtual_Set_6).wiki" "VS6O stub 49"
edit 'We'\''re The Bait (V) (Virtual Set 6)' "$STUBS/Were_The_Bait_(V)_(Virtual_Set_6).wiki" "VS6O stub 50"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 6 (Original)
Access Denied (V) (Virtual Set 6)
All My Urchins (V) (Virtual Set 6)
Beldon's Eye (V) (Virtual Set 6)
Bionic Hand (V) (Virtual Set 6)
Bright Hope (V) (Virtual Set 6)
Civil Disorder (V) (Virtual Set 6)
Computer Interface (V) (Virtual Set 6)
Courage Of A Skywalker (V) (Virtual Set 6)
Down With The Emperor! (V) (Virtual Set 6)
Hopping Mad (V) (Virtual Set 6)
Imperial Atrocity (V) (Virtual Set 6)
Kebyc (V) (Virtual Set 6)
Keep Your Eyes Open (V) (Virtual Set 6)
Leia Of Alderaan (V) (Virtual Set 6)
Lobot (V) (Virtual Set 6)
Luke's Blaster Pistol (V) (Virtual Set 6)
Princess Leia (V) (Virtual Set 6)
Rebel Planners (V) (Virtual Set 6)
Redemption (V) (Virtual Set 6)
Seeking An Audience (V) (Virtual Set 6)
Surreptitious Glance (V) (Virtual Set 6)
Weather Vane (V) (Light) (Virtual Set 6)
We'll Find Han (V) (Virtual Set 6)
Weapons Display (V) (Virtual Set 6)
Wookiee Strangle (V) (Virtual Set 6)
A Day Long Remembered (V) (Virtual Set 6)
Ability, Ability, Ability (V) (Virtual Set 6)
Atmospheric Assault (V) (Virtual Set 6)
Boba Fett (V) (Virtual Set 6)
Boba Fett's Blaster Rifle (V) (Virtual Set 6)
Captain Bewil (V) (Virtual Set 6)
Despair (V) (Virtual Set 6)
E-3PO (V) (Virtual Set 6)
Firepower (V) (Virtual Set 6)
He's All Yours, Bounty Hunter (V) (Virtual Set 6)
I Am Your Father (V) (Virtual Set 6)
I Had No Choice (V) (Virtual Set 6)
Imperial Decree (V) (Virtual Set 6)
Imperial Propaganda (V) (Virtual Set 6)
Jabba's Influence (V) (Virtual Set 6)
Kuat Drive Yards (V) (Virtual Set 6)
Lando Calrissian (V) (Virtual Set 6)
Levitation Attack (V) (Virtual Set 6)
Slip Sliding Away (V) (Virtual Set 6)
Special Delivery (V) (Virtual Set 6)
The Emperor (V) (Virtual Set 6)
The Emperor's Prize (V) (Virtual Set 6)
Vader's Bounty (V) (Virtual Set 6)
Weather Vane (V) (Dark) (Virtual Set 6)
We're The Bait (V) (Virtual Set 6)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=['Access_Denied_(V)_(Virtual_Set_6)', 'All_My_Urchins_(V)_(Virtual_Set_6)', "Beldon's_Eye_(V)_(Virtual_Set_6)", 'Bionic_Hand_(V)_(Virtual_Set_6)', 'Bright_Hope_(V)_(Virtual_Set_6)', 'Civil_Disorder_(V)_(Virtual_Set_6)', 'Computer_Interface_(V)_(Virtual_Set_6)', 'Courage_Of_A_Skywalker_(V)_(Virtual_Set_6)', 'Down_With_The_Emperor!_(V)_(Virtual_Set_6)', 'Hopping_Mad_(V)_(Virtual_Set_6)', 'Imperial_Atrocity_(V)_(Virtual_Set_6)', 'Kebyc_(V)_(Virtual_Set_6)', 'Keep_Your_Eyes_Open_(V)_(Virtual_Set_6)', 'Leia_Of_Alderaan_(V)_(Virtual_Set_6)', 'Lobot_(V)_(Virtual_Set_6)', "Luke's_Blaster_Pistol_(V)_(Virtual_Set_6)", 'Princess_Leia_(V)_(Virtual_Set_6)', 'Rebel_Planners_(V)_(Virtual_Set_6)', 'Redemption_(V)_(Virtual_Set_6)', 'Seeking_An_Audience_(V)_(Virtual_Set_6)', 'Surreptitious_Glance_(V)_(Virtual_Set_6)', 'Weather_Vane_(V)_(Light)_(Virtual_Set_6)', "We'll_Find_Han_(V)_(Virtual_Set_6)", 'Weapons_Display_(V)_(Virtual_Set_6)', 'Wookiee_Strangle_(V)_(Virtual_Set_6)', 'A_Day_Long_Remembered_(V)_(Virtual_Set_6)', 'Ability,_Ability,_Ability_(V)_(Virtual_Set_6)', 'Atmospheric_Assault_(V)_(Virtual_Set_6)', 'Boba_Fett_(V)_(Virtual_Set_6)', "Boba_Fett's_Blaster_Rifle_(V)_(Virtual_Set_6)", 'Captain_Bewil_(V)_(Virtual_Set_6)', 'Despair_(V)_(Virtual_Set_6)', 'E-3PO_(V)_(Virtual_Set_6)', 'Firepower_(V)_(Virtual_Set_6)', "He's_All_Yours,_Bounty_Hunter_(V)_(Virtual_Set_6)", 'I_Am_Your_Father_(V)_(Virtual_Set_6)', 'I_Had_No_Choice_(V)_(Virtual_Set_6)', 'Imperial_Decree_(V)_(Virtual_Set_6)', 'Imperial_Propaganda_(V)_(Virtual_Set_6)', "Jabba's_Influence_(V)_(Virtual_Set_6)", 'Kuat_Drive_Yards_(V)_(Virtual_Set_6)', 'Lando_Calrissian_(V)_(Virtual_Set_6)', 'Levitation_Attack_(V)_(Virtual_Set_6)', 'Slip_Sliding_Away_(V)_(Virtual_Set_6)', 'Special_Delivery_(V)_(Virtual_Set_6)', 'The_Emperor_(V)_(Virtual_Set_6)', "The_Emperor's_Prize_(V)_(Virtual_Set_6)", "Vader's_Bounty_(V)_(Virtual_Set_6)", 'Weather_Vane_(V)_(Dark)_(Virtual_Set_6)', "We're_The_Bait_(V)_(Virtual_Set_6)"]
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
print("STUBS %d/50 PASS fail=%s" % (pass_n, fail[:10]))
u="https://wiki.swccg.com/wiki/Virtual_Set_6_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS6O STUBS APPLY OK")
PY

