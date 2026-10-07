#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

echo "== import GEMP txt =="
docker exec swccg_wiki mkdir -p /tmp/rem2026-media
if [ -d "$ROOT/remaining-2026-media" ]; then
  docker cp "$ROOT/remaining-2026-media/." swccg_wiki:/tmp/rem2026-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="GEMP import 2026 US Nats / BWC / Outrider" \
    /tmp/rem2026-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

python3 - <<'PY'
from pathlib import Path
rows = [
    ("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"),
    ("2026 U.S. National Championship", "pages/2026_U.S._National_Championship.wiki"),
    ("2026 Boston Winter Classic", "pages/2026_Boston_Winter_Classic.wiki"),
    ("2026 Outrider Cup IV", "pages/2026_Outrider_Cup_IV.wiki"),
    ("2026 Jawa Cup", "pages/2026_Jawa_Cup.wiki"),
    ("2026 Retro U.S. Nationals", "pages/2026_Retro_U.S._Nationals.wiki"),
    ("2026 Regional Championships", "pages/2026_Regional_Championships.wiki"),
]
pages = Path("pages")
for pat in ("2026_US_Nationals*.wiki", "2026_BWC*.wiki", "2026_Outrider_Cup_IV_*.wiki"):
    for p in sorted(pages.glob(pat)):
        rows.append((p.stem.replace("_", " "), str(p).replace("\\", "/")))
keys = (
    "2026 U.S. National Championship",
    "2026 Boston Winter Classic",
    "2026 Outrider Cup IV",
    "2026 Jawa Cup",
    "2026 Retro U.S. Nationals",
    "2026 Regional Championships",
)
for folder in (Path("pages/player-stubs"), Path("pages")):
    if not folder.is_dir():
        continue
    for p in sorted(folder.glob("*.wiki")):
        text = p.read_text(encoding="utf-8", errors="replace")
        if not any(k in text for k in keys):
            continue
        title = p.stem.replace("_", " ")
        if title.startswith("2026 "):
            continue
        rows.append((title, str(p).replace("\\", "/")))
seen = {}
for t, r in rows:
    seen[t] = r
Path("rem2026-titles.tsv").write_text(
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
    --summary="2026 remaining tournament hubs and GEMP decks" \
    "$title" < "$f"
done < "$ROOT/rem2026-titles.tsv"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
List of SWCCG tournaments
2026 U.S. National Championship
2026 Boston Winter Classic
2026 Outrider Cup IV
2026 Jawa Cup
2026 Retro U.S. Nationals
2026 Regional Championships
Hayes Hunter
Phil Aasen
EOF
echo DONE rem2026 n=$n
