#!/bin/bash
# Apply 2014 European Championship hub and 2014 winner updates.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-ec.tgz" ]; then
  tar xzf "$ROOT/y2014-ec.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-ec-titles.tsv}"
SUMMARY="${2:-2014 European Championship hub and 2014 champions}"

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
European Championships
2014 European Championship
2014 European Championship Reset Beta
2014 US Nationals
2014 Match Play Championship
2014 Texas Mini Worlds
Category:2014
Casper Jørgensen
Matthew Harrison-Trainor
Kevin Shannon
Greg Shaw
Legacy Open
EOF
echo APPLY-2014-EC-DONE
