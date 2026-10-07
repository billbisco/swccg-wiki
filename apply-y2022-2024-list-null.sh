#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
tar -xf /tmp/y2022-2024-list-null.tar
bash "$ROOT/apply-tsv.sh" "$ROOT/y2022-2024-list-null.tsv" "null-edit tournament list after 2022-2024 category and player stubs"
printf '%s\n' "List of SWCCG tournaments" "Patrick Lima" "Category:2022" "Category:2023" "Category:2024" \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo LIST_NULL_DONE
