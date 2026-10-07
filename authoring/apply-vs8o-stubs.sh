#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs8-original
STUBS=$ROOT/pages/vs8-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs8o-stubs-import

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

echo "== importImages VS8O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS8O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs8o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs8o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 8 (Original) Remaster slip faces from VirtualCards8.pdf" \
  --overwrite \
  /tmp/vs8o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 8 (Original)" "$HUBS/Virtual_Set_8_(Original).wiki" "VS8 Original: link all 50 Remaster slip stubs"

edit 'Attark (V) (Virtual Set 8)' "$STUBS/Attark_(V)_(Virtual_Set_8).wiki" "VS8O stub 01"
edit 'Aved Luun (V) (Virtual Set 8)' "$STUBS/Aved_Luun_(V)_(Virtual_Set_8).wiki" "VS8O stub 02"
edit 'BG-J38 (V) (Virtual Set 8)' "$STUBS/BG-J38_(V)_(Virtual_Set_8).wiki" "VS8O stub 03"
edit 'Bargaining Table (V) (Virtual Set 8)' "$STUBS/Bargaining_Table_(V)_(Virtual_Set_8).wiki" "VS8O stub 04"
edit 'Careful Planning (V) (Virtual Set 8)' "$STUBS/Careful_Planning_(V)_(Virtual_Set_8).wiki" "VS8O stub 05"
edit 'Don'\''t Forget The Droids (V) (Virtual Set 8)' "$STUBS/Don't_Forget_The_Droids_(V)_(Virtual_Set_8).wiki" "VS8O stub 06"
edit 'Ellorrs Madak (V) (Virtual Set 8)' "$STUBS/Ellorrs_Madak_(V)_(Virtual_Set_8).wiki" "VS8O stub 07"
edit 'I Must Be Allowed To Speak (V) (Virtual Set 8)' "$STUBS/I_Must_Be_Allowed_To_Speak_(V)_(Virtual_Set_8).wiki" "VS8O stub 08"
edit 'Kalit (V) (Virtual Set 8)' "$STUBS/Kalit_(V)_(Virtual_Set_8).wiki" "VS8O stub 09"
edit 'Krayt Dragon Howl (V) (Virtual Set 8)' "$STUBS/Krayt_Dragon_Howl_(V)_(Virtual_Set_8).wiki" "VS8O stub 10"
edit 'Laudica (V) (Virtual Set 8)' "$STUBS/Laudica_(V)_(Virtual_Set_8).wiki" "VS8O stub 11"
edit 'Leslomy Tacema (V) (Virtual Set 8)' "$STUBS/Leslomy_Tacema_(V)_(Virtual_Set_8).wiki" "VS8O stub 12"
edit 'Master Luke (V) (Virtual Set 8)' "$STUBS/Master_Luke_(V)_(Virtual_Set_8).wiki" "VS8O stub 13"
edit 'Obi-Wan Kenobi (V) (Virtual Set 8)' "$STUBS/Obi-Wan_Kenobi_(V)_(Virtual_Set_8).wiki" "VS8O stub 14"
edit 'Princess Leia Organa (V) (Virtual Set 8)' "$STUBS/Princess_Leia_Organa_(V)_(Virtual_Set_8).wiki" "VS8O stub 15"
edit 'See-Threepio (V) (Virtual Set 8)' "$STUBS/See-Threepio_(V)_(Virtual_Set_8).wiki" "VS8O stub 16"
edit 'Tamtel Skreej (V) (Virtual Set 8)' "$STUBS/Tamtel_Skreej_(V)_(Virtual_Set_8).wiki" "VS8O stub 17"
edit 'Tanus Spijek (V) (Virtual Set 8)' "$STUBS/Tanus_Spijek_(V)_(Virtual_Set_8).wiki" "VS8O stub 18"
edit 'The Signal (V) (Virtual Set 8)' "$STUBS/The_Signal_(V)_(Virtual_Set_8).wiki" "VS8O stub 19"
edit 'The Time For Our Attack Has Come (V) (Virtual Set 8)' "$STUBS/The_Time_For_Our_Attack_Has_Come_(V)_(Virtual_Set_8).wiki" "VS8O stub 20"
edit 'Thrown Back (V) (Virtual Set 8)' "$STUBS/Thrown_Back_(V)_(Virtual_Set_8).wiki" "VS8O stub 21"
edit 'Tusken Breath Mask (V) (Virtual Set 8)' "$STUBS/Tusken_Breath_Mask_(V)_(Virtual_Set_8).wiki" "VS8O stub 22"
edit 'Ultimatum (V) (Virtual Set 8)' "$STUBS/Ultimatum_(V)_(Virtual_Set_8).wiki" "VS8O stub 23"
edit 'Yarna d'\''al'\'' Gargan (V) (Virtual Set 8)' "$STUBS/Yarna_d'al'_Gargan_(V)_(Virtual_Set_8).wiki" "VS8O stub 24"
edit 'Yerka Mig (V) (Virtual Set 8)' "$STUBS/Yerka_Mig_(V)_(Virtual_Set_8).wiki" "VS8O stub 25"
edit 'All Wrapped Up (V) (Virtual Set 8)' "$STUBS/All_Wrapped_Up_(V)_(Virtual_Set_8).wiki" "VS8O stub 26"
edit 'Bantha Herd (V) (Virtual Set 8)' "$STUBS/Bantha_Herd_(V)_(Virtual_Set_8).wiki" "VS8O stub 27"
edit 'Boba Fett (persona only) (V) (Virtual Set 8)' "$STUBS/Boba_Fett_(persona_only)_(V)_(Virtual_Set_8).wiki" "VS8O stub 28"
edit 'Cane Adiss (V) (Virtual Set 8)' "$STUBS/Cane_Adiss_(V)_(Virtual_Set_8).wiki" "VS8O stub 29"
edit 'Combat Readiness (V) (Virtual Set 8)' "$STUBS/Combat_Readiness_(V)_(Virtual_Set_8).wiki" "VS8O stub 30"
edit 'Den Of Thieves (V) (Virtual Set 8)' "$STUBS/Den_Of_Thieves_(V)_(Virtual_Set_8).wiki" "VS8O stub 31"
edit 'Drop! (V) (Virtual Set 8)' "$STUBS/Drop!_(V)_(Virtual_Set_8).wiki" "VS8O stub 32"
edit 'Fozec (V) (Virtual Set 8)' "$STUBS/Fozec_(V)_(Virtual_Set_8).wiki" "VS8O stub 33"
edit 'Gela Yeens (V) (Virtual Set 8)' "$STUBS/Gela_Yeens_(V)_(Virtual_Set_8).wiki" "VS8O stub 34"
edit 'Hermi Odle (V) (Virtual Set 8)' "$STUBS/Hermi_Odle_(V)_(Virtual_Set_8).wiki" "VS8O stub 35"
edit 'Hutt Bounty (V) (Virtual Set 8)' "$STUBS/Hutt_Bounty_(V)_(Virtual_Set_8).wiki" "VS8O stub 36"
edit 'Jabba The Hutt (V) (Virtual Set 8)' "$STUBS/Jabba_The_Hutt_(V)_(Virtual_Set_8).wiki" "VS8O stub 37"
edit 'Jabba'\''s Sail Barge (V) (Virtual Set 8)' "$STUBS/Jabba's_Sail_Barge_(V)_(Virtual_Set_8).wiki" "VS8O stub 38"
edit 'Jabba'\''s Space Cruiser (V) (Virtual Set 8)' "$STUBS/Jabba's_Space_Cruiser_(V)_(Virtual_Set_8).wiki" "VS8O stub 39"
edit 'J'\''Quille (V) (Virtual Set 8)' "$STUBS/J'Quille_(V)_(Virtual_Set_8).wiki" "VS8O stub 40"
edit 'Malakili (V) (Virtual Set 8)' "$STUBS/Malakili_(V)_(Virtual_Set_8).wiki" "VS8O stub 41"
edit 'Nizuc Bek (V) (Virtual Set 8)' "$STUBS/Nizuc_Bek_(V)_(Virtual_Set_8).wiki" "VS8O stub 42"
edit 'None Shall Pass (V) (Virtual Set 8)' "$STUBS/None_Shall_Pass_(V)_(Virtual_Set_8).wiki" "VS8O stub 43"
edit 'Sacrifice (V) (Virtual Set 8)' "$STUBS/Sacrifice_(V)_(Virtual_Set_8).wiki" "VS8O stub 44"
edit 'Twi'\''lek Advisor (V) (Virtual Set 8)' "$STUBS/Twi'lek_Advisor_(V)_(Virtual_Set_8).wiki" "VS8O stub 45"
edit 'URoRRuR'\''R'\''R (V) (Virtual Set 8)' "$STUBS/URoRRuR'R'R_(V)_(Virtual_Set_8).wiki" "VS8O stub 46"
edit 'URoRRuR'\''R'\''R'\''s Bantha (V) (Virtual Set 8)' "$STUBS/URoRRuR'R'R's_Bantha_(V)_(Virtual_Set_8).wiki" "VS8O stub 47"
edit 'Ur'\''Ru'\''r (V) (Virtual Set 8)' "$STUBS/Ur'Ru'r_(V)_(Virtual_Set_8).wiki" "VS8O stub 48"
edit 'Vizam (V) (Virtual Set 8)' "$STUBS/Vizam_(V)_(Virtual_Set_8).wiki" "VS8O stub 49"
edit 'Wooof (V) (Virtual Set 8)' "$STUBS/Wooof_(V)_(Virtual_Set_8).wiki" "VS8O stub 50"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 8 (Original)
Attark (V) (Virtual Set 8)
Aved Luun (V) (Virtual Set 8)
BG-J38 (V) (Virtual Set 8)
Bargaining Table (V) (Virtual Set 8)
Careful Planning (V) (Virtual Set 8)
Don't Forget The Droids (V) (Virtual Set 8)
Ellorrs Madak (V) (Virtual Set 8)
I Must Be Allowed To Speak (V) (Virtual Set 8)
Kalit (V) (Virtual Set 8)
Krayt Dragon Howl (V) (Virtual Set 8)
Laudica (V) (Virtual Set 8)
Leslomy Tacema (V) (Virtual Set 8)
Master Luke (V) (Virtual Set 8)
Obi-Wan Kenobi (V) (Virtual Set 8)
Princess Leia Organa (V) (Virtual Set 8)
See-Threepio (V) (Virtual Set 8)
Tamtel Skreej (V) (Virtual Set 8)
Tanus Spijek (V) (Virtual Set 8)
The Signal (V) (Virtual Set 8)
The Time For Our Attack Has Come (V) (Virtual Set 8)
Thrown Back (V) (Virtual Set 8)
Tusken Breath Mask (V) (Virtual Set 8)
Ultimatum (V) (Virtual Set 8)
Yarna d'al' Gargan (V) (Virtual Set 8)
Yerka Mig (V) (Virtual Set 8)
All Wrapped Up (V) (Virtual Set 8)
Bantha Herd (V) (Virtual Set 8)
Boba Fett (persona only) (V) (Virtual Set 8)
Cane Adiss (V) (Virtual Set 8)
Combat Readiness (V) (Virtual Set 8)
Den Of Thieves (V) (Virtual Set 8)
Drop! (V) (Virtual Set 8)
Fozec (V) (Virtual Set 8)
Gela Yeens (V) (Virtual Set 8)
Hermi Odle (V) (Virtual Set 8)
Hutt Bounty (V) (Virtual Set 8)
Jabba The Hutt (V) (Virtual Set 8)
Jabba's Sail Barge (V) (Virtual Set 8)
Jabba's Space Cruiser (V) (Virtual Set 8)
J'Quille (V) (Virtual Set 8)
Malakili (V) (Virtual Set 8)
Nizuc Bek (V) (Virtual Set 8)
None Shall Pass (V) (Virtual Set 8)
Sacrifice (V) (Virtual Set 8)
Twi'lek Advisor (V) (Virtual Set 8)
URoRRuR'R'R (V) (Virtual Set 8)
URoRRuR'R'R's Bantha (V) (Virtual Set 8)
Ur'Ru'r (V) (Virtual Set 8)
Vizam (V) (Virtual Set 8)
Wooof (V) (Virtual Set 8)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=['Attark_(V)_(Virtual_Set_8)', 'Aved_Luun_(V)_(Virtual_Set_8)', 'BG-J38_(V)_(Virtual_Set_8)', 'Bargaining_Table_(V)_(Virtual_Set_8)', 'Careful_Planning_(V)_(Virtual_Set_8)', "Don't_Forget_The_Droids_(V)_(Virtual_Set_8)", 'Ellorrs_Madak_(V)_(Virtual_Set_8)', 'I_Must_Be_Allowed_To_Speak_(V)_(Virtual_Set_8)', 'Kalit_(V)_(Virtual_Set_8)', 'Krayt_Dragon_Howl_(V)_(Virtual_Set_8)', 'Laudica_(V)_(Virtual_Set_8)', 'Leslomy_Tacema_(V)_(Virtual_Set_8)', 'Master_Luke_(V)_(Virtual_Set_8)', 'Obi-Wan_Kenobi_(V)_(Virtual_Set_8)', 'Princess_Leia_Organa_(V)_(Virtual_Set_8)', 'See-Threepio_(V)_(Virtual_Set_8)', 'Tamtel_Skreej_(V)_(Virtual_Set_8)', 'Tanus_Spijek_(V)_(Virtual_Set_8)', 'The_Signal_(V)_(Virtual_Set_8)', 'The_Time_For_Our_Attack_Has_Come_(V)_(Virtual_Set_8)', 'Thrown_Back_(V)_(Virtual_Set_8)', 'Tusken_Breath_Mask_(V)_(Virtual_Set_8)', 'Ultimatum_(V)_(Virtual_Set_8)', "Yarna_d'al'_Gargan_(V)_(Virtual_Set_8)", 'Yerka_Mig_(V)_(Virtual_Set_8)', 'All_Wrapped_Up_(V)_(Virtual_Set_8)', 'Bantha_Herd_(V)_(Virtual_Set_8)', 'Boba_Fett_(persona_only)_(V)_(Virtual_Set_8)', 'Cane_Adiss_(V)_(Virtual_Set_8)', 'Combat_Readiness_(V)_(Virtual_Set_8)', 'Den_Of_Thieves_(V)_(Virtual_Set_8)', 'Drop!_(V)_(Virtual_Set_8)', 'Fozec_(V)_(Virtual_Set_8)', 'Gela_Yeens_(V)_(Virtual_Set_8)', 'Hermi_Odle_(V)_(Virtual_Set_8)', 'Hutt_Bounty_(V)_(Virtual_Set_8)', 'Jabba_The_Hutt_(V)_(Virtual_Set_8)', "Jabba's_Sail_Barge_(V)_(Virtual_Set_8)", "Jabba's_Space_Cruiser_(V)_(Virtual_Set_8)", "J'Quille_(V)_(Virtual_Set_8)", 'Malakili_(V)_(Virtual_Set_8)', 'Nizuc_Bek_(V)_(Virtual_Set_8)', 'None_Shall_Pass_(V)_(Virtual_Set_8)', 'Sacrifice_(V)_(Virtual_Set_8)', "Twi'lek_Advisor_(V)_(Virtual_Set_8)", "URoRRuR'R'R_(V)_(Virtual_Set_8)", "URoRRuR'R'R's_Bantha_(V)_(Virtual_Set_8)", "Ur'Ru'r_(V)_(Virtual_Set_8)", 'Vizam_(V)_(Virtual_Set_8)', 'Wooof_(V)_(Virtual_Set_8)']
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
u="https://wiki.swccg.com/wiki/Virtual_Set_8_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS8O STUBS APPLY OK")

PY

