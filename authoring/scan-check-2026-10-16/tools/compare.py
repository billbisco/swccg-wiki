import json, re, glob, collections, sys
PAGES = '/home/claude/swccg-wiki/pages'
def norm(s):
    s = s.replace('•', '').replace('’', "'").lower()
    s = re.sub(r'\((dark|light)\)', '', s)
    s = re.sub(r'\((premiere|coruscant|reflections[^)]*|special edition|virtual set[^)]*|v\) \(virtual[^)]*)\)', '', s)
    s = s.replace('&', ' and ').replace('/', ' and ')
    s = re.sub(r"[^a-z0-9() ]", '', s)
    return re.sub(r'\s+', ' ', s).strip()
def head(name):  # compare by the card's first name part; combos/objectives by front
    return norm(name.split(' / ')[0])
def wiki_cards(text):
    d = text.split('== Decklist ==')[1].split('== Scan ==')[0]
    out = collections.Counter()
    for line in d.splitlines():
        m = re.match(r"^[*#]\s*(?:(\d+)x\s*)?(.*)$", line.strip())
        if not m or not m.group(2): continue
        body = m.group(2); n = int(m.group(1) or 1)
        cl = re.match(r"\{\{CardLink\|([^|}]+)\|[^|}]*(?:\|label=([^}]+))?\}\}", body)
        wl = re.match(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", body)
        if cl: name = cl.group(2) or cl.group(1)
        elif wl: name = wl.group(2) or wl.group(1)
        else: continue
        out[head(name)] += n
    return out
def tx_cards(tx):
    out = collections.Counter()
    for e in tx['main'] + tx['shields']:
        if e.get('struck'): continue
        out[head(e['card'])] += 1
    return out
def diff(a, b):
    return (a - b), (b - a)
