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
    for name in ["t86388p20", "t86388p40", "oc3forum", "wrap2021art"]:
        hp = P / f"{name}.html"
        print("=" * 80, name)
        if not hp.exists():
            print("MISSING")
            continue
        t = strip(hp.read_text(encoding="utf-8", errors="replace"))
        # find result-ish
        for needle in (
            "def.",
            "defeated",
            "wins",
            "Scoreboard",
            "North America",
            "Team USA",
            "Team Europe",
            "7-",
            "8-",
            "9-",
            "Shaw",
            "Hunter",
            "Hagen",
            "Jorgenson",
            "Jørgensen",
        ):
            i = t.find(needle)
            if i >= 0:
                print("---", needle, "at", i)
        print(t[400:9000])
        print()


if __name__ == "__main__":
    main()
