#!/usr/bin/env python3
"""Rebuild the 17 Original Virtual Set pages to the wiki style guide.

Reads ovsN.wiki (live text), writes out/ovsN.wiki (article) and out/talkN.wiki (Talk section).
"""
import re, os, json

ORD = "first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth fourteenth fifteenth sixteenth seventeenth".split()
titles = {int(l.split('|')[0]): l.split('|', 1)[1].strip() for l in open('titles.txt')}
REORG = ('<ref name="reorg2009">[https://web.archive.org/web/20090918131415/http://www.starwarsccg.org/ starwarsccg.org] '
         '(Internet Archive, 18 September 2009): the Players Committee realigned Virtual Sets 1–18 into thematic Virtual Blocks.</ref>')

# Release facts. legal: (infobox label, infobox value, lead sentence) ; None = unknown (blank cell, note to Talk)
RELEASE = {
    1: ("Legal", "9 March 2002", "It became tournament-legal on 9 March 2002."),
    2: ("Legal", "1 June 2002", "It became tournament-legal on 1 June 2002."),
    3: ("Legal", "20 September 2002", "It became tournament-legal on 20 September 2002."),
    4: ("Legal", "5 February 2003", "It became tournament-legal on 5 February 2003."),
    5: ("Legal", "6 June 2003", "It became tournament-legal on 6 June 2003."),
    6: ("Legal", "12 January 2004", "The Committee released it on 21 November 2003; the final revised text became tournament-legal on 12 January 2004."),
    7: ("Released", "16 July 2004", "The Committee released it on 16 July 2004."),
    8: ("Released", "24 November 2004", "The Committee released it on 24 November 2004."),
}
# Re-edits of the sheet: list of (date, [slip numbers])
ERRATA = {
    2: [("28 July 2007", [34])], 3: [("28 July 2007", [39])],
    5: [("14 September 2007", [49])], 6: [("14 September 2007", [32])],
    8: [("25 June 2007", [5, 30]), ("17 September 2007", [22])],
    9: [("17 September 2007", [10])], 11: [("25 June 2007", [8, 27])],
}
# Clean 'ia' ref text overrides (research notes moved to Talk)
IA_FIX = {
    9: '<ref name="ia">[https://res.starwarsccg.org/legacyblocks/VirtualCards9.pdf VirtualCards9.pdf] (Players Committee sheet, starwarsccg.org); [https://web.archive.org/web/20071024153015/http://www.swccgpc.com/Resources/VirtualCards9.pdf swccgpc.com copy] (Internet Archive, 24 October 2007).</ref>',
    14: '<ref name="ia">[https://res.starwarsccg.org/legacyblocks/VirtualCards14.pdf VirtualCards14.pdf] (Players Committee sheet, starwarsccg.org).</ref>',
}

def split_ref(cell):
    m = re.search(r'(<ref name="[^"]+">.*?</ref>)', cell)
    return (cell[:m.start()].strip() if m else cell.strip()), (m.group(1) if m else '')

def link_list(xs):
    return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' and ' + xs[-1]

