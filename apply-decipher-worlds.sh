#!/bin/bash
# Apply Format-column indexes + Decipher Worlds 1996-2001 hubs/decks.
# VPS apply only. Never prints /opt/swccg-wiki/.env
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"

TSV="$ROOT/decipher-worlds-titles.tsv"
if [ ! -s "$TSV" ]; then
  echo "ERROR: missing $TSV" >&2
  exit 1
fi

n=0
while IFS=$'\t' read -r title rel; do
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
p.write_text(text, encoding="utf-8", newline="\n")
PY
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="Format column + Decipher World Championships 1996-2001" \
    "$title" < "$f"
done < "$TSV"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
List of SWCCG tournaments
European Championships
Championships
Formats
Tournaments
Premiere - Death Star II
Premiere - A New Hope
Premiere - Cloud City
Premiere - Special Edition
Premiere - Endor
Premiere - Reflections III
Jawa Format
Premiere to Virtual Set 3
2026 Jawa Cup
2025 Online Retro Event for Charity
1996 Decipher World Championship
1997 Decipher World Championship
1998 Decipher World Championship
1999 Decipher World Championship
2000 Decipher World Championship
2001 Decipher World Championship
World Championship 1996
Raphael Asselin
Bastian Winkelhaus
Martin Akesson
Philipp Jacobs
Gary Carman
Matt Sokol
Bjørn Sørgjerd
Kevin Reitzel
Michael Riboulet
Matt Potter
Paul Todd Feldman
Main Page
EOF

echo DONE decipher-worlds n=$n
