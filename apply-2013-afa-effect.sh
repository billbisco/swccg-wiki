#!/bin/bash
# Apply leftover: Anger, Fear, Aggression (V) is an Effect, not an Interrupt.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-afa-effect.tgz" ]; then
  tar xzf "$ROOT/y2013-afa-effect.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-afa-effect-titles.tsv}"
SUMMARY="${2:-Anger, Fear, Aggression (V) is Effect not Interrupt}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true
bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
echo "== purge TSV titles =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo APPLY-2013-AFA-EFFECT-DONE
