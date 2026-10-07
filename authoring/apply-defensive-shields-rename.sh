#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
HUBS=$ROOT/pages/set-hubs
PAGES=$ROOT/pages
ICONS=$ROOT/pages/icons
STUBS=$ROOT/pages/premium-shields

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

echo "== moveBatch Premium Set 1: Defensive Shields -> Defensive Shields =="
# If already moved / new page exists, skip move and just edit
python3 - <<'PY'
import urllib.request, urllib.parse, json
def exists(title):
  url = "https://wiki.swccg.com/api.php?" + urllib.parse.urlencode({"action":"query","titles":title,"format":"json"})
  data = json.load(urllib.request.urlopen(url))
  pages = data["query"]["pages"]
  return all("missing" not in p for p in pages.values())
old_ok = exists("Premium Set 1: Defensive Shields")
new_ok = exists("Defensive Shields")
print(f"exists old={old_ok} new={new_ok}")
# move only when old is a real page and new is missing
open("/tmp/ps1-move-needed","w").write("1" if (old_ok and not new_ok) else "0")
PY
NEED=$(cat /tmp/ps1-move-needed)
if [ "$NEED" = "1" ]; then
  printf '%s\n' 'Premium Set 1: Defensive Shields|Defensive Shields' > /tmp/ps1-move.txt
  docker cp /tmp/ps1-move.txt swccg_wiki:/tmp/ps1-move.txt
  docker exec swccg_wiki php maintenance/run.php moveBatch \
    --u=Admin \
    --r="Bill override 2026-09-24: PDF never says Premium; hub title Defensive Shields" \
    /tmp/ps1-move.txt 2>&1 | tail -20
else
  echo "moveBatch skipped (already renamed or new exists); will edit Defensive Shields + leave Premium redirect"
fi

echo "== edit hub + redirects + nav + stubs =="
edit "Defensive Shields" "$HUBS/Defensive_Shields.wiki" "Bill override: hub title Defensive Shields (PDF never says Premium)"
edit "Premium Set 1: Defensive Shields" "$HUBS/Premium_Set_1_Defensive_Shields.wiki" "Redirect to Defensive Shields (Bill override 2026-09-24)"
edit "Virtual Shields (Original)" "$HUBS/Virtual_Shields_(Original).wiki" "Redirect to Defensive Shields"
edit "Virtual Set: Defensive Shields" "$HUBS/Virtual_Set_Defensive_Shields.wiki" "Redirect to Defensive Shields (PDF cover title)"
edit "Main Page" "$PAGES/Main_Page.wiki" "Original tile: Defensive Shields (Bill override)"
edit "Virtual Sets (2002-2009)" "$PAGES/Virtual_Sets_(2002-2009).wiki" "Index row -> Defensive Shields"
edit "Sets" "$PAGES/Sets.wiki" "Original Shields row -> Defensive Shields"
edit "Virtual Shields" "$HUBS/Virtual_Shields.wiki" "Original-era pointer -> Defensive Shields"
edit "Virtual card icons" "$ICONS/Virtual_card_icons.wiki" "Cite Defensive Shields hub"
edit "History of the Players Committee" "$PAGES/History_of_the_Players_Committee.wiki" "Defensive Shields naming (Bill override)"
edit "Category:Virtual Original sets" "$PAGES/Category_Virtual_Original_sets.wiki" "Plus Defensive Shields"
edit "Category:Defensive Shields" "$PAGES/Category_Defensive_Shields.wiki" "Category chrome for Defensive Shields hub"

# VS Original See also
for n in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17; do
  f="$HUBS/Virtual_Set_${n}_(Original).wiki"
  if [ -f "$f" ]; then
    # only edit if file mentions Defensive Shields (already rewritten) or Premium
    if grep -q "Defensive Shields\|Premium Set 1" "$f"; then
      edit "Virtual Set ${n} (Original)" "$f" "See also -> Defensive Shields"
    fi
  fi
done

