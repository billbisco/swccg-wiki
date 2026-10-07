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
text = raw.decode("utf-8").replace("\r\n", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "Chuck Kallenbach" "$PAGES/Chuck_Kallenbach.wiki" "new: Decipher playtester to staff designer stub (not founding SWCCG designer)"
edit "Tom Lischke" "$PAGES/Tom_Lischke.wiki" "new: Decipher product/game designer stub (SWCCG RFD + Jedi Knights/LOTR)"
edit "Justin Pakes" "$PAGES/Justin_Pakes.wiki" "new: thin RFD late-SWCCG design guest stub"
edit "Juz Pakes" "$PAGES/Juz_Pakes.wiki" "redirect to Justin Pakes"
edit "Joe Alread" "$PAGES/Joe_Alread.wiki" "new: thin RFD late-SWCCG design guest stub"
edit "Creators of SWCCG" "$PAGES/Creators_of_SWCCG.wiki" "Related: link Kallenbach/Lischke/Pakes/Alread stubs; keep not-founding labels"
edit "Jerry Darcy" "$PAGES/Jerry_Darcy.wiki" "See also: soft links to later Decipher design staff"
edit "Tom Braunlich" "$PAGES/Tom_Braunlich.wiki" "See also: soft links to later Decipher design staff"
edit "Rollie Tesh" "$PAGES/Rollie_Tesh.wiki" "See also: soft links to later Decipher design staff"

echo FlaggedRevs reviewAllPages
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo purgePage
docker exec -i swccg_wiki php maintenance/run.php purgePage <<EOFPURGE || true
Chuck Kallenbach
Tom Lischke
Justin Pakes
Juz Pakes
Joe Alread
Creators of SWCCG
Jerry Darcy
Tom Braunlich
Rollie Tesh
EOFPURGE

echo VERIFY
for t in "Chuck Kallenbach" "Tom Lischke" "Justin Pakes" "Joe Alread" "Creators of SWCCG"; do
  echo "==== $t"
  docker exec swccg_wiki php maintenance/run.php getText "$t" | head -8
done

echo "==== Holland untouched check (first lines)"
docker exec swccg_wiki php maintenance/run.php getText "Warren Holland" | head -3

echo HTTP
for u in Chuck_Kallenbach Tom_Lischke Justin_Pakes Juz_Pakes Joe_Alread Creators_of_SWCCG Jerry_Darcy Tom_Braunlich Rollie_Tesh Warren_Holland; do
  code=$(curl -sL -o /dev/null -w "%{http_code}" "https://wiki.swccg.com/wiki/$u")
  echo "$code $u"
done
echo designer-stubs apply done
