#!/usr/bin/env python3
from pathlib import Path
import html as H
import re

P = Path("/tmp/outrider-src")


def first_post_html(html: str) -> str | None:
    m = re.search(r'class="postbody"(.*?)class="back2top"', html, re.S | re.I)
    if not m:
        m = re.search(r'id="post_content\d+"(.*?)class="back2top"', html, re.S | re.I)
    if not m:
        return None
    chunk = m.group(1)
    chunk = re.sub(r"(?is)<script.*?</script>", " ", chunk)
    chunk = re.sub(r"<br\s*/?>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</p>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</(li|div|tr|h[1-6])>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"(?s)<[^>]+>", " ", chunk)
    chunk = H.unescape(chunk)
    chunk = re.sub(r"[ \t]+", " ", chunk)
    chunk = re.sub(r"\n{3,}", "\n\n", chunk)
    return chunk.strip()


def main() -> None:
    names = [
        "t74065",
        "t74291",
        "t73620",
        "t73630",
        "t73616",
        "t74436",
        "t74099",
        "t86388",
        "t86377",
        "t86302",
        "t86478b",
        "t86478",
    ]
    for name in names:
        hp = P / f"{name}.html"
        print("=" * 80)
        if not hp.exists():
            print("MISSING HTML", name)
            continue
        html = hp.read_text(encoding="utf-8", errors="replace")
        tm = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
        title = re.sub(r"\s+", " ", H.unescape(tm.group(1))) if tm else "?"
        print(name, "TITLE:", title[:220])
        fp = first_post_html(html)
        if fp:
            print(fp[:9000])
        else:
            print("NO first post; txt head:")
            tp = P / f"{name}.txt"
            print(tp.read_text(encoding="utf-8", errors="replace")[:4000] if tp.exists() else "no txt")
        print()


if __name__ == "__main__":
    main()
