from pathlib import Path
import json,re,requests
api='https://wiki.swccg.com/api.php'
s=requests.Session()
s.headers['User-Agent']='SWCCG Wiki card title audit (Memory Core ChatGPT)'
def get(**params):
    r=s.get(api,params={'format':'json','formatversion':2,**params},timeout=25)
    r.raise_for_status()
    obj=r.json()
    if 'error' in obj: raise RuntimeError(obj['error']['info'])
    return obj
def collect(category):
    cont={}
    out=[]
    while True:
        r=get(action='query',list='categorymembers',cmtitle='Category:'+category,cmlimit='max',cmnamespace=0,**cont)
        out+=r['query']['categorymembers']
        if 'continue' not in r: return out
        cont=r['continue']
def pages(titles):
    results={}
    for i in range(0,len(titles),24):
        r=get(action='query',titles='|'.join(titles[i:i+24]),prop='revisions',rvprop='ids|content',rvslots='main')
        for p in r['query']['pages']:
            results[p['title']]=p
    return results
def attrs(p):
    raw=p.get('revisions',[{}])[0].get('slots',{}).get('main',{}).get('content','')
    return {k:v.strip() for k,v in re.findall(r'^\|\s*([\w_]+)\s*=([^\n]*)',raw,re.M)}
if __name__=='__main__':
    allcards=collect('Cards')
    titles={p['title'] for p in allcards}
    suffix=re.compile(r' \((Dark|Light)\)')
    tagged=sorted(t for t in titles if suffix.search(t))
    bare={t:suffix.sub('',t,1) for t in tagged}
    rows=pages(sorted(set(tagged)|set(bare.values()) & titles))
    out=[]
    for t in tagged:
        p=attrs(rows[t]); counterpart=attrs(rows.get(bare[t],{}))
        out.append({'title':t,'base':bare[t],'id':p.get('card_uid'),'type':p.get('type'),'side':p.get('side'),'set':p.get('set'),
                    'base_id':counterpart.get('card_uid'),'base_type':counterpart.get('type'),'base_side':counterpart.get('side'),
                    'base_set':counterpart.get('set'),'pageid':rows[t].get('pageid')})
    Path('work/wiki-title-audit.json').write_text(json.dumps({'count':len(titles),'tagged':len(tagged),'rows':out},indent=2,ensure_ascii=False),encoding='utf8')
    print(f'{len(titles)} card articles, {len(tagged)} side-qualified titles')
    for row in out:
        if row['side'] and row['side']==row['base_side']:
            print(json.dumps(row,ensure_ascii=False))
