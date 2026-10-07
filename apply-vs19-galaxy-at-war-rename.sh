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
p.write_bytes(b)
n=sum(1 for c in b.decode("utf-8") if ord(c)>127)
print(f"  {p.name} nonascii={n}")
assert n==0, p
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip "$file"
  echo "edit: $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

echo "== moveBatch Virtual Set 19 (Cancelled) -> Virtual Set 19: Galaxy At War =="
python3 - <<'PY'
import urllib.request, urllib.parse, json
def exists(title):
  url = "https://wiki.swccg.com/api.php?" + urllib.parse.urlencode({"action":"query","titles":title,"format":"json"})
  data = json.load(urllib.request.urlopen(url, timeout=60))
  pages = data["query"]["pages"]
  for p in pages.values():
    if "missing" in p:
      return False
  return True
old_ok = exists("Virtual Set 19 (Cancelled)")
new_ok = exists("Virtual Set 19: Galaxy At War")
print(f"exists old={old_ok} new={new_ok}")
need = "1" if (old_ok and not new_ok) else "0"
# If old exists and new missing, move. If both exist, skip move.
open("/tmp/vs19-move-needed","w").write(need)
PY
NEED=$(cat /tmp/vs19-move-needed)
if [ "$NEED" = "1" ]; then
  printf '%s\n' 'Virtual Set 19 (Cancelled)|Virtual Set 19: Galaxy At War' > /tmp/vs19-move.txt
  docker cp /tmp/vs19-move.txt swccg_wiki:/tmp/vs19-move.txt
  docker exec swccg_wiki php maintenance/run.php moveBatch \
    --u=Admin \
    --r="Bill/Chief 2026-09-24: rename to Virtual Set 19: Galaxy At War" \
    /tmp/vs19-move.txt 2>&1 | tail -30
else
  echo "moveBatch skipped (already renamed or new exists); will edit hub + redirect"
fi

echo "== edit hub + redirect + inbound =="
edit "Virtual Set 19: Galaxy At War" "$PAGES/Virtual_Set_19_Galaxy_At_War.wiki" "Bill/Chief: retitle hub Virtual Set 19: Galaxy At War (cancelled/unreleased)"
edit "Virtual Set 19 (Cancelled)" "$PAGES/Virtual_Set_19_(Cancelled).wiki" "Redirect to Virtual Set 19: Galaxy At War"
edit "Main Page" "$PAGES/Main_Page.wiki" "VO tile: Virtual Set 19: Galaxy At War (Cancelled)"
edit "Virtual Set 18 (Re-organized)" "$PAGES/Virtual_Set_18_(Re-organized).wiki" "Link -> Virtual Set 19: Galaxy At War"
edit "Cancelled Virtual Sets" "$PAGES/Cancelled_Virtual_Sets.wiki" "Link VS19 hub Virtual Set 19: Galaxy At War"
edit "Virtual Sets (2002-2009)" "$PAGES/Virtual_Sets_(2002-2009).wiki" "Link Galaxy At War -> renamed VS19 hub"
edit "2009 Virtual Block Reorganization" "$PAGES/2009_Virtual_Block_Reorganization.wiki" "Link Galaxy At War -> renamed VS19 hub"

echo "== surgical hatnote patch: modern Virtual Set 19 =="
python3 - <<'PY'
import subprocess, tempfile, os
from pathlib import Path

# getText from container
raw = subprocess.check_output(
    ["docker", "exec", "swccg_wiki", "php", "maintenance/run.php", "getText", "Virtual Set 19"],
    text=True,
)
old = ":''Not to be confused with the unreleased Original-era plan '''Virtual Set 19: Galaxy at War''' &mdash; see [[Cancelled Virtual Sets]].''"
new = ":''Not to be confused with the unreleased Original-era plan '''[[Virtual Set 19: Galaxy At War]]''' (cancelled) &mdash; see also [[Cancelled Virtual Sets]].''"
if old not in raw:
    # tolerate already patched
    if "[[Virtual Set 19: Galaxy At War]]" in raw.splitlines()[0]:
        print("modern VS19 hatnote already patched")
        raise SystemExit(0)
    raise SystemExit("modern VS19 hatnote pattern miss:\n" + "\n".join(raw.splitlines()[:3]))
patched = raw.replace(old, new, 1)
path = Path("/tmp/Virtual_Set_19_hatnote.wiki")
path.write_bytes(patched.encode("utf-8"))
print("patched bytes", path.stat().st_size, "first:", patched.splitlines()[0][:120])
subprocess.check_call([
    "docker", "cp", str(path), "swccg_wiki:/tmp/Virtual_Set_19_hatnote.wiki"
])
# edit via stdin from host file
with open(path, "rb") as f:
    subprocess.run(
        ["docker", "exec", "-i", "swccg_wiki", "php", "maintenance/run.php", "edit",
         "--user=Admin",
         "--summary=Hatnote -> Virtual Set 19: Galaxy At War (cancelled)",
         "Virtual Set 19"],
        input=f.read(),
        check=True,
    )
print("modern VS19 hatnote edit OK")
PY

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

echo "== purgePage =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 19: Galaxy At War
Virtual Set 19 (Cancelled)
Main Page
Virtual Set 18 (Re-organized)
Cancelled Virtual Sets
Cancelled Expansions
Virtual Sets (2002-2009)
2009 Virtual Block Reorganization
Virtual Set 19
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, json, urllib.parse
def api(**kw):
  return json.load(urllib.request.urlopen("https://wiki.swccg.com/api.php?"+urllib.parse.urlencode({**kw,"format":"json"}), timeout=60))

q=api(action="query", titles="Virtual Set 19: Galaxy At War|Virtual Set 19 (Cancelled)|Main Page|Virtual Set 19", prop="info|revisions", rvprop="content", rvslots="main")
for pid,p in q["query"]["pages"].items():
  title=p.get("title")
  missing="missing" in p
  redir="redirect" in p
  print("PAGE", title, "missing" if missing else ("redirect" if redir else "ok"), "len", p.get("length"))
  if title=="Main Page" and not missing:
    c=p["revisions"][0]["slots"]["main"]["*"]
    assert "Virtual Set 19: Galaxy At War (Cancelled)" in c, "Main tile label missing"
    assert "[[Virtual Set 19: Galaxy At War|" in c, "Main tile link missing"
    print("Main Page tile OK")
  if title=="Virtual Set 19" and not missing:
    c=p["revisions"][0]["slots"]["main"]["*"]
    assert "[[Virtual Set 19: Galaxy At War]]" in c.splitlines()[0], c.splitlines()[0]
    print("modern hatnote OK")

q2=api(action="query", titles="Virtual Set 19 (Cancelled)", redirects=1, prop="info")
print("REDIRECTS", q2["query"].get("redirects"))
print("RESOLVED", [(p.get("title"), p.get("pageid")) for p in q2["query"]["pages"].values()])

for u in [
 "https://wiki.swccg.com/wiki/Virtual_Set_19:_Galaxy_At_War",
 "https://wiki.swccg.com/wiki/Virtual_Set_19_(Cancelled)",
]:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print("HEAD", r.status, u, "final", r.geturl())

fr=api(action="query", titles="Virtual Set 19: Galaxy At War|Main Page", prop="flagged|info")
for pid,p in fr["query"]["pages"].items():
  fl=p.get("flagged",{})
  print("FR", p["title"], "stable", fl.get("stable_revid"), "last", p.get("lastrevid"), "pending", fl.get("pending_since"))

print("VS19 GALAXY AT WAR RENAME APPLY OK")
PY
