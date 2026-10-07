#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
tar -xf /tmp/y2022-2024-html.tar
bash "$ROOT/apply-tsv.sh" "$ROOT/y2022-2024-html-titles.tsv" "2022-2024 HTML tournament decks, hubs, and player stubs"
