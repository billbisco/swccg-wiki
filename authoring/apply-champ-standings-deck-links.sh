#!/bin/bash
# Apply championship standings strategy-cell deck links; remove Decklists section.
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

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
print(p.name, "ok", len(text))
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  if [ ! -s "$file" ]; then echo "ERROR: missing $file" >&2; exit 1; fi
  strip_bom "$file"
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

TITLE="2026 Retro GEMP Match Play Championship (Premiere to DSII)"
FILE="$PAGES/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki"

edit "$TITLE" "$FILE" \
  "Standings: link Dark/Light strategy cells to sample decklists (Timo+Jonny); remove duplicate Decklists section"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20

echo "== purgePage =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
2026 Retro GEMP Match Play Championship (Premiere to DSII)
2026 Retro GEMPC Timo Dusel DS Ralltiir Operations
2026 Retro GEMPC Timo Dusel LS Hidden Base
2026 Retro GEMPC Jonny Chu DS Ralltiir Operations
2026 Retro GEMPC Jonny Chu LS Throne Room Mains
Main Page
EOFPURGE

echo "== verify raw =="
RAW=$(docker exec swccg_wiki php maintenance/run.php getText "$TITLE")
python3 - "$RAW" <<'PY'
import sys
text = sys.argv[1]
checks = [
  ("timo DS", "[[2026 Retro GEMPC Timo Dusel DS Ralltiir Operations|ROps]]"),
  ("timo LS", "[[2026 Retro GEMPC Timo Dusel LS Hidden Base|Hidden Base]]"),
  ("jonny DS", "[[2026 Retro GEMPC Jonny Chu DS Ralltiir Operations|ROps]]"),
  ("jonny LS", "[[2026 Retro GEMPC Jonny Chu LS Throne Room Mains|TRM]]"),
  ("no Decklists", None),
]
ok = True
for name, needle in checks:
    if needle is None:
        present = "== Decklists ==" in text
        print(f"{name}: {'FAIL still present' if present else 'OK gone'}")
        ok = ok and (not present)
    else:
        present = needle in text
        print(f"{name}: {'OK' if present else 'FAIL missing'} -> {needle}")
        ok = ok and present
# unlinked sample
print("jeremy unlinked:", "| 3 || [[Jeremy Christoffel]] || SYCFA || EBO" in text)
if not ok:
    raise SystemExit("verify failed")
print("verify OK")
PY

echo champ-standings-deck-links applied