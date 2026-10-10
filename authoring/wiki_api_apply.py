#!/usr/bin/env python3
"""Apply a batch to wiki.swccg.com through the web API as Holocron Claude — no SSH, no PC.

Reads the bot password from the environment (cloud environment variables, never a file in git):
    WIKI_BOT_USER="Holocron Claude@claude"   WIKI_BOT_PASS=...
The account has autoreview, so FlaggedRevs marks these edits reviewed.

    python3 wiki_api_apply.py y-dt-batch-06.tsv [--files gemp-import-dt-batch-06/*.txt] [--summary ...]

TSV rows: title<TAB>relative/path/to/page.wiki (the same TSV apply-tsv.sh takes). Files are
uploaded (overwriting an existing file of that name) before the pages, so download links are
live when the pages land. Pages whose text is unchanged are skipped (nochange).
"""
from __future__ import annotations

import argparse
import http.cookiejar
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

API = "https://wiki.swccg.com/api.php"
UA = "swccg-wiki-dest/1.0 (Holocron Claude; https://github.com/billbisco/swccg-wiki)"


class Wiki:
    def __init__(self) -> None:
        user, pw = os.environ.get("WIKI_BOT_USER"), os.environ.get("WIKI_BOT_PASS")
        if not user or not pw:
            raise SystemExit("WIKI_BOT_USER / WIKI_BOT_PASS not set (cloud environment variables)")
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        self.op.addheaders = [("User-Agent", UA)]
        t = self.get(action="query", meta="tokens", type="login")["query"]["tokens"]["logintoken"]
        r = self.post(action="login", lgname=user, lgpassword=pw, lgtoken=t)["login"]
        if r.get("result") != "Success":
            raise SystemExit(f"login failed: {r.get('result')} {r.get('reason', '')}")
        self.csrf = self.get(action="query", meta="tokens")["query"]["tokens"]["csrftoken"]

    def _open(self, req, tries: int = 5) -> dict:
        for i in range(tries):
            try:
                with self.op.open(req, timeout=180) as r:
                    d = json.loads(r.read().decode("utf-8"))
                if d.get("error", {}).get("code") == "maxlag":
                    time.sleep(5 * (i + 1))
                    continue
                return d
            except urllib.error.URLError:
                if i == tries - 1:
                    raise
                time.sleep(5 * (i + 1))
        raise RuntimeError("API retries exhausted")

    def get(self, **p) -> dict:
        q = {"format": "json", "formatversion": "2", **p}
        return self._open(API + "?" + urllib.parse.urlencode(q))

    def post(self, **p) -> dict:
        q = {"format": "json", "formatversion": "2", **p}
        return self._open(urllib.request.Request(API, urllib.parse.urlencode(q).encode("utf-8")))

    def edit(self, title: str, text: str, summary: str) -> str:
        for wait in (0, 20, 40, 60, 60, 60):  # the wiki rate-limits edits per account; wait it out
            time.sleep(wait)
            d = self.post(action="edit", title=title, text=text, summary=summary, bot="1",
                          token=self.csrf, maxlag="5")
            if d.get("error", {}).get("code") != "ratelimited":
                break
        if "error" in d:
            return f"ERROR {d['error'].get('code')}: {d['error'].get('info', '')[:120]}"
        e = d["edit"]
        status = "nochange" if e.get("nochange") else ("created" if e.get("new") else "edited")
        return status + self.review(title)

    def review(self, title: str) -> str:
        """FlaggedRevs autoreview skips new pages and edits on top of an unreviewed revision;
        review the current revision explicitly (Holocron Claude has the review right)."""
        p = self.get(action="query", titles=title, prop="flagged|revisions", rvprop="ids")["query"]["pages"][0]
        f = p.get("flagged")
        if p.get("missing") or "revisions" not in p:
            return ""
        if f is not None and not f.get("pending_since"):
            return ""
        d = self.post(action="review", revid=str(p["revisions"][0]["revid"]), flag_accuracy="1",
                      comment="Holocron Claude batch apply", token=self.csrf)
        if "error" in d:
            return f" (review ERROR {d['error'].get('code')})"
        return " (reviewed)"

    def upload(self, path: Path, comment: str) -> str:
        boundary = uuid.uuid4().hex
        fields = {"action": "upload", "format": "json", "formatversion": "2", "filename": path.name,
                  "comment": comment, "ignorewarnings": "1", "token": self.csrf}
        body = b"".join(
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode("utf-8")
            for k, v in fields.items())
        body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{path.name}\"\r\n"
                 f"Content-Type: text/plain\r\n\r\n").encode("utf-8") + path.read_bytes() + f"\r\n--{boundary}--\r\n".encode()
        req = urllib.request.Request(API, body, {"Content-Type": f"multipart/form-data; boundary={boundary}"})
        d = self._open(req)
        if d.get("error", {}).get("code") == "fileexists-no-change":
            return "unchanged"
        if "error" in d:
            return f"ERROR {d['error'].get('code')}: {d['error'].get('info', '')[:120]}"
        u = d["upload"]
        return u.get("result", "?") + (" (unchanged)" if "duplicate" in json.dumps(u.get("warnings", {})) else "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tsv", type=Path)
    ap.add_argument("--files", nargs="*", type=Path, default=[])
    ap.add_argument("--summary", default="DeckTech dest (Holocron Claude)")
    a = ap.parse_args()
    base = a.tsv.resolve().parent
    w = Wiki()
    bad = 0
    for f in a.files:
        r = w.upload(f, a.summary)
        bad += r.startswith("ERROR")
        print(f"FILE {f.name}: {r}", flush=True)
    for line in a.tsv.read_text(encoding="utf-8").splitlines():
        if "\t" not in line:
            continue
        title, rel = line.split("\t", 1)
        r = w.edit(title, (base / rel).read_text(encoding="utf-8"), a.summary)
        bad += r.startswith("ERROR")
        print(f"PAGE {title}: {r}", flush=True)
    print("DONE errors", bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
