"""Final cross-product census and exact uploaded-image identity audit."""
import collections,json,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from publication_policy import lint,standard_lint
root=Path(__file__).parent;manifest=json.loads((root/'manifest.json').read_bytes());titles=[r['proposed_article'] for r in manifest];products=list(dict.fromkeys(r['product'] for r in manifest))
def fetch(batch,images=False):
    params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged'+('|imageinfo' if images else ''),rvprop='ids|timestamp|content',rvslots='main')
    if images:params['iiprop']='url|sha1|timestamp|size|mime'
    response=requests.get('https://wiki.swccg.com/api.php',params=params,timeout=60);response.raise_for_status();data=response.json();assert 'error' not in data,data;return data['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+35] for i in range(0,len(titles),35)]+[products]):heads.update({h['title']:h for h in batch})
sets={product:{str(link.title).strip() for link in mw.parse(heads[product]['revisions'][0]['slots']['main']['content']).filter_wikilinks()} for product in products}
report=[];problems=[];images={};ids={}
for row in manifest:
    title=row['proposed_article'];head=heads.get(title,{})
    if 'revisions' not in head:problems.append(dict(title=title,problem='missing article'));continue
    revision=head['revisions'][0];text=revision['slots']['main']['content'];cards=[t for t in mw.parse(text).filter_templates(recursive=False) if str(t.name).strip()=='Card']
    if len(cards)!=1:problems.append(dict(title=title,problem='expected one shared Card template'));continue
    card=cards[0];flags=lint(text,title)[0]
    if flags:problems.append(dict(title=title,problem='non-archive style flags',flags=flags))
    if title not in sets[row['product']]:problems.append(dict(title=title,problem='set lacks direct article link',product=row['product']))
    if not card.has('image') or not str(card.get('image').value).strip():problems.append(dict(title=title,problem='missing image'))
    else:images[title]='File:'+str(card.get('image').value).strip()
    if not card.has('publication_id'):problems.append(dict(title=title,problem='missing publication identity'))
    else:
        pid=str(card.get('publication_id').value).strip()
        if pid in ids:problems.append(dict(title=title,problem='duplicate publication identity',other=ids[pid]))
        ids[pid]=title
    if head.get('flagged',{}).get('stable_revid')!=revision['revid']:problems.append(dict(title=title,problem='public reviewed revision not current'))
    report.append(dict(title=title,product=row['product'],language=row['language'],revid=revision['revid'],direct_set_link=title in sets[row['product']],non_archive_flags=flags,deferred_archive_flags=[f for f in standard_lint(text,title)[0] if f.startswith('ARCHIVE')]))
files={};file_titles=sorted(set(images.values()))
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(lambda titles:fetch(titles,True),[file_titles[i:i+35] for i in range(0,len(file_titles),35)]):files.update({h['title']:h for h in batch})
expected={r['title']:r for f in root.glob('*-files-payload.json') for r in json.loads(f.read_bytes()) if r.get('sha1') and not r.get('draft_only')}
image_report=[]
for article,title in images.items():
    head=files.get(title,{});info=head.get('imageinfo',[None])[0]
    if not info:problems.append(dict(title=article,problem='missing uploaded image',file=title));continue
    matched=info['sha1']==expected[title]['sha1'] if title in expected else None
    if matched is False:problems.append(dict(title=article,problem='exact original image hash mismatch',file=title))
    image_report.append(dict(article=article,file=title,timestamp=info['timestamp'],sha1=info['sha1'],exact_uploaded_original_sha1_matched=matched))
result=dict(scope='Current cross-product article/infobox/identity/direct-set-link census and uploaded-original hash identity. Per-batch reports prove guarded publication, supported review, conservation and public/visual output; archive work explicitly deferred to412.',total_slots=len(manifest),articles_present=len(report),distinct_publication_ids=len(ids),per_product=dict(collections.Counter(r['product'] for r in report)),images=image_report,articles=report,problems=problems)
(root/'final-inventory-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
(root/'final-inventory-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8');print(len(report),'of314 card articles;',len(image_report),'image originals;',len(problems),'problems');print(json.dumps(problems,ensure_ascii=True,indent=2));assert not problems,'Resolve reported inventory issues before completion'
