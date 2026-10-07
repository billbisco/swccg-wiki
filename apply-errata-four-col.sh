#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
HT_BEFORE_EXPECTED=3a3ee5afcd96a081a9ae73b683a4001c93ad862c
HT_PATH=/var/www/html/images/5/58/ANH-L-attackrun.gif

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
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

ht_hex() {
  docker exec swccg_wiki sha1sum "$HT_PATH" | awk '{print $1}'
}

echo "== SAFETY: Errata page-edit only; never importImages =="
echo "== Holotable sha1 BEFORE =="
HT_HEX_BEFORE=$(ht_hex)
echo "ht_hex_before=$HT_HEX_BEFORE"
echo "$HT_HEX_BEFORE" > /tmp/ht-sha1-before-four-col.txt
if [ "$HT_HEX_BEFORE" != "$HT_BEFORE_EXPECTED" ]; then
  echo "FATAL: Holotable hex $HT_HEX_BEFORE != expected $HT_BEFORE_EXPECTED" >&2
  exit 1
fi

edit "Errata" "$PAGES/Errata.wiki" \
  "Decipher+PC Errata: 4 cols Card|Original|Errata|PC Errata|Notes; Holotable 350px own cell; Notes prose-only"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --user=Admin 2>&1 | tail -20 \
  || true

echo "purge Errata"
docker exec swccg_wiki php maintenance/run.php purgePage "Errata" 2>/dev/null \
  || docker exec swccg_wiki php maintenance/purgePage.php "Errata" 2>/dev/null \
  || true

echo "== Holotable sha1 AFTER =="
HT_HEX_AFTER=$(ht_hex)
echo "ht_hex_after=$HT_HEX_AFTER"
if [ "$HT_HEX_AFTER" != "$HT_HEX_BEFORE" ] || [ "$HT_HEX_AFTER" != "$HT_BEFORE_EXPECTED" ]; then
  echo "FATAL: Holotable sha1 changed or mismatch before=$HT_HEX_BEFORE after=$HT_HEX_AFTER" >&2
  exit 1
fi
echo "ht_unchanged_proof OK $HT_HEX_AFTER"

docker exec -i swccg_wiki php maintenance/run.php getText "Errata" 2>/dev/null \
  | tr -d '\r' \
  | python3 -c '
import sys
wt=sys.stdin.read()
dual=wt.split("== Decipher and PC Errata ==")[1].split("== PC Errata ==")[0]
print("headers_ok", "! Card !! Original !! Errata !! PC Errata !! Notes" in dual)
print("pc_col_350", "ANH-L-attackrun.gif|350px" in dual)
print("wb_col_350", "ANH-L-attackrun-wb-decipher.gif|350px" in dual)
print("orig_353", "ANH-L-attackrun-decipher-archive.gif|353px" in dual)
notes=dual.split("| style=\"vertical-align:top; max-width:28em\" |",1)[1]
print("notes_has_File", "[[File:" in notes)
print("notes_has_Media", "[[Media:" in notes)
print("intro_mentions_three", "PC Errata" in dual.split("{|")[0] and "350px" in dual.split("{|")[0])
'
echo "DONE_APPLY"
