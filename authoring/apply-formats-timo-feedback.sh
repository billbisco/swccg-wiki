#!/bin/bash
# Apply Bill feedback: full standings, hover fix, alt decks, player stubs, write-up.
# VPS only; no git remote. Never prints /opt/swccg-wiki/.env
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

edit() {
  local title="$1"; local file="$2"; local summary="$3"
  if [ ! -s "$file" ]; then echo "ERROR: missing $file" >&2; exit 1; fi
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

python3 - <<'PY'
from pathlib import Path
import re
p = Path('/opt/swccg-wiki/extra-settings.php')
t = p.read_text(encoding='utf-8')
epoch = '20260923203633'
t2, n = re.subn(r"\$wgCacheEpoch\s*=\s*'[^']*';", "$wgCacheEpoch = '%s';" % epoch, t, count=1)
if not n:
    raise SystemExit('CacheEpoch not found')
p.write_text(t2, encoding='utf-8')
print('CacheEpoch set', epoch)
PY

edit "MediaWiki:Common.js" "$PAGES/MediaWiki_Common.js.wiki" "Common.js: clear #swccg-card-zoom src before load so Firefox never flashes previous card"
edit "2026 Retro GEMP Match Play Championship (Premiere to DSII)" "$PAGES/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki" "Full #1-#50 standings; Challonge/forum details; descriptive write-up; player stub links"
edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations.wiki" "Cross-link picture and two-column alternate layouts; link Timo stub"
edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)" "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations_(picture_layout).wiki" "Alternate decklist: inline card pictures (test)"
edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)" "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations_(two-column_layout).wiki" "Alternate decklist: two-column text layout"

