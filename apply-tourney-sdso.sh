#!/bin/bash
# Tournaments hub expansion + 2026 San Diego Super Open decks. VPS only.
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

echo "== stage images =="
mkdir -p "$ROOT/encyclopedia/upload" "$ROOT/encyclopedia/preserved/tournament-sources"
for f in \
  ratings-search-20011113.png \
  aboutratings-20020808.png \
  ratings-index-20011201.png \
  dc2000-day3.png \
  dc2000-day2.png \
  pc-decklist-current-p1.png \
  SDSO26-Joe.jpg \
  SDSO26-Everyone.jpg \
  SDSO26-banner.jpg
do
  if [ -f "$ROOT/encyclopedia/tournament-sources/png/$f" ]; then
    cp -f "$ROOT/encyclopedia/tournament-sources/png/$f" "$ROOT/encyclopedia/upload/$f"
  fi
done

echo "== importImages screenshots =="
docker exec swccg_wiki mkdir -p /tmp/tourney-sdso
for f in ratings-search-20011113.png aboutratings-20020808.png ratings-index-20011201.png dc2000-day3.png dc2000-day2.png pc-decklist-current-p1.png SDSO26-Joe.jpg SDSO26-Everyone.jpg SDSO26-banner.jpg; do
  if [ -f "$ROOT/encyclopedia/upload/$f" ]; then
    docker cp "$ROOT/encyclopedia/upload/$f" swccg_wiki:/tmp/tourney-sdso/
  fi
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher ratings search, Elo page, DecipherCon 2000 Day 2/3" \
  /tmp/tourney-sdso || true

echo "== importImages GEMP decks =="
docker exec swccg_wiki mkdir -p /tmp/sdso-media
docker cp "$ROOT/sdso-2026-media/." swccg_wiki:/tmp/sdso-media/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="GEMP import from 2026 SDSO Day One/Day Two zips (forum t=86618)" \
  /tmp/sdso-media || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

python3 - <<'PY'
from pathlib import Path
rows = [
    ("Tournaments", "pages/Tournaments.wiki"),
    ("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"),
    ("Championships", "pages/Championships.wiki"),
    ("MediaWiki:Sidebar", "pages/MediaWiki_Sidebar.wiki"),
    ("2026 San Diego Super Open", "pages/2026_San_Diego_Super_Open.wiki"),
    ("Chris Schoenthal", "pages/player-stubs/Chris_Schoenthal.wiki"),
    ("Eddie Szwabowski", "pages/player-stubs/Eddie_Szwabowski.wiki"),
]
pages = Path("pages")
for p in sorted(pages.glob("2026_SDSO*.wiki")):
    rows.append((p.stem.replace("_", " "), str(p).replace("\\", "/")))
for folder in (Path("pages/player-stubs"), Path("pages"), Path("pages/people")):
    if not folder.is_dir():
        continue
    for p in sorted(folder.glob("*.wiki")):
        text = p.read_text(encoding="utf-8", errors="replace")
        if "2026 San Diego Super Open" not in text:
            continue
        title = p.stem.replace("_", " ")
        if title.startswith("2026 "):
            continue
        rows.append((title, str(p).replace("\\", "/")))
seen = {}
for t, r in rows:
    seen[t] = r
Path("tourney-sdso-titles.tsv").write_text(
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
    --summary="Tournaments refs + 2000 Worlds cut; 2026 San Diego Super Open decks" \
    "$title" < "$f"
done < "$ROOT/tourney-sdso-titles.tsv"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Tournaments
List of SWCCG tournaments
Championships
MediaWiki:Sidebar
2026 San Diego Super Open
2026 SDSO Day 2 Joe Olson DS EOps
2026 SDSO Day 2 Daniel Amor DS TFOR
Joe Olson
Daniel Amor
Patrick Johnson
EOF

echo "== verify =="
docker exec swccg_wiki php maintenance/run.php getText "Tournaments" > /tmp/t.txt
docker exec swccg_wiki php maintenance/run.php getText "2026 San Diego Super Open" > /tmp/s.txt
docker exec swccg_wiki php maintenance/run.php getText "2026 SDSO Day 2 Joe Olson DS EOps" > /tmp/o.txt
python3 - <<'PY'
t=open("/tmp/t.txt",encoding="utf-8").read()
s=open("/tmp/s.txt",encoding="utf-8").read()
o=open("/tmp/o.txt",encoding="utf-8").read()
ok=True
checks=[
    ("t ratings file", "ratings-search-20011113.png" in t),
    ("t 0699", "tournamentguide0699.pdf" in t),
    ("t sokol", "Matt Sokol" in t),
    ("t shannon modified", "Modified Win" in t),
    ("t drtorch", "b9f9tNBiU2I" in t),
    ("t decklist ref", "decklist-form-bw.pdf" in t),
    ("t current form", "pc-decklist-current-p1.png" in t),
    ("t 2016 pdf", "Decklist-2016-without-shields.pdf" in t),
    ("s olson", "Joe Olson" in s),
    ("s amor", "Daniel Amor" in s),
    ("o eops", "Endor Operations" in o),
    ("o start field", "Starting Card" in o),
    ("o open", "[[Open]]" in o),
]
for n,hit in checks:
    print(("OK" if hit else "FAIL"), n)
    ok = ok and hit
if not ok:
    raise SystemExit("verify failed")
PY
echo DONE tourney-sdso n=$n
