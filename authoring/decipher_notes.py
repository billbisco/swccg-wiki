"""Published Decipher.com Deck Designs prose around the card list.

Keep before-list text under == Introduction == immediately before
== Decklist ==, and after-list text under == Strategy == immediately after
the table. Deck info Strategy stays the published title. Do not paste the
card list twice. Empty chrome dests get neither heading.
"""
from __future__ import annotations

import html as htmlmod
import re

TYPE_HINT = re.compile(
    r"<(?:b|strong)>\s*(?:objectives?|characters?|locations?|sites?|effects?|"
    r"interrupts?|starships?|vehicles?|weapons?|creatures?|devices?|"
    r"jedi tests?|admiral'?s orders?|epic events?|ships?|fleet|"
    r"used interrupts?|lost interrupts?|starting)\b",
    re.I,
)
LABEL_KEEP = (
    r"introduction|intro|strategy|notes?|how it works|opening strategy|"
    r"mid-game|end-game|locations?|characters?|starships?|vehicles?|"
    r"weapons?(?: and devices)?|devices?|effects?|used interrupts?|"
    r"lost interrupts?|interrupts?"
)
CHROME_LINE = re.compile(
    r"^(?:"
    r"\d{1,2}/\d{2}(?:/\d{2,4})?\s*[-–].*"
    r"|by\s+.+"
    r"|(?:beginner|intermediate|expert)(?:\s+level)?(?:\s+design)?"
    r"|(?:light|dark)(?:\s+side)?(?:\s+deck)?"
    r"|star wars ccg"
    r"|content by\b.*"
    r"|send us\b.*"
    r"|decipher(?:\.com| inc).*"
    r"|tm\b.*|"
    r"terms and usage"
    r"|all rights reserved.*"
    r"|top|map"
    r")\s*$",
    re.I,
)
DATE_PREFIX = re.compile(r"^\d{1,2}/\d{2}(?:/\d{2,4})?\s*[-–]\s*")
LEVEL_TAIL = re.compile(
    r"\s*(?:beginner|intermediate|expert)(?:\s+level)?(?:\s+design)?\s*$",
    re.I,
)
MAILTO = re.compile(r"<a\s+[^>]*href\s*=\s*['\"]mailto:[^'\"]+['\"][^>]*>(.*?)</a>", re.I | re.S)
FOOTER_CUT = re.compile(
    r"(?:CardListBack|javascript:history|listback\.gif|#EndEditable|TM\s*&|"
    r"<p[^>]*align\s*=\s*['\"]right['\"])",
    re.I,
)
PERSON = re.compile(
    r"^[A-Z][A-Za-z'.\-]+(?:\s+[A-Z][A-Za-z'.\-]+){0,3}$"
)
EVENT_CHROME = re.compile(
    r"(?:open|regional|championship|finals|invitational|grand slam|champs?).*"
    r"(?:winner|winning|champion|runner-?up)|"
    r"(?:winner|winning|champion|runner-?up).*"
    r"(?:light|dark|deck)",
    re.I,
)
FORMAT_SUB = re.compile(
    r"^(?:light|dark)\s+side\s*[-–:].+",
    re.I,
)
OBJECTIVE_ALNUM = {
    "huntdownanddestroythejedi",
    "thereisgoodinhim",
    "bringhimbeforeme",
    "courtofthevilegangster",
    "hiddenbase",
    "localuprising",
    "mindwhatyouhavelearned",
    "ifthemissiledoesnotgetyouthemunitionswill",
    "massassibaseoperations",
    "ralltiiroperations",
    "imperialoccupation",
    "yavin4baseoperations",
    "endoroperations",
    "watchyourstep",
    "youcanrunbutyoucannothide",
    "carbonchambertesting",
    "thisdealisgettingworseallthetime",
    "mykindofscum",
    "heisthechosenone",
    "theyhavenoideawearecoming",
    "noonetostopusthistime",
    "setyourcourseforalderaan",
    "wellhandlethis",
    "iwantthatmap",
    "agentsinthecourt",
    "isboperations",
    "twilekadvisor",
}


