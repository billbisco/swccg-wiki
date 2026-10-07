#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

python3 - <<'PY'
from pathlib import Path
root = Path("/opt/swccg-wiki/pages")
need = [
  "Cancelled_Virtual_Sets.wiki",
  "Virtual_Set_18.wiki",
  "Virtual_Sets_2002-2009.wiki",
  "Virtual_Block_6.wiki",
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

cv = (root / "Cancelled_Virtual_Sets.wiki").read_text("utf-8")
for s in ["Do not treat Fifth Anthology like Galaxy at War", "Reflections IV", "VirtualCards18.pdf", "Galaxy at War", "niewydany"]:
    assert s in cv, s
vs = (root / "Virtual_Set_18.wiki").read_text("utf-8")
assert "Not to be confused" in vs[:500]
assert "Fifth Anthology" in vs[:800]
vsets = (root / "Virtual_Sets_2002-2009.wiki").read_text("utf-8")
assert "released via Reflections IV" in vsets
assert "plfifth" in vsets
vb6 = (root / "Virtual_Block_6.wiki").read_text("utf-8")
assert "Fifth Anthology / Original VS18 path" in vb6
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

edit "Cancelled Virtual Sets" "Cancelled_Virtual_Sets.wiki" \
  "Fifth Anthology: naming/PDF note only (previewed VS18, no VirtualCards18.pdf, released via Reflections IV); keep Galaxy at War as niewydany cancel"
edit "Virtual Set 18" "Virtual_Set_18.wiki" \
  "Hatnote: disambiguate modern VS18 (2022) from Original Fifth Anthology / Reflections IV path"
edit "Virtual Sets (2002-2009)" "Virtual_Sets_2002-2009.wiki" \
  "VS18 Fifth Anthology: previewed; no standalone PDF; released via Reflections IV / VB6 (not cancelled like Galaxy at War)"
edit "Virtual Block 6" "Virtual_Block_6.wiki" \
  "Note Fifth Anthology / Original VS18 preview path into Reflections IV core"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
Cancelled Virtual Sets
Virtual Set 18
Virtual Sets (2002-2009)
Virtual Block 6
EOFPURGE

python3 - <<'PY'
import urllib.request
checks = {
  "https://wiki.swccg.com/wiki/Cancelled_Virtual_Sets": [
    "Do not treat Fifth Anthology like Galaxy at War",
    "Reflections IV",
    "VirtualCards18.pdf",
    "Galaxy at War",
    "niewydany",
  ],
  "https://wiki.swccg.com/wiki/Virtual_Set_18": [
    "Not to be confused",
    "Fifth Anthology",
  ],
  "https://wiki.swccg.com/wiki/Virtual_Sets_(2002-2009)": [
    "released via Reflections IV",
    "Fifth Anthology",
  ],
  "https://wiki.swccg.com/wiki/Virtual_Block_6": [
    "Fifth Anthology",
    "VirtualBlock6_1.pdf",
  ],
}
for u, needles in checks.items():
  req = urllib.request.Request(u, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
  html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
  print("====", u, "len", len(html))
  for c in needles:
    print(("OK" if c in html else "MISSING"), c)
print("DONE")
PY
