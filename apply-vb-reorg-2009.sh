#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

python3 - <<'PY'
from pathlib import Path
root = Path("/opt/swccg-wiki/pages")
need = [
  "2009_Virtual_Block_Reorganization.wiki",
  "Virtual_Sets_to_Virtual_Blocks.wiki",
  "Virtual_Sets_(2002-2009).wiki",
  "Virtual_Block_6.wiki",
  "Cancelled_Virtual_Sets.wiki",
  "History_of_the_Players_Committee.wiki",
]
for name in need:
    p = root / name
    b = p.read_bytes()
    if b.startswith(b"\xef\xbb\xbf"):
        b = b[3:]
        p.write_bytes(b)
    text = b.decode("utf-8").replace("\r\n","\n").replace("\r","\n")
    p.write_text(text, encoding="utf-8")
    assert "\r" not in text, name
    print(name, "ok", len(text))

main = (root / "2009_Virtual_Block_Reorganization.wiki").read_text("utf-8")
for s in ["previous 18 virtual sets", "Fifth Anthology", "Open research", "VirtualCards18.pdf", "7 December 2009"]:
    assert s in main, s
redir = (root / "Virtual_Sets_to_Virtual_Blocks.wiki").read_text("utf-8").strip()
assert redir.startswith("#REDIRECT [[2009 Virtual Block Reorganization]]")
for name in ["Virtual_Sets_(2002-2009).wiki", "Virtual_Block_6.wiki", "Cancelled_Virtual_Sets.wiki", "History_of_the_Players_Committee.wiki"]:
    t = (root / name).read_text("utf-8")
    assert "[[2009 Virtual Block Reorganization]]" in t, name
print("preflight OK")
PY

edit() {
  local title="$1"
  local file="$2"
  local summary="$3"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="$summary" \
    "$title" < "$PAGES/$file"
}

edit "2009 Virtual Block Reorganization" "2009_Virtual_Block_Reorganization.wiki" \
  "New hub: 2009 VS to Virtual Blocks remap; Fifth Anthology/VS18 path via Reflections IV; open research kept"
edit "Virtual Sets to Virtual Blocks" "Virtual_Sets_to_Virtual_Blocks.wiki" \
  "Redirect to 2009 Virtual Block Reorganization"
edit "Virtual Sets (2002-2009)" "Virtual_Sets_(2002-2009).wiki" \
  "See also: 2009 Virtual Block Reorganization"
edit "Virtual Block 6" "Virtual_Block_6.wiki" \
  "See also: 2009 Virtual Block Reorganization"
edit "Cancelled Virtual Sets" "Cancelled_Virtual_Sets.wiki" \
  "See also: 2009 Virtual Block Reorganization (Fifth Anthology full story)"
edit "History of the Players Committee" "History_of_the_Players_Committee.wiki" \
  "Link 2009 Virtual Block Reorganization from Reorg/Blocks section"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
2009 Virtual Block Reorganization
Virtual Sets to Virtual Blocks
Virtual Sets (2002-2009)
Virtual Block 6
Cancelled Virtual Sets
History of the Players Committee
EOFPURGE

python3 - <<'PY'
import urllib.request
checks = {
  "https://wiki.swccg.com/wiki/2009_Virtual_Block_Reorganization": [
    "previous 18 virtual sets",
    "Fifth Anthology",
    "Open research",
    "VirtualCards18.pdf",
  ],
  "https://wiki.swccg.com/wiki/Virtual_Sets_to_Virtual_Blocks": [
    "2009 Virtual Block Reorganization",
  ],
  "https://wiki.swccg.com/wiki/Virtual_Sets_(2002-2009)": [
    "2009 Virtual Block Reorganization",
  ],
  "https://wiki.swccg.com/wiki/Virtual_Block_6": [
    "2009 Virtual Block Reorganization",
  ],
  "https://wiki.swccg.com/wiki/Cancelled_Virtual_Sets": [
    "2009 Virtual Block Reorganization",
  ],
  "https://wiki.swccg.com/wiki/History_of_the_Players_Committee": [
    "2009 Virtual Block Reorganization",
  ],
}
for u, needles in checks.items():
  req = urllib.request.Request(u, headers={"Cache-Control": "no-cache", "Pragma": "no-cache", "User-Agent": "GrokBotWiki/1.0"})
  html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
  print("====", u, "len", len(html))
  for c in needles:
    print(("OK" if c in html else "MISSING"), c)
print("DONE")
PY
