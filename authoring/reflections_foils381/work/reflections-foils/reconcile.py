"""Checklist discovery ledger; candidates require physical-face verification."""
from concurrent.futures import ThreadPoolExecutor
import collections,csv,json,re,sys
from pathlib import Path
import requests
sys.path.insert(0,'work/japanese-infobox287/vendor')
import mwparserfromhell as mw
root=Path(__file__).parent
sets=['Reflections','Reflections II: Expanding the Galaxy','Reflections III']
bootstrap=json.loads((root/'bootstrap-heads.json').read_bytes())
existing=json.loads((root/'existing-foil-heads.json').read_bytes())
rows=[]
for product in sets:
    text=bootstrap[product]['revisions'][0]['slots']['main']['content']
    body=re.split(r'\n==[^=]',text.split('== Possible foils ==',1)[1],maxsplit=1)[0]
    side=rarity=None
    for line in body.splitlines():
        m=re.search(r'===\s*(Light|Dark) Side\s*===',line)
        if m:side=m[1];rarity=None;continue
        m=re.search(r"'''''(Ultra Rare|Super Rare|Very Rare)'''''",line)
        if m:rarity={'Ultra Rare':'UR','Super Rare':'SR','Very Rare':'VR'}[m[1]];continue
        if side and rarity:
            for link in mw.parse(line).filter_wikilinks():
                target=str(link.title).strip();label=str(link.text or link.title).strip()
                rows.append(dict(product=product,side=side,rarity=rarity,checklist_target=target,label=label,language='English',existing_article=None))
    assert sum(r['product']==product for r in rows)=={'Reflections':114,'Reflections II: Expanding the Galaxy':100,'Reflections III':100}[product]
def params(text):
    for t in mw.parse(text).filter_templates(recursive=False):
        if str(t.name).strip()=='Card':return {str(p.name).strip():str(p.value).strip() for p in t.params}
    return {}
unmatched=[]
for title,page in existing.items():
    if 'Foil)' not in title:continue
    p=params(page['revisions'][0]['slots']['main']['content'])
    if not p:continue
    product=p.get('set','').replace("Reflections III: A Collector's Bounty",'Reflections III')
    if product not in sets:continue
    label=p.get('title',title.split(' (')[0])
    options=[r for r in rows if r['product']==product and r['side']==p.get('side') and (r['label']==label or r['checklist_target']==label)]
    if len(options)!=1:unmatched.append(dict(title=title,label=label,product=product,side=p.get('side'),matches=len(options)));continue
    row=options[0];assert not row['existing_article'],(row,title)
    row.update(existing_article=title,language='Japanese' if 'Japanese' in title else 'English',existing_revid=page['revisions'][0]['revid'],image=p.get('image',''),publication_id=p.get('publication_id',''))
titles={r['checklist_target'] for r in rows}
for row in rows:
    titles.add(row['label']);titles.add(row['label']+' (Dark)');titles.add(row['label']+' (Light)')
def fetch(batch):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
heads={};titles=sorted(titles)
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+30] for i in range(0,len(titles),30)]):heads.update({p['title']:p for p in batch})
(root/'counterpart-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
for row in rows:
    options=[t for t in [row['checklist_target'],row['label'],row['label']+' (Dark)',row['label']+' (Light)'] if t in heads and 'revisions' in heads[t] and params(heads[t]['revisions'][0]['slots']['main']['content']).get('side')==row['side']]
    row['counterpart_candidates']=list(dict.fromkeys(options))
    row['status']='existing' if row['existing_article'] else 'missing'
    qualifier={'Reflections':'Reflections Foil','Reflections II: Expanding the Galaxy':'Reflections II Foil','Reflections III':'Reflections III Foil'}[row['product']]
    candidate=row['counterpart_candidates'][0] if row['counterpart_candidates'] else row['label']
    row['proposed_article']=row['existing_article'] or candidate+' ('+qualifier+')'
    row['evidence_status']='existing article requires scoped validation' if row['existing_article'] else 'foil face and printed fields not yet inspected'
(root/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
(root/'unmatched-existing.json').write_text(json.dumps(unmatched,ensure_ascii=False,indent=2),encoding='utf8')
with (root/'inventory.csv').open('w',encoding='utf8',newline='') as f:
    keys=['product','side','rarity','label','language','status','existing_article','proposed_article','evidence_status'];w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore');w.writeheader();w.writerows(rows)
print(collections.Counter((r['product'],r['language'],r['status']) for r in rows));print('Unmatched existing',unmatched)
print('Counterpart unresolved',[(r['product'],r['side'],r['label']) for r in rows if not r['counterpart_candidates']])
