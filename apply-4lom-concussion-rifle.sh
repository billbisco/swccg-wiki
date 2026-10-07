#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
HT_FILE=Dagobah-D-4lomsconcussionrifle.gif
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

ht_sha1() {
  docker exec swccg_wiki bash -lc 'f=$(find /var/www/html/images -name Dagobah-D-4lomsconcussionrifle.gif | head -1); test -n "$f"; sha1sum "$f"' | awk '{print $1}'
}

echo "== Holotable BEFORE =="
HT_BEFORE=$(ht_sha1)
echo "ht_before=$HT_BEFORE"
test -n "$HT_BEFORE"

echo "== SAFETY: no importImages this pass (archive+Holotable already on wiki) =="

edit "4-LOM's Concussion Rifle (Errata)" "$PAGES/4-LOM's_Concussion_Rifle_(Errata).wiki" \
  "Reclass: Decipher Glossary Version 2.0 Errata (uid 4_174d); App A kept Decipher text"
edit "4-LOM's Concussion Rifle" "$PAGES/4-LOM's_Concussion_Rifle.wiki" \
  "Bare default = Glossary 1998 Errata text (uid 4_174); peer Advosze pattern"
edit "4-LOM's Concussion Rifle (Original)" "$PAGES/4-LOM's_Concussion_Rifle_(Original).wiki" \
  "Point print archive to (Errata); keep print game text uid 4_174o"
edit "4-LOM's Concussion Rifle (PC Errata)" "$PAGES/4-LOM's_Concussion_Rifle_(PC_Errata).wiki" \
  "Retire misbin: redirect to 4-LOM's Concussion Rifle (Errata)"
edit "Errata" "$PAGES/Errata.wiki" \
  "Move 4-LOM's Concussion Rifle from PC Errata to Decipher Errata (Glossary 1998)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" \
  "Index: 4-LOM's Concussion Rifle reclassed to Decipher Errata"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

purge "4-LOM's Concussion Rifle"
purge "4-LOM's Concussion Rifle (Original)"
purge "4-LOM's Concussion Rifle (Errata)"
purge "4-LOM's Concussion Rifle (PC Errata)"
purge "Errata"
purge "PC Errata"

echo "== Holotable AFTER =="
HT_AFTER=$(ht_sha1)
echo "ht_after=$HT_AFTER"
if [ "$HT_AFTER" != "$HT_BEFORE" ]; then
  echo "FATAL: Holotable sha1 changed" >&2
  exit 1
fi
echo "ht_unchanged=1"
echo "DONE_APPLY_4LOM_CONCUSSION_RIFLE"
