#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

python3 - <<'PY'
from pathlib import Path
pages = Path("pages")
rows = [("2026 Tenth Annual GEMPC", "pages/2026_Tenth_Annual_GEMPC.wiki")]
for p in sorted(pages.glob("2026_GEMPC*.wiki")):
    rows.append((p.stem.replace("_", " "), str(p).replace("\\", "/")))
for folder in (Path("pages/player-stubs"), Path("pages"), Path("pages/people")):
    if not folder.is_dir():
        continue
    for p in sorted(folder.glob("*.wiki")):
        text = p.read_text(encoding="utf-8", errors="replace")
        if "2026 Tenth Annual GEMPC" not in text:
            continue
        title = p.stem.replace("_", " ")
        if title.startswith("2026 "):
            continue
        rows.append((title, str(p).replace("\\", "/")))
seen = {}
for t, r in rows:
    seen[t] = r
Path("gempc-start-titles.tsv").write_text(
    "\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8"
)
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
    --summary="Starting Card + Starting Interrupt; (V) only when in card title" \
    "$title" < "$f"
done < "$ROOT/gempc-start-titles.tsv"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
2026 Tenth Annual GEMPC
2026 GEMPC Top 8 Pat Johnson DS TDIGWATT(V)
2026 GEMPC Amar Banger LS LTWW(V)
2026 GEMPC Robbie Hendon LS LTWW(V)
Patrick Johnson
Amar Banger
EOF

docker exec swccg_wiki php maintenance/run.php getText "2026 GEMPC Top 8 Pat Johnson DS TDIGWATT(V)" > /tmp/pj.txt
docker exec swccg_wiki php maintenance/run.php getText "2026 GEMPC Amar Banger LS LTWW(V)" > /tmp/ab.txt
docker exec swccg_wiki php maintenance/run.php getText "2026 Tenth Annual GEMPC" > /tmp/h.txt
python3 - <<'PY'
pj=open("/tmp/pj.txt",encoding="utf-8").read()
ab=open("/tmp/ab.txt",encoding="utf-8").read()
h=open("/tmp/h.txt",encoding="utf-8").read()
ok=True
checks=[
    ("deal V visible", "This Deal Is Getting Worse All The Time (V)" in pj),
    ("start loc field", "Starting Card" in pj),
    ("banger chambers", "Naboo: Boss Nass' Chambers" in ab),
    ("banger LTWW V", "Let The Wookiee Win (V)" in ab),
    ("banger interrupt field", "Starting Interrupt" in ab),
    ("hub deal V", "This Deal Is Getting Worse All The Time (V)" in h),
    ("hub verge no tacked V", "|On The Verge Of Greatness]]" in h),
    ("hub hidden path no V", "|The Hidden Path]]" in h),
    ("hub LTWW", "Let The Wookiee Win (V)" in h),
]
for n,hit in checks:
    print(("OK" if hit else "FAIL"), n)
    ok = ok and hit
if not ok:
    raise SystemExit("verify failed")
PY
echo DONE gempc-start n=$n
