#!/bin/bash
# Apply Tony G → Tony Garcia informed-identity merge.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/tony-g.tgz" ]; then
  tar xzf "$ROOT/tony-g.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/tony-g-titles.tsv}"
SUMMARY="${2:-Tony G dested Tony Garcia}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Tony G
Tony Garcia
Unknown players
2013 Match Play Championship
2013 Match Play Championship Day 1 Tony G LS Communing
2013 Match Play Championship Day 1 Tony G DS Set Your Course For Alderaan
Category:2013
EOF
echo APPLY-TONY-G-DONE
