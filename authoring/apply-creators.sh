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

edit "Creators of SWCCG" "$PAGES/Creators_of_SWCCG.wiki" "new: sourced Decipher-era creators overview"
edit "Designers of SWCCG" "$PAGES/Designers_of_SWCCG.wiki" "redirect to Creators of SWCCG"
edit "Creators of Star Wars CCG" "$PAGES/Creators_of_Star_Wars_CCG.wiki" "redirect to Creators of SWCCG"
edit "SWCCG creators" "$PAGES/SWCCG_creators.wiki" "redirect to Creators of SWCCG"
edit "Tom Braunlich" "$PAGES/Tom_Braunlich.wiki" "new: sourced SWCCG designer stub"
edit "Rollie Tesh" "$PAGES/Rollie_Tesh.wiki" "new: sourced SWCCG designer stub"
edit "Jerry Darcy" "$PAGES/Jerry_Darcy.wiki" "new: sourced SWCCG designer stub"
edit "Warren Holland" "$PAGES/Warren_Holland.wiki" "new: sourced Decipher founder / SWCCG designer-credit stub"
edit "Decipher" "$PAGES/Decipher.wiki" "hub: keep license + creators cross-links"
edit "Decipher, Inc." "$PAGES/Decipher,_Inc..wiki" "redirect to Decipher"
edit "Decipher Inc." "$PAGES/Decipher_Inc.wiki" "redirect to Decipher"
edit "Star Wars CCG" "$PAGES/Star_Wars_CCG.wiki" "fix designer credits to Wikipedia line; link Creators of SWCCG"
edit "Players Committee" "$PAGES/Players_Committee.wiki" "cross-link Creators of SWCCG (preserve license links)"
edit "History of the Players Committee" "$PAGES/History_of_the_Players_Committee.wiki" "see also: Creators of SWCCG (preserve license link)"
edit "Main Page" "$PAGES/Main_Page.wiki" "nav: Creators of SWCCG"
edit "Premiere Limited" "$PAGES/Premiere_Limited.wiki" "see also: Creators of SWCCG"

echo FlaggedRevs reviewAllPages
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo purgePage
docker exec -i swccg_wiki php maintenance/run.php purgePage <<EOF || true
Creators of SWCCG
Designers of SWCCG
Creators of Star Wars CCG
SWCCG creators
Tom Braunlich
Rollie Tesh
Jerry Darcy
Warren Holland
Decipher
Decipher, Inc.
Decipher Inc.
Star Wars CCG
Players Committee
History of the Players Committee
Main Page
Premiere Limited
Decipher and the Star Wars CCG Lucasfilm license
EOF

echo VERIFY
docker exec swccg_wiki php maintenance/run.php getText "Creators of SWCCG" | head -12
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Tom Braunlich" | head -5
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Rollie Tesh" | head -5
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Jerry Darcy" | head -5
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Warren Holland" | head -5
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Decipher" | grep -n "Creators\|Lucasfilm license" | head -10
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Main Page" | grep -n "Creators of SWCCG" | head -5
echo ----
docker exec swccg_wiki php maintenance/run.php getText "History of the Players Committee" | grep -n "Creators of SWCCG\|Lucasfilm license" | head -10
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Decipher and the Star Wars CCG Lucasfilm license" | head -8
echo ----
for u in Creators_of_SWCCG Tom_Braunlich Rollie_Tesh Jerry_Darcy Warren_Holland Decipher Decipher_and_the_Star_Wars_CCG_Lucasfilm_license; do
  code=$(curl -sL -o /dev/null -w "%{http_code}" "https://wiki.swccg.com/wiki/$u")
  echo "$code $u"
done
echo creators apply done