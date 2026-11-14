"""Build clear, duplicate-free family navigation on the new articles only."""
import hashlib,json,re,sys
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
root=Path(__file__).parent
heads=json.loads((root/'published-heads.json').read_bytes());baseline=json.loads((root/'first-family-heads.json').read_bytes());families=json.loads((root/'first-families.json').read_bytes());readings=json.loads((root/'first-readings.json').read_bytes())
def card(s):return next(t for t in mw.parse(s).filter_templates(recursive=False) if str(t.name).strip()=='Card')
def canonical(title):
    seen=set()
    while title in baseline and title not in seen:
        seen.add(title);p=baseline[title]
        if 'revisions' not in p:break
        m=re.match(r'#REDIRECT\s*\[\[([^\]]+)\]\]',p['revisions'][0]['slots']['main']['content'],re.I)
        if not m:break
        title=m[1]
    return title
def label(title,t):
    era=str(t.get('era').value) if t.has('era') else ''
    suffix=' Errata'+(' 2' if '(Errata 2)' in title else ' 3' if '(Errata 3)' in title else '') if '(Errata' in title else ''
    for key in ['Virtual Original','Virtual Legacy','Virtual Modern']:
        if key in era:return key+suffix
    if '(PC Errata' in title:return 'PC Errata'+(' 2' if '(PC Errata 2)' in title else '')
    if '(Errata' in title:return 'Decipher Errata'+(' 2' if '(Errata 2)' in title else '')
    if 'Japanese' in title:return 'Decipher (Japanese)'
    if '(Revised)' in title:return 'Decipher (Revised)'
    if '(Unlimited)' in title:return 'Decipher (Unlimited)'
    return 'Decipher'
rows=[];report=[]
for r in readings:
    root_t=card(baseline[r['title']]['revisions'][0]['slots']['main']['content']);oldvalue=str(root_t.get('versions' if root_t.has('versions') else 'printings').value)
    order=[r['title']]+[canonical(str(w.title).strip()) for w in mw.parse(oldvalue).filter_wikilinks()]
    order+=families[r['title']];order=list(dict.fromkeys(t for t in order if t in families[r['title']]))
    entries=[]
    for i,title in enumerate(order):
        t=card(baseline[title]['revisions'][0]['slots']['main']['content']);prefix=label(title,t)
        group=0 if prefix.startswith('Decipher') and 'Errata' not in prefix else 1 if prefix.startswith('Decipher') else 2 if prefix.startswith('PC') else 3 if prefix.startswith('Virtual Original') else 4 if prefix.startswith('Virtual Legacy') else 5
        entries.append((group,i,"'''"+prefix+"''' — [["+title+']]'))
    entries.append((0,10000,"'''Decipher (Reflections foil)''' — '''this page'''"))
    value='<br />'.join(e[2] for e in sorted(entries))
    p=heads[r['article']];rev=p['revisions'][0];old=rev['slots']['main']['content'];code=mw.parse(old);t=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card');t.get('versions').value=value+'\n';new=str(code)
    rows.append(dict(title=r['article'],text=new,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Normalize foil family labels and remove redirect-duplicate destinations (#381)'))
    report.append(dict(title=r['article'],unique_family_destinations=len(order),closed_era_labels=True,gameplay_ids_not_reasserted=True))
(root/'first-nav-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
(root/'first-nav-normalization.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
