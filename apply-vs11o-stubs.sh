#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs11-original
STUBS=$ROOT/pages/vs11-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs11o-stubs-import

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

echo "== importImages VS11O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS11O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs11o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs11o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 11 (Original) Remaster slip faces from VirtualCards11.pdf" \
  --overwrite \
  /tmp/vs11o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 11 (Original)" "$HUBS/Virtual_Set_11_(Original).wiki" "VS11 Original: link all 30 Remaster slip stubs"

edit 'Advantage (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Advantage_(V)_(Virtual_Set_11).wiki' "VS11O stub 01"
edit 'Captain Verrack (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Captain_Verrack_(V)_(Virtual_Set_11).wiki' "VS11O stub 02"
edit 'Disarming Creature (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Disarming_Creature_(V)_(Virtual_Set_11).wiki' "VS11O stub 03"
edit 'Dismantle On Sight (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Dismantle_On_Sight_(V)_(Virtual_Set_11).wiki' "VS11O stub 04"
edit 'Green Squadron 1 (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Green_Squadron_1_(V)_(Virtual_Set_11).wiki' "VS11O stub 05"
edit 'Han'\''s Toolkit (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Han'\''s_Toolkit_(V)_(Virtual_Set_11).wiki' "VS11O stub 06"
edit 'I Don'\''t Need Their Scum, Either (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/I_Don'\''t_Need_Their_Scum,_Either_(V)_(Virtual_Set_11).wiki' "VS11O stub 07"
edit 'Let'\''s Keep A Little Optimism Here (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Let'\''s_Keep_A_Little_Optimism_Here_(V)_(Virtual_Set_11).wiki' "VS11O stub 08"
edit 'Meditation (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Meditation_(V)_(Virtual_Set_11).wiki' "VS11O stub 09"
edit 'Medium Transport (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Medium_Transport_(V)_(Virtual_Set_11).wiki' "VS11O stub 10"
edit 'Obi-Wan Kenobi, Jedi Knight (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Obi-Wan_Kenobi,_Jedi_Knight_(V)_(Virtual_Set_11).wiki' "VS11O stub 11"
edit 'Our Most Desperate Hour (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Our_Most_Desperate_Hour_(V)_(Virtual_Set_11).wiki' "VS11O stub 12"
edit 'Padme Naberrie (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Padme_Naberrie_(V)_(Virtual_Set_11).wiki' "VS11O stub 13"
edit 'Plastoid Armor (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Plastoid_Armor_(V)_(Virtual_Set_11).wiki' "VS11O stub 14"
edit 'Strikeforce (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Strikeforce_(V)_(Virtual_Set_11).wiki' "VS11O stub 15"
edit 'Cold Feet (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Cold_Feet_(V)_(Virtual_Set_11).wiki' "VS11O stub 16"
edit 'Deep Hatred (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Deep_Hatred_(V)_(Virtual_Set_11).wiki' "VS11O stub 17"
edit 'Emperor'\''s Power (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Emperor'\''s_Power_(V)_(Virtual_Set_11).wiki' "VS11O stub 18"
edit 'Endor Shield (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Endor_Shield_(V)_(Virtual_Set_11).wiki' "VS11O stub 19"
edit 'Establish Control (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Establish_Control_(V)_(Virtual_Set_11).wiki' "VS11O stub 20"
edit 'Forced Landing (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Forced_Landing_(V)_(Virtual_Set_11).wiki' "VS11O stub 21"
edit 'Frozen Dinner (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Frozen_Dinner_(V)_(Virtual_Set_11).wiki' "VS11O stub 22"
edit 'He Is Not Ready (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/He_Is_Not_Ready_(V)_(Virtual_Set_11).wiki' "VS11O stub 23"
edit 'I Want That Ship (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/I_Want_That_Ship_(V)_(Virtual_Set_11).wiki' "VS11O stub 24"
edit 'I'\''ve Lost Artoo (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/I'\''ve_Lost_Artoo_(V)_(Virtual_Set_11).wiki' "VS11O stub 25"
edit 'Lord Vader (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Lord_Vader_(V)_(Virtual_Set_11).wiki' "VS11O stub 26"
edit 'Luke? Luuuuke! (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Luke?_Luuuuke!_(V)_(Virtual_Set_11).wiki' "VS11O stub 27"
edit 'Restricted Access (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Restricted_Access_(V)_(Virtual_Set_11).wiki' "VS11O stub 28"
edit 'Sim Aloo (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Sim_Aloo_(V)_(Virtual_Set_11).wiki' "VS11O stub 29"
edit 'Something Special Planned For Them (V) (Virtual Set 11)' '/opt/swccg-wiki/pages/vs11-original/Something_Special_Planned_For_Them_(V)_(Virtual_Set_11).wiki' "VS11O stub 30"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 11 (Original)
Advantage (V) (Virtual Set 11)
Captain Verrack (V) (Virtual Set 11)
Disarming Creature (V) (Virtual Set 11)
Dismantle On Sight (V) (Virtual Set 11)
Green Squadron 1 (V) (Virtual Set 11)
Han's Toolkit (V) (Virtual Set 11)
I Don't Need Their Scum, Either (V) (Virtual Set 11)
Let's Keep A Little Optimism Here (V) (Virtual Set 11)
Meditation (V) (Virtual Set 11)
Medium Transport (V) (Virtual Set 11)
Obi-Wan Kenobi, Jedi Knight (V) (Virtual Set 11)
Our Most Desperate Hour (V) (Virtual Set 11)
Padme Naberrie (V) (Virtual Set 11)
Plastoid Armor (V) (Virtual Set 11)
Strikeforce (V) (Virtual Set 11)
Cold Feet (V) (Virtual Set 11)
Deep Hatred (V) (Virtual Set 11)
Emperor's Power (V) (Virtual Set 11)
Endor Shield (V) (Virtual Set 11)
Establish Control (V) (Virtual Set 11)
Forced Landing (V) (Virtual Set 11)
Frozen Dinner (V) (Virtual Set 11)
He Is Not Ready (V) (Virtual Set 11)
I Want That Ship (V) (Virtual Set 11)
I've Lost Artoo (V) (Virtual Set 11)
Lord Vader (V) (Virtual Set 11)
Luke? Luuuuke! (V) (Virtual Set 11)
Restricted Access (V) (Virtual Set 11)
Sim Aloo (V) (Virtual Set 11)
Something Special Planned For Them (V) (Virtual Set 11)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=['Advantage_(V)_(Virtual_Set_11)', 'Captain_Verrack_(V)_(Virtual_Set_11)', 'Disarming_Creature_(V)_(Virtual_Set_11)', 'Dismantle_On_Sight_(V)_(Virtual_Set_11)', 'Green_Squadron_1_(V)_(Virtual_Set_11)', "Han's_Toolkit_(V)_(Virtual_Set_11)", "I_Don't_Need_Their_Scum,_Either_(V)_(Virtual_Set_11)", "Let's_Keep_A_Little_Optimism_Here_(V)_(Virtual_Set_11)", 'Meditation_(V)_(Virtual_Set_11)', 'Medium_Transport_(V)_(Virtual_Set_11)', 'Obi-Wan_Kenobi,_Jedi_Knight_(V)_(Virtual_Set_11)', 'Our_Most_Desperate_Hour_(V)_(Virtual_Set_11)', 'Padme_Naberrie_(V)_(Virtual_Set_11)', 'Plastoid_Armor_(V)_(Virtual_Set_11)', 'Strikeforce_(V)_(Virtual_Set_11)', 'Cold_Feet_(V)_(Virtual_Set_11)', 'Deep_Hatred_(V)_(Virtual_Set_11)', "Emperor's_Power_(V)_(Virtual_Set_11)", 'Endor_Shield_(V)_(Virtual_Set_11)', 'Establish_Control_(V)_(Virtual_Set_11)', 'Forced_Landing_(V)_(Virtual_Set_11)', 'Frozen_Dinner_(V)_(Virtual_Set_11)', 'He_Is_Not_Ready_(V)_(Virtual_Set_11)', 'I_Want_That_Ship_(V)_(Virtual_Set_11)', "I've_Lost_Artoo_(V)_(Virtual_Set_11)", 'Lord_Vader_(V)_(Virtual_Set_11)', 'Luke?_Luuuuke!_(V)_(Virtual_Set_11)', 'Restricted_Access_(V)_(Virtual_Set_11)', 'Sim_Aloo_(V)_(Virtual_Set_11)', 'Something_Special_Planned_For_Them_(V)_(Virtual_Set_11)']
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
print("STUBS %d/30 PASS fail=%s" % (pass_n, fail[:10]))
u="https://wiki.swccg.com/wiki/Virtual_Set_11_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS11O STUBS APPLY OK")

PY
