#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
ART="$ROOT/set-art"
PAGES="$ROOT/pages"
mkdir -p "$ART"
cd "$ROOT"

UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
W='https://static.wikia.nocookie.net/starwars/images'

download() {
  local dest="$1"
  shift
  if [ -s "$dest" ]; then
    return 0
  fi
  local url
  for url in "$@"; do
    if curl -fsSL -A "$UA" --max-time 25 -o "$dest.tmp" "$url"; then
      if [ -s "$dest.tmp" ] && ! grep -q 'Just a moment' "$dest.tmp" 2>/dev/null; then
        mv "$dest.tmp" "$dest"
        echo "got $(basename "$dest") from $url"
        return 0
      fi
    fi
    rm -f "$dest.tmp"
  done
  echo "MISS $(basename "$dest")"
  return 0
}

# Wookieepedia product photos (box when possible, otherwise pack/product).
download "$ART/Set-premiere-limited.jpg" \
  "$W/e/e4/SWCCG-PremiereLimitedBox.jpg/revision/latest"
download "$ART/Set-premiere-unlimited.jpg" \
  "$W/2/2a/SWCCG-PremiereUnlimitedBox.jpg/revision/latest"
download "$ART/Set-premiere-2p.jpg" \
  "$W/7/75/SWCCG_Premier_Intro_box.png/revision/latest"
download "$ART/Set-rebel-leader.jpg" \
  "$W/5/5d/Rebel_Leader_Pack_CCG.jpg/revision/latest"
download "$ART/Set-a-new-hope.jpg" \
  "$W/6/64/ANH_CCG_Limited_pack.jpg/revision/latest" \
  "$W/c/ce/ANH_Revised_CCG.jpg/revision/latest"
download "$ART/Set-esb-2p.jpg" \
  "$W/6/62/TESB_Introductory_CCG.jpg/revision/latest"
download "$ART/Set-hoth.jpg" \
  "$W/4/49/41jTwyM0l-L.jpg/revision/latest"
download "$ART/Set-dagobah.jpg" \
  "$W/4/40/Dagobah_CCG_box.jpg/revision/latest"
download "$ART/Set-jedi-pack.jpg" \
  "$W/5/54/JediPackBooster.jpg/revision/latest"
download "$ART/Set-first-anthology.jpg" \
  "$W/5/52/Star_wars_First_Anthology.png/revision/latest"
download "$ART/Set-cloud-city.jpg" \
  "$W/3/35/CloudCity_CCG.jpg/revision/latest"
download "$ART/Set-jabbas-palace.jpg" \
  "$W/6/60/JabbasPalaceLimitedExpansionSet.jpg/revision/latest"
download "$ART/Set-otsd.jpg" \
  "$W/3/3f/Official_Tournament_Sealed_Deck_CCG.jpg/revision/latest"
download "$ART/Set-second-anthology.jpg" \
  "$W/5/5f/Swsecondanthology.jpg/revision/latest"
download "$ART/Set-revised-anh.jpg" \
  "$W/c/ce/ANH_Revised_CCG.jpg/revision/latest"
download "$ART/Set-revised-hoth.jpg" \
  "$W/5/54/Hoth_unlimited.jpg/revision/latest"
download "$ART/Set-revised-dagobah.jpg" \
  "$W/4/40/Dagobah_CCG_box.jpg/revision/latest"
download "$ART/Set-special-edition.jpg" \
  "$W/1/17/51p5KGdwsqL.jpg/revision/latest"
download "$ART/Set-enhanced-premiere.jpg" \
  "$W/4/40/Enhanced_Premiere_CCG.jpg/revision/latest"
download "$ART/Set-endor.jpg" \
  "$W/9/91/Clip-123842686.png/revision/latest"
download "$ART/Set-enhanced-cloud-city.jpg" \
  "$W/4/4c/Enhanced_Cloud_City_CCG_Lando_pack.jpg/revision/latest"
download "$ART/Set-enhanced-jabbas-palace.jpg" \
  "$W/8/88/Enhanced_Jabbas_Palace_CCG_Mara_Jade_box.jpg/revision/latest"
download "$ART/Set-reflections.jpg" \
  "$W/8/86/Sw-reflect-pack.jpg/revision/latest"
download "$ART/Set-third-anthology.jpg" \
  "$W/7/7a/Third_Anthology_CCG_box.jpg/revision/latest"
download "$ART/Set-death-star-ii.jpg" \
  "$W/3/38/DeathStarIILimitedExpansionPack.jpg/revision/latest"
download "$ART/Set-ds2-starters.jpg" \
  "$W/3/38/DeathStarIILimitedExpansionPack.jpg/revision/latest"
download "$ART/Set-jp-sealed.jpg" \
  "$W/8/8a/Jabbas_Palace_Sealed_Deck.jpg/revision/latest"
download "$ART/Set-reflections-ii.jpg" \
  "$W/d/df/Reflections_II_SWCCG_box.jpg/revision/latest"
download "$ART/Set-tatooine.jpg" \
  "$W/6/65/SW_CCG_Tatooine.png/revision/latest"
download "$ART/Set-coruscant.jpg" \
  "$W/0/0e/Coruscant_CCG_box.jpg/revision/latest" \
  "$W/9/9a/Coruscant_CCG.jpg/revision/latest" \
  "$W/c/c8/CoruscantLimited.jpg/revision/latest"
download "$ART/Set-reflections-iii.jpg" \
  "$W/4/48/Reflections_III.png/revision/latest"
download "$ART/Set-theed-palace.jpg" \
  "$W/3/35/SW_CCG_Theed_Palace.png/revision/latest"

# If a download missed, reuse Premiere box so tiles are never broken.
fallback="$ART/Set-premiere-limited.jpg"
for f in "$ART"/Set-*.jpg; do
  [ -s "$f" ] || { [ -s "$fallback" ] && cp "$fallback" "$f" && echo "fallback $(basename "$f")"; }
done

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d
docker cp "$ART" swccg_wiki:/tmp/set-art
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="Wookieepedia set product art" --overwrite /tmp/set-art \
  || docker exec swccg_wiki php maintenance/importImages.php --user=Admin --overwrite /tmp/set-art || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images

edit() {
  local title="$1" file="$2"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="layout/expansions" "$title" < "$file"
}

edit "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki"
edit "MediaWiki:Common.js" "$PAGES/MediaWiki_Common.js.wiki"
edit "MediaWiki:Sidebar" "$PAGES/MediaWiki_Sidebar.wiki"
edit "Main Page" "$PAGES/Main_Page.wiki"
edit "Sets" "$PAGES/Sets.wiki"
python3 "$ROOT/import_set_pages.py"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec swccg_wiki php maintenance/run.php purgePage --namespace=0 "Main Page" || true
echo "layout+expansions done"
curl -sI -m 8 https://wiki.swccg.com/wiki/Main_Page | head -8
