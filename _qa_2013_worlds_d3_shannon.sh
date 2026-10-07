#!/bin/bash
set -euo pipefail
echo "== LS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Kevin_Shannon_LS_Communing?action=raw" | head -n 10
echo "== DS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Kevin_Shannon_DS_Set_Your_Course_For_Alderaan?action=raw" | head -n 10
echo "== HUB =="
curl -sS "https://wiki.swccg.com/wiki/2013_World_Championship?action=raw" | grep -n "Kevin Shannon" || true
echo "== PLAYER =="
curl -sS "https://wiki.swccg.com/wiki/Kevin_Shannon?action=raw" | grep "2013 World Championship" || true
echo QA-D3-SHANNON-DONE
