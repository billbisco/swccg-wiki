#!/bin/bash
# Apply VB1–9 dual-title objective pages, 0-side redirects, hubs, neighbors.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/legacy-obj.tgz" ]; then
  tar xzf "$ROOT/legacy-obj.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/legacy-obj-titles.tsv}"
SUMMARY="${2:-Legacy Block objectives: dual titles, both faces, (V) on reprint faces}"
bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Category:Objective
Wookiee Slaving Operation
Wookiee Slaving Operation / Indentured To The Empire
Contract Killers / Feared Throughout The Galaxy
Imperial Occupation (V) / Imperial Control (V)
Imperial Entanglements / No One To Stop Us This Time (Virtual Block 1)
A Stunning Move / A Valuable Hostage (Virtual Block 7)
Local Uprising (V) / Liberation (V)
Hidden Base (V) / Systems Will Slip Through Your Fingers (V)
Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)
Watch Your Step (V) / This Place Can Be A Little Rough (V)
We Have A Plan (V) / They Will Be Lost And Confused (V)
We'll Handle This (V) / Duel Of The Fates (V)
Mind What You Have Learned (V) / Save You It Can (V)
Rebel Strike Team (V) / Garrison Destroyed (V)
Center Of Tyranny / A Liberated World
Infiltration / Unlikely Allies
Republic At War / Aggressive Negotiations
Separatist Uprising / At War With Itself
Virtual Block 1
Virtual Block 2
Virtual Block 4
Virtual Block 5
Virtual Block 6
Virtual Block 7
Virtual Block 8
Virtual Block 9
EOF
echo APPLY-LEGACY-OBJ-DONE
