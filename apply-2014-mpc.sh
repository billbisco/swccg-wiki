#!/bin/bash
# Apply 2014 Match Play Championship Holotable hubs and decks.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-mpc.tgz" ]; then
  tar xzf "$ROOT/y2014-mpc.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-mpc-titles.tsv}"
SUMMARY="${2:-2014 Match Play Championship Holotable lists}"
# apply-tsv.sh also runs reviewAllPages; still force ReviewTitles for already-reviewed pages.
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
echo "== FlaggedRevs ReviewTitles =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2014 Match Play Championship
Category:2014
Brian Fred
Chris Terwilliger
Cole Lepine
Greg Shaw
Kevin Shannon
Matthew Harrison-Trainor
Reid Smith
Stephen Cellucci
EOF
echo APPLY-2014-MPC-DONE n=$n
