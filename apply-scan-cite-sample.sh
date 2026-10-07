#!/bin/bash
# One-page Cite sample: scan image [1] → References. Do not roll out.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
TITLE="2014 Worlds Day 3 Matthew Harrison-Trainor LS Communing"
PAGE="$ROOT/pages/2014_Worlds_Day_3_Matthew_Harrison-Trainor_LS_Communing.wiki"
if [ ! -f "$PAGE" ]; then
  echo "ERROR: missing $PAGE" >&2
  exit 1
fi

python3 - "$PAGE" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
if not text.endswith("\n"):
    text += "\n"
p.write_text(text, encoding="utf-8", newline="\n")
print("normalized", p, "bytes", p.stat().st_size)
if "<ref>" not in text:
    raise SystemExit("local page missing <ref>")
PY

echo "== edit =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Scan Cite [1] beside the image (sample, one page)" \
  "$TITLE" < "$PAGE"

echo "== getText =="
docker exec swccg_wiki php maintenance/run.php getText "$TITLE" > /tmp/scan-cite-gettext.txt
python3 - <<'PY'
from pathlib import Path
t = Path("/tmp/scan-cite-gettext.txt").read_text(encoding="utf-8")
if "<ref>" not in t:
    raise SystemExit("GETTEXT_FAIL no <ref>")
if "Page 5 of [[:File:2014 Worlds Day 3.pdf]]" not in t:
    raise SystemExit("GETTEXT_FAIL missing colon-File ref")
scan = t.split("== Scan ==", 1)[1].split("== See also ==", 1)[0]
if "Page 5 of" in scan.split("<ref>", 1)[0]:
    raise SystemExit("GETTEXT_FAIL caption still in Scan body")
print("GETTEXT_OK")
print(scan)
PY

echo "== FlaggedRevs this page =="
docker cp "$ROOT/ReviewScanCite.php" swccg_wiki:/var/www/html/maintenance/ReviewScanCite.php
docker exec swccg_wiki php maintenance/run.php ReviewScanCite

echo "== purge =="
printf '%s\n' "$TITLE" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true

echo "== localhost raw/html =="
docker exec swccg_wiki curl -sS -H "Cache-Control: no-cache" \
  "http://localhost/wiki/2014_Worlds_Day_3_Matthew_Harrison-Trainor_LS_Communing?action=raw" \
  > /tmp/scan-cite-raw.txt
python3 - <<'PY'
from pathlib import Path
t = Path("/tmp/scan-cite-raw.txt").read_text(encoding="utf-8")
if "<ref>" not in t:
    raise SystemExit("LOCALHOST_RAW_FAIL no <ref>")
print("LOCALHOST_RAW_OK", "bytes", len(t))
PY
docker exec swccg_wiki curl -sS -H "Cache-Control: no-cache" \
  "http://localhost/wiki/2014_Worlds_Day_3_Matthew_Harrison-Trainor_LS_Communing" \
  > /tmp/scan-cite-html.txt
python3 - <<'PY'
from pathlib import Path
import re
html = Path("/tmp/scan-cite-html.txt").read_text(encoding="utf-8", errors="replace")
# public HTML should have a Cite [1] and the PDF line only in References
has_ref = 'class="reference"' in html or ">[1]<" in html or ">1<" in html and "mw-references" in html
has_cite = bool(re.search(r'id="cite_ref[^"]*"', html)) or "mw-references-wrap" in html or 'class="references"' in html
scan = html[html.find('id="Scan"'): html.find('id="See_also"') if 'id="See_also"' in html else html.find('id="Sources"')]
print("HTML cite", has_cite, "body_caption_in_scan", "Page 5 of" in scan)
print("---SCAN---")
print(scan[:2500])
if "Page 5 of" in scan:
    raise SystemExit("LOCALHOST_HTML_FAIL Scan still has Page 5 caption")
if not has_cite and "[1]" not in html:
    raise SystemExit("LOCALHOST_HTML_FAIL no Cite [1]")
if re.search(r"</figure>\s*<p>\s*<sup[^>]*cite_ref", scan):
    raise SystemExit("LOCALHOST_HTML_FAIL [1] still under the image")
if "cite_ref" not in scan and "cite&#95;ref" not in scan:
    raise SystemExit("LOCALHOST_HTML_FAIL no [1] in Scan")
if "<td" not in scan.lower() and "<table" not in scan.lower():
    raise SystemExit("LOCALHOST_HTML_FAIL Scan is not a side-by-side table")
oldid = re.search(r"oldid=(\d+)", html)
print("oldid", oldid.group(1) if oldid else "?")
print("LOCALHOST_HTML_OK")
PY
echo APPLY-SCAN-CITE-SAMPLE-DONE
