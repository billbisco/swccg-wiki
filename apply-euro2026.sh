#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
python3 - <<'PY'
from pathlib import Path
rows = [
    ("2026 European Championship", "pages/2026_European_Championship.wiki"),
    ("European Championships", "pages/European_Championships.wiki"),
    ("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"),
    ("Championships", "pages/Championships.wiki"),
    ("Tournaments", "pages/Tournaments.wiki"),
    ("Category:Tournaments", "pages/Category_Tournaments.wiki"),
    ("Category:Championships", "pages/Category_Championships.wiki"),
    ("Category:2026", "pages/Category_2026.wiki"),
    ("Category:Decklists", "pages/Category_Decklists.wiki"),
    ("Category:Players", "pages/Category_Players.wiki"),
    ("Category:Dark Side decks", "pages/Category_Dark_Side_decks.wiki"),
    ("Category:Light Side decks", "pages/Category_Light_Side_decks.wiki"),
]
pages = Path("pages")
for p in sorted(pages.glob("2026_European_Championship*.wiki")):
    if p.name == "2026_European_Championship.wiki":
        continue
    rows.append((p.stem.replace("_", " "), str(p).replace("\\", "/")))
for folder in (Path("pages/player-stubs"), Path("pages")):
    if not folder.is_dir():
        continue
    for p in sorted(folder.glob("*.wiki")):
        text = p.read_text(encoding="utf-8", errors="replace")
        if "2026 European Championship" not in text:
            continue
        title = p.stem.replace("_", " ")
        if title.startswith("2026 "):
            continue
        rows.append((title, str(p).replace("\\", "/")))
seen = {}
for t, r in rows:
    seen[t] = r
Path("euro2026-titles.tsv").write_text(
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
  python3 - "$f" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
PY
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="2026 European Championship decks; European Championships hub" \
    "$title" < "$f"
done < "$ROOT/euro2026-titles.tsv"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
2026 European Championship
European Championships
List of SWCCG tournaments
Championships
Tournaments
2026 European Championship Top 8 Timo Dusel DS Thrawn
Timo Dusel
Category:Tournaments
Category:Championships
Category:2026
Category:Decklists
Category:Players
EOF
docker exec swccg_wiki php maintenance/run.php getText "2026 European Championship" > /tmp/e.txt
docker exec swccg_wiki php maintenance/run.php getText "List of SWCCG tournaments" > /tmp/l.txt
python3 - <<'PY'
e=open("/tmp/e.txt",encoding="utf-8").read()
l=open("/tmp/l.txt",encoding="utf-8").read()
ok=True
checks=[
    ("hub timo", "Timo Dusel" in e),
    ("hub open", "[[Open]]" in e),
    ("hub thrawn", "A Great Tactician Creates Plans" in e),
    ("list event link", "[[2026 European Championship]]" in l),
    ("list euro hub", "[[European Championships]]" in l),
]
for n,hit in checks:
    print(("OK" if hit else "FAIL"), n)
    ok = ok and hit
if not ok:
    raise SystemExit("verify failed")
PY
echo DONE euro2026 n=$n
