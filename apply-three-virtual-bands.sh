#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES=$ROOT/pages
HUBS=$PAGES/set-hubs

strip_bom() {
  python3 - <<PY
from pathlib import Path
p=Path("$1")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"):
  b=b[3:]
p.write_bytes(b)
n=sum(1 for c in b.decode("utf-8") if ord(c)>127)
print(f"  {p.name} nonascii={n}")
if n:
  raise SystemExit(f"non-ascii in {p}")
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit: $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

# Main / index
edit "Main Page" "$PAGES/Main_Page.wiki" "three Virtual bands: Original / Legacy / Modern; dual Shields tiles"
edit "Sets" "$PAGES/Sets.wiki" "Sets index: Original / Legacy / Modern bands"

# Categories (soft; keep Current Virtual + Virtual Legacy names for generators)
edit "Category:Sets" "$PAGES/Category_Sets.wiki" "Sets parent: three Virtual subcats"
edit "Category:Virtual Original sets" "$PAGES/Category_Virtual_Original_sets.wiki" "new: Virtual Original sets category"
edit "Category:Virtual Legacy sets" "$PAGES/Category_Virtual_Legacy_sets.wiki" "Legacy = Blocks+Shields 2009-2014"
edit "Category:Current Virtual sets" "$PAGES/Category_Current_Virtual_sets.wiki" "Current Virtual = Modern; keep generator name"
edit "Category:Virtual Modern sets" "$PAGES/Category_Virtual_Modern_sets.wiki" "soft alias for Current Virtual sets"

# Dual Shields
edit "Virtual Shields (Original)" "$HUBS/Virtual_Shields_(Original).wiki" "Original/Premium Shields hub stub"
edit "Virtual Shields (Legacy)" "$PAGES/Virtual_Shields_(Legacy).wiki" "redirect to Virtual Shields"
edit "Virtual Shields" "$HUBS/Virtual_Shields.wiki" "Legacy Shields hub: cross-link Original"

# Original VS stubs 1-17
for n in $(seq 1 17); do
  edit "Virtual Set ${n} (Original)" "$HUBS/Virtual_Set_${n}_(Original).wiki" "Original era hub stub VS${n}"
done

# Overview light note
edit "Virtual Sets (2002-2009)" "$PAGES/Virtual_Sets_(2002-2009).wiki" "label Virtual Original era"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -3

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Main Page
Sets
Category:Sets
Category:Virtual Original sets
Category:Virtual Legacy sets
Category:Current Virtual sets
Category:Virtual Modern sets
Virtual Shields
Virtual Shields (Original)
Virtual Shields (Legacy)
Virtual Sets (2002-2009)
Virtual Set 1 (Original)
Virtual Set 17 (Original)
EOF

python3 - <<'PY'
from pathlib import Path
import subprocess
checks = [
  "Main Page",
  "Virtual Shields (Original)",
  "Virtual Shields",
  "Category:Virtual Original sets",
  "Virtual Set 1 (Original)",
  "Sets",
]
for title in checks:
  out = subprocess.check_output(
    ["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],
    text=True, errors="replace")
  Path("/tmp/chk.txt").write_text(out, encoding="utf-8")
  t = out
  non = sum(1 for c in t if ord(c)>127)
  moj = any(x in t for x in ["â€","Â·","Ã¢"])
  print(f"{title}: nonascii={non} mojibake={moj} len={len(t)}")
# Main Page band checks
main = subprocess.check_output(
  ["docker","exec","swccg_wiki","php","maintenance/run.php","getText","Main Page"],
  text=True, errors="replace")
for needle in [
  "Virtual Original (2002",
  "Virtual Legacy (2009",
  "Virtual Modern (2014",
  "Virtual Shields (Original)",
  "link=Virtual Shields]]",
  "Set-V27-title",
  "Virtual Set 1 (Original)",
]:
  print("MAIN", needle, needle in main or needle.replace("]]","") in main)
print("MAIN tiles", main.count("set-tile"))
print("SLICE OK")
PY