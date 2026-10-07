#!/bin/bash
set -euo pipefail
echo "== LS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Jonny_Chu_LS_Communing?action=raw" | head -n 10
echo "== DS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Jonny_Chu_DS_Spice_Mine_Operations?action=raw" | head -n 10
echo "== HUB =="
curl -sS "https://wiki.swccg.com/wiki/2013_World_Championship?action=raw" | grep -n "Jonny Chu" || true
echo "== PLAYER =="
curl -sS "https://wiki.swccg.com/wiki/Jonny_Chu?action=raw" | grep "2013 World Championship" || true
echo QA-D3-CHU-DONE
