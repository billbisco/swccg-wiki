#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

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
print(p.name, "ok", len(text), "game_text_note", "game_text_note" in text)
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "Projective Telepathy (Original)" "$PAGES/Projective_Telepathy_(Original).wiki" \
  "UI: drop game_text_note italic; short notes; Original vs Errata side-by-side after Card"

edit "Projective Telepathy (Errata)" "$PAGES/Projective_Telepathy_(Errata).wiki" \
  "UI: remove long game_text_note; notes point Gloss Supp + Original"

edit "Errata" "$PAGES/Errata.wiki" \
  "Hub: Decipher vs PC framing; Changes via Decipher errata seeded with Projective Telepathy only"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20

echo "purgePage"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
Projective Telepathy (Original)
Projective Telepathy (Errata)
Errata
Errata on Projective Telepathy
Projective Telepathy
EOFPURGE

python3 - <<'PY'
import urllib.request
# --- wiki.swccg.com wikitext via api.php (anonymous index.php?action=raw is rate-limited: 429) ---
import io as _io, json as _json, time as _time, urllib.error as _ue, urllib.parse as _up, urllib.request as _ur
_WIKI_API = "https://wiki.swccg.com/api.php"
_WIKI_UA = "SWCCGWikiTools/1.0 (https://wiki.swccg.com/wiki/User:Comlink_Cursor; wikitext reader)"
_wiki_last = [0.0]
def _wiki_api_get(params, timeout=90, tries=7):
    url = _WIKI_API + "?" + _up.urlencode(params); delay = 2.0
    for attempt in range(tries):
        w = 0.35 - (_time.monotonic() - _wiki_last[0])
        if w > 0: _time.sleep(w)
        _wiki_last[0] = _time.monotonic()
        try:
            with _ur.urlopen(_ur.Request(url, headers={"User-Agent": _WIKI_UA}), timeout=timeout) as r:
                return _json.loads(r.read().decode("utf-8"))
        except _ue.HTTPError as e:
            if e.code in (429, 502, 503, 504) and attempt < tries - 1:
                ra = (e.headers.get("Retry-After") or "").strip()
                _time.sleep(float(ra) if ra.isdigit() else delay); delay = min(delay * 2, 60.0); continue
            raise
def wiki_raw_many(titles):
    """{title as given: current wikitext, or None if the page is missing/invalid}; 50 titles per request."""
    titles = list(dict.fromkeys(titles)); out = {}
    for i in range(0, len(titles), 50):
        pending = titles[i:i + 50]
        while pending:
            q = _wiki_api_get({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                               "titles": "|".join(pending), "format": "json", "formatversion": "2"}).get("query") or {}
            norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
            pages = {p.get("title"): p for p in q.get("pages", [])}
            retry = []
            for t in pending:
                p = pages.get(norm.get(t, t))
                if p is None or p.get("missing") or p.get("invalid"): out[t] = None
                elif p.get("revisions"): out[t] = p["revisions"][0]["slots"]["main"].get("content", "")
                elif len(pending) > 1: retry.append(t)  # response truncated by size limit: ask again
                else: out[t] = None
            if retry and len(retry) == len(pending):  # no progress: one title per request
                for t in retry: out.update(wiki_raw_many([t]))
                retry = []
            pending = retry
    return out
def wiki_raw(title):
    """Same result as index.php?title=T&action=raw: text, or urllib HTTPError 404 for a missing page."""
    t = wiki_raw_many([title])[title]
    if t is None: raise _ue.HTTPError(_WIKI_API, 404, "Not Found", {}, _io.BytesIO(b""))
    return t
# --- end api.php helper ---
checks = {
 "https://wiki.swccg.com/wiki/Projective_Telepathy_%28Original%29": [
   "A player who just initiated",
   "Original vs. Errata",
   "opponent must choose to use 2 Force",
 ],
 "https://wiki.swccg.com/wiki/Projective_Telepathy_%28Errata%29": [
   "If your opponent just initiated",
   "Glossary Supplement",
 ],
 "https://wiki.swccg.com/wiki/Errata": [
   "Changes to cards via Decipher errata",
   "Projective Telepathy",
   "A player who just initiated",
   "opponent must choose to use 2 Force",
 ],
}
for u, needles in checks.items():
  req = urllib.request.Request(u, headers={"Cache-Control":"no-cache","Pragma":"no-cache"})
  html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8","replace")
  missing = "noarticletext" in html or "does not have a page" in html.lower()
  print(("LIVE" if not missing else "MISSING"), u, "len", len(html))
  # italic note under game text often comes from Template:Card game_text_note
  if "Original" in u:
    bad = "This is the <b>printed Cloud City face</b> wording" in html or "printed Cloud City face</i>" in html.lower()
    # also check raw absence via action=raw
    print("  game_text_note italic markers absent-ish check skipped in HTML; see raw")
  for c in needles:
    print(("  OK" if c in html else "  MISS"), c)

# raw checks for game_text_note gone
for title in ["Projective_Telepathy_(Original)", "Projective_Telepathy_(Errata)"]:
  raw = wiki_raw(title)
  print("RAW", title, "game_text_note", "game_text_note" in raw, "len", len(raw))
print("DONE")
PY
