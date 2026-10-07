#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
IMG_SRC="$ROOT/set-card-art/CC-D-projectivetelepathy-decipher-archive.gif"
STAGE=/tmp/pt-archive-gif

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
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

echo "== importImages Decipher archive face =="
if [ ! -f "$IMG_SRC" ]; then
  echo "MISSING image $IMG_SRC" >&2
  exit 1
fi
mkdir -p "$STAGE"
cp -f "$IMG_SRC" "$STAGE/CC-D-projectivetelepathy-decipher-archive.gif"
docker exec swccg_wiki mkdir -p /tmp/pt-archive-gif
docker cp "$STAGE/." swccg_wiki:/tmp/pt-archive-gif/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com Cloud City face archive (Wayback 2008-05-20); printed Original Projective Telepathy" \
  --overwrite \
  /tmp/pt-archive-gif
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com Cloud City face archive (Wayback 2008-05-20); printed Original Projective Telepathy" \
    /tmp/pt-archive-gif || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Projective Telepathy (Original)" "$PAGES/Projective_Telepathy_(Original).wiki" \
  "New: printed Cloud City face (A player); Decipher archive GIF; siblings Original/Errata/V"

edit "Projective Telepathy (Errata)" "$PAGES/Projective_Telepathy_(Errata).wiki" \
  "New: Decipher Gloss Supp opponent wording; card_uid 5_149-DE; not PC errata"

edit "Projective Telepathy" "$PAGES/Projective_Telepathy.wiki" \
  "Default=Gloss Supp opponent text; hatnotes/printings/sources to Original+Errata; version_label Decipher final"

edit "Errata on Projective Telepathy" "$PAGES/Errata_on_Projective_Telepathy.wiki" \
  "Fix: Original=A player printed; Errata/Current=Gloss Supp opponent; Decipher era not PC rewrite"

edit "Errata" "$PAGES/Errata.wiki" \
  "LOTR-style hub: Decipher vs PC; table of Decipher errata with Projective Telepathy first row"

edit "PC Errata" "$PAGES/PC_Errata.wiki" \
  "Document Title (PC Errata) human naming + -PC; contrast -DE / Projective Telepathy (Errata)"

edit "Card versions" "$PAGES/Card_versions.wiki" \
  "Document (Errata)/-DE and Title (PC Errata)/-PC human titles; PT example"

edit "Projective Telepathy (V)" "$PAGES/Projective_Telepathy_(V).wiki" \
  "Hatnote: link Original/Errata siblings + comparison"

edit "Players Committee rule changes" "$PAGES/Players_Committee_rule_changes.wiki" \
  "See also: Projective Telepathy Original/Errata/V siblings"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
Projective Telepathy
Projective Telepathy (Original)
Projective Telepathy (Errata)
Projective Telepathy (V)
Errata on Projective Telepathy
Errata
PC Errata
Card versions
Players Committee rule changes
EOFPURGE

python3 - <<'PY'
import urllib.request
checks = {
 "https://wiki.swccg.com/wiki/Projective_Telepathy": [
   "If your opponent just initiated",
   "Projective Telepathy (Original)",
   "Projective Telepathy (Errata)",
 ],
 "https://wiki.swccg.com/wiki/Projective_Telepathy_(Original)": [
   "A player who just initiated",
 ],
 "https://wiki.swccg.com/wiki/Projective_Telepathy_(Errata)": [
   "If your opponent just initiated",
 ],
 "https://wiki.swccg.com/wiki/Errata": [
   "Projective Telepathy",
   "Decipher era",
   "List of cards with official Decipher errata",
 ],
 "https://wiki.swccg.com/wiki/Errata_on_Projective_Telepathy": [
   "A player who just initiated",
 ],
}
for u, needles in checks.items():
  html = urllib.request.urlopen(urllib.request.Request(u, headers={"Cache-Control":"no-cache"}), timeout=45).read().decode("utf-8","replace")
  missing = "noarticletext" in html or "does not have a page" in html.lower()
  print(("LIVE" if not missing else "MISSING"), u, "len", len(html))
  for c in needles:
    print(("  OK" if c in html else "  MISS"), c)
print("DONE")
PY
