#!/bin/bash
# Timo DS side CardLink fix + two-column preferred. VPS only; never print .env; no wiki git remote.
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

edit() {
  local title="$1"; local file="$2"; local summary="$3"
  if [ ! -s "$file" ]; then echo "ERROR: missing $file" >&2; exit 1; fi
  # strip BOM / normalize newlines
  python3 - <<PY
from pathlib import Path
p = Path("$file")
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
PY
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations" \
  "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations.wiki" \
  "Side-correct CardLinks: Dark pages+art for Forest/Ralltiir/Spaceport*/Speeder Bike; two-column preferred"

edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)" \
  "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations_(two-column_layout).wiki" \
  "Preferred canonical layout; Dark-side CardLinks for dual-title sites + Speeder Bike"

edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)" \
  "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations_(picture_layout).wiki" \
  "Alternate layout; Dark-side File+CardLink for dual-title sites + Speeder Bike"

edit "2026 Retro GEMP Match Play Championship (Premiere to DSII)" \
  "$PAGES/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki" \
  "Decklists: promote two-column as preferred; label single-column and picture as alternates"

edit "Timo Dusel" \
  "$PAGES/Timo_Dusel.wiki" \
  "Link Dark ROps decklists with two-column preferred"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
printf '%s\n' \
  '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations' \
  '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)' \
  '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)' \
  '2026 Retro GEMP Match Play Championship (Premiere to DSII)' \
  'Timo Dusel' \
  'Main Page' \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true

echo "== verify no leftover -L- on DS deck pages =="
for t in \
  "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations" \
  "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)" \
  "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)"
do
  echo "---- $t ----"
  docker exec swccg_wiki php maintenance/run.php getText "$t" | grep -E -- '-L-|Spaceport Docking Bay|Forest \(Dark\)|Speeder Bike \(Dark\)' || true
done

echo timo-ds-side-fix applied
