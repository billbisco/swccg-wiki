#!/bin/bash
set -euo pipefail
echo "== LS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Steve_Baroni_LS_Communing?action=raw" | head -n 12
echo "== DS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Steve_Baroni_DS_Hunt_Down_And_Destroy_The_Jedi_%28V%29?action=raw" | head -n 12
echo "== HUB =="
curl -sS "https://wiki.swccg.com/wiki/2013_World_Championship?action=raw" | grep -n "Steve Baroni" || true
echo "== PLAYER =="
curl -sS "https://wiki.swccg.com/wiki/Steve_Baroni?action=raw" | grep "Day 3" || true
echo QA-D3-BARONI-DONE
