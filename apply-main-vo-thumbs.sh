#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES=$ROOT/pages

strip() {
  python3 - <<PY
from pathlib import Path
p=Path("$1")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"): b=b[3:]
b=b.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
p.write_bytes(b)
n=sum(1 for c in b.decode("utf-8") if ord(c)>127)
print(f"  {p.name} nonascii={n} bytes={len(b)}")
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip "$file"
  echo "edit: $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "Main Page" "$PAGES/Main_Page.wiki" "VO thumbs: vertical pack facsimiles VS1-17+Defensive Shields; add VS18 Re-organized + VS19 Cancelled tiles"
edit "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki" "set-tile-vert: show vertical pack facsimiles without banner crop"
edit "Virtual Set 18 (Re-organized)" "$PAGES/Virtual_Set_18_(Re-organized).wiki" "stub: Original Fifth Anthology / VS18 reorganized into Reflections IV (not cancelled like VS19)"
edit "Virtual Set 19 (Cancelled)" "$PAGES/Virtual_Set_19_(Cancelled).wiki" "stub: Original Galaxy at War unreleased (niewydany)"
edit "Virtual Set 18 (Cancelled)" "$PAGES/Virtual_Set_18_(Cancelled).wiki" "redirect to Virtual Set 18 (Re-organized) — VS18 was reorg not cancel"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "== purgePage =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Main Page
MediaWiki:Common.css
Virtual Set 18 (Re-organized)
Virtual Set 19 (Cancelled)
Virtual Set 18 (Cancelled)
Defensive Shields
Cancelled Virtual Sets
2009 Virtual Block Reorganization
File:VS1-Legacy-pack.png
File:VS2O-pack.png
File:PS1-DefensiveShields-pack.png
PURGE

# bump cache epoch so CSS hits
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import re
p = Path("/opt/swccg-wiki/extra-settings.php")
if not p.is_file():
    print("no extra-settings.php; skip epoch")
else:
    t = p.read_text()
    new = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    pat = re.compile(r"\$wgCacheEpoch\s*=\s*'[^']*';")
    if pat.search(t):
        p.write_text(pat.sub(f"$wgCacheEpoch = '{new}';", t, count=1))
        print(f"epoch bumped to {new}")
    else:
        print("WARNING: no \$wgCacheEpoch")
PY

if [ -f /opt/swccg-wiki/docker-compose.yml ]; then
  (cd /opt/swccg-wiki && docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d wiki) || true
  sleep 3
fi

python3 - <<'PY'
import urllib.request, subprocess, re
main = subprocess.check_output(
    ["docker","exec","swccg_wiki","php","maintenance/run.php","getText","Main Page"],
    text=True, errors="replace")
vo = re.search(r"== Virtual Original.*?== Virtual Legacy", main, re.S)
assert vo, "no VO"
vo = vo.group(0)
checks = [
    ("VS1-Legacy-pack", "VS1-Legacy-pack.png" in vo),
    ("VS2O-pack", "VS2O-pack.png" in vo),
    ("PS1 pack", "PS1-DefensiveShields-pack.png" in vo),
    ("Defensive link", "link=Defensive Shields" in vo),
    ("no Premium label", "Premium Set 1" not in vo),
    ("no title banners", "Set-VS1O-title" not in vo and "Set-PS1-title" not in vo),
    ("VS18 Re-organized", "Virtual Set 18 (Re-organized)" in vo),
    ("VS19 Cancelled", "Virtual Set 19 (Cancelled)" in vo),
    ("20 tiles", len(__import__("re").findall(r'class="set-tile[^\"]*"', vo)) == 20),
    ("vert class", "set-tile-vert" in vo),
]
for name, ok in checks:
    print(("PASS" if ok else "FAIL"), name)
assert all(ok for _, ok in checks)

# live HTTP
for u, needles in [
    ("https://wiki.swccg.com/wiki/Main_Page", ["VS1-Legacy-pack", "PS1-DefensiveShields-pack", "Virtual Set 18 (Re-organized)", "Virtual Set 19 (Cancelled)", "Defensive Shields"]),
    ("https://wiki.swccg.com/wiki/Virtual_Set_18_(Re-organized)", ["Fifth Anthology", "Re-organized", "2009 Virtual Block Reorganization"]),
    ("https://wiki.swccg.com/wiki/Virtual_Set_19_(Cancelled)", ["Galaxy at War", "niewydany", "Cancelled Virtual Sets"]),
    ("https://wiki.swccg.com/wiki/Virtual_Set_18_(Cancelled)", ["Re-organized"]),
]:
    req = urllib.request.Request(u, headers={"Cache-Control":"no-cache","Pragma":"no-cache","User-Agent":"Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8","replace")
    miss = [n for n in needles if n not in html]
    print(("PASS" if not miss else "FAIL"), u, "miss="+str(miss))
    if miss:
        raise SystemExit(1)
print("MAIN VO THUMBS APPLY OK")
PY
