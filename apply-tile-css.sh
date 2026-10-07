#!/bin/bash
# CSS-only Main Page tile fix + V16/V27 banner re-crop.
# Does NOT edit Main_Page.wiki captions or Set-VB* collage art.
# Never prints /opt/swccg-wiki/.env
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

CSS_SRC="$PAGES/MediaWiki_Common.css.wiki"
if [ ! -s "$CSS_SRC" ]; then
  echo "ERROR: missing $CSS_SRC" >&2
  exit 1
fi

echo "== edit MediaWiki:Common.css =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="set-tile wrap + mobile header min-width" \
  "MediaWiki:Common.css" < "$CSS_SRC"

echo "== re-crop Set-V16-title.jpg + Set-V27-title.jpg =="
python3 - <<'PY'
from pathlib import Path
import importlib.util
from PIL import Image

ROOT = Path("/opt/swccg-wiki")
spec = importlib.util.spec_from_file_location("cvb", str(ROOT / "crop_virtual_banners.py"))
cvb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvb)

def stats(im: Image.Image):
    mean, std = cvb._luma_stats(im)
    return mean, std

stage = ROOT / "set-art-virtual-cropped"
stage.mkdir(parents=True, exist_ok=True)
upload = Path("/tmp/set-tile-banners")
upload.mkdir(parents=True, exist_ok=True)

for name in ("Set-V16-title", "Set-V27-title"):
    src = ROOT / "set-art-virtual" / f"{name}.gif"
    if not src.is_file():
        raise SystemExit(f"missing source {src}")
    im = Image.open(src)
    cropped = cvb.crop_strip(im)
    mean0, std0 = stats(cropped)
    out = cvb.maybe_collage_fallback(cropped, src.name)
    mean, std = stats(out)
    method = "collage" if abs(mean - mean0) > 0.05 or abs(std - std0) > 0.05 else "maxvar/letterbox"
    dest = stage / f"{name}.jpg"
    # Preserve a previously staged collage if new crop is tiny (e.g. V27 REVII white crop ~9k)
    if dest.is_file() and dest.stat().st_size >= 30000:
        import io
        buf = io.BytesIO(); out.save(buf, "JPEG", quality=92)
        if len(buf.getvalue()) < 15000:
            print(f"{name}: keeping existing staged collage ({dest.stat().st_size} B) over tiny crop")
            import shutil
            shutil.copy2(dest, upload / f"{name}.jpg")
            mean, std = stats(Image.open(dest))
            print(f"{name}: preserved mean={mean:.1f} stdev={std:.1f} bytes={dest.stat().st_size}")
            continue
    out.save(dest, "JPEG", quality=92)
    out.save(upload / f"{name}.jpg", "JPEG", quality=92)
    print(f"{name}: {method} mean={mean:.1f} stdev={std:.1f} bytes={dest.stat().st_size} (pre mean={mean0:.1f} stdev={std0:.1f})")
print("staged", upload)
PY

docker exec swccg_wiki rm -rf /tmp/set-tile-banners
docker cp /tmp/set-tile-banners swccg_wiki:/tmp/set-tile-banners
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="V16/V27 title crop fix" --overwrite /tmp/set-tile-banners \
  || docker exec swccg_wiki php maintenance/importImages.php --user=Admin --overwrite /tmp/set-tile-banners || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge Main Page + Common.css + File pages =="
printf '%s\n' \
  'Main Page' \
  'MediaWiki:Common.css' \
  'File:Set-V16-title.jpg' \
  'File:Set-V27-title.jpg' \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true

echo "== bump \$wgCacheEpoch + restart wiki =="
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import re
p = Path("/opt/swccg-wiki/extra-settings.php")
t = p.read_text()
new = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
pat = re.compile(r"\$wgCacheEpoch\s*=\s*'[^']*';")
if pat.search(t):
    p.write_text(pat.sub(f"$wgCacheEpoch = '{new}';", t, count=1))
    print(f"epoch bumped to {new}")
else:
    print("WARNING: $wgCacheEpoch line not found; skip bump")
PY

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d wiki
sleep 4

echo "== apply-tile-css done =="
