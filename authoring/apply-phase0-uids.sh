#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys, re
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
m = re.search(r"\|notes=(.*?)(\n\|[a-z_]+=|\n\}\})", text, re.S)
if m and re.search(r"\[\[File:[^\]]*\.gif", m.group(1), re.I):
    raise SystemExit(f"FATAL: gif File embed in notes of {p.name}")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "2-1B (Too-Onebee)" "$PAGES/2-1B_(Too-Onebee).wiki" "card_uid letter suffix: print/bare 3_1o (Bill lock)"
edit "2-1B (Too-Onebee) (Original)" "$PAGES/2-1B_(Too-Onebee)_(Original).wiki" "card_uid 3_1o (was 3_1-OR)"
edit "2-1B (Too-Onebee) (PC Errata)" "$PAGES/2-1B_(Too-Onebee)_(PC_Errata).wiki" "card_uid bare 3_1 (was 3_1-PC); PC playable"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata 2-1B Notes: trim + link Players Committee Advanced Rulebook"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Docs: letter suffixes o/d/bare; not -PC/-OR playable ids"
edit "Card versions" "$PAGES/Card_versions.wiki" "Identifiers: bare GEMP=PC when delta; print o; Decipher d; no -PC/-OR"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -25 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -25 \
  || true

purge() {
  echo "purge $1"
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null \
    || true
}
purge "2-1B (Too-Onebee)"
purge "2-1B (Too-Onebee) (Original)"
purge "2-1B (Too-Onebee) (PC Errata)"
purge "Errata"
purge "PC Errata"
purge "Card versions"

echo "== VERIFY card_uid =="
for t in "2-1B (Too-Onebee)" "2-1B (Too-Onebee) (Original)" "2-1B (Too-Onebee) (PC Errata)"; do
  echo "--- $t ---"
  docker exec swccg_wiki php maintenance/run.php getText "$t" 2>/dev/null | rg -n "card_uid=" || \
  docker exec swccg_wiki php maintenance/getText.php "$t" 2>/dev/null | rg -n "card_uid=" || true
done
echo "DONE_PHASE0_UIDS"
