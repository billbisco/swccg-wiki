#!/usr/bin/env python3
"""Test GEMP importable decklists (.txt XML) against a live GEMP SWCCG server.

Does over plain HTTP what the deck builder's Import button does: the web client
reads the file's <card>/<cardOutsideDeck> blueprintIds and POSTs them to
/gemp-swccg-server/deck as "id,id,...|outside,..." (deckContents). The server
silently drops any blueprintId its card library does not know, so this script
reads the saved deck back and diffs it against what was sent. It also posts to
/deck/stats (the deck builder's validation panel) and reports each format's
valid/invalid message.

Usage:
    export GEMP_TEST_USER=... GEMP_TEST_PASS=...      # or: set -a; . creds.env; set +a
    python3 gemp_import_test.py deck1.txt [deck2.txt ...] [--server URL]
            [--keep] [--deck-name NAME] [--formats all|NAME,...] [--json]

    --keep        leave the imported decks on the server (default: delete after)
    --deck-name   save every file under this one name (e.g. "ZZ test") instead of
                  the filename minus .txt
    --formats     which format validation lines to print (default: a short list)
    --names       print the server's card names for each saved deck
    --blueprints  extra blueprint ids to probe (e.g. 13_88,5_23) as a one-off deck

Exit code: 0 if every blueprint id in every file was kept, 1 otherwise.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from http.cookiejar import CookieJar

DEFAULT_SERVER = "https://test.swccg.com"
DEFAULT_FORMATS = ["Open", "Legacy", "Premiere-Hoth", "Premiere", "Hoth"]  # substring matches


class Gemp:
    def __init__(self, server):
        self.base = server.rstrip("/") + "/gemp-swccg-server"
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CookieJar()))

    def _req(self, method, path, params=None):
        url = self.base + path
        data = None
        if method == "GET" and params:
            url += "?" + urllib.parse.urlencode(params)
        elif params is not None:
            data = urllib.parse.urlencode(params).encode("utf-8")
        req = urllib.request.Request(url, data=data, method=method)
        if data is not None:
            req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
        try:
            with self.opener.open(req, timeout=60) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode("utf-8", "replace")

    def login(self, user, password):
        code, _ = self._req("POST", "/login", {"login": user, "password": password})
        if code != 200:
            raise SystemExit(f"login failed: HTTP {code} (401 = bad user/password)")

    def save(self, name, contents):
        return self._req("POST", "/deck", {"deckName": name, "deckContents": contents})

    def get(self, name):
        return self._req("GET", "/deck", {"deckName": name})

    def stats(self, contents):
        return self._req("POST", "/deck/stats", {"deckContents": contents})

    def html(self, name):
        return self._req("GET", "/deck/html", {"deckName": name})

    def delete(self, name):
        return self._req("POST", "/deck/delete", {"deckName": name})


def read_deck_file(path):
    root = ET.parse(path).getroot()
    if root.tag != "deck":
        raise ValueError(f"root element is <{root.tag}>, expected <deck>")
    inside = [(c.get("blueprintId"), c.get("title") or "") for c in root.iter("card")]
    outside = [(c.get("blueprintId"), c.get("title") or "") for c in root.iter("cardOutsideDeck")]
    return inside, outside


def parse_server_deck(xml_text):
    root = ET.fromstring(xml_text)
    inside = [c.get("blueprintId") for c in root.iter("card")]
    outside = [c.get("blueprintId") for c in root.iter("cardOutsideDeck")]
    return inside, outside


class _StatsParser(HTMLParser):
    """Collect text of each id'd <span>, including text of nested spans (card names)."""

    def __init__(self):
        super().__init__()
        self.stack = []   # index into items (or None) per open span
        self.items = []   # [id, text]

    def handle_starttag(self, tag, attrs):
        if tag == "span":
            sid = dict(attrs).get("id")
            if sid:
                self.items.append([sid, ""])
                self.stack.append(len(self.items) - 1)
            else:
                self.stack.append(None)

    def handle_endtag(self, tag):
        if tag == "span" and self.stack:
            self.stack.pop()

    def handle_data(self, data):
        for idx in reversed(self.stack):
            if idx is not None:
                self.items[idx][1] += data
                break


def parse_stats(html):
    p = _StatsParser()
    p.feed(html)
    out = {"light": None, "dark": None, "formats": []}
    pending = None
    for sid, text in p.items:
        text = text.strip()
        if sid == "deckstats-light-content":
            out["light"] = text
        elif sid == "deckstats-dark-content":
            out["dark"] = text
        elif sid.startswith("deckstats-format-") and not sid.endswith("-content"):
            pending = text.rstrip(":")
        elif sid.startswith("deckstats-format-") and sid.endswith("-content") and pending:
            out["formats"].append((pending, text))
            pending = None
        elif sid == "deckstats-invalid-deck":
            out["error"] = text
    return out


def contents_of(ids_in, ids_out):
    return ",".join(ids_in) + "|" + ",".join(ids_out)


