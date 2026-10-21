#!/usr/bin/env python3
"""Fetch current wikitext from wiki.swccg.com through api.php instead of index.php?action=raw.

nginx rate-limits anonymous index.php views (3 r/s, burst 30, 429 beyond that), so scripts read
page text with action=query&prop=revisions&rvslots=main, up to 50 titles per request.

fetch_raw(title)          -> text, or urllib.error.HTTPError 404 for a missing page (as action=raw)
fetch_raw_many(titles)    -> {title as given: text or None (missing/invalid)}

CLI (for shell scripts): wiki_api_fetch.py TITLE prints the text with no added newline, or
nothing for a missing page (as `curl -sS ...?action=raw` did). TITLE may use underscores or
%-escapes, as in /wiki/ URLs.
"""
from __future__ import annotations

import io
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
USER_AGENT = "SWCCGWikiTools/1.0 (https://wiki.swccg.com/wiki/User:Comlink_Cursor; wikitext reader)"
BATCH = 50
MIN_INTERVAL = 0.35  # seconds between requests (stay under 3 r/s)
_last = [0.0]


def api_get(params: dict, timeout: float = 90, tries: int = 7) -> dict:
    url = API + "?" + urllib.parse.urlencode(params)
    delay = 2.0
    for attempt in range(tries):
        wait = MIN_INTERVAL - (time.monotonic() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.monotonic()
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < tries - 1:
                ra = (e.headers.get("Retry-After") or "").strip()
                time.sleep(float(ra) if ra.isdigit() else delay)
                delay = min(delay * 2, 60.0)
                continue
            raise
    raise RuntimeError("unreachable")


def fetch_raw_many(titles) -> dict:
    """Map each title (as given) to its current wikitext, or None if missing/invalid."""
    titles = list(dict.fromkeys(titles))
    out: dict = {}
    for i in range(0, len(titles), BATCH):
        batch = titles[i:i + BATCH]
        pending = list(batch)
        while pending:
            data = api_get({
                "action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                "titles": "|".join(pending), "format": "json", "formatversion": "2",
            })
            q = data.get("query") or {}
            norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
            pages = {p.get("title"): p for p in q.get("pages", [])}
            retry = []
            for t in pending:
                p = pages.get(norm.get(t, t))
                if p is None or p.get("missing") or p.get("invalid"):
                    out[t] = None
                elif p.get("revisions"):
                    out[t] = p["revisions"][0]["slots"]["main"].get("content", "")
                elif len(pending) > 1:  # response truncated by the size limit: ask again
                    retry.append(t)
                else:
                    out[t] = None
            if retry and len(retry) == len(pending):  # no progress: one title per request
                for t in retry:
                    out.update(fetch_raw_many([t]))
                retry = []
            pending = retry
    return out


def fetch_raw(title: str) -> str:
    """Same result as index.php?title=T&action=raw: text, or HTTPError 404 if the page is missing."""
    text = fetch_raw_many([title])[title]
    if text is None:
        raise urllib.error.HTTPError(API, 404, "Not Found", {}, io.BytesIO(b""))
    return text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: wiki_api_fetch.py TITLE")
    t = urllib.parse.unquote(sys.argv[1]).replace("_", " ")
    txt = fetch_raw_many([t])[t]
    if txt:
        sys.stdout.write(txt)