def editable_html(raw: str) -> str:
    m = re.search(
        r"SWCCGmaincontent.*?-->(.*)(?:<!--\s*#EndEditable|</BODY>)",
        raw,
        re.I | re.S,
    )
    chunk = m.group(1) if m else raw
    chunk = re.sub(r"<script[\s\S]*?</script>", " ", chunk, flags=re.I)
    chunk = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", chunk)
    chunk = re.sub(r"</table\s*>", "</table>", chunk, flags=re.I)
    return chunk


def _table_spans(html: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    i = 0
    low = html.lower()
    while True:
        start = low.find("<table", i)
        if start < 0:
            break
        depth = 0
        j = start
        while j < len(low):
            nxt_open = low.find("<table", j)
            nxt_close = low.find("</table>", j)
            if nxt_close < 0:
                break
            if nxt_open >= 0 and nxt_open < nxt_close:
                depth += 1
                j = nxt_open + 6
                continue
            depth -= 1
            j = nxt_close + 8
            if depth == 0:
                spans.append((start, j))
                i = j
                break
        else:
            break
        if j >= len(low) and (not spans or spans[-1][0] != start):
            break
    return spans


def split_list_html(chunk: str) -> tuple[str, str]:
    """HTML before and after the card-list table."""
    best: tuple[int, int] | None = None
    best_n = 0
    for start, end in _table_spans(chunk):
        inner = chunk[start:end]
        n = len(TYPE_HINT.findall(inner))
        if n > best_n:
            best_n = n
            best = (start, end)
    if not best or best_n < 1:
        return chunk, ""
    start, end = best
    return chunk[:start], chunk[end:]


def _isolate_header_lines(text: str) -> str:
    """Keep title / date-byline lines from joining the following prose."""
    out: list[str] = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            out.append("")
            continue
        if DATE_PREFIX.match(s) or _is_date_byline(s) or (
            _is_event_chrome(s) and len(s.split()) <= 12
        ):
            out.extend(["", s, ""])
        else:
            out.append(s)
    return "\n".join(out)


def _unwrap(text: str) -> str:
    text = "\n".join(line.strip() for line in text.splitlines())
    paras = []
    for p in re.split(r"\n\s*\n", text):
        line = re.sub(r"\s*\n\s*", " ", p).strip()
        if line:
            paras.append(line)
    return "\n\n".join(paras)


def _protect_wiki(p: str) -> str:
    if p[:1] in "*#;:= " or p.startswith("="):
        return "<nowiki></nowiki>" + p
    return p


def _alnum(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def _is_heading_chrome(s: str) -> bool:
    """Objective / published-title line with no real sentence."""
    if len(s) > 80:
        return False
    if re.match(r"^Game\s+\d+", s, re.I):
        return False
    if re.search(r"[.!]", s):
        return False
    key = _alnum(s)
    if key in OBJECTIVE_ALNUM:
        return True
    if FORMAT_SUB.match(s) and len(s.split()) <= 12:
        return True
    words = re.findall(r"[A-Za-z']+", s)
    if not words or len(words) > 12:
        return False
    prose = {
        "deck", "decks", "this", "these", "here", "thanks", "sent", "used",
        "play", "start", "pretty", "just", "below", "follows", "includes",
        "because", "created", "based", "never", "always",
    }
    if any(w.lower() in prose for w in words):
        return False
    small = {"the", "of", "and", "a", "an", "in", "him", "is", "for", "that", "to", "or", "no", "us", "what", "you", "have", "your"}
    cap = sum(1 for w in words if w[0].isupper() or w.lower() in small)
    return cap >= len(words) * 0.8


def _has_prose_marker(s: str) -> bool:
    return bool(
        re.search(
            r"\b(this|these|here's|here is|used in|because|pretty|below|follows)\b",
            s,
            re.I,
        )
    )


def _is_date_byline(s: str) -> bool:
    if not re.search(r"\d{1,2}/\d{2}(?:/\d{2,4})?\s*[-–]\s*[A-Za-z]", s):
        return False
    return not _has_prose_marker(s)


def _is_event_chrome(s: str) -> bool:
    if not EVENT_CHROME.search(s) or len(s) > 110:
        return False
    if _has_prose_marker(s):
        return False
    if _is_date_byline(s):
        return True
    return not re.search(r"(?<![A-Z])\.(?![A-Z.])", s)


def _is_chrome(line: str) -> bool:
    s = line.strip().strip('"“”')
    s = re.sub(r"^[-–—]\s*", "", s)
    if not s:
        return True
    if CHROME_LINE.match(s):
        return True
    if re.fullmatch(r"\d{1,2}/\d{2}(?:/\d{2,4})?", s):
        return True
    if re.search(
        r"closed circuit video|streaming video lasts|go to deciphercon|choose the streaming option",
        s,
        re.I,
    ):
        return True
    if re.match(r"^(?:final(?:s| match)? deck,?\s*)?deciphercon\b", s, re.I) and len(s) < 60:
        return True
    if PERSON.match(s) and len(s.split()) <= 4:
        return True
    if re.match(
        r"^[A-Z][A-Za-z'.\-]+(?:\s+[A-Z][A-Za-z'.\-]+){0,3}\s*,\s*'*(?:champion|runner-?up|winner)",
        s,
        re.I,
    ):
        return True
    if _is_event_chrome(s):
        return True
    if _is_date_byline(s) and len(s) < 160:
        return True
    if re.fullmatch(r"[A-Za-z0-9 .,'\"!?:/\-]{1,80}", s) and LEVEL_TAIL.search(s):
        if len(s.split()) <= 10:
            return True
    if re.fullmatch(r"(?:light|dark)\s+deck\b.*", s, re.I) and len(s) < 80:
        return True
    if re.search(r"(?:light|dark)\s+side\s+deck\s*$", s, re.I) and len(s) < 90 and not _has_prose_marker(s):
        return True
    if re.search(r"\b\d+\s*card\b", s, re.I) and re.search(r"(?:junior|light|dark)\s+.*deck", s, re.I) and len(s) < 90:
        return True
    if "@" in s and len(s.split()) <= 8:
        return True
    if _is_heading_chrome(s):
        return True
    return False


def _is_title_line(p: str, title_norm: str) -> bool:
    if not title_norm:
        return False
    low = _alnum(p)
    t = _alnum(title_norm)
    if not t or not low:
        return False
    if low == t:
        return True
    if t in low and len(low) <= len(t) + 30:
        return True
    if low in t and len(low) >= 16:
        return True
    return False


def html_to_notes(html: str, *, drop_title: str = "") -> str:
    if not html:
        return ""
    cut = FOOTER_CUT.search(html)
    if cut:
        html = html[: cut.start()]
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    html = re.sub(r"<[^>]*$", " ", html)
    quotes: list[str] = []

    def keep_quote(m: re.Match) -> str:
        inner = html_to_notes(m.group(1), drop_title="")
        if not inner:
            return ""
        quotes.append(inner)
        return f"\n\n@@QUOTE{len(quotes) - 1}@@\n\n"

    html = re.sub(r"<blockquote\b[^>]*>(.*?)</blockquote>", keep_quote, html, flags=re.I | re.S)
    html = MAILTO.sub(r"\1", html)
    html = re.sub(r"<a\s+[^>]*>", "", html, flags=re.I)
    html = re.sub(r"</a>", "", html, flags=re.I)
    html = re.sub(
        rf"<(?:b|strong)>\s*({LABEL_KEEP})\s*:?\s*</(?:b|strong)>",
        lambda m: f"'''{m.group(1)}:'''",
        html,
        flags=re.I,
    )
    html = re.sub(r"<(?:b|strong)>(.*?)</(?:b|strong)>", r"\1", html, flags=re.I | re.S)
    html = re.sub(r"<(?:i|em)>(.*?)</(?:i|em)>", r"''\1''", html, flags=re.I | re.S)
    html = re.sub(r"<br\s*/?>\s*<br\s*/?>", "\n\n", html, flags=re.I)
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    html = re.sub(r"</p>", "\n\n", html, flags=re.I)
    html = re.sub(r"<p\b[^>]*>", "", html, flags=re.I)
    html = re.sub(r"</(?:div|h[1-6]|li|tr|td)>", "\n", html, flags=re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    html = htmlmod.unescape(html)
    html = html.replace("\u2019", "'").replace("\u2018", "'")
    html = html.replace("\u201c", '"').replace("\u201d", '"')
    text = _unwrap(_isolate_header_lines(html))
    title_norm = re.sub(r"\s+", " ", drop_title).strip().lower() if drop_title else ""
    kept: list[str] = []
    skipped_title = not bool(title_norm)
    for para in text.split("\n\n"):
        p = re.sub(r"[ \t]+", " ", para).strip()
        p = DATE_PREFIX.sub("", p).strip(" ,-")
        p = re.sub(r"^[-–—]\s*", "", p)
        p = re.sub(r"<[^>]*$", "", p).strip()
        if p.startswith("''") and p.endswith("''") and not p.startswith("'''"):
            p = p[2:-2].strip()
        if p.startswith("'''") and p.endswith("'''") and p.count("'''") == 2:
            inner = p[3:-3].strip()
            if inner and "'''" not in inner:
                p = inner
        if not p:
            continue
        if p.startswith("@@QUOTE") and p.endswith("@@"):
            kept.append(p)
            continue
        empty_label = re.match(
            rf"^'''\s*({LABEL_KEEP})\s*:?\s*'''\s*$",
            p,
            flags=re.I,
        )
        if empty_label:
            kept.append(f"'''{empty_label.group(1).lower()}:'''")
            continue
        if not skipped_title and _is_title_line(p, title_norm):
            skipped_title = True
            continue
        if _is_chrome(p):
            continue
        if re.match(r"^<[^>]*$", p) or re.match(r"^</?\w+\b", p):
            continue
        if not p:
            continue
        kept.append(_protect_wiki(p))
    out = "\n\n".join(kept)
    for i, q in enumerate(quotes):
        block = f"<blockquote>\n{q}\n</blockquote>"
        out = out.replace(f"@@QUOTE{i}@@", block)
    out = re.sub(r"\n{3,}", "\n\n", out).strip()
    if len(re.sub(r"\W+", "", out)) < 25:
        return ""
    return out


def parse_article_notes(raw: str, *, pub_title: str = "") -> tuple[str, str]:
    chunk = editable_html(raw)
    before_html, after_html = split_list_html(chunk)
    before = html_to_notes(before_html, drop_title=pub_title)
    after = html_to_notes(after_html, drop_title="")
    return before, after


def inject_strategy(wiki: str, before: str, after: str) -> str:
    """Insert Introduction before Decklist and Strategy after the live 60."""
    wiki = wiki.replace("\r\n", "\n")
    heading = r"\n== (?:Introduction|Strategy) ==\n.*?"
    for _ in range(2):
        wiki = re.sub(
            heading + r"(?=\n== Decklist ==)",
            "",
            wiki,
            count=1,
            flags=re.S,
        )
        wiki = re.sub(
            heading + r"(?=\n== See also ==)",
            "",
            wiki,
            count=1,
            flags=re.S,
        )
    wiki = re.sub(r"\n{3,}(?=== Decklist ==)", "\n\n", wiki)
    wiki = re.sub(r"\n{3,}(?=== See also ==)", "\n\n", wiki)
    if before:
        if "== Decklist ==" not in wiki:
            raise ValueError("missing Decklist heading")
        wiki = wiki.replace(
            "== Decklist ==",
            f"== Introduction ==\n\n{before}\n\n== Decklist ==",
            1,
        )
    if after:
        m = re.search(r"== Decklist ==\n+\{\|.*?^\|\}\n", wiki, re.S | re.M)
        if not m:
            raise ValueError("missing Decklist table")
        wiki = wiki[: m.end()] + f"\n== Strategy ==\n\n{after}\n" + wiki[m.end() :]
    return wiki
