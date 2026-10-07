#!/usr/bin/env python3
from pathlib import Path
import html as H
import re

P = Path("/tmp/outrider-src")


def strip(html: str) -> str:
    html = re.sub(r"(?is)<script.*?</script>", " ", html)
    html = re.sub(r"(?is)<style.*?</style>", " ", html)
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    html = re.sub(r"</p>", "\n", html, flags=re.I)
    html = re.sub(r"</(li|div|tr|h[1-6])>", "\n", html, flags=re.I)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    html = H.unescape(html)
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()


def main() -> None:
    # Full first post of t74099 (not truncated)
    html = (P / "t74099.html").read_text(encoding="utf-8", errors="replace")
    m = re.search(r'class="postbody"(.*?)class="back2top"', html, re.S | re.I)
    chunk = m.group(1) if m else html
    print("=" * 80, "t74099 FIRST POST FULL")
    print(strip(chunk)[:15000])
    print()

    for name in ["t74099p20", "t74099p40", "t74099p60", "t74291p20"]:
        hp = P / f"{name}.html"
        if not hp.exists():
            print("MISSING", name)
            continue
        t = strip(hp.read_text(encoding="utf-8", errors="replace"))
        print("=" * 80, name, "len", len(t))
        # keep result-ish lines
        for needle in (
            "wins",
            "conced",
            "Game",
            "youtu",
            "Europe",
            "USA",
            "Scoreboard",
            "def.",
            "defeated",
            "+",
        ):
            pass
        print(t[:8000])
        print()

    for name in ["wrap2019", "wrap2021", "wrap2021decks", "wrap2023decks", "wrap2026"]:
        tp = P / f"{name}.txt"
        if not tp.exists():
            print("MISSING", name)
            continue
        t = tp.read_text(encoding="utf-8", errors="replace")
        print("=" * 80, name, "len", len(t))
        print(t[800:7000] if name.startswith("wrap") else t[:6000])
        print()


if __name__ == "__main__":
    main()
