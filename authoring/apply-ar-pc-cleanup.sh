#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PC="$ROOT/pages/Attack_Run_PC_Errata.wiki"
ER="$ROOT/pages/Attack_Run_Errata.wiki"
HT_EXPECTED=3a3ee5afcd96a081a9ae73b683a4001c93ad862c

ht_hex() {
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name ANH-L-attackrun.gif | head -1); sha1sum "$f" | awk "{print \$1}"'
}

echo "== Holotable BEFORE =="
HT_BEFORE=$(ht_hex)
echo "ht_before=$HT_BEFORE"
test "$HT_BEFORE" = "$HT_EXPECTED"

normalize() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys, re
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
for sec in ("notes", "printings"):
    m = re.search(r"\|" + sec + r"=(.*?)(\n\|[a-z_]+=|\n\}\})", text, re.S)
    if not m:
        continue
    chunk = m.group(1)
    if re.search(r"\[\[File:[^\]]*\.gif", chunk, re.I):
        raise SystemExit(f"FATAL: gif File embed in {sec} of {p.name}")
    if "do not treat" in chunk.lower():
        raise SystemExit(f"FATAL: do-not-treat essay in {sec} of {p.name}")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
# PC locks
if p.name.startswith("Attack_Run_PC"):
    assert "|image=ANH-L-attackrun.gif" in text
    assert "opponent's" in text or "opponent's" in text
    assert "just before Pull Up!" in text or "just before Pull Up!" in text
PY
}
normalize "$PC"
normalize "$ER"

echo "== edit Attack Run (PC Errata) =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="PC Errata cleanup: short hatnote; prose-only notes/printings (no File:gif); keep Holotable + AR 2023 text" \
  "Attack Run (PC Errata)" < "$PC"

echo "== edit Attack Run (Errata) =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Errata cleanup: prose-only notes (no File:gif embeds); leave WB image + Decipher game text" \
  "Attack Run (Errata)" < "$ER"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  echo "purge $1"
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null \
    || true
}
purge "Attack Run (PC Errata)"
purge "Attack Run (Errata)"
purge "Attack Run"
purge "Errata"
purge "File:ANH-L-attackrun.gif"

echo "== Holotable AFTER =="
HT_AFTER=$(ht_hex)
echo "ht_after=$HT_AFTER"
test "$HT_AFTER" = "$HT_EXPECTED"
echo "HOLOTABLE_OK"
echo "DONE_APPLY_AR_PC_CLEANUP"
