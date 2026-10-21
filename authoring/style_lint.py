#!/usr/bin/env python3
"""Pre-save style lint for wiki.swccg.com articles (SWCCG Wiki:Style guide).

Usage:
  style_lint.py "Page title"            # lint current revision, compare to previous
  style_lint.py page.wiki [--title T]   # lint a local draft; with --title, compare to live page
Exit 1 if any flag is raised.

Citation checks (Bill, 2026-10-20; SWCCG Wiki:Style guide):
  ARCHIVE  every external URL cited on the page (<ref>, list items, body, External links) needs a
           Preserved copy: a web.archive.org/web/<14 digits>/<url> or archive.org/details link.
           A URL inside a <ref> needs the copy inside that same <ref>; a URL anywhere else passes
           if its own line has a copy or the same URL has a Wayback copy anywhere on the page. A Wayback
           capture of swccg.com/snapshots/forum/tNNNNN.html (or forum-tNNNNN.html) counts as a copy of
           forum.starwarsccg.org viewtopic.php?t=NNNNN, and one of swccg.com/snapshots/pc/<slug>.html as a
           copy of the www.starwarsccg.org URL ending in /<slug>/ (Chief, 2026-10-20).
           Skipped: wiki.swccg.com, swccg.com/images and the archive links themselves.
           Exempt: the Main Page (its body links are navigation to live resources, not
           citations; Chief, 2026-10-20). Its URLs are still queued for Wayback.
           Talk pages (Chief, 2026-10-20): a URL passes if a Preserved copy of it appears anywhere
           on the page, including a Wayback capture of swccg.com/snapshots/forum/tNNNNN.html for a
           forum.starwarsccg.org viewtopic.php?t=NNNNN link, and of swccg.com/snapshots/pc/<slug>.html
           for a www.starwarsccg.org URL whose last path segment is <slug>.
Talk pages (Chief, 2026-10-20): signed comments by other accounts are their authors' words. The
  banned-word, hedge and long-sentence checks skip any comment whose signature is not the bot's own
  (Comlink Cursor); the bot's comments, unsigned text and the other checks still apply.
  EMAIL    personal email addresses (decipher.com addresses and lines marked "email-ok" pass).
  REF      a <ref> with no URL and no source text.
  HEADING  a == Sources == section on a page that is not a deck, event, card or set-table page. Deck/event pages
           are detected by category: Decklists, Dark Side decks, Light Side decks, GEMP
           importable decklists, Tournaments, Championships, World Championships, Events,
           Retro League (in the wikitext, plus the live page's categories when linting by title).
           Card pages ({{Card}} or Category:Cards) and set-table pages (Category:Sets or any
           "... sets" category) may also keep Sources (Bill, 2026-10-20).
           Only a heading written in the page's own wikitext fails. A heading a template generates
           (Template:Card's == Sources ==, inside <includeonly>) is exempt, both on the template
           page and on the pages that transclude it (Chief, 2026-10-20).
"""
import json, re, sys, urllib.parse, urllib.request, argparse, os

API = "https://wiki.swccg.com/api.php"
BANNED = ["note", "research", "this pass", "not found", "no source", "unverified", "soft", "reportedly",
          "appears to", "appear to", "it is unclear", "unclear", "pending", "inferred", "is said to",
          "allegedly", "apparently", "possibly", "probably", "likely", "seems", "gaps", "we ", "this page",
          "this article", "see talk", "according to sources"]
BAD_HEADINGS = {"gaps", "notes", "research", "open questions", "sources", "research notes", "notes and gaps"}
CAPTION_WORDS = ["shows", "showing", "visible", "left", "right", "pictured", "depicts", "seen", "background",
                 "foreground", "top", "bottom", "behind"]
MAX_SENT = 30
MAX_CAPTION = 12

def fetch(title, n=2):
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "revisions", "rvprop": "content|ids",
                                "rvslots": "main", "rvlimit": n, "format": "json", "formatversion": 2})
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": "swccg-style-lint/1.0"})
    p = json.load(urllib.request.urlopen(req, timeout=60))["query"]["pages"][0]
    return [(r["revid"], r["slots"]["main"]["content"]) for r in p.get("revisions", [])]

