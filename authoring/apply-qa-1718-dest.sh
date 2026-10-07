#!/bin/bash
# Apply Twin Suns / JCC dest fills and the Outrider Cup series hub.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/qa-1718-dest.tgz" ]; then
  tar xzf "$ROOT/qa-1718-dest.tgz" -C "$ROOT"
fi
bash "$ROOT/apply-tsv.sh" "$ROOT/qa-1718-dest-titles.tsv" "2017-2018 dest fills: Twin Suns, Jedi Council Chamber; Outrider Cup series"
echo "== extra hub purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Outrider Cup
2018 European Championship
2018 European Match Play Championship
2017 European Championship
Team USA
Team Europe
Category:Teams
Gosse Zeilstra
Jeff Visseaux
Peter Rowlands
Mike Klarenbeek
EOF
echo "APPLY-QA-1718-DEST-DONE"
