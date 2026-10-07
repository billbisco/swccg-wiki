#!/usr/bin/env python3
"""Live QA: Anger, Fear, Aggression (V) groups under Effect, not Interrupt."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
TITLES = [
    "2013 Match Play Championship Day 1 John Anderson LS Mind What You Have Learned (V)",
    "2013 Match Play Championship Day 1 Brian Herold LS Mind What You Have Learned (V)",
    "2013 Match Play Championship Day 1 Amar Banger LS Anger, Fear, Aggression (V)",
    "2013 SoCal Grand Prix Day 1 Phil Aasen LS It Is The Future You See (V)",
    "2013 Texas Mini Worlds Day 1 Evan Kirkpatrick LS Anger, Fear, Aggression (V)",
    "2013 Worlds Day 2 Casey Anis LS Anger, Fear, Aggression (V)",
    "2013 Alderaan Regionals Ryan Jellison LS Hidden Base (V)",
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}?{q}", headers={"User-Agent": "swccg-wiki-qa/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def section(text: str, heading: str) -> str:
    m = re.search(
        r"'''" + re.escape(heading) + r"'''(.*?)(?:'''|\|})",
        text,
        re.S,
    )
    return m.group(1) if m else ""


def main() -> int:
    n = 0
    for t in TITLES:
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
        effect = section(text, "Effect")
        interrupt = section(text, "Interrupt")
        needle = "Anger, Fear, Aggression (V)"
        if needle not in effect:
            got.append("AFA_V_NOT_EFFECT")
        if needle in interrupt:
            got.append("AFA_V_IN_INTERRUPT")
        parsed = api(
            {
                "action": "parse",
                "format": "json",
                "page": t,
                "prop": "text",
            }
        )
        html = (parsed.get("parse") or {}).get("text", {}).get("*", "")
        # Heading then list item: Effect section should contain the (V) link.
        if "Anger, Fear, Aggression (V)" not in html:
            got.append("PARSE_MISSING_AFA_V")
        # If Interrupt heading appears after AFA (V) in HTML before Effect, that's a miss.
        m_eff = re.search(
            r"<b>Effect</b>(.*?)<b>", html, re.S | re.I
        )
        m_int = re.search(
            r"<b>Interrupt</b>(.*?)<b>", html, re.S | re.I
        )
        eff_html = m_eff.group(1) if m_eff else ""
        int_html = m_int.group(1) if m_int else ""
        if "Anger, Fear, Aggression (V)" not in eff_html:
            got.append("PARSE_AFA_V_NOT_EFFECT")
        if "Anger, Fear, Aggression (V)" in int_html:
            got.append("PARSE_AFA_V_IN_INTERRUPT")
        print(t)
        print("  stable", stable, "latest", latest, "len", len(text), "html", len(html))
        print("  issues", got or ["OK"])
        n += len(got)
    print("TOTAL", n, "issues")
    return 1 if n else 0


if __name__ == "__main__":
    raise SystemExit(main())
