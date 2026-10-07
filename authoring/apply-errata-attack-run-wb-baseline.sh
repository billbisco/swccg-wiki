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

echo "== SAFETY: page-edits only; never importImages (esp. Holotable) =="
if [ -d /tmp/errata-attack-run-wb-baseline-gifs ]; then
  rm -rf /tmp/errata-attack-run-wb-baseline-gifs
fi
if [ -f "$ROOT/set-card-art/ANH-L-attackrun.gif" ]; then
  echo "WARN: Holotable present under set-card-art but this script does NOT importImages; leaving it untouched"
fi

echo "== Holotable sha1 BEFORE =="
HT_HEX_BEFORE=$(ht_hex)
echo "ht_hex_before=$HT_HEX_BEFORE"
echo "$HT_HEX_BEFORE" > /tmp/ht-sha1-before-wb-baseline.txt
if [ "$HT_HEX_BEFORE" != "$HT_BEFORE_EXPECTED" ]; then
  echo "FATAL: Holotable hex $HT_HEX_BEFORE != expected $HT_BEFORE_EXPECTED" >&2
  exit 1
fi

edit "Attack Run" "$PAGES/Attack_Run.wiki" \
  "WB Decipher baseline face + gametext (Gloss Supp); not PC wording"
edit "Attack Run (Errata)" "$PAGES/Attack_Run_(Errata).wiki" \
  "Same WB baseline as bare Attack Run; Holotable moved to PC Errata page"
edit "Attack Run (PC Errata)" "$PAGES/Attack_Run_(PC_Errata).wiki" \
  "Holotable lives here; Decipher WB baseline on Attack Run / (Errata)"
edit "Attack Run (Original)" "$PAGES/Attack_Run_(Original).wiki" \
  "Hatnote/sibling links: WB baseline vs PC Holotable"
edit "Errata" "$PAGES/Errata.wiki" \
  "Section 2 Errata column = WB Decipher baseline (not Holotable/cite-only)"
edit "File:ANH-L-attackrun-wb-decipher.gif" "$PAGES/File_ANH-L-attackrun-wb-decipher.gif.wiki" \
  "Baseline / Decipher Errata face on Attack Run and (Errata); not cite-only"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

purge "Errata"
purge "Attack Run"
purge "Attack Run (Original)"
purge "Attack Run (Errata)"
purge "Attack Run (PC Errata)"
purge "File:ANH-L-attackrun-wb-decipher.gif"
purge "File:ANH-L-attackrun.gif"

echo "== Holotable sha1 AFTER (must match before AND expected) =="
HT_HEX_AFTER=$(ht_hex)
echo "ht_hex_after=$HT_HEX_AFTER"
if [ "$HT_HEX_AFTER" != "$HT_HEX_BEFORE" ]; then
  echo "FATAL: Holotable sha1 changed $HT_HEX_BEFORE -> $HT_HEX_AFTER" >&2
  exit 1
fi
if [ "$HT_HEX_AFTER" != "$HT_BEFORE_EXPECTED" ]; then
  echo "FATAL: Holotable sha1 $HT_HEX_AFTER != expected $HT_BEFORE_EXPECTED" >&2
  exit 1
fi
echo "ht_unchanged_proof OK $HT_HEX_AFTER"

echo "== verify page images via grep on DB dump-ish =="
for title in "Attack Run" "Attack Run (Errata)" "Attack Run (PC Errata)"; do
  echo "--- $title ---"
  docker exec -i swccg_wiki php maintenance/run.php getText "$title" 2>/dev/null \
    | tr -d '\r' \
    | python3 -c '
import sys,re
wt=sys.stdin.read()
m=re.search(r"\|image=([^\n|]+)", wt)
print("image=", m.group(1).strip() if m else None)
gt=re.search(r"\|game_text=([^\n]+)", wt)
g=gt.group(1) if gt else ""
print("opponents=", "opponent" in g, "just_before=", "just before Pull Up" in g)
print("wb_z=", "TIE pilots in trench." in g)
' || echo "getText failed for $title"
done

docker exec -i swccg_wiki php maintenance/run.php getText "Errata" 2>/dev/null \
  | tr -d '\r' \
  | python3 -c '
import sys
wt=sys.stdin.read()
dual=wt.split("== Decipher and PC Errata ==")[1].split("== PC Errata ==")[0]
print("Errata_sec2_wb350=", "ANH-L-attackrun-wb-decipher.gif|350px" in dual)
print("Errata_sec2_ht350=", "ANH-L-attackrun.gif|350px" in dual)
print("Errata_sec2_120=", "120px" in dual)
'

echo "ht_before=$HT_HEX_BEFORE"
echo "ht_after=$HT_HEX_AFTER"
echo "== DONE apply-errata-attack-run-wb-baseline (page edits only; Holotable untouched) =="
