#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/premium-shields
STUBS=$ROOT/pages/premium-shields
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/ps1-stubs-import

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

echo "== importImages stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/PS1-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/ps1-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/ps1-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Premium Set 1 Defensive Shields slip faces from DefensiveShields.pdf" \
  --overwrite \
  /tmp/ps1-stubs-import
rc=$?
set -e
echo "importImages rc=$rc (non-zero OK if overwrites of existing hub assets failed)"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Premium Set 1: Defensive Shields" "$HUBS/Premium_Set_1_Defensive_Shields.wiki" "Premium Set 1: link all 18 Defensive Shield stubs"

edit "A Tragedy Has Occurred (V) (Premium Set 1)" "$STUBS/A_Tragedy_Has_Occurred_(V)_(Premium_Set_1).wiki" "PS1 stub 01"
edit "Aim High (V) (Premium Set 1)" "$STUBS/Aim_High_(V)_(Premium_Set_1).wiki" "PS1 stub 02"
edit "Battle Plan (V) (Premium Set 1)" "$STUBS/Battle_Plan_(V)_(Premium_Set_1).wiki" "PS1 stub 03"
edit "Do, Or Do Not (V) (Premium Set 1)" "$STUBS/Do_Or_Do_Not_(V)_(Premium_Set_1).wiki" "PS1 stub 04"
edit "Don't Do That Again (V) (Premium Set 1)" "$STUBS/Dont_Do_That_Again_(V)_(Premium_Set_1).wiki" "PS1 stub 05"
edit "Ounee Ta (V) (Premium Set 1)" "$STUBS/Ounee_Ta_(V)_(Premium_Set_1).wiki" "PS1 stub 06"
edit "Wise Advice (V) (Premium Set 1)" "$STUBS/Wise_Advice_(V)_(Premium_Set_1).wiki" "PS1 stub 07"
edit "Your Insight Serves You Well (V) (Premium Set 1)" "$STUBS/Your_Insight_Serves_You_Well_(V)_(Premium_Set_1).wiki" "PS1 stub 08"
edit "Allegations Of Corruption (V) (Premium Set 1)" "$STUBS/Allegations_Of_Corruption_(V)_(Premium_Set_1).wiki" "PS1 stub 09"
edit "Battle Order (V) (Premium Set 1)" "$STUBS/Battle_Order_(V)_(Premium_Set_1).wiki" "PS1 stub 10"
edit "Come Here You Big Coward (V) (Premium Set 1)" "$STUBS/Come_Here_You_Big_Coward_(V)_(Premium_Set_1).wiki" "PS1 stub 11"
edit "Do They Have A Code Clearance? (V) (Premium Set 1)" "$STUBS/Do_They_Have_A_Code_Clearance_(V)_(Premium_Set_1).wiki" "PS1 stub 12"
edit "Fanfare (V) (Premium Set 1)" "$STUBS/Fanfare_(V)_(Premium_Set_1).wiki" "PS1 stub 13"
edit "No Escape (V) (Premium Set 1)" "$STUBS/No_Escape_(V)_(Premium_Set_1).wiki" "PS1 stub 14"
edit "Oppressive Enforcement (V) (Premium Set 1)" "$STUBS/Oppressive_Enforcement_(V)_(Premium_Set_1).wiki" "PS1 stub 15"
edit "Secret Plans (V) (Premium Set 1)" "$STUBS/Secret_Plans_(V)_(Premium_Set_1).wiki" "PS1 stub 16"
edit "There Is No Try (V) (Premium Set 1)" "$STUBS/There_Is_No_Try_(V)_(Premium_Set_1).wiki" "PS1 stub 17"
edit "You Cannot Hide Forever (V) (Premium Set 1)" "$STUBS/You_Cannot_Hide_Forever_(V)_(Premium_Set_1).wiki" "PS1 stub 18"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -5

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Premium Set 1: Defensive Shields
A Tragedy Has Occurred (V) (Premium Set 1)
Aim High (V) (Premium Set 1)
Battle Plan (V) (Premium Set 1)
Do, Or Do Not (V) (Premium Set 1)
Don't Do That Again (V) (Premium Set 1)
Ounee Ta (V) (Premium Set 1)
Wise Advice (V) (Premium Set 1)
Your Insight Serves You Well (V) (Premium Set 1)
Allegations Of Corruption (V) (Premium Set 1)
Battle Order (V) (Premium Set 1)
Come Here You Big Coward (V) (Premium Set 1)
Do They Have A Code Clearance? (V) (Premium Set 1)
Fanfare (V) (Premium Set 1)
No Escape (V) (Premium Set 1)
Oppressive Enforcement (V) (Premium Set 1)
Secret Plans (V) (Premium Set 1)
There Is No Try (V) (Premium Set 1)
You Cannot Hide Forever (V) (Premium Set 1)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import subprocess, urllib.request
pass_n=0
fail=[]
slugs=[
 "A_Tragedy_Has_Occurred_(V)_(Premium_Set_1)",
 "Aim_High_(V)_(Premium_Set_1)",
 "Battle_Plan_(V)_(Premium_Set_1)",
 "Do,_Or_Do_Not_(V)_(Premium_Set_1)",
 "Don't_Do_That_Again_(V)_(Premium_Set_1)",
 "Ounee_Ta_(V)_(Premium_Set_1)",
 "Wise_Advice_(V)_(Premium_Set_1)",
 "Your_Insight_Serves_You_Well_(V)_(Premium_Set_1)",
 "Allegations_Of_Corruption_(V)_(Premium_Set_1)",
 "Battle_Order_(V)_(Premium_Set_1)",
 "Come_Here_You_Big_Coward_(V)_(Premium_Set_1)",
 "Do_They_Have_A_Code_Clearance%3F_(V)_(Premium_Set_1)",
 "Fanfare_(V)_(Premium_Set_1)",
 "No_Escape_(V)_(Premium_Set_1)",
 "Oppressive_Enforcement_(V)_(Premium_Set_1)",
 "Secret_Plans_(V)_(Premium_Set_1)",
 "There_Is_No_Try_(V)_(Premium_Set_1)",
 "You_Cannot_Hide_Forever_(V)_(Premium_Set_1)",
]
for slug in slugs:
  u="https://wiki.swccg.com/wiki/"+slug
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    ok=(r.status==200)
  except Exception:
    ok=False
  print(("PASS" if ok else "FAIL"), u)
  if ok: pass_n+=1
  else: fail.append(u)
print("STUBS %d/18 PASS fail=%s" % (pass_n, fail))
print("PS1 STUBS APPLY OK")
PY
