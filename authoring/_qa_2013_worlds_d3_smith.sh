#!/bin/bash
set -euo pipefail
echo "== LS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Reid_Smith_LS_There_Is_Good_In_Him?action=raw" | head -n 10
echo "== DS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Reid_Smith_DS_Wookiee_Slaving_Operation?action=raw" | head -n 10
echo "== HUB =="
curl -sS "https://wiki.swccg.com/wiki/2013_World_Championship?action=raw" | grep -n "Reid Smith" || true
echo "== PLAYER =="
curl -sS "https://wiki.swccg.com/wiki/Reid_Smith?action=raw" | grep "2013 World Championship" || true
echo QA-D3-SMITH-DONE
