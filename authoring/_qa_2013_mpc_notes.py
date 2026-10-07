#!/usr/bin/env python3
"""Live QA: 2013 MPC dest-note cleanup (hub + Day 1 decks)."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://wiki.swccg.com/api.php"
TSV = Path(__file__).resolve().parent / "y2013-mpc-notes-titles.tsv"
DUMP = (
    " dested ",
    "dittos inherit",
    "Form left column reprints",
    "(V) from the checkbox",
    "Handwritten 2010 Xerox Print Form",
    "Typed 2010 Xerox Print Form",
    "Typed printout (not a handwritten",
    "Informal handwritten list",
)


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def main() -> int:
    titles = [
        line.split("\t", 1)[0].strip()
        for line in TSV.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    n = 0
    for t in titles:
        data = api(
            {
                "action": "query",
                "format": "json",
                "prop": "info|flagged|revisions",
                "rvprop": "ids|content",
                "rvslots": "main",
                "titles": t,
            }
        )
        page = next(iter(data["query"]["pages"].values()))
        flagged = page.get("flagged") or {}
        stable = flagged.get("stable_revid")
        latest = page.get("lastrevid")
        text = ""
        revs = page.get("revisions") or []
        if revs:
            text = revs[0].get("slots", {}).get("main", {}).get("*", "")
        got: list[str] = []
        if "missing" in page:
            got.append("MISSING")
        if stable and latest and int(stable) != int(latest):
            got.append(f"UNSTABLE stable={stable} latest={latest}")
        for marker in DUMP:
            if marker in text:
                got.append(f"DUMP_{marker.strip()[:24]}")
        if t.startswith("2013 Match Play Championship Day 1"):
            if '{| style="margin:0 auto;border:0' not in text:
                got.append("MISSING_SCAN_TABLE")
            if "|center|" in text:
                got.append("CENTER_SCAN")
        if got:
            n += 1
            print("FAIL", t, got)
        else:
            print("OK", t)
    print("TOTAL", n)
    return n


if __name__ == "__main__":
    raise SystemExit(main())
