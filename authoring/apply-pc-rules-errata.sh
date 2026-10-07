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

edit "Players Committee rule changes" "$PAGES/Players_Committee_rule_changes.wiki" \
  "New hub: PC rules changes with before/after; seed personas Nov 2021; LOTR Legacy_Ruling_1 pattern; cite announce+Wayback"

edit "Errata on Projective Telepathy" "$PAGES/Errata_on_Projective_Telepathy.wiki" \
  "New: Original/Errata/Current table for Projective Telepathy; original sourced; divergent PC errata gap labeled; LOTR PC_Errata/Table pattern"

edit "Errata" "$PAGES/Errata.wiki" \
  "Expand stub: link Players Committee rule changes + Errata on Projective Telepathy + PC Errata"

edit "PC Errata" "$PAGES/PC_Errata.wiki" \
  "Expand stub: link rule-changes hub and Projective Telepathy comparison"

edit "History of the Players Committee" "$PAGES/History_of_the_Players_Committee.wiki" \
  "See also: Players Committee rule changes hub"

edit "Formats" "$PAGES/Formats.wiki" \
  "See also: Players Committee rule changes"

edit "Projective Telepathy" "$PAGES/Projective_Telepathy.wiki" \
  "Hatnote: Errata on Projective Telepathy + rules-changes hub"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
Players Committee rule changes
Errata on Projective Telepathy
Errata
PC Errata
History of the Players Committee
Formats
Projective Telepathy
EOFPURGE

python3 - <<'PY'
import urllib.request
pages = [
 "https://wiki.swccg.com/wiki/Players_Committee_rule_changes",
 "https://wiki.swccg.com/wiki/Errata_on_Projective_Telepathy",
 "https://wiki.swccg.com/wiki/Errata",
 "https://wiki.swccg.com/wiki/PC_Errata",
 "https://wiki.swccg.com/wiki/History_of_the_Players_Committee",
 "https://wiki.swccg.com/wiki/Formats",
 "https://wiki.swccg.com/wiki/Projective_Telepathy",
]
checks = {
 "Players_Committee_rule_changes": [
   "Personas rule changes", "9 November 2021", "Two Landos", "Sidious",
   "Legacy Ruling 1", "Errata on Projective Telepathy", "Count of rule-change entries",
 ],
 "Errata_on_Projective_Telepathy": [
   "Original (Decipher print)", "Source needed", "use 2 Force",
   "Anger, Fear, Aggression (V)", "PC Errata/Table",
 ],
 "Errata": ["Players Committee rule changes", "Errata on Projective Telepathy"],
 "PC_Errata": ["Players Committee rule changes", "Errata on Projective Telepathy"],
 "History_of_the_Players_Committee": ["Players Committee rule changes"],
 "Formats": ["Players Committee rule changes"],
 "Projective_Telepathy": ["Errata on Projective Telepathy"],
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
