#!/bin/bash
set -u
ART=/opt/swccg-wiki/set-art-boxes
mkdir -p "$ART"
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
W='https://static.wikia.nocookie.net/starwars/images'

to_jpg() {
  python3 - "$1" "$2" <<'PY'
import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
Image.open(src).convert("RGB").save(dst, "JPEG", quality=90)
print("jpg", dst)
PY
}

get() {
  local dest="$1" url="$2"
  echo "GET $dest"
  if curl -fsSL -A "$UA" -e 'https://starwars.fandom.com/' --max-time 30 -o "$dest.tmp" "$url"; then
    sz=$(wc -c < "$dest.tmp")
    if [ "$sz" -gt 8000 ]; then
      to_jpg "$dest.tmp" "$dest"
      rm -f "$dest.tmp"
      return 0
    fi
  fi
  rm -f "$dest.tmp"
  echo "FAIL $dest"
  return 1
}

# User-specified images
get "$ART/Set-premiere-2p.jpg" \
  "https://cf.geekdo-images.com/rqqwPQg_-PcE8YUAe0s71Q__opengraph/img/geyEiIpny-ewk2kTx4AOqn075Bs=/fit-in/1200x630/filters:strip_icc()/pic3456072.jpg"
get "$ART/Set-a-new-hope.jpg" \
  "https://storage.googleapis.com/images.pricecharting.com/ht2p4ou2oqnfgekg/1600.jpg"

# Packs (keep existing boxes)
get "$ART/Set-a-new-hope-pack.jpg" \
  "$W/6/64/ANH_CCG_Limited_pack.jpg/revision/latest"
get "$ART/Set-premiere-limited-pack.jpg" \
  "$W/e/e4/SWCCG-PremiereLimitedBox.jpg/revision/latest"
# If that was a box, try pack-like names
get "$ART/Set-hoth-pack.jpg" \
  "$W/5/54/Hoth_unlimited.jpg/revision/latest" || true
get "$ART/Set-death-star-ii-pack.jpg" \
  "$W/3/38/DeathStarIILimitedExpansionPack.jpg/revision/latest" || true
get "$ART/Set-endor-pack.jpg" \
  "$W/9/91/Clip-123842686.png/revision/latest" || true
get "$ART/Set-jabbas-palace-pack.jpg" \
  "$W/6/60/JabbasPalaceLimitedExpansionSet.jpg/revision/latest" || true
get "$ART/Set-cloud-city-pack.jpg" \
  "$W/3/35/CloudCity_CCG.jpg/revision/latest" || true
get "$ART/Set-special-edition-pack.jpg" \
  "$W/1/17/51p5KGdwsqL.jpg/revision/latest" || true
get "$ART/Set-dagobah-pack.jpg" \
  "$W/4/40/Dagobah_CCG_box.jpg/revision/latest" || true
get "$ART/Set-tatooine-pack.jpg" \
  "$W/6/65/SW_CCG_Tatooine.png/revision/latest" || true
get "$ART/Set-coruscant-pack.jpg" \
  "$W/f/f8/Coruscant_CCG_box.jpg/revision/latest" || true
get "$ART/Set-theed-palace-pack.jpg" \
  "$W/3/35/SW_CCG_Theed_Palace.png/revision/latest" || true
get "$ART/Set-premiere-unlimited-pack.jpg" \
  "$W/2/2a/SWCCG-PremiereUnlimitedBox.jpg/revision/latest" || true

# Owner DS2 Light Side starter
if [ -s "/opt/swccg-wiki/SWCCG-DS2-LS-starter.jpg" ]; then
  to_jpg "/opt/swccg-wiki/SWCCG-DS2-LS-starter.jpg" "$ART/Set-ds2-starter-ls.jpg"
fi
if [ -s "/opt/swccg-wiki/Set-ds2-starter-ds.jpg" ] || [ -s "/opt/swccg-wiki/SWCCG-DS2-DS-starter.jpg" ]; then
  if [ -s "/opt/swccg-wiki/SWCCG-DS2-DS-starter.jpg" ]; then
    to_jpg "/opt/swccg-wiki/SWCCG-DS2-DS-starter.jpg" "$ART/Set-ds2-starter-ds.jpg"
  fi
