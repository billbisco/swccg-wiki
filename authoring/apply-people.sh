#!/bin/bash
# Historian person stubs + Squadron Members hub. Do NOT touch Main Page.
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Historian stubs: Squadron Members, anagram people, preserved fan sites"

MAP="$ROOT/people/titles.tsv"
if [ ! -f "$MAP" ]; then
  echo "missing $MAP" >&2
  exit 1
fi

n=0
while IFS=$'\t' read -r title rel; do
  [ -z "${title:-}" ] && continue
  f="$ROOT/$rel"
  if [ ! -f "$f" ]; then
    echo "MISSING FILE $f" >&2
    exit 1
  fi
  n=$((n+1))
  echo "== edit $n $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin "$title" < "$f"
done < "$MAP"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge hubs =="
for t in \
  'Squadron Members' \
  'Anagrams' \
  'Anagramed Decipherians' \
  'Radio Free Decipher' \
  'Corellian Engineering Corporation (fan site)' \
  'DeckTech' \
  'GamePlayers Network' \
  'Chuck Kallenbach' \
  'Joe Alread' \
  'Sandy Wible' \
  'Kendrick Summers' \
  'Kyle Heuer' \
  'Jonathan Quesenberry' \
  'Carol Wisely' \
  'Creators of SWCCG' \
  'Category:People' \
  'Category:Squadron Members'
do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE people historian apply n=$n"
