#!/bin/bash
cd /home/claude/errgen
run(){ slug=$1; origin=$2; era=$3; f=$slug/refused.tsv; [ -s $f ] || return; args=(); while IFS=$'\t' read -r fam rest; do [ -n "$fam" ] && args+=(--family "$fam"); done < <(cut -f1 $f | sort -u); python3 errgen.py --out /home/claude/errgen/rr2/$slug --keep-stamp-only --origin-set "$origin" --era "$era" "${args[@]}" > logs/rr2-$slug.log 2>&1; echo "$slug $(tail -1 logs/rr2-$slug.log)"; }
for n in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 D P; do run vs$n "Virtual Set $n" "Virtual Modern" & [ $(jobs -r | wc -l) -ge 3 ] && wait -n; done; wait
for n in 1 2 3 4 5 6 7 8 9; do run vb$n "Virtual Block $n" "Virtual Legacy" & [ $(jobs -r | wc -l) -ge 3 ] && wait -n; done; wait
run vshields "Virtual Shields" "Virtual Legacy"
echo ALLDONE
