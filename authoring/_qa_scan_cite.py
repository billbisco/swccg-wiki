#!/usr/bin/env python3
import json
import re
import time
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
PAGE = "2014 Worlds Day 3 Matthew Harrison-Trainor LS Communing"
UA = {"User-Agent": "SWCCGWikiQA/1.0", "Cache-Control": "no-cache"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def api(**kw):
    kw.setdefault("format", "json")
    return json.loads(get(API + "?" + urllib.parse.urlencode(kw)))


info = api(action="query", titles=PAGE, prop="info|flagged|revisions", rvprop="ids|comment", rvlimit="2")
page = next(iter(info["query"]["pages"].values()))
print("last", page.get("lastrevid"), "stable", page.get("flagged", {}).get("stable_revid"))
print("comment", page.get("revisions", [{}])[0].get("comment"))

parsed = api(action="parse", page=PAGE, prop="text|revid", disablelimitreport="1")
html = parsed["parse"]["text"]["*"]
print("parse_revid", parsed["parse"]["revid"])
scan = html[html.find('id="Scan"') : html.find('id="See_also"')]
print("---SCAN---")
print(scan)
print("table", "<table" in scan)
print("td_count", len(re.findall(r"<td", scan, re.I)))
print("cite_in_scan", "cite_ref" in scan or "cite&#95;ref" in scan)
print("under_image", bool(re.search(r"</figure>\s*<p>\s*<sup", scan)))
print("page5_in_scan", "Page 5 of" in scan)
refs = html[html.find('id="References"') :]
print("page5_in_refs", "Page 5 of" in refs)
