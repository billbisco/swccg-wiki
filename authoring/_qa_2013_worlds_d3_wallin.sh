#!/bin/bash
set -euo pipefail
echo "== LS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Emil_Wallin_LS_There_Is_Good_In_Him?action=raw" | head -n 12
echo "== DS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_3_Emil_Wallin_DS_Imperial_Entanglements?action=raw" | head -n 12
echo "== HUB =="
curl -sS "https://wiki.swccg.com/wiki/2013_World_Championship?action=raw" | grep -n "Emil Wallin" || true
echo "== PLAYER =="
curl -sS "https://wiki.swccg.com/wiki/Emil_Wallin?action=raw" | grep "2013 World Championship" || true
echo QA-D3-WALLIN-DONE
