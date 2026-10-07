#!/usr/bin/env python3
"""Live QA for VB1–9 dual-title objective rename."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
UA = {"User-Agent": "SWCCGWikiBot/1.0 (legacy-obj QA)"}

CHECKS = [
    ("Wookiee Slaving Operation", True, None),
    ("Wookiee Slaving Operation / Indentured To The Empire", False, "Indentured To The Empire"),
    ("Contract Killers / Feared Throughout The Galaxy", False, "Feared Throughout The Galaxy"),
    ("Imperial Occupation", True, None),
    ("Imperial Occupation (V) / Imperial Control (V)", False, "Imperial Control (V)"),
    ("Imperial Entanglements", True, None),
    (
        "Imperial Entanglements / No One To Stop Us This Time (Virtual Block 1)",
        False,
        "No One To Stop Us This Time",
    ),
    ("A Stunning Move", True, None),
    (
        "A Stunning Move / A Valuable Hostage (Virtual Block 7)",
        False,
        "A Valuable Hostage",
    ),
    ("Local Uprising (V) / Liberation (V)", False, "Liberation (V)"),
    (
        "Hidden Base (V) / Systems Will Slip Through Your Fingers (V)",
        False,
        "Systems Will Slip Through Your Fingers (V)",
    ),
    (
        "Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)",
        False,
        "Their Fire Has Gone Out Of The Universe (V)",
    ),
    ("Infiltration / Unlikely Allies", False, "Unlikely Allies"),
    ("Center Of Tyranny / A Liberated World", False, "A Liberated World"),
    ("Republic At War / Aggressive Negotiations", False, "Aggressive Negotiations"),
    ("Separatist Uprising / At War With Itself", False, "At War With Itself"),
    (
        "Rebel Strike Team (V) / Garrison Destroyed (V)",
        False,
        "Garrison Destroyed (V)",
    ),
    (
        "Mind What You Have Learned (V) / Save You It Can (V)",
        False,
        "Save You It Can (V)",
    ),
    (
        "Watch Your Step (V) / This Place Can Be A Little Rough (V)",
        False,
        "This Place Can Be A Little Rough (V)",
    ),
    (
        "We Have A Plan (V) / They Will Be Lost And Confused (V)",
        False,
        "They Will Be Lost And Confused (V)",
    ),
    ("We'll Handle This (V) / Duel Of The Fates (V)", False, "Duel Of The Fates (V)"),
]

OLD_SINGLES = [
    "Wookiee Slaving Operation",
    "Contract Killers",
    "Imperial Occupation",
    "Imperial Entanglements",
    "A Stunning Move",
    "Local Uprising",
    "Hidden Base",
    "Watch Your Step",
    "Hunt Down And Destroy The Jedi",
    "We Have A Plan",
    "We'll Handle This",
    "Mind What You Have Learned",
    "Center Of Tyranny",
    "Rebel Strike Team",
    "Infiltration",
    "Republic At War",
    "Separatist Uprising",
]


def api(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(API + "?" + q, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def raw(title: str) -> str:
    q = urllib.parse.urlencode({"title": title, "action": "raw"})
    req = urllib.request.Request("https://wiki.swccg.com/index.php?" + q, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def html(title: str) -> str:
    q = urllib.parse.urlencode({"title": title})
    req = urllib.request.Request("https://wiki.swccg.com/index.php?" + q, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def cat_members() -> list[str]:
    titles = []
    cm = None
    while True:
        p = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": "Category:Objective",
            "cmlimit": "500",
            "format": "json",
        }
        if cm:
            p["cmcontinue"] = cm
        data = api(p)
        titles.extend(m["title"] for m in data["query"]["categorymembers"])
        cm = data.get("continue", {}).get("cmcontinue")
        if not cm:
            break
    return titles


def main() -> None:
    issues = []
    for title, expect_redir, side7 in CHECKS:
        try:
            text = raw(title)
        except Exception as e:
            issues.append(f"FETCHFAIL {title}: {e}")
            print("FETCHFAIL", title, e)
            continue
        is_redir = text.lstrip().upper().startswith("#REDIRECT")
        if expect_redir and not is_redir:
            issues.append(f"NOT REDIR {title}")
            print("NOT REDIR", title)
        elif not expect_redir and is_redir:
            issues.append(f"UNEXPECTED REDIR {title} -> {text[:80]!r}")
            print("UNEXPECTED REDIR", title)
        elif not expect_redir:
            ok = True
            if "|image2=" not in text:
                issues.append(f"NO IMAGE2 {title}")
                ok = False
            if "'''7 side" not in text:
                issues.append(f"NO 7 SIDE {title}")
                ok = False
            if side7 and side7 not in text:
                issues.append(f"MISSING 7 NAME {title}: {side7}")
                ok = False
            if "|image2_layout=responsive" not in text:
                issues.append(f"NO LAYOUT {title}")
                ok = False
            print("OK" if ok else "BAD", title)
        else:
            print("REDIR OK", title, text.strip().splitlines()[0][:100])

    titles = cat_members()
    print("Category:Objective", len(titles))
    new_dests = [c[0] for c in CHECKS if not c[1]]
    still = [t for t in OLD_SINGLES if t in titles]
    missing = [t for t in new_dests if t not in titles]
    print("old singles still in cat:", still)
    print("new dests missing from cat:", missing)
    if still:
        issues.append(f"OLD IN CAT {still}")
    if missing:
        issues.append(f"NEW MISSING CAT {missing}")

    for hub, needle in (
        ("Virtual Block 8", "Wookiee Slaving Operation / Indentured To The Empire"),
        ("Virtual Block 2", "Imperial Occupation (V) / Imperial Control (V)"),
        ("Virtual Block 1", "Imperial Entanglements / No One To Stop Us This Time (Virtual Block 1)"),
        ("Virtual Block 7", "A Stunning Move / A Valuable Hostage (Virtual Block 7)"),
    ):
        h = raw(hub)
        if needle not in h:
            issues.append(f"HUB MISS {hub} {needle}")
            print("HUB MISS", hub)
        else:
            print("HUB OK", hub)

    # Rendered HTML: both faces present on Wookiee dest
    page = "Wookiee Slaving Operation / Indentured To The Empire"
    body = html(page)
    for token in (
        "VB8-D-wookieeslavingoperation-pre.gif",
        "VB8-D-indenturedtotheempire-pre.gif",
        "0 side",
        "7 side",
    ):
        if token not in body:
            issues.append(f"HTML MISS {page} {token}")
            print("HTML MISS", token)
        else:
            print("HTML OK", token)

    occ = html("Imperial Occupation (V) / Imperial Control (V)")
    if "Imperial Occupation (V)" not in occ or "Imperial Control (V)" not in occ:
        issues.append("HTML MISS Imperial Occupation (V) both faces")
        print("HTML BAD occupation")
    else:
        print("HTML OK Imperial Occupation (V) both faces")

    print("ISSUES", len(issues))
    for i in issues:
        print(" -", i)


if __name__ == "__main__":
    main()
