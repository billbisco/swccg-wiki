#!/bin/bash
# Apply 2013 MPC Day 1 D'Ambrosio Lingrell Reisch Shaw Tenneson Thomas Veasey leftover.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-mpc-seven.tgz" ]; then
  tar xzf "$ROOT/y2013-mpc-seven.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-mpc-seven-titles.tsv}"
SUMMARY="${2:-2013 MPC Day 1 DAmbrosio Lingrell Reisch Shaw Tenneson Thomas Veasey}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
if [ -d "$ROOT/y2013-mpc-seven-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-mpc-seven-media
  docker cp "$ROOT/y2013-mpc-seven-media/." swccg_wiki:/tmp/y2013-mpc-seven-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Match Play Championship DAmbrosio Lingrell Reisch Shaw Tenneson Thomas Veasey scans" \
    --extensions=png \
    /tmp/y2013-mpc-seven-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
2013 Match Play Championship
2013 Match Play Championship Day 1 Mike D'Ambrosio DS Contract Killers
2013 Match Play Championship Day 1 Mike D'Ambrosio LS Communing
2013 Match Play Championship Day 1 Scott Lingrell DS Agents Of Black Sun
2013 Match Play Championship Day 1 Scott Lingrell LS Hidden Base (V)
2013 Match Play Championship Day 1 Nick Reisch DS Set Your Course For Alderaan
2013 Match Play Championship Day 1 Nick Reisch LS Let The Wookiee Win (V)
2013 Match Play Championship Day 1 Greg Shaw DS Hunt Down And Destroy The Jedi (V)
2013 Match Play Championship Day 1 Greg Shaw LS There Is Good In Him
2013 Match Play Championship Day 1 Peter Tenneson DS Ralltiir Operations
2013 Match Play Championship Day 1 Peter Tenneson LS Anger, Fear, Aggression (V)
2013 Match Play Championship Day 1 Michael Thomas DS Invasion
2013 Match Play Championship Day 1 Michael Thomas LS Local Uprising (V)
2013 Match Play Championship Day 1 John Veasey DS A Stunning Move
2013 Match Play Championship Day 1 John Veasey LS Communing
Mike D'Ambrosio
Scott Lingrell
Nick Reisch
Greg Shaw
Peter Tenneson
Michael Thomas
John Veasey
EOF
echo APPLY-2013-MPC-SEVEN-DONE
