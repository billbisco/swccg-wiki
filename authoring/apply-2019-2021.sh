#!/bin/bash
# Apply 2019–2021 hubs, decks, player tables, List rows. importImages + edit + FlaggedRevs.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
TSV="${1:-$ROOT/y2019-2021-titles.tsv}"
SUMMARY="${2:-2019-2021 tournament hubs and published decks}"
if [ ! -s "$TSV" ]; then
  echo "ERROR: missing $TSV" >&2
  exit 1
fi

echo "== import GEMP txt =="
if [ -d "$ROOT/y2019-2021-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2019-2021-media
  docker cp "$ROOT/y2019-2021-media/." swccg_wiki:/tmp/y2019-2021-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="GEMP import 2019-2021 tournament decks" \
    /tmp/y2019-2021-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

n=0
while IFS=$'\t' read -r title rel; do
  title="${title%$'\r'}"
  rel="${rel%$'\r'}"
  [ -z "${title:-}" ] && continue
  f="$ROOT/$rel"
  if [ ! -f "$f" ]; then
    echo "MISSING $f" >&2
    continue
  fi
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
if not text.endswith("\n"):
    text += "\n"
p.write_text(text, encoding="utf-8", newline="\n")
PY
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="$SUMMARY" \
    "$title" < "$f" || echo "EDITFAIL $title" >&2
done < "$TSV"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge hubs =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
European Championships
Formats
Premiere - Death Star II
Premiere - Reflections II
2021 World Championship
2021 Worlds Throwback Event
2021 Online Championship Series Playoffs
2021 Outrider Cup
2021 Regional Championships
2021 U.S. National Championship
2021 Retro Event (Premiere to Death Star II)
2021 Match Play Championship
2020 World Championship
2020 Online Championship Series Playoffs
2020 Texas Mini Worlds
2020 Match Play Championship
2020 Endor Grand Prix
2019 Outrider Cup
2019 Online Championship Series Playoffs
2019 World Championship
2019 North American Continental Championship
2019 European Championship
2019 Match Play Championship
2019 Endor Grand Prix
Joe Olson
Bastian Winkelhaus
Brian Fred
Matthew Harrison-Trainor
Greg Shaw
Hayes Hunter
Justin Desai
Jonny Chu
Chris Kelly
Stephen Skilton
EOF

echo DONE n=$n tsv=$TSV
