"""Check introduced foil destinations against current family navigation sources."""
import collections,json,sys,re
from concurrent.futures import ThreadPoolExecutor
import requests
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor')
import mwparserfromhell as mw
from navigation import canonical,card
root=Path(__file__).parent
heads=json.loads((root/'published-heads.json').read_bytes())
supplement={}
def fetch(batch):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);r.raise_for_status();return r.json()['query']['pages']
needed={title for file in root.glob('*-families.json') for members in json.loads(file.read_bytes()).values() for title in members}
while needed-set(heads):
    missing=sorted(needed-set(heads))
    with ThreadPoolExecutor(max_workers=3) as pool:
        for batch in pool.map(fetch,[missing[i:i+30] for i in range(0,len(missing),30)]):
            for h in batch:heads[h['title']]=h;supplement[h['title']]=h
    for title in list(needed):
        h=heads.get(title,{})
        if 'revisions' not in h:continue
        text=h['revisions'][0]['slots']['main']['content']
        m=re.match(r'#REDIRECT\s*\[\[([^\]]+)\]\]',text,re.I)
        if m:needed.add(m[1])
        for t in mw.parse(text).filter_templates():
            name=str(t.name).strip()
            if name.startswith('Card versions/'):needed.add('Template:'+name)
(root/'final-navigation-supplemental-heads.json').write_text(json.dumps(supplement,ensure_ascii=False,indent=2),encoding='utf8')
requirements=collections.defaultdict(set)
for file in root.glob('*-families.json'):
    stage=file.name[:-len('-families.json')]
    reading=root/(stage+'-readings.json')
    if not reading.exists():continue
    families=json.loads(file.read_bytes())
    for row in json.loads(reading.read_bytes()):
        for member in families[row['title']]:
            requirements[canonical(member,heads)].add(row['article'])
report=[];problems=[];historically_missing=[]
def links(text,seen=None):
    seen=set() if seen is None else seen
    code=mw.parse(text)
    found=[canonical(str(w.title).strip(),heads) for w in code.filter_wikilinks()]
    for template in code.filter_templates():
        name=str(template.name).strip()
        if name=='Card version link' and template.has('page'):
            found.append(canonical(str(template.get('page').value).strip(),heads))
        if not name.startswith('Card versions/') or name in seen:continue
        seen.add(name);title='Template:'+name
        if title not in heads:
            problems.append(dict(title=title,problem='shared navigator absent from final heads'));continue
        found+=links(heads[title]['revisions'][0]['slots']['main']['content'],seen)
    return found
for member,required in sorted(requirements.items()):
    if member not in heads or 'revisions' not in heads[member]:
        historically_missing.append(dict(title=member,missing_in_current_api=True));continue
    t=card(heads[member]['revisions'][0]['slots']['main']['content'])
    blocks={k:collections.Counter(links(str(t.get(k).value))) for k in ['versions','printings'] if t.has(k)}
    for target in sorted(required-{member}):
        counts={k:v[target] for k,v in blocks.items()}
        if not counts or any(n!=1 for n in counts.values()):problems.append(dict(title=member,target=target,problem='introduced destination count per navigation field',counts=counts))
    report.append(dict(title=member,revid=heads[member]['revisions'][0]['revid'],required_foil_destinations=sorted(required-{member})))
result=dict(scope='Current exact membership of every foil destination introduced into its affected existing family; prior public/conservation receipts remain in each batch report. Historic candidate titles that do not exist are recorded separately; current redirects are resolved.',family_pages=len(report),memberships=sum(len(r['required_foil_destinations']) for r in report),pages=report,historical_nonexistent_candidates=historically_missing,problems=problems)
(root/'final-navigation-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(result['family_pages'],'current family pages;',result['memberships'],'foil memberships;',len(problems),'problems')
print(json.dumps(problems,ensure_ascii=True,indent=2))
assert not problems
