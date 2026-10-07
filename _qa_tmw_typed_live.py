#!/usr/bin/env python3
from __future__ import annotations
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2014 Texas Mini Worlds",
    "2014 Texas Mini Worlds Day 1 Nick Reisch DS Court Of The Vile Gangster",
    "2014 Texas Mini Worlds Day 1 Nick Reisch LS You Can Either Profit By This...",
    "2014 Texas Mini Worlds Day 1 Paul Bonsall DS Separatist Uprising",
    "2014 Texas Mini Worlds Day 2 Nick Reisch DS Ralltiir Operations",
    "Nick Reisch",
    "Paul Bonsall",
]


def api(**kw):
    q = urllib.parse.urlencode(kw)
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main() -> None:
    for t in TITLES:
        data = api(
            action="query",
            titles=t,
            prop="info|flagged|revisions",
            rvprop="ids|size",
            rvlimit="1",
            format="json",
        )
        p = next(iter(data["query"]["pages"].values()))
        flagged = p.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = p.get("lastrevid")
        size = (p.get("revisions") or [{}])[0].get("size")
        parse = api(action="parse", page=t, prop="wikitext|text", format="json")
        wt = parse["parse"]["wikitext"]["*"]
        html = parse["parse"]["text"]["*"]
        issues = []
        if "missing" in p:
            issues.append("MISSING")
        if stable != latest:
            issues.append(f"stable!=latest {stable} {latest}")
        if t == "2014 Texas Mini Worlds":
            for n in ("Nick Reisch", "Paul Bonsall", "Greg Shaw", "Legacy Open", "Court Of The Vile Gangster"):
                if n not in wt:
                    issues.append(f"missing {n!r}")
        if "Day 1" in t and "File:" not in wt:
            issues.append("no scan File")
        if "'''Unknown'''" in wt:
            issues.append("UNKNOWN_TYPE")
        if t.startswith("2014 Texas Mini Worlds Day") and "cite" not in html:
            issues.append("no cite")
        status = "OK" if not issues else "FAIL " + ",".join(issues)
        print(status, t, "id", p.get("pageid"), "stable", stable, "size", size)
    print("DONE")


if __name__ == "__main__":
    main()
