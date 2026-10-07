#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE_GIF=/tmp/errata-attack-run-pc-gifs
STAGE_PDF=/tmp/errata-attack-run-pc-pdf
HT_BEFORE_EXPECTED=3a3ee5afcd96a081a9ae73b683a4001c93ad862c

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

ht_sha1() {
  docker exec swccg_wiki php maintenance/run.php eval '
$t = Title::newFromText("File:ANH-L-attackrun.gif");
$file = MediaWiki\MediaWikiServices::getInstance()->getRepoGroup()->findFile($t);
if ($file) { echo $file->getSha1() . " size=" . $file->getSize(); }
else { echo "MISSING"; }
' 2>/dev/null | tr -d '\r'
}

echo "== Holotable sha1 BEFORE =="
HT_BEFORE=$(ht_sha1)
echo "ht_before=$HT_BEFORE"
# MediaWiki stores sha1 in base36; API returned hex. Prefer local file hash via docker.
HT_HEX_BEFORE=$(docker exec swccg_wiki php -r '
$t = Title::newFromText ?? null;
' 2>/dev/null || true)
# Resolve actual file path inside container and sha1sum hex
HT_PATH=$(docker exec swccg_wiki php maintenance/run.php eval '
$t = Title::newFromText("File:ANH-L-attackrun.gif");
$file = MediaWiki\MediaWikiServices::getInstance()->getRepoGroup()->findFile($t);
if ($file) { echo $file->getLocalRefPath(); }
' 2>/dev/null | tr -d '\r')
echo "ht_path=$HT_PATH"
if [ -n "$HT_PATH" ] && [ "$HT_PATH" != "" ]; then
  HT_HEX=$(docker exec swccg_wiki sha1sum "$HT_PATH" | awk "{print \$1}")
  echo "ht_hex_before=$HT_HEX"
  echo "$HT_HEX" > /tmp/ht-sha1-before.txt
  if [ "$HT_HEX" != "$HT_BEFORE_EXPECTED" ]; then
    echo "WARN: Holotable hex sha1 $HT_HEX != expected $HT_BEFORE_EXPECTED (continuing; will still verify AFTER matches BEFORE)"
  fi
else
  echo "WARN: could not resolve Holotable path"
fi

echo "== SAFETY: refuse to import Holotable ANH-L-attackrun.gif =="
mkdir -p "$STAGE_GIF" "$STAGE_PDF"
rm -f "$STAGE_GIF"/* "$STAGE_PDF"/*
WB=ANH-L-attackrun-wb-decipher.gif
PDF=SWCCG_2023_AdvancedRulebook.pdf
test -f "$ROOT/set-card-art/$WB"
test -f "$ROOT/media-upload/$PDF"
cp -f "$ROOT/set-card-art/$WB" "$STAGE_GIF/$WB"
cp -f "$ROOT/media-upload/$PDF" "$STAGE_PDF/$PDF"
rm -f "$STAGE_GIF/ANH-L-attackrun.gif" "$STAGE_GIF/ANH-L-attackrun-decipher-archive.gif"
ls -la "$STAGE_GIF" "$STAGE_PDF"
if ls "$STAGE_GIF"/ANH-L-attackrun.gif >/dev/null 2>&1; then
  echo "REFUSING: Holotable gif in STAGE" >&2
  exit 1
fi
n=$(find "$STAGE_GIF" -maxdepth 1 -type f -name '*.gif' | wc -l)
if [ "$n" -ne 1 ]; then
  echo "REFUSING: expected exactly 1 gif in STAGE_GIF, got $n" >&2
  exit 1
fi

echo "== importImages WB Decipher face ONLY =="
docker exec swccg_wiki mkdir -p /tmp/errata-attack-run-pc-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/errata-attack-run-pc-gifs/*'
docker cp "$STAGE_GIF/." swccg_wiki:/tmp/errata-attack-run-pc-gifs/
COMMENT_WB='Decipher.com A New Hope Light white-border/site correction face (Wayback 2002-12-14 attackrunwb.gif); flush crop + exterior corner pads bleached #FFFFFF (~350x490). Cite-only on Errata Decipher+PC Notes. DO NOT replace Holotable ANH-L-attackrun.gif.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="$COMMENT_WB" \
  --overwrite \
  /tmp/errata-attack-run-pc-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages WB overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="$COMMENT_WB" \
    /tmp/errata-attack-run-pc-gifs || true
fi

echo "== importImages AR2023 PDF =="
docker exec swccg_wiki mkdir -p /tmp/errata-attack-run-pc-pdf
docker exec swccg_wiki bash -c 'rm -rf /tmp/errata-attack-run-pc-pdf/*'
docker cp "$STAGE_PDF/." swccg_wiki:/tmp/errata-attack-run-pc-pdf/
COMMENT_PDF='Players Committee SWCCG 2023 Advanced Rulebook (local wiki copy). Appendix A Errata includes Attack Run full rewrite. Cite for Errata Decipher+PC section.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="$COMMENT_PDF" \
  --overwrite \
  /tmp/errata-attack-run-pc-pdf
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages PDF overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="$COMMENT_PDF" \
    /tmp/errata-attack-run-pc-pdf || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "File:ANH-L-attackrun-wb-decipher.gif" "$PAGES/File_ANH-L-attackrun-wb-decipher.gif.wiki" \
  "Describe WB Decipher correction face; cite-only; Holotable untouched"
edit "File:SWCCG_2023_AdvancedRulebook.pdf" "$PAGES/File_SWCCG_2023_AdvancedRulebook.pdf.wiki" \
  "Describe local AR2023 PDF; Appendix A Attack Run PC Errata cite"
edit "Attack Run (PC Errata)" "$PAGES/Attack_Run_(PC_Errata).wiki" \
  "New: PC AR 2023 Appendix A Attack Run rewrite (2_42-PC); dual-layer with Decipher Gloss Supp"
edit "Attack Run (Errata)" "$PAGES/Attack_Run_(Errata).wiki" \
  "Holotable Decipher face page; link PC sibling + WB cite; do not change Holotable image"
edit "Attack Run (Original)" "$PAGES/Attack_Run_(Original).wiki" \
  "See-also PC Errata sibling"
edit "Attack Run" "$PAGES/Attack_Run.wiki" \
  "Keep Decipher baseline gametext; PC callout + (PC Errata) link; hub section 2"
edit "PC Errata" "$PAGES/PC_Errata.wiki" \
  "Link Attack Run (PC Errata) dual-layer prototype"
edit "Errata" "$PAGES/Errata.wiki" \
  "Three sections Decipher / Decipher+PC / PC; move Attack Run to section 2 with prose Notes"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

purge "Errata"
purge "Attack Run"
purge "Attack Run (Original)"
purge "Attack Run (Errata)"
purge "Attack Run (PC Errata)"
purge "PC Errata"
purge "File:ANH-L-attackrun-wb-decipher.gif"
purge "File:SWCCG_2023_AdvancedRulebook.pdf"
purge "File:ANH-L-attackrun.gif"
purge "File:ANH-L-attackrun-decipher-archive.gif"

echo "== Holotable sha1 AFTER (must match before) =="
if [ -n "${HT_PATH:-}" ]; then
  HT_HEX_AFTER=$(docker exec swccg_wiki sha1sum "$HT_PATH" | awk "{print \$1}")
  echo "ht_hex_after=$HT_HEX_AFTER"
  if [ -f /tmp/ht-sha1-before.txt ]; then
    HT_HEX_BEFORE=$(cat /tmp/ht-sha1-before.txt)
    if [ "$HT_HEX_AFTER" != "$HT_HEX_BEFORE" ]; then
      echo "FATAL: Holotable sha1 changed $HT_HEX_BEFORE -> $HT_HEX_AFTER" >&2
      exit 1
    fi
    echo "ht_unchanged_proof OK $HT_HEX_AFTER"
  fi
fi

# Report uploaded file sha1s via API-ish eval
docker exec swccg_wiki php maintenance/run.php eval '
foreach (["File:ANH-L-attackrun.gif","File:ANH-L-attackrun-wb-decipher.gif","File:ANH-L-attackrun-decipher-archive.gif","File:SWCCG_2023_AdvancedRulebook.pdf"] as $name) {
  $t = Title::newFromText($name);
  $file = MediaWiki\MediaWikiServices::getInstance()->getRepoGroup()->findFile($t);
  if ($file) {
    $path = $file->getLocalRefPath();
    $hex = $path ? sha1_file($path) : "nopath";
    echo $name . " mwsha1=" . $file->getSha1() . " hex=" . $hex . " size=" . $file->getSize() . "\n";
  } else {
    echo $name . " MISSING\n";
  }
}
' 2>/dev/null || true

echo "== DONE errata-attack-run-pc (WB+AR2023 only; Holotable untouched) =="