def captions(t):
    out = []
    for m in re.finditer(r"\[\[(?:File|Image):[^\[\]]*?(?:\[\[[^\]]*\]\][^\[\]]*?)*\]\]", t):
        parts = re.split(r"\|(?![^\[]*\]\])", m.group(0)[2:-2])
        cap = [p for p in parts[1:] if not re.fullmatch(r"\s*(thumb|thumbnail|frame|frameless|left|right|center|none|upright[=\d.]*|\d+(x\d+)?px|alt=.*|link=.*)\s*", p)]
        if cap: out.append(cap[-1])
    for g in re.finditer(r"<gallery[^>]*>(.*?)</gallery>", t, re.S):
        for line in g.group(1).splitlines():
            if "|" in line: out.append(line.split("|", 1)[1])
    return out

def body(t):
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<ref[^>/]*/>", " ", t)
    t = re.sub(r"<ref[^>]*>.*?</ref>", " ", t, flags=re.S)
    t = re.sub(r"<references[^>]*>.*?</references>|<references\s*/>", " ", t, flags=re.S)
    t = re.sub(r"<gallery[^>]*>.*?</gallery>", " ", t, flags=re.S)
    for _ in range(3): t = re.sub(r"^\{\|(?:(?!^\{\|).)*?^\|\}", " ", t, flags=re.S | re.M)
    for _ in range(3): t = re.sub(r"\{\{[^{}]*\}\}", " ", t)
    for _ in range(3): t = re.sub(r"\[\[(?:File|Image|Category):[^\[\]]*(?:\[\[[^\]]*\]\][^\[\]]*)*\]\]", " ", t)
    # drop See also / References sections entirely; External links stays in (Bill, 2026-10-20),
    # minus its link titles (those are the linked page's own wording)
    t = re.sub(r"^==\s*(?:See also|References)\s*==.*?(?=^==[^=]|\Z)", " ", t, flags=re.M | re.S | re.I)
    t = re.sub(r"(^==\s*External links\s*==.*?)(?=^==[^=]|\Z)",
               lambda m: re.sub(r"\[https?://[^\]]*\]", " ", m.group(1)), t, flags=re.M | re.S | re.I)
    t = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\[\[([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\[https?://\S+\s([^\]]*)\]", r"\1", t)
    t = re.sub(r"<br\s*/?>", "\n", t, flags=re.I)
    t = re.sub(r"'''?|<[^>]+>|^[*#:;]+", "", t, flags=re.M)
    return t

def words(t): return len(re.findall(r"[A-Za-z0-9][\w'’.-]*", re.sub(r"^=+.*?=+\s*$", "", t, flags=re.M)))

def unquote(t):
    return re.sub(r"\"[^\"\n]*\"|“[^”\n]*”", " ", t)

def is_list_page(title, text):
    return bool(title and "/" in title) or body(text).lstrip().lower().startswith("this page lists")

# Deck and event pages keep a == Sources == list (decklist URL + Preserved copy); no other page does.
SOURCES_CATEGORIES = {"decklists", "dark side decks", "light side decks", "gemp importable decklists",
                      "tournaments", "championships", "world championships", "events", "retro league"}

def page_categories(text):
    return {re.sub(r"[\s_]+", " ", c).strip().lower()
            for c in re.findall(r"\[\[\s*Category\s*:\s*([^\]|]+)", text, re.I)}

# Pages whose body links are navigation, not citations (Chief, 2026-10-20): no ARCHIVE check.
ARCHIVE_EXEMPT_TITLES = {"main page"}

def norm_title(title):
    return re.sub(r"[\s_]+", " ", title or "").strip().lower()

def archive_exempt(title):
    return norm_title(title) in ARCHIVE_EXEMPT_TITLES

def own_headings(text):
    """Headings written in the page's own wikitext. Template output (the <includeonly> part of a
    template page) is not the page's own heading: it renders on the pages that transclude it."""
    t = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    t = re.sub(r"<includeonly>.*?(?:</includeonly>|\Z)", " ", t, flags=re.S | re.I)
    return re.findall(r"^=+\s*(.*?)\s*=+\s*$", t, re.M)

# Bill, 2026-10-20 (Sources vs References): a Sources list is also allowed on pages that transcribe a
# single source: card pages (pages using Template:Card, or in Category:Cards) and set-table pages
# (Category:Sets or any "... sets" category, e.g. Decipher sets, Virtual Legacy sets).
CARD_TEMPLATE_RX = re.compile(r"\{\{\s*(?:Template\s*:\s*)?Card\s*(?:\||\n|\}\})", re.I)
CARD_CATEGORIES = {"cards"}

def is_set_category(c):
    return c == "sets" or c.endswith(" sets")

def allows_sources(text, cats=None):
    have = page_categories(text) | {re.sub(r"^Category:", "", c, flags=re.I).strip().lower() for c in (cats or ())}
    if have & (SOURCES_CATEGORIES | CARD_CATEGORIES) or any(is_set_category(c) for c in have):
        return True
    return bool(CARD_TEMPLATE_RX.search(re.sub(r"<!--.*?-->", " ", text, flags=re.S)))


# Preserved copies (Bill, 2026-10-20): every cited external URL needs a Wayback / archive.org copy.
URL_RX = re.compile(r"https?://[^\s\[\]|<>\"{}]+", re.I)
ARCHIVE_LINK_RX = re.compile(r"https?://(?:web\.archive\.org/web/\d{14}(?:[a-z]{2}_)?/\S|archive\.org/details/\S)", re.I)
WAYBACK_RX = re.compile(r"https?://web\.archive\.org/web/\d{14}(?:[a-z]{2}_)?/((?:https?://)?[^\s\[\]|<>\"{}]+)", re.I)
SKIP_URL_RX = re.compile(r"https?://(?:[\w-]+\.)*(?:archive\.org|archive\.ph|archive\.today|archive\.is|archive\.li|"
                         r"wiki\.swccg\.com)(?=[/:?#]|$)|https?://(?:www\.)?swccg\.com/images/", re.I)
REF_RX = re.compile(r"<ref\b[^>]*?(?<!/)>(.*?)</ref\s*>", re.S | re.I)

def clean_url(u):
    u = u.replace("&amp;", "&")
    while u and u[-1] in ".,;:!?'\u2019\"":
        u = u[:-1]
    while u.endswith(")") and u.count(")") > u.count("("):
        u = u[:-1]
    return u

def norm_url(u):
    u = clean_url(u).split("#", 1)[0]
    u = re.sub(r"^(?:https?:)?//", "", u, flags=re.I)
    u = re.sub(r"^www\.", "", u, flags=re.I)
    host, _, rest = u.partition("/")
    return (host.lower().split(":", 1)[0] + ("/" + rest if rest else "")).rstrip("/")

def cited_units(text):
    """(kind, text) units: each <ref> body, then each remaining line that carries a URL."""
    t = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    t = re.sub(r"<nowiki>.*?</nowiki>", " ", t, flags=re.S | re.I)
    for m in REF_RX.finditer(t):
        yield "ref", m.group(1)
    for line in REF_RX.sub(" ", t).splitlines():
        if URL_RX.search(line):
            yield "line", line

# Talk pages (Chief, 2026-10-20): a Preserved copy anywhere on the page counts, and a capture of the
# swccg.com forum snapshot (forum/tNNNNN.html, or the older flat forum-tNNNNN.html) covers that thread.
FORUM_THREAD_RX = re.compile(r"^forum\.starwarsccg\.org/viewtopic\.php\?(?:[^#]*&)?t=(\d+)(?:[&#]|$)", re.I)
FORUM_SNAPSHOT_RX = re.compile(r"^swccg\.com/snapshots/forum[/-]t(\d+)\.html$", re.I)
# Players Committee posts (archiving.md "Players Committee news"): the snapshot is pc/<post-slug>.html, where
# <post-slug> is the last path segment of the www.starwarsccg.org URL. Checked against every live-URL +
# snapshot-capture pair in the wiki backup (pages/, 2026-10-21: 5,282 pairs, no exceptions).
PC_POST_RX = re.compile(r"^starwarsccg\.org/(?:[^?#]*/)?([^/?#]+)$", re.I)
PC_SNAPSHOT_RX = re.compile(r"^swccg\.com/snapshots/pc/([^/?#]+)\.html$", re.I)

def archive_keys(url):
    """Keys under which a cited URL counts as archived: its normalised URL, plus its forum thread."""
    n = norm_url(url)
    keys = {n}
    m = FORUM_THREAD_RX.match(n) or FORUM_SNAPSHOT_RX.match(n)
    if m: keys.add(f"forum-thread:{m.group(1)}")
    m = PC_POST_RX.match(n) or PC_SNAPSHOT_RX.match(n)
    if m: keys.add(f"pc-post:{m.group(1).lower()}")
    return keys

def archive_flags(text, talk=False):
    # A capture of the swccg.com snapshot counts like a direct capture of the forum thread / PC post it
    # preserves, on articles and Talk pages alike (Chief, 2026-10-20).
    archived = set().union(*(archive_keys(m.group(1)) for m in WAYBACK_RX.finditer(text)))
    out, seen = [], set()
    for kind, unit in cited_units(text):
        unit_has_copy = bool(ARCHIVE_LINK_RX.search(unit))
        for raw in URL_RX.findall(unit):
            url = clean_url(raw)
            if SKIP_URL_RX.match(url) or url in seen:
                continue
            if talk and (unit_has_copy or archive_keys(url) & archived):
                continue
            if kind == "ref":
                if unit_has_copy: continue
                msg = f"ARCHIVE  <ref> cites {url} with no Preserved copy (Wayback/archive.org) in the same <ref>"
            else:
                if unit_has_copy or archive_keys(url) & archived: continue
                msg = f"ARCHIVE  {url} has no Preserved copy (Wayback/archive.org) on the page"
            seen.add(url); out.append(msg)
    return out


# Personal email addresses (Bill, 2026-10-14). Decipher corporate addresses and Players Committee role
# addresses (rules@starwarsccg.org, ...) are organisational, not personal.
EMAIL_RX = re.compile(r"(?<![\w.%+-])[A-Za-z0-9][A-Za-z0-9._%+-]*@(?:[A-Za-z0-9-]+\.)+([A-Za-z]{2,})\b")
EMAIL_OK_DOMAINS = re.compile(r"@(?:[\w-]+\.)*decipher\.com$|^(?:rules|design|marketing|multimedia|communications|"
                              r"webmaster|info|tournaments|events|gemp|errata|ocs|leagues?)@(?:www\.)?starwarsccg\.org$", re.I)
FILE_EXT = {"png", "jpg", "jpeg", "gif", "svg", "webp", "pdf", "txt", "htm", "html", "tif", "tiff", "bmp", "zip", "wiki"}

def email_flags(text):
    out = []
    for line in re.sub(r"<!--(?!\s*email-ok).*?-->", " ", text, flags=re.S).splitlines():
        if re.search(r"email-ok", line, re.I): continue
        scan = re.sub(r"https?://[^\s\[\]|<>\"]+", " ", line, flags=re.I)
        for m in EMAIL_RX.finditer(scan):
            if m.group(1).lower() in FILE_EXT or EMAIL_OK_DOMAINS.search(m.group(0)): continue
            out.append(f"EMAIL    personal email address on the page: {m.group(0)}")
    return out


def ref_flags(text):
    out = []
    t = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    for m in REF_RX.finditer(t):
        b = m.group(1)
        if URL_RX.search(b): continue
        plain = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]", r"\1", b)
        plain = re.sub(r"<[^>]+>|'{2,}|[{}\[\]|=]", " ", plain)
        if len(re.findall(r"[^\W\d_]{2,}", plain)) < 2:
            out.append(f"REF      <ref> has no URL and no source text: {' '.join(m.group(0).split())[:90]}")
    return out


# Service rule (Bill, 2026-10-14): any service named in a person page's prose needs a row in == Service ==.
SERVICE_TERMS = {
    "tournament director": r"tournament director|\bTDs?\b|TD'?d",
    "judge": r"\b(?:was|is|as|became) an? (?:head )?judge\b|\bjudged (?:at|the)\b|\bjudging at\b",
    "Squadron": r"\bSquadron Member\b(?! tables?| lists?| roster)|\b(?:Red|Gold|Blue|Green|Bravo|Rogue) \d+\b(?!'s)|\bSquadron Leader|\bGold Leader",
    "volunteer": r"\bvolunteer(?:ed|s)?\b",
    "Players Committee": r"\b(?:member|volunteer|advocate|chair)s? (?:of|for|on) the Players'? Committee|\bPC (?:member|advocate|chair)|(?<![-\d] )(?<!-)\badvocate\b(?! award)(?!\))",
    "Decipher": r"\bDecipherian\b|worked (?:at|for) Decipher|Decipher employee|(?<!independent )Decipher staff(?:er)?\b(?! [A-Z][a-z]+ [A-Z])",
    "host": r"\bhost(?:ed|s|ing)? (?:a|an|the|three|two|several|\d+)\b|\boriginal host\b",
    "organizer": r"\borganiz(?:ed|er|es|ing) (?:the|a|an)\b|\b(?:league|event|tournament)'?s? organizer\b|\bran (?:the|an|a)\b",
    "GEMP/dev": r"\bslicer\b|\bdeveloper\b|\bcoder\b|\bprogrammer\b",
}
SERVICE_ACCEPT = {
    "tournament director": r"tournament director|\bTDs?\b|\bran\b|organi[sz]|director|host",
    "judge": r"judge",
    "Squadron": r"Squadron",
    "volunteer": r"Players'? Committee|\bPC\b|Advocate|orgchart|organi[sz]ation chart|team|Council|volunteer|Squadron",
    "Players Committee": r"Players'? Committee|\bPC\b|Advocate|orgchart|organi[sz]ation chart|team|Council",
    "Decipher": r"Decipher",
    "host": r"host|organi[sz]|\bran\b|director",
    "organizer": r"host|organi[sz]|\bran\b|director",
    "GEMP/dev": r"GEMP|slicer|develop|coder|program",
}
def is_person_page(text):
    if re.search(r"\[\[Category:(?:Teams|Star Wars CCG teams|Organizations)\b", text, re.I): return False
    lead = body(text).lstrip()[:300]
    # handle redirects-in-prose and articles about a feature/card are not person pages
    if re.search(r"^[^\n.]{0,80}? is (?:the (?:forum |GEMP |online )?handle of|an? (?:[\w-]+ ){0,4}(?:feature|article|card|interview|poll)\b)", lead): return False
    return bool(re.search(r"\[\[Category:(?:Players|People|Decipher Squadron Members|Decipherians|Tournament Directors)\s*(?:\||\]\])", text, re.I)) or "== Tournament Results ==" in text or "== Squadron listing ==" in text

def service_flags(text, title=None):
    if not is_person_page(text): return []
    m = re.search(r"^==\s*Service\s*==\s*$(.*?)(?=^==[^=]|\Z)", text, re.M | re.S)
    svc = body(m.group(1)) + " " + (m.group(1) if m else "") if m else ""
    rest = text if not m else text[:m.start()] + text[m.end():]
    # prose only: drop tables and the Squadron listing / Tournament Results sections
    prose = body(re.sub(r"^==\s*(?:Tournament Results|Retro League|Squadron listing)\s*==.*?(?=^==[^=]|\Z)", "", rest, flags=re.M | re.S | re.I))
    prose = unquote(re.sub(r"^=+.*?=+\s*$", "", prose, flags=re.M))
    out = []
    for name, rx in SERVICE_TERMS.items():
        for mm in re.finditer(rx, prose, re.I if name not in ("tournament director",) else 0):
            # someone else did it: a capitalised non-subject word right before "ran a"/"hosted" etc.
            if name in ("organizer", "host") and re.search(r"\b(?!He\b|She\b|They\b)[A-Z][a-z]+ $", prose[max(0, mm.start()-30):mm.start()]) and not (title and prose[max(0, mm.start()-30):mm.start()].split()[-1] in title.split()): continue
            # PC/volunteer: any existing Service row counts (orgchart-sourced pages)
            if m and name in ("volunteer", "Players Committee") and re.search(r"^\|(?![-}])", m.group(1), re.M): break
            ctx = " ".join(prose[max(0, mm.start()-50):mm.end()+50].split())
            if not m: out.append(f"SERVICE  '{mm.group(0)}' in prose but page has no == Service == table: …{ctx}…")
            elif not re.search(SERVICE_ACCEPT[name], m.group(1), re.I): out.append(f"SERVICE  '{mm.group(0)}' in prose has no matching Service row: …{ctx}…")
            break
    return out

# Card titles and link text are names, not the editor's voice (Chief, 2026-10-20): the banned-word
# check skips [[link text]], [url link titles] (templates such as {{CardLink|...}} are already
# stripped by body()) and printed card titles from card_title_map.json ("We Have A Prisoner",
# "Probably Not...", "Note The Drop" ...).
CARD_TITLE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "card_title_map.json")
_card_titles = None

def card_title_phrases():
    """Printed card titles (and each half of a combo card) that contain a banned word, longest first."""
    global _card_titles
    if _card_titles is None:
        try:
            with open(CARD_TITLE_FILE, encoding="utf-8") as fh:
                names = set(json.load(fh).values())
        except (OSError, ValueError):
            names = set()
        phrases = set()
        for n in names:
            n = n.replace("\u2022", "").replace("&amp;", "&")
            n = re.sub(r"\s*\([^()]*\)", "", n).strip()   # (V), (Dark), (AI), (Virtual Block 5) ...
            for part in [n] + [x.strip() for x in re.split(r" & | / ", n)]:
                if len(part.split()) >= 2 and any(re.search(rf"\b{re.escape(w.strip())}\b", part, re.I) for w in BANNED):
                    phrases.add(part)
        _card_titles = sorted(phrases, key=len, reverse=True)
    return _card_titles

# The page's own bold name and a decklist's title are names too (Chief, 2026-10-20): the lead's
# '''We'll Handle This''' on a deck page, any bold span equal to the page title, and the title on a
# decklist title line ('''Deck title:''' ... / Sheet deck title '''...''') are not scanned for "we".
DECK_TITLE_LINE = re.compile(r"^([*#:;\s]*'''\s*(?:deck|decklist|list)\s*(?:title|name)\s*:?\s*'''\s*:?)[^\n]*$", re.I | re.M)
DECK_TITLE_BOLD = re.compile(r"(\b(?:deck|decklist|list)\s+(?:title|name)\s*:?\s*)'''(?:(?!''')[^\n])+'''", re.I)

def mask_page_name(t, title=None):
    """Blank the page's bold name in the lead, bold spans equal to the title, and decklist titles."""
    lead = re.split(r"^==", t, maxsplit=1, flags=re.M)[0]
    m = re.search(r"^'''((?:(?!''')[^\n])+)'''(?=[^\n]*\w)", lead, re.M)   # bold name opening the first prose line
    if m and (len(m.group(1).split()) >= 2 or (title and m.group(1).strip() == title.strip())):
        t = t[:m.start()] + " " + t[m.end():]
    if title:
        t = re.sub(r"'''\s*" + re.escape(title.strip()) + r"\s*'''", " ", t)
    t = DECK_TITLE_LINE.sub(r"\1 ", t)
    t = DECK_TITLE_BOLD.sub(r"\1 ", t)
    return t

def mask_names(t, title=None):
    """Blank out link text, card titles and the page's own name so the banned-word scan does not read them."""
    t = mask_page_name(t, title)
    t = re.sub(r"\[\[(?!\s*(?:File|Image|Category)\s*:)[^\[\]]*\]\]", " ", t, flags=re.I)
    t = re.sub(r"\[(?:https?:)?//[^\s\]]+\s[^\]]*\]", " ", t, flags=re.I)
    t = t.replace("&amp;", "&").replace("\u2022", "")
    for ph in card_title_phrases():
        if ph in t:
            t = re.sub(rf"(?<![\w'])(?:{re.escape(ph)})(?![\w'])", " ", t)
    return t

# Transcript pages (Chief, 2026-10-20): quoted speech is the speaker's words, not the editor's voice.
# A page is a transcript when its title ends in "(transcript)" (or a "/Transcript" subpage) or it is in
# Category:Transcripts; on such pages each speaker turn ('''[00:10] Henry Dunn:''' ... or '''Interviewer:''' ...)
# is skipped by the banned-word and sentence-length checks. The page's own prose is still checked.
TRANSCRIPT_TITLE_RX = re.compile(r"\(\s*transcripts?\s*\)\s*$|/\s*transcripts?\s*$", re.I)
TRANSCRIPT_CATEGORIES = {"transcripts", "interview transcripts"}
SPEECH_RX = re.compile(r"^[*:#]*[ \t]*'''[ \t]*(?:\[\d{1,2}(?::\d{2}){1,2}\][ \t]*)?[^'\n:\[\]]{1,60}:[ \t]*'''.*$", re.M)

def is_transcript_page(title, text, cats=None):
    if title and TRANSCRIPT_TITLE_RX.search(title.strip()):
        return True
    have = page_categories(text) | {re.sub(r"^Category:", "", c, flags=re.I).strip().lower() for c in (cats or ())}
    return bool(have & TRANSCRIPT_CATEGORIES)

EDITORIAL_LABELS = {"note", "notes", "editor's note", "editors' note", "source", "sources", "summary", "context", "transcription"}

def mask_speech(text):
    """Blank each speaker turn (a line opening with a bold 'Speaker:' label, optionally timestamped).
    Editorial labels ('''Note:''', '''Source:''' ...) are the editor's voice and stay in."""
    def blank(m):
        label = re.sub(r"^[*:#\s]*'''\s*(?:\[[\d:]+\]\s*)?", "", m.group(0)).split(":", 1)[0].strip().lower()
        return m.group(0) if label in EDITORIAL_LABELS else " "
    return SPEECH_RX.sub(blank, text)

# Talk pages (Chief, 2026-10-20): other editors' signed comments are their own words, so the banned-word,
# hedge and long-sentence checks skip them. A comment is the block of lines that ends with a signature
# line ([[User:X|...]] followed by a "HH:MM, D Month YYYY (UTC)" timestamp) and starts after the previous
# signature line or level-2 (== ==) heading; sub-headings (=== ===) inside it belong to the comment.
# A block counts as the bot's own when any signer on its signature line is Comlink Cursor, or when it
# is signed with an unexpanded ~~~~ (a draft the bot is about to save).
TALK_TITLE_RX = re.compile(r"^\s*(?:(?:User|SWCCG[ _]Wiki|Project|File|Image|MediaWiki|Template|Help|Category)[ _])?talk\s*:", re.I)
BOT_ACCOUNTS = {"comlink cursor"}
SIG_USER_RX = re.compile(r"\[\[\s*User\s*:\s*([^|\]]+)", re.I)
SIG_TIME_RX = re.compile(r"\d{1,2}:\d{2},\s*\d{1,2}\s+[A-Z][a-z]+\s+\d{4}\s*\(UTC\)")
LEVEL2_RX = re.compile(r"^==[^=].*?[^=]==\s*$")

def is_talk_page(title):
    return bool(title and TALK_TITLE_RX.match(title))

def signers(line):
    """Accounts signing this line (a User link before a timestamp), '~~~~' for an unexpanded signature."""
    out = set()
    if "~~~~" in line: out.add("~~~~")
    for m in SIG_USER_RX.finditer(line):
        if SIG_TIME_RX.search(line, m.end()):
            out.add(re.sub(r"[\s_]+", " ", m.group(1)).strip().lower())
    return out

def mask_foreign_comments(text):
    """Blank signed comments whose signers are all accounts other than the bot (line count kept)."""
    lines = text.split("\n")
    start = 0
    for i, line in enumerate(lines):
        if LEVEL2_RX.match(line):
            start = i + 1
            continue
        who = signers(line)
        if not who: continue
        if not (who & (BOT_ACCOUNTS | {"~~~~"})):
            for j in range(start, i + 1):
                lines[j] = ""
        start = i + 1
    return "\n".join(lines)

def lint(text, title=None, cats=None):
    flags = []
    for h in own_headings(text):
        hl = h.strip().lower()
        if hl == "sources" and allows_sources(text, cats): continue
        if hl == "sources":
            flags.append("HEADING  'Sources' is only for deck, event, card and set-table pages; cite sources as <ref> in References "
                         "(Preserved copy inside each ref) and keep further reading in External links")
            continue
        if hl in BAD_HEADINGS: flags.append(f"HEADING  '{h}' is not allowed")
    for c in captions(text):
        plain = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]|\[\[([^\]]*)\]\]", lambda m: m.group(1) or m.group(2), c)
        n = len(plain.split())
        if n > MAX_CAPTION: flags.append(f"CAPTION  {n} words (> {MAX_CAPTION}): {plain[:90]}")
        for wd in CAPTION_WORDS:
            if re.search(rf"\b{wd}\b", plain, re.I): flags.append(f"CAPTION  describes image ('{wd}'): {plain[:90]}")
    b = body(text)
    own = mask_speech(text) if is_transcript_page(title, text, cats) else text   # transcripts: skip speech
    talk = is_talk_page(title)
    if talk: own = mask_foreign_comments(own)                                   # Talk: skip others' comments
    prose = re.sub(r"^=+.*?=+\s*$", "", body(own), flags=re.M)
    scan = unquote(re.sub(r"^=+.*?=+\s*$", "", body(mask_names(own, title)), flags=re.M))
    for wd in BANNED:
        if wd.strip() in ("this page", "we") and is_list_page(title, text): continue
        for m in re.finditer(rf"\b{re.escape(wd.strip())}\b", scan, re.I):
            ctx = " ".join(scan[max(0, m.start()-50):m.end()+50].split())
            flags.append(f"BANNED   '{wd.strip()}': …{ctx}…")
    paras = prose.split("\n")  # list items and lines are separate units
    sents = [x for para in paras for x in re.split(r"(?<=[.!?])[\"”’']?\s+(?=[A-Z\"“'])", " ".join(para.split()))]
    for s in sents:
        if is_list_page(title, text): break          # transcripts and lists: no sentence-length check
        if s.count(",") >= 6: continue                # name lists (credits, playtesters)
        n = len(s.split())
        if n > MAX_SENT: flags.append(f"LONG     {n} words: {s[:100]}…")
    flags += service_flags(text, title)
    if not archive_exempt(title): flags += archive_flags(text, talk=talk)
    flags += email_flags(text)
    flags += ref_flags(text)
    return flags, words(b)

def fetch_categories(title):
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "categories", "cllimit": "max",
                                "format": "json", "formatversion": 2})
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": "swccg-style-lint/1.0"})
    try:
        p = json.load(urllib.request.urlopen(req, timeout=60))["query"]["pages"][0]
    except Exception:  # noqa: BLE001 - categories are a bonus; wikitext categories still count
        return set()
    return {c["title"] for c in p.get("categories", [])}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target"); ap.add_argument("--title")
    a = ap.parse_args()
    prev = None
    if os.path.isfile(a.target):
        text = open(a.target, encoding="utf-8").read()
        if a.title:
            r = fetch(a.title, 1); prev = r[0][1] if r else None
    else:
        r = fetch(a.target, 2)
        if not r: sys.exit(f"no such page: {a.target}")
        text = r[0][1]; prev = r[1][1] if len(r) > 1 else None
    title = a.title or (None if os.path.isfile(a.target) else a.target)
    cats = fetch_categories(title) if title else None
    flags, n = lint(text, title, cats)
    for f in flags: print(f)
    if prev is not None:
        pn = lint(prev, title, cats)[1]; print(f"WORDS    body {n} (previous {pn}, {n-pn:+d})")
    else: print(f"WORDS    body {n}")
    print(f"{len(flags)} flag(s)")
    sys.exit(1 if flags else 0)

if __name__ == "__main__": main()
