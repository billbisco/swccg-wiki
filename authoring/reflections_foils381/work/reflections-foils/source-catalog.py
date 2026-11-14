import collections,json,re,unicodedata
from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).parent;manifest=json.loads((root/'manifest.json').read_bytes());photos=json.loads((root/'photo-candidates.json').read_bytes())
def norm(s):
    s=re.sub(r'\([^)]*\)','',s)
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    s=re.sub(r'[^a-z0-9]','',s)
    return s.replace('c3p0','c3po').replace('it0','ito').replace('vibroaxe','vibroax').replace('pallaeon','pellaeon').replace('lottdodd','lottdod').replace('holotheater','holotheatre')
selected=[];ambiguous=[]
for row in manifest:
    if row['language']!='English':continue
    options=[p for p in photos if p['product']==row['product'] and 'FOIL' in p['caption'] and 'JAPANESE' not in p['caption'] and norm(p['caption_title'])==norm(row['label'])]
    options=[p for p in options if not ('DARKSIDE' in p['caption'] and row['side']=='Light') and not ('LIGHTSIDE' in p['caption'] and row['side']=='Dark')]
    twins=sum(x['product']==row['product'] and norm(x['label'])==norm(row['label']) for x in manifest)>1
    if twins:options=[p for p in options if ('DARKSIDE' in p['caption'] if row['side']=='Dark' else 'LIGHTSIDE' in p['caption'])]
    if options:
        options.sort(key=lambda p:(0 if p['source_html']=='ri-robert.html' else 1 if '72239' in p['source_html'] or p['source_html']=='riii-collector.html' else 2,0 if 'cloudfront' in p['url'] else 1))
        p=options[0];selected.append(dict(article=row['proposed_article'],product=row['product'],side=row['side'],label=row['label'],number=row['checklist_number'],alternate_image=row['alternate_image'],candidate=p,verification='unverified physical face; caption match is discovery only'))
swca=[];soup=BeautifulSoup(Path('work/japanese-complete/swca-cat.html').read_text(encoding='utf8'),'html.parser')
for a in soup.select('a[href]'):
    title=a.get_text(' ',strip=True)
    m=re.match(r'Reflections (I Foil|II|III), (Dark|Light) Side, (?:Foil, )?(?:(?:SRF|VRF|URF), )?(.*)',title)
    if not m:continue
    product={'I Foil':'Reflections','II':'Reflections II: Expanding the Galaxy','III':'Reflections III'}[m[1]]
    label=m[3];options=[r for r in manifest if r['product']==product and r['side']==m[2] and norm(r['label'])==norm(label)]
    if len(options)!=1:continue
    row=options[0]
    swca.append(dict(article=row['proposed_article'],product=product,side=m[2],label=label,url='https://theswca.com'+a['href'],item_id=re.search(r'item_id=(\d+)',a['href'])[1],catalog_title=title,source='Earlier complete CCG category index; item must be fetched/inspected afresh'))
covered={p['article'] for p in selected}|{r['existing_article'] for r in manifest if r['existing_article']}
needed=[p for p in swca if p['article'] not in covered]
requests=[];seen=set()
for p in needed:
    if p['item_id'] in seen:continue
    seen.add(p['item_id']);requests.append(dict(name='swca-'+p['item_id'],url=p['url'],article=p['article']))
(root/'selected-photo-leads.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf8')
(root/'swca-index.json').write_text(json.dumps(swca,ensure_ascii=False,indent=2),encoding='utf8')
(root/'swca-requests.json').write_text(json.dumps(requests,ensure_ascii=False,indent=2),encoding='utf8')
print('PSA source candidates',collections.Counter(p['product'] for p in selected));print('SWCA matches',len(swca),'; needed item requests',len(requests))
print('No selected PSA or SWCA entry',[(r['product'],r['label']) for r in manifest if r['language']=='English' and r['proposed_article'] not in covered and r['proposed_article'] not in {x['article'] for x in swca}])