fi

# Side-by-side composite for Main Page / infobox (Dark then Light)
python3 - <<'PY'
from PIL import Image
from pathlib import Path
art = Path("/opt/swccg-wiki/set-art-boxes")
ds = art / "Set-ds2-starter-ds.jpg"
ls = art / "Set-ds2-starter-ls.jpg"
if not ds.exists() or not ls.exists():
    print("missing starter stills", ds.exists(), ls.exists())
    raise SystemExit(0)
a = Image.open(ds).convert("RGB")
b = Image.open(ls).convert("RGB")
h = max(a.height, b.height)
def fit_h(im, h):
    w = max(1, int(im.width * h / im.height))
    return im.resize((w, h), Image.Resampling.LANCZOS)
a = fit_h(a, h)
b = fit_h(b, h)
w = max(a.width, b.width)
def pad(im, w, h):
    c = Image.new("RGB", (w, h), (16, 16, 16))
    c.paste(im, ((w - im.width) // 2, 0))
    return c
a = pad(a, w, h)
b = pad(b, w, h)
gap = 16
out = Image.new("RGB", (w * 2 + gap, h), (16, 16, 16))
out.paste(a, (0, 0))
out.paste(b, (w + gap, 0))
dest = art / "Set-ds2-starters.jpg"
out.save(dest, "JPEG", quality=90)
print("composite", dest, out.size, dest.stat().st_size)
PY

# Place hashed files (do NOT touch Set-premiere-limited.jpg)
python3 - <<'PY'
import hashlib, subprocess
from pathlib import Path
art = Path("/opt/swccg-wiki/set-art-boxes")
skip = {"Set-premiere-limited.jpg"}
for p in sorted(art.glob("Set-*.jpg")):
    if p.name in skip:
        print("skip", p.name)
        continue
    h = hashlib.md5(p.name.encode()).hexdigest()
    dest = f"/var/www/html/images/{h[0]}/{h[:2]}/{p.name}"
    subprocess.run(["docker", "exec", "swccg_wiki", "mkdir", "-p", f"/var/www/html/images/{h[0]}/{h[:2]}"], check=False)
    subprocess.run(["docker", "cp", str(p), f"swccg_wiki:{dest}"], check=False)
    subprocess.run(["docker", "exec", "swccg_wiki", "bash", "-c",
                    f"rm -rf /var/www/html/images/thumb/{h[0]}/{h[:2]}/{p.name}"], check=False)
    print("placed", p.name, p.stat().st_size)
PY
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images

# Import only new/changed files, not the Premiere Limited owner box
mkdir -p /tmp/set-import
find "$ART" -maxdepth 1 -name 'Set-*.jpg' ! -name 'Set-premiere-limited.jpg' -exec cp {} /tmp/set-import/ \;
docker cp /tmp/set-import swccg_wiki:/tmp/set-import
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --overwrite /tmp/set-import || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="set-pair css" "MediaWiki:Common.css" < /opt/swccg-wiki/pages/MediaWiki_Common.css.wiki
python3 /opt/swccg-wiki/import_set_pages.py
python3 - <<'PY'
from pathlib import Path
import importlib.util
spec = importlib.util.spec_from_file_location("isp", "/opt/swccg-wiki/import_set_pages.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
article = mod.PAGES["Premiere Limited"]
thumbs = Path("/opt/swccg-wiki/premiere-thumbs.wiki").read_text(encoding="utf-8")
if "[[Category:Decipher sets]]" in article:
    article = article.replace("[[Category:Decipher sets]]", thumbs + "\n[[Category:Decipher sets]]\n")
else:
    article += "\n" + thumbs
Path("/tmp/premiere-limited.wiki").write_text(article, encoding="utf-8")
print("premiere chars", len(article))
PY
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="keep thumbs" "Premiere Limited" < /tmp/premiere-limited.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf 'Main Page\nDeath Star II Starter Decks\nA New Hope\nPremiere Two-Player Introductory Game\nFile:Set-ds2-starters.jpg\nFile:Set-ds2-starter-ls.jpg\nFile:Set-premiere-2p.jpg\nFile:Set-a-new-hope.jpg\n' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo set-photos done
