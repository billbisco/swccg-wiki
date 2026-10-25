"""Hand edits for tr-batch-10 on the built package (Claude 2026-10-25). python3 tr10_post.py /tmp/claude-0/tr-batch-10pkg"""
import sys
from pathlib import Path

pk = Path(sys.argv[1]) / "pages"


def edit(title, fn):
    p = pk / (title.replace(" ", "_").replace("/", "%2F") + ".wiki")
    t = p.read_text(encoding="utf-8")
    n = fn(t)
    print(("edited " if n != t else "UNCHANGED ") + title)
    p.write_text(n, encoding="utf-8")


def marlton(t):
    return t.replace("* '''Players:''' 28\n", "* '''Players:''' 28\n* '''Winner:''' [[Chris Praskac]]<ref name=\"tr-d1135\" />\n", 1)


# the builder now adds the Winner line itself (Claude 2026-10-25)