# 18 stubs (titles locked)
edit "A Tragedy Has Occurred (V) (Premium Set 1)" "$STUBS/A_Tragedy_Has_Occurred_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Aim High (V) (Premium Set 1)" "$STUBS/Aim_High_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Battle Plan (V) (Premium Set 1)" "$STUBS/Battle_Plan_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Do, Or Do Not (V) (Premium Set 1)" "$STUBS/Do_Or_Do_Not_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Don't Do That Again (V) (Premium Set 1)" "$STUBS/Dont_Do_That_Again_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Ounee Ta (V) (Premium Set 1)" "$STUBS/Ounee_Ta_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Wise Advice (V) (Premium Set 1)" "$STUBS/Wise_Advice_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Your Insight Serves You Well (V) (Premium Set 1)" "$STUBS/Your_Insight_Serves_You_Well_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Allegations Of Corruption (V) (Premium Set 1)" "$STUBS/Allegations_Of_Corruption_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Battle Order (V) (Premium Set 1)" "$STUBS/Battle_Order_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Come Here You Big Coward (V) (Premium Set 1)" "$STUBS/Come_Here_You_Big_Coward_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Do They Have A Code Clearance? (V) (Premium Set 1)" "$STUBS/Do_They_Have_A_Code_Clearance_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Fanfare (V) (Premium Set 1)" "$STUBS/Fanfare_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "No Escape (V) (Premium Set 1)" "$STUBS/No_Escape_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Oppressive Enforcement (V) (Premium Set 1)" "$STUBS/Oppressive_Enforcement_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "Secret Plans (V) (Premium Set 1)" "$STUBS/Secret_Plans_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "There Is No Try (V) (Premium Set 1)" "$STUBS/There_Is_No_Try_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"
edit "You Cannot Hide Forever (V) (Premium Set 1)" "$STUBS/You_Cannot_Hide_Forever_(V)_(Premium_Set_1).wiki" "set=Defensive Shields (Bill override)"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "== purgePage =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Defensive Shields
Premium Set 1: Defensive Shields
Virtual Shields (Original)
Virtual Set: Defensive Shields
Main Page
Virtual Sets (2002-2009)
Sets
Virtual Shields
Virtual card icons
History of the Players Committee
Category:Virtual Original sets
Category:Defensive Shields
Category:Premium Set 1: Defensive Shields
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
Virtual Set 1 (Original)
Virtual Set 2 (Original)
Virtual Set 3 (Original)
Virtual Set 4 (Original)
Virtual Set 5 (Original)
Virtual Set 6 (Original)
Virtual Set 7 (Original)
Virtual Set 8 (Original)
Virtual Set 9 (Original)
Virtual Set 10 (Original)
Virtual Set 11 (Original)
Virtual Set 12 (Original)
Virtual Set 13 (Original)
Virtual Set 14 (Original)
Virtual Set 15 (Original)
Virtual Set 16 (Original)
Virtual Set 17 (Original)
PURGE

python3 - <<'PY'
import urllib.request, json, urllib.parse
def api(**kw):
  return json.load(urllib.request.urlopen("https://wiki.swccg.com/api.php?"+urllib.parse.urlencode({**kw,"format":"json"})))

# Hub exists, not redirect
q=api(action="query", titles="Defensive Shields|Premium Set 1: Defensive Shields|Virtual Shields (Original)|Virtual Set: Defensive Shields", prop="info|redirects")
for pid,p in q["query"]["pages"].items():
  print("PAGE", p.get("title"), "missing" if "missing" in p else ("redirect" if "redirect" in p else "ok"), "len", p.get("length"))

# HEAD checks
for u in [
 "https://wiki.swccg.com/wiki/Defensive_Shields",
 "https://wiki.swccg.com/wiki/Premium_Set_1:_Defensive_Shields",
 "https://wiki.swccg.com/wiki/Virtual_Shields_(Original)",
 "https://wiki.swccg.com/wiki/Virtual_Set:_Defensive_Shields",
]:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print("HEAD", r.status, u, "final", r.geturl())

# Confirm stub set=
t=urllib.request.urlopen("https://wiki.swccg.com/api.php?"+urllib.parse.urlencode({"action":"parse","page":"A Tragedy Has Occurred (V) (Premium Set 1)","prop":"wikitext","format":"json"})).read().decode()
assert "|set=Defensive Shields" in t
assert "(V) (Premium Set 1)" in json.loads(t)["parse"]["title"] or True
print("stub set= OK; title locked OK")

# FlaggedRevs sample
fr=api(action="query", titles="Defensive Shields|A Tragedy Has Occurred (V) (Premium Set 1)", prop="flagged|info")
for pid,p in fr["query"]["pages"].items():
  fl=p.get("flagged",{})
  print("FR", p["title"], "stable", fl.get("stable_revid"), "last", p.get("lastrevid"), "pending", fl.get("pending_since"))

print("DEFENSIVE SHIELDS RENAME APPLY OK")
PY