def diff(sent, kept):
    missing = Counter(sent) - Counter(kept)
    extra = Counter(kept) - Counter(sent)
    return missing, extra


def test_one(g, label, deck_name, inside, outside, titles, args, force_names=False):
    ids_in = [b for b, _ in inside]
    ids_out = [b for b, _ in outside]
    res = {"file": label, "deckName": deck_name, "sent": len(ids_in), "sentOutside": len(ids_out)}
    contents = contents_of(ids_in, ids_out)
    code, body = g.save(deck_name, contents)
    res["saveHttp"] = code
    if code != 200:
        res["error"] = f"save failed HTTP {code}: {body[:200]}"
        return res
    code, body = g.get(deck_name)
    if code != 200:
        res["error"] = f"read-back failed HTTP {code}"
        return res
    k_in, k_out = parse_server_deck(body)
    res["kept"], res["keptOutside"] = len(k_in), len(k_out)
    m_in, x_in = diff(ids_in, k_in)
    m_out, x_out = diff(ids_out, k_out)
    res["dropped"] = [{"blueprintId": b, "count": n, "title": titles.get(b, "")}
                      for b, n in sorted((m_in + m_out).items())]
    res["unexpected"] = sorted((x_in + x_out).elements())
    if args.names or force_names:
        code, page = g.html(deck_name)
        if code == 200:
            res["serverList"] = [ln.strip() for ln in re.sub(r"<[^>]+>", "\n", page).splitlines()
                                 if ln.strip() and ln.strip() not in ("Deck:", deck_name)]
    code, html = g.stats(contents)
    res["stats"] = parse_stats(html) if code == 200 else {"error": f"HTTP {code}"}
    if not args.keep:
        g.delete(deck_name)
    return res


def print_result(res, args):
    print(f"== {res['file']}")
    if res["deckName"] != os.path.splitext(os.path.basename(res["file"]))[0]:
        print(f"   saved as: {res['deckName']}")
    if "error" in res:
        print(f"   ERROR: {res['error']}")
        return
    print(f"   cards sent {res['sent']} (+{res['sentOutside']} outside deck); "
          f"server kept {res['kept']} (+{res['keptOutside']} outside deck)")
    if res["dropped"]:
        print("   DROPPED by server (unknown blueprint ids):")
        for d in res["dropped"]:
            print(f"     {d['blueprintId']} x{d['count']}  {d['title']}")
    else:
        print("   all blueprint ids accepted")
    if res["unexpected"]:
        print(f"   unexpected extra ids in read-back: {res['unexpected']}")
    if res.get("serverList"):
        print("   server's card list:")
        for ln in res["serverList"]:
            print(f"     {ln}")
    st = res.get("stats", {})
    if st.get("error"):
        print(f"   validation: {st['error']}")
    else:
        print(f"   server counts: Light {st.get('light')}, Dark {st.get('dark')}")
        want = None if args.formats == "all" else (
            DEFAULT_FORMATS if args.formats is None else [f.strip() for f in args.formats.split(",")])
        for name, msg in st.get("formats", []):
            if want is None or any(w.lower() == name.lower() for w in want):
                print(f"   [{name}] {msg}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--server", default=os.environ.get("GEMP_TEST_SERVER", DEFAULT_SERVER))
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--deck-name")
    ap.add_argument("--formats")
    ap.add_argument("--blueprints", help="comma-separated ids to probe as a one-off deck")
    ap.add_argument("--names", action="store_true",
                    help="also print the server's own card names for the saved deck (/deck/html)")
    ap.add_argument("--json", action="store_true", help="print results as JSON")
    args = ap.parse_args()
    if not args.files and not args.blueprints:
        ap.error("give at least one .txt file or --blueprints")

    user, pw = os.environ.get("GEMP_TEST_USER"), os.environ.get("GEMP_TEST_PASS")
    if not user or not pw:
        raise SystemExit("set GEMP_TEST_USER and GEMP_TEST_PASS")
    g = Gemp(args.server)
    g.login(user, pw)

    results = []
    for path in args.files:
        label = os.path.basename(path)
        try:
            inside, outside = read_deck_file(path)
        except Exception as e:  # noqa: BLE001
            results.append({"file": label, "deckName": "", "error": f"cannot parse XML: {e}"})
            continue
        titles = {b: t for b, t in inside + outside}
        name = args.deck_name or os.path.splitext(label)[0]
        name = name[:45]  # deck builder refuses names over 45 chars
        results.append(test_one(g, label, name, inside, outside, titles, args))
    if args.blueprints:
        ids = [b.strip() for b in args.blueprints.split(",") if b.strip()]
        results.append(test_one(g, "--blueprints probe", args.deck_name or "ZZ probe",
                                [(b, "") for b in ids], [], {}, args, force_names=True))

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for r in results:
            print_result(r, args)
    ok = all("error" not in r and not r["dropped"] for r in results)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
