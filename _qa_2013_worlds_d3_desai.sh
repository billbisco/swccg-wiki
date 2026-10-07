#!/bin/bash
set -euo pipefail
echo "== LS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Justin_Desai_LS_It_Is_The_Future_You_See_(V)?action=raw" | head -n 10
echo "== DS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Justin_Desai_DS_Imperial_Occupation?action=raw" | head -n 10
echo "== HUB =="
curl -sS "https://wiki.swccg.com/wiki/2013_World_Championship?action=raw" | grep -n "Justin Desai" || true
echo "== PLAYER =="
curl -sS "https://wiki.swccg.com/wiki/Justin_Desai?action=raw" | grep "2013 World Championship" || true
echo QA-D3-DESAI-DONE