edit "Timo Dusel" "$PAGES/Timo_Dusel.wiki" "Player stub: Timo Dusel at 2026 Retro GEMPC; cite PC news"
edit "Jonny Chu" "$PAGES/Jonny_Chu.wiki" "Player stub: Jonny Chu at 2026 Retro GEMPC; cite PC news"
edit "Jeremy Christoffel" "$PAGES/Jeremy_Christoffel.wiki" "Player stub: Jeremy Christoffel at 2026 Retro GEMPC; cite PC news"
edit "Kevin Bing" "$PAGES/Kevin_Bing.wiki" "Player stub: Kevin Bing at 2026 Retro GEMPC; cite PC news"
edit "Ian Monteith" "$PAGES/Ian_Monteith.wiki" "Player stub: Ian Monteith at 2026 Retro GEMPC; cite PC news"
edit "Bill Bisco" "$PAGES/Bill_Bisco.wiki" "Player stub: Bill Bisco at 2026 Retro GEMPC; cite PC news"
edit "Brad Kippel" "$PAGES/Brad_Kippel.wiki" "Player stub: Brad Kippel at 2026 Retro GEMPC; cite PC news"
edit "Will Tarbox" "$PAGES/Will_Tarbox.wiki" "Player stub: Will Tarbox at 2026 Retro GEMPC; cite PC news"
edit "David Garcia" "$PAGES/David_Garcia.wiki" "Player stub: David Garcia at 2026 Retro GEMPC; cite PC news"
edit "Joe Horbey" "$PAGES/Joe_Horbey.wiki" "Player stub: Joe Horbey at 2026 Retro GEMPC; cite PC news"
edit "Evan Coupland" "$PAGES/Evan_Coupland.wiki" "Player stub: Evan Coupland at 2026 Retro GEMPC; cite PC news"
edit "Alex Prodoehl" "$PAGES/Alex_Prodoehl.wiki" "Player stub: Alex Prodoehl at 2026 Retro GEMPC; cite PC news"
edit "Andrew Bethell" "$PAGES/Andrew_Bethell.wiki" "Player stub: Andrew Bethell at 2026 Retro GEMPC; cite PC news"
edit "Matthew Ford" "$PAGES/Matthew_Ford.wiki" "Player stub: Matthew Ford at 2026 Retro GEMPC; cite PC news"
edit "Garrett Larson" "$PAGES/Garrett_Larson.wiki" "Player stub: Garrett Larson at 2026 Retro GEMPC; cite PC news"
edit "Chris Madaio" "$PAGES/Chris_Madaio.wiki" "Player stub: Chris Madaio at 2026 Retro GEMPC; cite PC news"
edit "Patrick Johnson" "$PAGES/Patrick_Johnson.wiki" "Player stub: Patrick Johnson at 2026 Retro GEMPC; cite PC news"
edit "Kendall Halman" "$PAGES/Kendall_Halman.wiki" "Player stub: Kendall Halman at 2026 Retro GEMPC; cite PC news"
edit "Tony Petersson" "$PAGES/Tony_Petersson.wiki" "Player stub: Tony Petersson at 2026 Retro GEMPC; cite PC news"
edit "Charlie Hickey" "$PAGES/Charlie_Hickey.wiki" "Player stub: Charlie Hickey at 2026 Retro GEMPC; cite PC news"
edit "Matt Simpson" "$PAGES/Matt_Simpson.wiki" "Player stub: Matt Simpson at 2026 Retro GEMPC; cite PC news"
edit "Jeff Anderson" "$PAGES/Jeff_Anderson.wiki" "Player stub: Jeff Anderson at 2026 Retro GEMPC; cite PC news"
edit "Ben Lindstrom" "$PAGES/Ben_Lindstrom.wiki" "Player stub: Ben Lindstrom at 2026 Retro GEMPC; cite PC news"
edit "Geoffrey Mikulka" "$PAGES/Geoffrey_Mikulka.wiki" "Player stub: Geoffrey Mikulka at 2026 Retro GEMPC; cite PC news"
edit "Robert Waldon" "$PAGES/Robert_Waldon.wiki" "Player stub: Robert Waldon at 2026 Retro GEMPC; cite PC news"
edit "Jarrett McBride" "$PAGES/Jarrett_McBride.wiki" "Player stub: Jarrett McBride at 2026 Retro GEMPC; cite PC news"
edit "Brandon Wargo" "$PAGES/Brandon_Wargo.wiki" "Player stub: Brandon Wargo at 2026 Retro GEMPC; cite PC news"
edit "Adam Radic" "$PAGES/Adam_Radic.wiki" "Player stub: Adam Radic at 2026 Retro GEMPC; cite PC news"
edit "Michael Butler" "$PAGES/Michael_Butler.wiki" "Player stub: Michael Butler at 2026 Retro GEMPC; cite PC news"
edit "Phil Clark" "$PAGES/Phil_Clark.wiki" "Player stub: Phil Clark at 2026 Retro GEMPC; cite PC news"
edit "Randy Scott" "$PAGES/Randy_Scott.wiki" "Player stub: Randy Scott at 2026 Retro GEMPC; cite PC news"
edit "Steve Sanders" "$PAGES/Steve_Sanders.wiki" "Player stub: Steve Sanders at 2026 Retro GEMPC; cite PC news"
edit "Christian Deibler" "$PAGES/Christian_Deibler.wiki" "Player stub: Christian Deibler at 2026 Retro GEMPC; cite PC news"
edit "Zachary Behm" "$PAGES/Zachary_Behm.wiki" "Player stub: Zachary Behm at 2026 Retro GEMPC; cite PC news"
edit "Matthew Tennyson" "$PAGES/Matthew_Tennyson.wiki" "Player stub: Matthew Tennyson at 2026 Retro GEMPC; cite PC news"
edit "Phil Jasper" "$PAGES/Phil_Jasper.wiki" "Player stub: Phil Jasper at 2026 Retro GEMPC; cite PC news"
edit "Mike Adamson" "$PAGES/Mike_Adamson.wiki" "Player stub: Mike Adamson at 2026 Retro GEMPC; cite PC news"
edit "Brandon Price" "$PAGES/Brandon_Price.wiki" "Player stub: Brandon Price at 2026 Retro GEMPC; cite PC news"
edit "John Heft" "$PAGES/John_Heft.wiki" "Player stub: John Heft at 2026 Retro GEMPC; cite PC news"
edit "Robert Gravel" "$PAGES/Robert_Gravel.wiki" "Player stub: Robert Gravel at 2026 Retro GEMPC; cite PC news"
edit "Cedric Perugini" "$PAGES/Cedric_Perugini.wiki" "Player stub: Cedric Perugini at 2026 Retro GEMPC; cite PC news"
edit "Carter Vencill" "$PAGES/Carter_Vencill.wiki" "Player stub: Carter Vencill at 2026 Retro GEMPC; cite PC news"
edit "Thomas Nguyen" "$PAGES/Thomas_Nguyen.wiki" "Player stub: Thomas Nguyen at 2026 Retro GEMPC; cite PC news"
edit "Matt Blackstock" "$PAGES/Matt_Blackstock.wiki" "Player stub: Matt Blackstock at 2026 Retro GEMPC; cite PC news"
edit "Frank Amore" "$PAGES/Frank_Amore.wiki" "Player stub: Frank Amore at 2026 Retro GEMPC; cite PC news"
edit "Kurt Winter" "$PAGES/Kurt_Winter.wiki" "Player stub: Kurt Winter at 2026 Retro GEMPC; cite PC news"
edit "Joshua Parco" "$PAGES/Joshua_Parco.wiki" "Player stub: Joshua Parco at 2026 Retro GEMPC; cite PC news"
edit "Casey Johnson" "$PAGES/Casey_Johnson.wiki" "Player stub: Casey Johnson at 2026 Retro GEMPC; cite PC news"
edit "Justin McBride" "$PAGES/Justin_McBride.wiki" "Player stub: Justin McBride at 2026 Retro GEMPC; cite PC news"
edit "Scott Lingrell" "$PAGES/Scott_Lingrell.wiki" "Add 2026 Retro GEMPC finish #34 cite PC news"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
python3 - <<'PY'
import subprocess
titles = ['MediaWiki:Common.js', '2026 Retro GEMP Match Play Championship (Premiere to DSII)', '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations', '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)', '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)', 'Timo Dusel', 'Jonny Chu', 'Jeremy Christoffel', 'Kevin Bing', 'Ian Monteith', 'Bill Bisco', 'Brad Kippel', 'Will Tarbox', 'David Garcia', 'Joe Horbey', 'Evan Coupland', 'Alex Prodoehl', 'Andrew Bethell', 'Matthew Ford', 'Garrett Larson', 'Chris Madaio', 'Patrick Johnson', 'Kendall Halman', 'Tony Petersson', 'Charlie Hickey', 'Matt Simpson', 'Jeff Anderson', 'Ben Lindstrom', 'Geoffrey Mikulka', 'Robert Waldon', 'Jarrett McBride', 'Brandon Wargo', 'Adam Radic', 'Michael Butler', 'Phil Clark', 'Randy Scott', 'Steve Sanders', 'Christian Deibler', 'Zachary Behm', 'Matthew Tennyson', 'Phil Jasper', 'Mike Adamson', 'Brandon Price', 'John Heft', 'Robert Gravel', 'Cedric Perugini', 'Carter Vencill', 'Thomas Nguyen', 'Matt Blackstock', 'Frank Amore', 'Kurt Winter', 'Joshua Parco', 'Casey Johnson', 'Justin McBride', 'Scott Lingrell', 'Main Page']
proc = subprocess.run(["docker", "exec", "-i", "swccg_wiki", "php", "maintenance/run.php", "purgePage"], input="\n".join(titles)+"\n", text=True)
print('purge exit', proc.returncode)
PY

echo formats-timo-feedback applied
