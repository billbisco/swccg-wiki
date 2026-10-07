#!/bin/bash
set -euo pipefail
echo "== DS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_2_John_Veasey_DS_Agents_Of_Black_Sun?action=raw" | head -n 14
echo "== DS KEYS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_2_John_Veasey_DS_Agents_Of_Black_Sun?action=raw" | grep -E "p99 VeeZ|Bodyguard Droid|Death Star Sentry|Begin Landing|Username|dested" || true
echo "== LS =="
curl -sS "https://wiki.swccg.com/wiki/2013_Worlds_Day_2_John_Veasey_LS_Communing?action=raw" | grep -E "Starting Card|p100 VeeZ" || true
echo "== HUB =="
curl -sS "https://wiki.swccg.com/wiki/2013_World_Championship?action=raw" | grep -n "John Veasey" || true
echo "== PLAYER =="
curl -sS "https://wiki.swccg.com/wiki/John_Veasey?action=raw" | grep "2013 World Championship" || true
echo QA-D2-VEASEY-DONE
