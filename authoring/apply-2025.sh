#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

echo "== import GEMP txt =="
if [ -d "$ROOT/2025-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2025-media
  docker cp "$ROOT/2025-media/." swccg_wiki:/tmp/y2025-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="GEMP import 2025 Worlds / US Nats / GEMPC / Retro / Charity" \
    /tmp/y2025-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

python3 - <<'PY'
from pathlib import Path
rows = [
    ("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"),
    ("European Championships", "pages/European_Championships.wiki"),
    ("Category:2025", "pages/Category_2025.wiki"),
    ("2025 World Championship", "pages/2025_World_Championship.wiki"),
    ("2025 U.S. National Championship", "pages/2025_U.S._National_Championship.wiki"),
    ("2025 European Championship", "pages/2025_European_Championship.wiki"),
    ("2025 Ninth Annual GEMPC", "pages/2025_Ninth_Annual_GEMPC.wiki"),
    ("2025 Retro GEMP Match Play Championship (Premiere to DSII)", "pages/2025_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki"),
    ("2025 Online Retro Event for Charity", "pages/2025_Online_Retro_Event_for_Charity.wiki"),
    ("2025 Online Championship Series Playoffs", "pages/2025_Online_Championship_Series_Playoffs.wiki"),
    ("2025 Regional Championships", "pages/2025_Regional_Championships.wiki"),
    ("2025 Morristown Melee", "pages/2025_Morristown_Melee.wiki"),
    ("2025 Las Vegas Grand Prix", "pages/2025_Las_Vegas_Grand_Prix.wiki"),
]
pages = Path("pages")
for pat in (
    "2025_Worlds*.wiki",
    "2025_US_Nationals*.wiki",
    "2025_GEMPC*.wiki",
    "2025_Retro_GEMPC*.wiki",
    "2025_Charity*.wiki",
    "2025_LVGP*.wiki",
    "2025_Morristown*.wiki",
    "2025_European_Championship*.wiki",
):
    for p in sorted(pages.glob(pat)):
        rows.append((p.stem.replace("_", " "), str(p).replace("\\", "/")))
keys = (
    "2025 World Championship",
    "2025 U.S. National Championship",
    "2025 European Championship",
    "2025 Ninth Annual GEMPC",
    "2025 Retro GEMP Match Play Championship",
    "2025 Online Retro Event for Charity",
    "2025 Online Championship Series Playoffs",
    "2025 Regional Championships",
    "2025 Morristown Melee",
    "2025 Las Vegas Grand Prix",
)
for folder in (Path("pages/player-stubs"), Path("pages")):
    if not folder.is_dir():
        continue
    for p in sorted(folder.glob("*.wiki")):
        text = p.read_text(encoding="utf-8", errors="replace")
        if not any(k in text for k in keys):
            continue
        title = p.stem.replace("_", " ")
        if title.startswith("2025 "):
            continue
        rows.append((title, str(p).replace("\\", "/")))
seen = {}
for t, r in rows:
    seen[t] = r
Path("y2025-titles.tsv").write_text(
    "\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8"
)
print("titles", len(seen))
PY

n=0
while IFS=$'\t' read -r title rel; do
  [ -z "${title:-}" ] && continue
  f="$ROOT/$rel"
  if [ ! -f "$f" ]; then echo "MISSING $f" >&2; continue; fi
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
    --summary="2025 tournament hubs and GEMP decks" \
    "$title" < "$f"
done < "$ROOT/y2025-titles.tsv"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
List of SWCCG tournaments
European Championships
2025 World Championship
2025 U.S. National Championship
2025 European Championship
2025 Ninth Annual GEMPC
Greg Shaw
Matt Scott
Emil Wallin
EOF
echo DONE y2025 n=$n