def build(n):
    src = open(f'ovs{n}.wiki').read()
    title = titles[n]
    sym = f'VS{n}O-set-symbol.png' if n > 1 else 'VS1-Legacy-set-symbol.png'
    talk = {'missing': [], 'faulty': [], 'cuts': [], 'build': []}

    # --- hatnote + infobox
    hat = src.split('\n', 1)[0]
    ib = re.search(r'\{\| class="wikitable expansion-infobox".*?\n\|\}', src, re.S).group(0)
    pack = re.search(r'\[\[File:([^|\]]+)\|200px\]\]', ib).group(1)
    code = re.search(r'! Code\n\|\|(.*)', ib).group(1).strip()
    cards = re.search(r'! Cards\n\|\|(.*)', ib).group(1).strip()
    legal_cell = re.search(r'! Legal\n\|\|(.*)', ib).group(1)
    sheet_cell = re.search(r'! Remaster sheet\n\|\|(.*)', ib).group(1)
    _, legal_ref = split_ref(legal_cell)
    sheet_val, ia_ref = split_ref(sheet_cell)
    sheet_date = re.search(r'Official text as of ([0-9]+ \w+ [0-9]{4})', sheet_val).group(1)
    ia_ref = IA_FIX.get(n, ia_ref)
    if n in RELEASE:
        lab, val, lead_rel = RELEASE[n]
        rel_row = f'! {lab}\n| {val}{legal_ref}'
        lead_rel += '<ref name="legal" />'
    else:
        lab, val, lead_rel = 'Released', '', ''
        rel_row = '! Released\n| '
        note = re.sub(r'</?ref[^>]*>', '', legal_ref)
        talk['missing'].append(f'Release / tournament-legal date not found. Note moved from the infobox: "{note}" (Dates inferred from event credits on the slips stay here, not in the article.)')
    infobox = f'''{{| class="wikitable expansion-infobox"
! colspan="2" | {title}
|-
| colspan="2" style="text-align:center;" | [[File:{pack}|200px]]
|-
! Set symbol
| [[File:{sym}|40px]]
|-
! Code
| {code}
|-
! Publisher
| [[Players Committee|Star Wars CCG Players Committee]]
|-
! Era
| [[:Category:Virtual Original sets|Virtual Original]] (2002–2009)
|-
{rel_row}
|-
! Official text
| {sheet_date}{ia_ref}
|-
! Cards
| {cards}
|}}'''

    # --- card tables: add Set column
    rows = {}
    def addcol(t):
        t = t.replace('! # !! Slip !!', '! # !! Set !! Slip !!')
        def r(m):
            num = m.group(1)
            rest = m.group(2)
            lk = re.search(r'\|\| style="white-space:nowrap" \| (\[\[[^\]]+\]\])', rest)
            if lk: rows[int(num)] = lk.group(1)
            return f'| {num} || [[File:{sym}|24px|link=]] || {rest}'
        return re.sub(r'^\| (\d+) \|\| (.*)$', r, t, flags=re.M)
    cards_sec = src[src.index('== Cards =='):src.index('\n|}', src.index('=== [[Dark')) + 3]
    cards_sec = addcol(cards_sec)
    for red in ['Dark Jedi Master/Imperial', 'Rebel/Republic', 'Alien/Republic', 'Dark Jedi Master']:
        cards_sec = re.sub(r'\[\[' + re.escape(red) + r'(\|[^\]]*)?\]\]', lambda m: (m.group(1) or '|' + red)[1:], cards_sec)

    # --- lead
    old_lead = re.search(r"\n('''Virtual Set.*?)\n\n", src, re.S).group(1)
    desc = re.search(r"(Each of its \d+ cards is .*?as printed\.|Its \d+ cards are printed slips .*?caption\.)", old_lead).group(1)
    first = f"'''{title}''' is the {ORD[n-1]} of the [[Virtual Sets (2002-2009)|numbered Virtual Sets]] the [[Players Committee]] released between 2002 and 2009."
    if n <= 11:
        reissue = "In December 2006 the Committee reissued it as a ''Remaster'' sheet with new pack art, a set symbol and the final text." + '<ref name="ia" />'
    else:
        reissue = f"The set's sheet carries official text as of {sheet_date}." + '<ref name="ia" />'
    nc = re.search(r'\d+', desc).group(0)
    if desc.startswith('Each'):
        desc = (f"Each of its {nc} cards is a printed slip that replaces the bottom half of a [[Decipher]] card. "
                "The slip gives new game text, stats and icons; the title, lore and art stay as printed.")
    else:
        desc = (f"Its {nc} cards are printed slips placed over [[Decipher]] cards. Some replace only the bottom half, "
                "giving new game text, stats and icons. Others cover the whole card and make a new card; "
                "the slip's caption names the Decipher card it covers.")
    lead = ' '.join(x for x in [first, desc, lead_rel, reissue] if x)
    remaster = ("The Remaster column sets each slip onto its printed Decipher card, re-typeset at 600 DPI in the style of the "
                "Committee's later Holotable cards. They were made for the wiki in 2026 and are fan reconstructions, not Committee "
                "products (see [[Typography of Star Wars CCG cards]]). Game text is written out in full where the slips use the "
                "icon shorthand explained at [[Virtual card icons]].")

    # --- printings section
    hist = src[src.index('== History =='):src.index('== See also ==')] if '== History ==' in src else ''
    pr = []
    if n == 1:
        pr.append("The Committee first issued the set as a printable sheet in March 2002"
                  "<ref name=\"vs1a\">[https://res.starwarsccg.org/legacyblocks/VirtualCards1a.pdf VirtualCards1a.pdf] (Players Committee sheet, starwarsccg.org).</ref>"
                  ", then as a ''Premium Edition'' sheet"
                  "<ref name=\"vs1p\">[https://res.starwarsccg.org/legacyblocks/VirtualCards1Premium.pdf VirtualCards1Premium.pdf] (Players Committee sheet, starwarsccg.org).</ref>"
                  ". Decipher's own card lists offered the Committee's sets as printable PDFs to sleeve with the original cards, in black-border and white-border editions."
                  '<ref name="legal" />')
    if n in ERRATA:
        parts = []
        for d, nums in ERRATA[n]:
            names = [f"{rows[k]} (#{k})" if k in rows else f"#{k}" for k in nums]
            parts.append(f"on {d} with errata to {link_list(names)}")
        pr.append("The Committee re-edited the Remaster sheet " + parts[0] + '.<ref name="ia" />')
        for p in parts[1:]:
            pr.append("It re-edited it again " + p + '.<ref name="ia" />')
    pr.append("In the 2009 reorganisation the Committee regrouped the Original Virtual cards into the [[:Category:Virtual Legacy sets|Virtual Blocks]]." + REORG)
    printings = "== Printings ==\n" + ' '.join(pr)
    if n == 1:
        gal = hist[hist.index('{| class="wikitable" style="text-align:center;"'):]
        gal = gal[:gal.index('\n|}') + 3]
        gal = gal.replace('! Card !! 1A / early !! Premium !! Virtual Block 1',
                          '! Card !! March 2002<ref name="vs1a" /> !! Premium<ref name="vs1p" /> !! [[Virtual Block 1]]')
        printings += '\n\n' + gal

    # --- talk notes for removed history
    if hist:
        urls = sorted(set(re.findall(r'https?://[^\s\]|]+', hist)))
        talk['cuts'].append("Removed the History / Provenance section (sheet-provenance tables, PDF CreationDate and Wayback/CDN availability notes, editor guidance). Facts kept moved into the infobox, lead and Printings. Sources it listed: " + ', '.join(urls))
        for l in hist.split('\n'):
            if re.search(r'caveat|CardVault|CreationDate|CDX|redirects|no application/pdf|Launch \(approx\)', l):
                talk['faulty' if 'caveat' in l else 'cuts'].append('Cut row: <nowiki>' + l.strip().lstrip('|').strip()[:400] + '</nowiki>')
    if n == 1:
        talk['cuts'].append('Cut the two Decipher card-list blockquotes (kept as one sentence in Printings plus the ref) and the "Version / What it is / Image source" table (its PDFs are now refs on the gallery header).')
    talk['build'].append(f'Added a Set column with the set symbol (File:{sym}) to both card tables and a Set symbol row to the infobox. Rewrote the lead and replaced History with Printings per [[SWCCG Wiki:Style guide]].')

    body = f"""{hat}
{infobox}

{lead}

{remaster}

{cards_sec}

{printings}

== See also ==
* [[Virtual Sets (2002-2009)]] · [[History of the Players Committee]]
* [[Virtual card icons]] · [[Defensive Shields]] · [[Virtual Shields]]

== References ==
<references />

[[Category:Virtual Original sets]]
[[Category:Sets]]
"""
    t = ["== 2026-10-15 style pass (Holocron Claude) =="]
    for k, h in [('missing', 'Missing data'), ('faulty', 'Possibly faulty data'), ('cuts', 'Marginal cuts'), ('build', 'Build notes')]:
        if talk[k]:
            t.append(f"'''{h}:'''")
            t += ['* ' + x for x in talk[k]]
    t.append('~~~~')
    return title, body, '\n'.join(t) + '\n'

os.makedirs('out', exist_ok=True)
manifest = []
for n in range(1, 18):
    title, body, talk = build(n)
    open(f'out/ovs{n}.wiki', 'w').write(body)
    open(f'out/talk{n}.wiki', 'w').write(talk)
    manifest.append({'n': n, 'title': title})
json.dump(manifest, open('out/manifest.json', 'w'), indent=1)
print('ok')
