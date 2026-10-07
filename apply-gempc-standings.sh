#!/bin/bash
# Challonge finish-order standings + multi-event player identity for 10th Annual GEMPC.
set -euo pipefail
ROOT=/opt/swccg-wiki
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
if not text.endswith("\n"):
    text += "\n"
p.write_text(text, encoding="utf-8", newline="\n")
PY
}

edit() {
  local title="$1" file="$2"
  if [ ! -s "$file" ]; then echo "ERROR: missing $file" >&2; exit 1; fi
  strip_bom "$file"
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="Challonge 18vokbxb finish order; Pat Johnson=Patrick Johnson=Pmj; missing + overlap" \
    "$title" < "$file"
}

edit "2026 Tenth Annual GEMPC" "$ROOT/pages/2026_Tenth_Annual_GEMPC.wiki"
edit "2026 Retro GEMP Match Play Championship (Premiere to DSII)" \
  "$ROOT/pages/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki"

for pair in \
  "Patrick Johnson|pages/player-stubs/Patrick_Johnson.wiki" \
  "Timo Dusel|pages/player-stubs/Timo_Dusel.wiki" \
  "Brad Kippel|pages/player-stubs/Brad_Kippel.wiki" \
  "Joe Horbey|pages/player-stubs/Joe_Horbey.wiki" \
  "Alex Prodoehl|pages/player-stubs/Alex_Prodoehl.wiki" \
  "Matthew Ford|pages/player-stubs/Matthew_Ford.wiki" \
  "Garrett Larson|pages/player-stubs/Garrett_Larson.wiki" \
  "Kendall Halman|pages/player-stubs/Kendall_Halman.wiki" \
  "Charlie Hickey|pages/player-stubs/Charlie_Hickey.wiki" \
  "Randy Scott|pages/player-stubs/Randy_Scott.wiki" \
  "Casey Johnson|pages/player-stubs/Casey_Johnson.wiki" \
  "Scott Lingrell|pages/player-stubs/Scott_Lingrell.wiki" \
  "Pat Johnson|pages/Pat_Johnson.wiki" \
  "Pmj|pages/Pmj.wiki" \
  "Charles Hickey|pages/Charles_Hickey.wiki" \
  "Charless Hickey|pages/Charless_Hickey.wiki" \
  "2026 GEMPC Pat Johnson DS Court|pages/2026_GEMPC_Pat_Johnson_DS_Court.wiki" \
  "2026 GEMPC Pat Johnson LS WYS|pages/2026_GEMPC_Pat_Johnson_LS_WYS.wiki" \
  "2026 GEMPC Top 8 Pat Johnson DS TDIGWATT(V)|pages/2026_GEMPC_Top_8_Pat_Johnson_DS_TDIGWATT(V).wiki" \
  "2026 GEMPC Top 8 Pat Johnson LS Luke Saga|pages/2026_GEMPC_Top_8_Pat_Johnson_LS_Luke_Saga.wiki" \
  "2026 GEMPC Charles Hickey DS MKOS|pages/2026_GEMPC_Charles_Hickey_DS_MKOS.wiki" \
  "2026 GEMPC Charles Hickey LS Luke Saga|pages/2026_GEMPC_Charles_Hickey_LS_Luke_Saga.wiki"
do
  title="${pair%%|*}"
  rel="${pair#*|}"
  edit "$title" "$ROOT/$rel"
done

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
2026 Tenth Annual GEMPC
2026 Retro GEMP Match Play Championship (Premiere to DSII)
Patrick Johnson
Pat Johnson
Pmj
Timo Dusel
Charlie Hickey
Charles Hickey
Charless Hickey
Brad Kippel
Joe Horbey
Alex Prodoehl
Matthew Ford
Garrett Larson
Kendall Halman
Randy Scott
Casey Johnson
Scott Lingrell
2026 GEMPC Pat Johnson DS Court
2026 GEMPC Top 8 Pat Johnson DS TDIGWATT(V)
EOF

echo "== verify getText hub =="
docker exec swccg_wiki php maintenance/run.php getText "2026 Tenth Annual GEMPC" > /tmp/gempc-hub.txt
python3 - <<'PY'
t = open("/tmp/gempc-hub.txt", encoding="utf-8").read()
checks = [
    "challonge.com/18vokbxb",
    "[[Patrick Johnson]]",
    "Pat Johnson / Pmj",
    "== Missing from the GEMP zip / PC list ==",
    "== Also played Retro GEMPC ==",
    "Lost Finals",
    "Lost play-in (Round 1)",
    "[[Timo Dusel]]",
    "[[Charlie Hickey]]",
    "2026 GEMPC Charles Hickey DS MKOS",
    "[[Alex Prodoehl]]",
    "| 1 || 10 ||",
]
ok = True
for c in checks:
    hit = c in t
    print(("OK" if hit else "FAIL"), c)
    ok = ok and hit
print("hub_len", len(t))
if not ok:
    raise SystemExit("hub verify failed")
PY

echo "DONE gempc-standings"
