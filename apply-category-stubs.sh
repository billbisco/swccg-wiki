#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
PAGES="$ROOT/pages"

edit_page() {
  local title="$1"
  local file="$2"
  local summary="$3"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit_page "Category:Sets" "$PAGES/Category_Sets.wiki" "category stub: Sets parent index"
edit_page "Category:Cancelled sets" "$PAGES/Category_Cancelled_sets.wiki" "category stub: Cancelled sets"
edit_page "Category:Virtual Legacy sets" "$PAGES/Category_Virtual_Legacy_sets.wiki" "category stub: Virtual Legacy sets"
edit_page "Category:Current Virtual sets" "$PAGES/Category_Current_Virtual_sets.wiki" "category stub: Current Virtual sets"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Category:Sets
Category:Cancelled sets
Category:Virtual Legacy sets
Category:Current Virtual sets
EOF
echo category stubs done
