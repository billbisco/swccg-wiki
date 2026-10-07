#!/bin/bash
# Apply Anderson (+ Herold) LS dest corrections: MWYHL 7-side and Jedi Tests.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-mpc-anderson-fix.tgz" ]; then
  tar xzf "$ROOT/y2013-mpc-anderson-fix.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-mpc-anderson-fix-titles.tsv}"
SUMMARY="${2:-2013 MPC Anderson LS MWYHL 7-side Save You It Can and Jedi Tests}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true
bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
2013 Match Play Championship Day 1 John Anderson LS Mind What You Have Learned (V)
2013 Match Play Championship Day 1 Brian Herold LS Mind What You Have Learned (V)
EOF
echo APPLY-2013-MPC-ANDERSON-FIX-DONE
