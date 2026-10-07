#!/usr/bin/env python3
"""Live QA: 2013 MPC Smith collision retarget + Mack dest-dump check."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://wiki.swccg.com/api.php"
TSV = Path(__file__).resolve().parent / "y2013-mpc-smith-titles.tsv"
DUMP = (
    " dested ",
    "dittos inherit",
    "Form left column reprints",
    "(V) from the checkbox",
    "Handwritten 2010 Xerox Print Form",
    "Typed 2010 Xerox Print Form",
    "Typed slang list",
    "Informal handwritten list",
)
EXTRA = [
    "2013 Match Play Championship Day 1 Josh Mack LS Watch Your Step",
    "Smith",
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch(title: str) -> tuple[dict, str]:
    data = api(
        {
            "action": "query",
            "format": "json",
            "prop": "info|flagged|revisions",
            "rvprop": "ids|content",
            "rvslots": "main",
            "redirects": "1",
            "titles": title,
        }
    )
    page = next(iter(data["query"]["pages"].values()))
    text = ""
    revs = page.get("revisions") or []
    if revs:
        text = revs[0].get("slots", {}).get("main", {}).get("*", "")
    return page, text


def main() -> int:
    titles = [
        line.split("\t", 1)[0].strip()
        for line in TSV.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    n = 0
    for t in titles + EXTRA:
        page, text = fetch(t)
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        got: list[str] = []
        if "missing" in page:
            got.append("MISSING")
        if stable and latest and int(stable) != int(latest):
            got.append(f"UNSTABLE stable={stable} latest={latest}")
        for marker in DUMP:
            if marker in text:
                got.append(f"DUMP_{marker.strip()[:24]}")
        live_title = page.get("title") or t
        if t == "2013 Match Play Championship":
            if "[[Smith (2013 Match Play Championship)|Smith]]" not in text:
                got.append("HUB_SMITH_NOT_PIPED")
            if "| [[Smith]] ||" in text:
                got.append("HUB_BARE_SMITH")
        if t.startswith("2013 Match Play Championship Day 1 Smith"):
            if "[[Smith (2013 Match Play Championship)|Smith]]" not in text:
                got.append("DECK_SMITH_NOT_PIPED")
            if "* [[Smith]]" in text:
                got.append("DECK_BARE_SMITH")
            if '{| style="margin:0 auto;border:0' not in text:
                got.append("MISSING_SCAN_TABLE")
        if t == "Smith (2013 Match Play Championship)":
            if text.lstrip().startswith("#REDIRECT"):
                got.append("STUB_IS_REDIRECT")
            if "3MW8J8" not in text:
                got.append("STUB_USERNAME")
        if t == "Smith":
            if live_title != "Jacy Smith" and "Jacy Smith" not in text:
                got.append(f"SMITH_NOT_JACY live={live_title!r}")
        if got:
            n += 1
            print("FAIL", t, got)
        else:
            print("OK", t, "live", live_title)
    print("TOTAL", n)
    return n


if __name__ == "__main__":
    raise SystemExit(main())
