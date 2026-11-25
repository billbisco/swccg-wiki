#!/bin/bash
# par.sh g1 g2 ... : run step.sh for each group in parallel for ~40s, then print progress
cd /tmp/batches
for g in "$@"; do (timeout 42 env BUDGET=38 GRPS=$g ~/w/tools/step.sh > par.$g.out 2>&1 &); done
sleep 44
for g in "$@"; do head -1 par.$g.out; done
