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
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text), "game_text_note", "game_text_note" in text)
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "Projective Telepathy (Original)" "$PAGES/Projective_Telepathy_(Original).wiki" \
  "UI: drop game_text_note italic; short notes; Original vs Errata side-by-side after Card"

edit "Projective Telepathy (Errata)" "$PAGES/Projective_Telepathy_(Errata).wiki" \
  "UI: remove long game_text_note; notes point Gloss Supp + Original"

edit "Errata" "$PAGES/Errata.wiki" \
  "Hub: Decipher vs PC framing; Changes via Decipher errata seeded with Projective Telepathy only"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
Projective Telepathy (Original)
Projective Telepathy (Errata)
Errata
Errata on Projective Telepathy
Projective Telepathy
EOFPURGE

python3 - <<'PY'
import urllib.request
checks = {
 "https://wiki.swccg.com/wiki/Projective_Telepathy_%28Original%29": [
   "A player who just initiated",
   "Original vs. Errata",
   "opponent must choose to use 2 Force",
 ],
 "https://wiki.swccg.com/wiki/Projective_Telepathy_%28Errata%29": [
   "If your opponent just initiated",
   "Glossary Supplement",
 ],
 "https://wiki.swccg.com/wiki/Errata": [
   "Changes to cards via Decipher errata",
   "Projective Telepathy",
   "A player who just initiated",
   "opponent must choose to use 2 Force",
 ],
}
for u, needles in checks.items():
  req = urllib.request.Request(u, headers={"Cache-Control":"no-cache","Pragma":"no-cache"})
  html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8","replace")
  missing = "noarticletext" in html or "does not have a page" in html.lower()
  print(("LIVE" if not missing else "MISSING"), u, "len", len(html))
  # italic note under game text often comes from Template:Card game_text_note
  if "Original" in u:
    bad = "This is the <b>printed Cloud City face</b> wording" in html or "printed Cloud City face</i>" in html.lower()
    # also check raw absence via action=raw
    print("  game_text_note italic markers absent-ish check skipped in HTML; see raw")
  for c in needles:
    print(("  OK" if c in html else "  MISS"), c)

# raw checks for game_text_note gone
for title in ["Projective_Telepathy_(Original)", "Projective_Telepathy_(Errata)"]:
  ru = f"https://wiki.swccg.com/wiki/{title}?action=raw"
  raw = urllib.request.urlopen(urllib.request.Request(ru, headers={"Cache-Control":"no-cache"}), timeout=45).read().decode("utf-8","replace")
  print("RAW", title, "game_text_note", "game_text_note" in raw, "len", len(raw))
print("DONE")
PY
