#!/usr/bin/env python3
"""Live HTML QA: July 2017 Wayback MasterDS/MasterLS refs on Virtual Legacy."""
from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
UA = {"User-Agent": "SWCCGWikiQA/1.0", "Cache-Control": "no-cache"}

DS_TS = "20170704232650"
LS_TS = "20170705013057"


def get(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def api(**kw):
    kw.setdefault("format", "json")
    return json.loads(get(API + "?" + urllib.parse.urlencode(kw)))


fails: list[str] = []


def check(ok: bool, label: str) -> None:
    print(("OK  " if ok else "FAIL"), label)
    if not ok:
        fails.append(label)


info = api(action="query", titles="Virtual Legacy", prop="info|flagged")
page = next(iter(info["query"]["pages"].values()))
last = page.get("lastrevid")
st = page.get("flagged", {}).get("stable_revid")
print(f"Virtual Legacy last={last} stable={st}")
check(st is not None and last == st, "VL stable==latest")

parsed = api(
    action="parse",
    page="Virtual Legacy",
    prop="text|revid",
    disablelimitreport="1",
)
html = parsed["parse"]["text"]["*"]
print("parse revid", parsed["parse"]["revid"])
check("#REDIRECT" not in html, "VL not redirect")

for needle in [
    DS_TS,
    LS_TS,
    "MasterDS.pdf",
    "MasterLS.pdf",
    "Resources/MasterDS.pdf",
    "Resources/MasterLS.pdf",
    "Virtual Legacy Final Master DS",
    "Virtual Legacy Final Master LS",
]:
    check(needle in html, f"VL html has {needle}")

src_i = html.find('id="Sources"')
ref_i = html.find('id="References"')
src = html[src_i:ref_i] if src_i >= 0 and ref_i > src_i else ""
refs = html[ref_i:] if ref_i >= 0 else ""
check(DS_TS in src, "VL Sources has MasterDS Wayback")
check(LS_TS in src, "VL Sources has MasterLS Wayback")
check(DS_TS in refs, "VL References has MasterDS Wayback")
check(LS_TS in refs, "VL References has MasterLS Wayback")

for title, ts in [
    ("File:Virtual Legacy Final Master DS.pdf", DS_TS),
    ("File:Virtual Legacy Final Master LS.pdf", LS_TS),
]:
    p = api(action="parse", page=title, prop="text", disablelimitreport="1")
    fhtml = p["parse"]["text"]["*"]
    print(title, "html_len", len(fhtml))
    check(ts in fhtml, f"{title} html has {ts}")
    check("Virtual_Legacy" in fhtml, f"{title} used on VL")

mp = api(action="parse", page="Main Page", prop="text", disablelimitreport="1")
mhtml = mp["parse"]["text"]["*"]
check("Virtual_Legacy" in mhtml and "Overview" in mhtml, "Main Page Overview Virtual Legacy")

if fails:
    print("FAILS", len(fails))
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("QA_OK")
