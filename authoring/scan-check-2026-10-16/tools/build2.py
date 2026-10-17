import json, re, sys, collections
sys.path.insert(0, '/tmp/claude-0/ltm/build'); sys.path.insert(0, '/home/claude/swccg-wiki/authoring')
import resolve as R
from alias import A, EP1, MT
RES = json.load(open('/tmp/claude-0/ltm/build/res1.json'))
REF3 = json.load(open('/tmp/claude-0/ltm/build/ref3.json'))
DS06 = ['A Tragedy Has Occurred','Aim High','Allegations Of Corruption','Battle Order','Battle Plan','Come Here You Big Coward',
        'Do They Have A Code Clearance?','Do, Or Do Not',"Don't Do That Again",'Fanfare','No Escape','Oppressive Enforcement','Ounee Ta',
        'Secret Plans','There Is No Try','Wise Advice','You Cannot Hide Forever','Your Insight Serves You Well']
ORDER = ["Objective","Location","Character","Creature","Starship","Vehicle","Weapon","Device","Effect","Interrupt","Defensive Shield"]
LEFT = {"Objective","Location","Character","Creature"}
OVS = None
def ovs(name, date):
    global OVS
    import wiki_cardlink as w
    p, c = w.ovs_pick(name, date)
    if p: return p
    c = [x for x in c if w.ovs_set(x) <= 16]
    return c[-1] if len(c) == 1 else None
def clean(card):
    c = card.strip()
    c = re.sub(r"\s*\((AI|SE|Ep ?I|EPI|EP I|Pre|Premiere|Dest \d+|1/0|DS|LS)\)", "", c, flags=re.I)
    return c.strip()
def norm_key(c): return re.sub(r'[^a-z0-9]', '', c.lower().replace('(v)', ''))
DS06K = {norm_key(x): x for x in DS06}
def shield_target(card, v, side, date):
    base = re.sub(r"\s*\(V\)$", "", card)
    if v:
        if norm_key(base) in DS06K:
            return "Defensive Shield", f"{DS06K[norm_key(base)]} (V) (Virtual Set: Defensive Shields)"
        p = ovs(base, date)
        if p: return "Defensive Shield", p
    return None
def build(tx, side, date):
    secs = collections.OrderedDict((s, collections.OrderedDict()) for s in ORDER)
    unres, flags = [], []
    entries = [(e, False) for e in tx['main']] + [(e, True) for e in tx['shields']]
    first = None
    for e, inbox in entries:
        if e.get('struck'): continue
        raw = e['card']; card = clean(raw); v = bool(e.get('v')) or card.endswith('(V)')
        base = re.sub(r"\s*\(V\)$", "", card).strip()
        ep1 = '(Episode I)' in base or bool(re.search(r'\((Ep ?I|EPI|EP I)\)', raw, re.I))
        base = A.get(base, base); base = re.sub(r"\s*\(Episode I\)", "", base)
        card = base + (' (V)' if v else '')
        r = MT.get((card, side)) or MT.get((raw.strip(), side)) or MT.get((clean(raw), side))
        if r: pass
        elif ep1 and (base, side) in EP1: r = ("Location", EP1[(base, side)])
        elif base in ('Tatooine', 'Coruscant') and not v: r = ("Location", base)
        if r is None and not v and base in REF3: r = ("Defensive Shield", REF3[base])
        if r is None:
            r0 = RES.get(f"{card}|{side}")
            if r0 is None: r0 = R.resolve(card, side)
            if (r0 and r0[0] == 'Defensive Shield') or inbox:
                r = shield_target(card, v, side, date)
            if r is None and r0: r = tuple(r0)
            if r is None and v:
                p = ovs(base, date)
                if p: r = (R.info([p])[p][0] if R.info([p])[p] else 'Effect', p)
                if r and r[0] not in R.SECT.values(): r = (R.SECT.get(r[0], r[0]), r[1])
        if r is None:
            unres.append(raw); key = ('Unresolved', raw.strip())
            secs.setdefault('Unresolved', collections.OrderedDict())
            secs['Unresolved'][key] = secs['Unresolved'].get(key, 0) + 1
            continue
        sec, tgt = r
        if inbox and v and sec == 'Effect': sec = 'Defensive Shield'
        if sec not in secs: secs[sec] = collections.OrderedDict()
        if first is None: first = (tgt, card)
        secs[sec][(tgt, card)] = secs[sec].get((tgt, card), 0) + 1
    out = ['{| class="wikitable" style="width:100%;"', "|-", '| style="width:50%; vertical-align:top;" |']
    right = False
    order = ORDER + [s for s in secs if s not in ORDER and s != 'Unresolved'] + ['Unresolved']
    for s in order:
        if not secs.get(s): continue
        if s not in LEFT and not right:
            out.append('| style="width:50%; vertical-align:top;" |'); right = True
        out.append(f"'''{'Not identified' if s == 'Unresolved' else s}'''")
        for (tgt, lab), n in secs[s].items():
            pre = "* " if n == 1 else f"* {n}x "
            if s == 'Unresolved': out.append(pre + ('illegible line' if lab.strip() in ('?', 'unidentified (V)') else lab))
            else:
                disp = lab.split(' / ')[0]
                out.append(pre + (f"[[{tgt}]]" if disp == tgt else f"[[{tgt}|{disp}]]"))
        out.append("")
    if out[-1] == "": out.pop()
    out.append("|}")
    total = sum(sum(v.values()) for v in secs.values())
    return "\n".join(out), first, unres, total
