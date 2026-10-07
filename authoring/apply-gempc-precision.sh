#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

python3 - <<'PY'
from pathlib import Path
pages = Path("pages")
rows = [
    ("2026 Tenth Annual GEMPC", "pages/2026_Tenth_Annual_GEMPC.wiki"),
    ("Chris Gogolen", "pages/people/Chris_Gogolen.wiki"),
    ("Chris Kelly", "pages/Chris_Kelly.wiki"),
    ("Keith Brown", "pages/Keith_Brown.wiki"),
    ("Matt Wadden", "pages/player-stubs/Matt_Wadden.wiki"),
]
for p in sorted(pages.glob("2026_GEMPC*.wiki")):
    rows.append((p.stem.replace("_", " "), str(p).replace("\\", "/")))
stubs = Path("pages/player-stubs")
for p in sorted(stubs.glob("*.wiki")):
    text = p.read_text(encoding="utf-8", errors="replace")
    if "2026 Tenth Annual GEMPC" not in text:
        continue
    title = p.stem.replace("_", " ")
    if title in {"Charlie Hickey"}:
        continue
    rows.append((title, str(p).replace("\\", "/")))
# de-dupe titles, last wins
seen = {}
for t, r in rows:
    seen[t] = r
out = Path("gempc-precision-titles.tsv")
out.write_text("\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8")
print("titles", len(seen))
PY

n=0
while IFS=$'\t' read -r title rel; do
  [ -z "${title:-}" ] && continue
  f="$ROOT/$rel"
  if [ ! -f "$f" ]; then echo "MISSING $f" >&2; exit 1; fi
  n=$((n+1))
  echo "== edit $n $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="Printed GEMP card titles (not PC acronyms); player stubs" "$title" < "$f"
done < "$ROOT/gempc-precision-titles.tsv"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
2026 Tenth Annual GEMPC
2026 GEMPC Top 8 Pat Johnson DS TDIGWATT(V)
2026 GEMPC Top 8 Pat Johnson LS Luke Saga
Patrick Johnson
Drew Lichtenstein
Charles Hickey
Timo Dusel
Chris Gogolen
Matt Wadden
EOF

echo "== verify =="
docker exec swccg_wiki php maintenance/run.php getText "2026 GEMPC Top 8 Pat Johnson DS TDIGWATT(V)" > /tmp/pjds.txt
docker exec swccg_wiki php maintenance/run.php getText "2026 Tenth Annual GEMPC" > /tmp/hub.txt
python3 - <<'PY'
d = open("/tmp/pjds.txt", encoding="utf-8").read()
h = open("/tmp/hub.txt", encoding="utf-8").read()
ok = True
checks = [
    ("obj dual", "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further (V)" in d),
    ("obj visible", "This Deal Is Getting Worse All The Time" in d),
    ("evazan bullet", "Dr. Evazan & \u2022Ponda Baba" in d or "Dr. Evazan & •Ponda Baba" in d),
    ("hub no TDIGWATT pipe", "|TDIGWATT(V)]]" not in h),
    ("hub printed deal", "This Deal Is Getting Worse All The Time" in h),
    ("hub TFSIMF", "The Force Is Strong In My Family" in h),
]
for name, hit in checks:
    print(("OK" if hit else "FAIL"), name)
    ok = ok and hit
if not ok:
    raise SystemExit("verify failed")
PY
echo DONE gempc-precision n=$n
