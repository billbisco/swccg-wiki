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
  "Org chart 2021/2024 Advocate tables; resolve imrahil327/darkjediknight11/Lead; turnover Carulli/Kessling; cite PDF dates"

edit "History of the Players Committee" "$PAGES/History_of_the_Players_Committee.wiki" \
  "Light: org-chart era Advocate person See also + hub pointer"

edit "Scott Lingrell" "$PAGES/Scott_Lingrell.wiki" \
  "New: Lead Advocate / 2005 Card Design; org chart handle advocate"
edit "Greg Zinn" "$PAGES/Greg_Zinn.wiki" \
  "New: Rules Advocate Gergall (org chart 2021/2024)"
edit "Matt Carulli" "$PAGES/Matt_Carulli.wiki" \
  "New: Special Projects and Multimedia Advocate 2021; absent 2024 row"
edit "Jared Napolitano" "$PAGES/Jared_Napolitano.wiki" \
  "New: Marketing Advocate Jnapolit31 (org chart 2021/2024)"
edit "Chris Kelly" "$PAGES/Chris_Kelly.wiki" \
  "New: Design Advocate chriskelly (org chart 2021/2024)"
edit "Chris Schoenthal" "$PAGES/Chris_Schoenthal.wiki" \
  "New: Tournament Advocate imrahil327 (closes 2014 handle gap)"
edit "Keith Brown" "$PAGES/Keith_Brown.wiki" \
  "New: Communications Advocate darkjediknight11 (closes 2014 handle gap)"
edit "Mike Kessling" "$PAGES/Mike_Kessling.wiki" \
  "New: Production Advocate Kessling (2024 org chart)"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
Players Committee advocates
History of the Players Committee
Scott Lingrell
Greg Zinn
Matt Carulli
Jared Napolitano
Chris Kelly
Chris Schoenthal
Keith Brown
Mike Kessling
EOFPURGE

python3 - <<'PY'
import urllib.request
pages = [
 "https://wiki.swccg.com/wiki/Players_Committee_advocates",
 "https://wiki.swccg.com/wiki/History_of_the_Players_Committee",
 "https://wiki.swccg.com/wiki/Scott_Lingrell",
 "https://wiki.swccg.com/wiki/Greg_Zinn",
 "https://wiki.swccg.com/wiki/Matt_Carulli",
 "https://wiki.swccg.com/wiki/Jared_Napolitano",
 "https://wiki.swccg.com/wiki/Chris_Kelly",
 "https://wiki.swccg.com/wiki/Chris_Schoenthal",
 "https://wiki.swccg.com/wiki/Keith_Brown",
 "https://wiki.swccg.com/wiki/Mike_Kessling",
]
checks = {
 "Players_Committee_advocates": [
   "organization chart", "imrahil327", "Chris Schoenthal", "darkjediknight11",
   "Keith Brown", "Mike Kessling", "Matt Carulli", "quickdraw3457",
   "CreationDate", "20211005193353", "Unresolved", "Shewski",
 ],
 "History_of_the_Players_Committee": ["Scott Lingrell", "organization chart"],
 "Scott_Lingrell": ["Lead Advocate", "advocate", "Card Design Advocate"],
 "Chris_Schoenthal": ["imrahil327", "Tournament Advocate"],
 "Keith_Brown": ["darkjediknight11", "Communications Advocate"],
 "Mike_Kessling": ["Production Advocate", "Kessling"],
 "Matt_Carulli": ["Special Projects", "quickdraw3457"],
}
for u in pages:
  html = urllib.request.urlopen(urllib.request.Request(u, headers={"Cache-Control":"no-cache"}), timeout=30).read().decode("utf-8","replace")
  missing = "noarticletext" in html or "does not have a page" in html.lower()
  print(("LIVE" if not missing else "MISSING"), u, "len", len(html))
  key = u.rsplit("/",1)[-1]
  for c in checks.get(key, []):
    print(("  OK" if c in html else "  MISS"), c)
print("DONE")
PY
