#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
assert "`r`n" not in text, p.name
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text), "nonascii", sum(1 for c in text if ord(c) > 127))
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "Players Committee advocates" "$PAGES/Players_Committee_advocates.wiki" \
  "Expand: Decipher volunteer CALL; link first Advocates to person pages; GPN Taylor + VS1 Radke cites; keep mid-era/2014"
edit "History of the Players Committee" "$PAGES/History_of_the_Players_Committee.wiki" \
  "Decipher volunteer CALL cite; firm 25 Jan 2002 first Advocates letter; link person stubs"

edit "Doug Taylor" "$PAGES/Doug_Taylor.wiki" \
  "New: sourced PC Advocate / GPN Game Play Design interview stub"
edit "Josh Radke" "$PAGES/Josh_Radke.wiki" \
  "New: sourced Player Relations Advocate stub (VS1 + council + Arendt turnover)"
edit "Josh \"Red 84\" Radke" "$PAGES/Josh_Red_84_Radke_redirect.wiki" \
  "Redirect to Josh Radke"
edit "Michael Girard" "$PAGES/Michael_Girard.wiki" \
  "New: sourced first Advocates Player Support stub"
edit "John Arendt" "$PAGES/John_Arendt.wiki" \
  "New: sourced first Advocates Tournament Support + Howard turnover stub"
edit "Joe Helfrich" "$PAGES/Joe_Helfrich.wiki" \
  "New: sourced first Advocates Rules Support stub"
edit "Greg Anderson" "$PAGES/Greg_Anderson.wiki" \
  "New: sourced first Advocates / Rules Advocate stub"
edit "Eric Olson" "$PAGES/Eric_Olson.wiki" \
  "New: sourced first Advocates Gameplay / Card Design stub"
edit "Andrew Howard" "$PAGES/Andrew_Howard.wiki" \
  "New: sourced Tournament Support Advocate (Arendt successor) stub"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
Players Committee advocates
History of the Players Committee
Doug Taylor
Josh Radke
Josh "Red 84" Radke
Michael Girard
John Arendt
Joe Helfrich
Greg Anderson
Eric Olson
Andrew Howard
EOFPURGE

python3 - <<'PY'
import urllib.request
pages = [
 "https://wiki.swccg.com/wiki/Players_Committee_advocates",
 "https://wiki.swccg.com/wiki/History_of_the_Players_Committee",
 "https://wiki.swccg.com/wiki/Doug_Taylor",
 "https://wiki.swccg.com/wiki/Josh_Radke",
 "https://wiki.swccg.com/wiki/Michael_Girard",
 "https://wiki.swccg.com/wiki/John_Arendt",
 "https://wiki.swccg.com/wiki/Joe_Helfrich",
 "https://wiki.swccg.com/wiki/Greg_Anderson",
 "https://wiki.swccg.com/wiki/Eric_Olson",
 "https://wiki.swccg.com/wiki/Andrew_Howard",
]
for u in pages:
  html = urllib.request.urlopen(urllib.request.Request(u, headers={"Cache-Control":"no-cache"}), timeout=30).read().decode("utf-8","replace")
  missing = "noarticletext" in html or "does not have a page" in html.lower()
  print(("LIVE" if not missing else "MISSING"), u, "len", len(html))
  if "advocates" in u:
    for c in ["volunteer for the players", "Michael Girard", "Doug Taylor", "Interview With The Advocates", "Virtual Card Set #1"]:
      print(("  OK" if c in html else "  MISS"), c)
  if "History" in u:
    for c in ["volunteer for the players", "25 January 2002", "announcement122801"]:
      print(("  OK" if c in html else "  MISS"), c)
  if "Doug_Taylor" in u:
    for c in ["Game Play Design", "Seattle", "virtual cards", "DougRed4"]:
      print(("  OK" if c in html else "  MISS"), c)
  if "Josh_Radke" in u:
    for c in ["Red 84", "Player Relations", "Andrew Howard"]:
      print(("  OK" if c in html else "  MISS"), c)
print("DONE")
PY
