#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki

python3 - <<'PY'
from pathlib import Path
hist = Path("/opt/swccg-wiki/pages/History_of_the_Players_Committee.wiki")
adv = Path("/opt/swccg-wiki/pages/Players_Committee_advocates.wiki")
for p in (hist, adv):
    b = p.read_bytes()
    if b.startswith(b"\xef\xbb\xbf"):
        b = b[3:]
        p.write_bytes(b)
    text = b.decode("utf-8")
    assert "`r`n" not in text, p.name
    print(p.name, "ok", len(text), "nonascii", sum(1 for c in text if ord(c) > 127))
assert "swccgpc.com" in hist.read_text("utf-8")
assert "Players Committee advocates" in hist.read_text("utf-8")
assert "Michael Girard" in adv.read_text("utf-8")
assert "Shewski" in adv.read_text("utf-8")
PY

echo "edit History of the Players Committee"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Archive: swccgpc.com + 10 Jun 2009 domain move cites; link Players Committee advocates hub; fix Sources mojibake" \
  "History of the Players Committee" < "$ROOT/pages/History_of_the_Players_Committee.wiki"

echo "edit Players Committee advocates"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="New: sourced Advocate / Advocate Council roster by era (Decipher 2002, council.htm 2002-2005, starwarsccg.org About 2014); gaps labeled" \
  "Players Committee advocates" < "$ROOT/pages/Players_Committee_advocates.wiki"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -5

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
History of the Players Committee
Players Committee advocates
EOFPURGE

python3 - <<'PY'
import urllib.request
pages = [
 "https://wiki.swccg.com/wiki/History_of_the_Players_Committee",
 "https://wiki.swccg.com/wiki/Players_Committee_advocates",
]
for u in pages:
  html = urllib.request.urlopen(urllib.request.Request(u, headers={"Cache-Control":"no-cache"}), timeout=30).read().decode("utf-8","replace")
  print("====", u, "len", len(html))
  if "History" in u:
    for c in ["swccgpc.com","New Domain and Server","10 June 2009","Players Committee advocates"]:
      print(("OK" if c in html else "MISSING"), c)
  else:
    for c in ["Michael Girard","Greg Anderson","Andrew Howard","Mitch Velasco","Shewski","imrahil327","DougRed4"]:
      print(("OK" if c in html else "MISSING"), c)
print("DONE")
PY
