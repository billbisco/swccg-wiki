#!/usr/bin/env python3
"""Inventory Stephen Skilton DeckTech archives vs live decktech.net.

Writes wiki/decktech-inventory.json (post ids, titles, authors, dates, ratings).
Does not dest wiki pages. Index Light/Dark tags on Skilton listings are often
wrong; dest from post bodies.
"""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "decktech-inventory.json"
UA = "swccg-wiki-historian/1.0 (https://wiki.swccg.com)"

SKILTON = "https://www.stephenskilton.com/decktech_archives"
GITHUB = "https://stevetotheizz0.github.io/decktech_archives"
DECKTECH_DECKS = "http://www.decktech.net/starwarsccg/decks/"
DECKTECH_TR = "http://www.decktech.net/starwarsccg/tournament-reports/"

POST_RE = re.compile(
    r'<h2[^>]*>\s*<a href="(/decktech_archives/(\d+)/)"[^>]*>(.*?)</a>',
    re.I | re.S,
)
REPORT_RE = re.compile(
    r'<a href="(/decktech_archives/reports/([^"]+))"[\s\S]*?</a>\s*'
    r"<br>\s*([^<]+)\s*<br>\s*([^<]+)",
    re.I,
)
PAGER_RE = re.compile(r"/decktech_archives/page(\d+)/")


def fetch(url: str, timeout: int = 60) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, body
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace") if e.fp else ""
    except Exception as e:
        return 0, str(e)


def parse_index(html: str) -> list[dict]:
    posts = []
    for m in POST_RE.finditer(html):
        path, pid, title = m.group(1), m.group(2), re.sub(r"<[^>]+>", "", m.group(3))
        chunk = html[m.end() : m.end() + 800]
        rating = re.search(r"Rating:\s*([0-9.]+)", chunk)
        date = re.search(
            r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}",
            chunk,
        )
        author = re.search(r"([A-Z][a-z].{0,80}?)\s*<", chunk)
        posts.append(
            {
                "id": pid,
                "path": path,
                "title": re.sub(r"\s+", " ", title).strip(),
                "date": date.group(0) if date else "",
                "rating": rating.group(1) if rating else "",
                "author_guess": re.sub(r"\s+", " ", author.group(1)).strip()
                if author
                else "",
            }
        )
    return posts


def last_page(html: str) -> int:
    nums = [int(n) for n in PAGER_RE.findall(html)]
    return max(nums) if nums else 1


def main() -> None:
    print("FETCH", SKILTON + "/")
    st, html = fetch(SKILTON + "/")
    print("STATUS", st, "bytes", len(html))
    last = last_page(html)
    # Some themes only show next; probe upward if last==1.
    if last <= 1:
        for guess in (80, 100, 120, 150):
            gst, ghtml = fetch(f"{SKILTON}/page{guess}/")
            print("PROBE", guess, gst, len(ghtml))
            if gst == 200 and POST_RE.search(ghtml):
                last = max(last, guess, last_page(ghtml))
            elif gst == 404:
                break
            time.sleep(0.4)
    print("LAST_PAGE_HINT", last)
    posts: dict[str, dict] = {}
    page = 1
    empty = 0
    while page <= max(last, 1) + 5 and empty < 3:
        url = SKILTON + "/" if page == 1 else f"{SKILTON}/page{page}/"
        st, body = fetch(url)
        found = parse_index(body) if st == 200 else []
        print(f"PAGE {page} status={st} n={len(found)}")
        if not found:
            empty += 1
        else:
            empty = 0
            last = max(last, page, last_page(body))
            for p in found:
                posts[p["id"]] = p
        page += 1
        time.sleep(0.35)

    print("FETCH reports")
    rst, rhtml = fetch(SKILTON + "/tournament_reports/")
    reports = []
    for m in REPORT_RE.finditer(rhtml):
        reports.append(
            {
                "path": m.group(1),
                "slug": m.group(2),
                "author": re.sub(r"\s+", " ", m.group(3)).strip(),
                "date": re.sub(r"\s+", " ", m.group(4)).strip(),
            }
        )
    # Fallback: count report hrefs
    hrefs = re.findall(r'href="(/decktech_archives/reports/[^"]+)"', rhtml)
    print("REPORTS parsed", len(reports), "hrefs", len(hrefs), "status", rst)

    print("FETCH decktech.net")
    ds, dhtml = fetch(DECKTECH_DECKS)
    ts, thtml = fetch(DECKTECH_TR)
    print("DECKTECH decks", ds, "bytes", len(dhtml), "hrefs", dhtml.count("href="))
    print("DECKTECH reports", ts, "bytes", len(thtml), "hrefs", thtml.count("href="))

    inv = {
        "skilton": SKILTON,
        "github_pages": GITHUB,
        "deck_pages_crawled": page - 1,
        "deck_posts": len(posts),
        "report_hrefs": len(set(hrefs)),
        "reports_parsed": len(reports),
        "decktech_net_decks_status": ds,
        "decktech_net_reports_status": ts,
        "note": (
            "Skilton is a Jekyll dump of DeckTech posts (numeric ids) plus "
            "/reports/ tournament reports. Live decktech.net /decks/ and "
            "/tournament-reports/ are a later shell that does not list posts "
            "in static HTML. Dest from Skilton post bodies; listing Light/Dark "
            "tags are unreliable."
        ),
        "posts": sorted(posts.values(), key=lambda p: int(p["id"]), reverse=True),
        "reports": reports[:50],
    }
    OUT.write_text(json.dumps(inv, indent=2, ensure_ascii=False), encoding="utf-8")
    print("WROTE", OUT, "posts", len(posts), "reports_href", len(set(hrefs)))


if __name__ == "__main__":
    main()
