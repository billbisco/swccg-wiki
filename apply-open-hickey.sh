#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

python3 - <<'PY'
from pathlib import Path
pages = Path("pages")
rows = [
    ("Open", "pages/Open.wiki"),
    ("Formats", "pages/Formats.wiki"),
    ("2026 Tenth Annual GEMPC", "pages/2026_Tenth_Annual_GEMPC.wiki"),
    ("2026 Retro GEMP Match Play Championship (Premiere to DSII)",
     "pages/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki"),
    ("Charles Hickey", "pages/Charles_Hickey.wiki"),
    ("Charlie Hickey", "pages/Charlie_Hickey.wiki"),
    ("Charless Hickey", "pages/Charless_Hickey.wiki"),
]
for name in [
    "Patrick_Johnson", "Timo_Dusel", "Brad_Kippel", "Joe_Horbey", "Alex_Prodoehl",
    "Matthew_Ford", "Garrett_Larson", "Kendall_Halman", "Randy_Scott",
    "Casey_Johnson", "Scott_Lingrell",
]:
    rows.append((name.replace("_", " "), f"pages/player-stubs/{name}.wiki"))
for p in sorted(pages.glob("2026_GEMPC*.wiki")):
    title = p.stem.replace("_", " ")
    rows.append((title, str(p).replace("\\", "/")))
for p in sorted(pages.glob("2026_Retro_GEMPC_Charlie_Hickey*.wiki")):
    title = p.stem.replace("_", " ")
    rows.append((title, str(p).replace("\\", "/")))
Path("open-hickey-titles.tsv").write_text(
    "\n".join(f"{t}\t{r}" for t, r in rows) + "\n", encoding="utf-8"
)
print("titles", len(rows))
PY

n=0
while IFS=$'\t' read -r title rel; do
  [ -z "${title:-}" ] && continue
  f="$ROOT/$rel"
  if [ ! -f "$f" ]; then echo "MISSING $f" >&2; exit 1; fi
  n=$((n+1))
  echo "== edit $n $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="Open format; Charles Hickey (GEMP teacher)" "$title" < "$f"
done < "$ROOT/open-hickey-titles.tsv"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
2026 Tenth Annual GEMPC
Open
Formats
Charles Hickey
Charlie Hickey
Charless Hickey
Timo Dusel
Patrick Johnson
2026 Retro GEMP Match Play Championship (Premiere to DSII)
EOF

echo "== verify =="
docker exec swccg_wiki php maintenance/run.php getText "2026 Tenth Annual GEMPC" > /tmp/gempc.txt
docker exec swccg_wiki php maintenance/run.php getText "Charles Hickey" > /tmp/ch.txt
python3 - <<'PY'
g = open("/tmp/gempc.txt", encoding="utf-8").read()
c = open("/tmp/ch.txt", encoding="utf-8").read()
ok = True
for name, t, needle in [
    ("hub Open", g, "[[Open]]"),
    ("no Standard virtual", g, "Standard virtual"),
    ("Charles", g, "[[Charles Hickey]]"),
    ("teacher", g, "teacher"),
    ("no Charlie link", g, "[[Charlie Hickey]]"),
    ("charles lead", c, "GEMP '''teacher'''"),
    ("charles Open", c, "[[Open]]"),
]:
    hit = needle in t
    expect_miss = name.startswith("no ")
    good = (not hit) if expect_miss else hit
    print(("OK" if good else "FAIL"), name)
    ok = ok and good
if not ok:
    raise SystemExit("verify failed")
PY
echo DONE open-hickey n=$n
