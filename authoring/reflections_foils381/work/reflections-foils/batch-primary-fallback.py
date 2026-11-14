"""Preserve exact resources and selected public API data when direct saves fail."""
import base64,hashlib,html,json,re,subprocess,sys
from pathlib import Path
from urllib.parse import urlencode
import requests
root=Path(__file__).parent;stage=sys.argv[1]
latest={r['url']:r for r in map(json.loads,(root/(stage+'-citation-captures.jsonl')).read_text().splitlines())}
rows=[r for r in latest.values() if r.get('status')!='verified'];records=[];errors=[]
cache=root/'primary-cache';cache.mkdir(exist_ok=True)
local_sources={}
for request_file in root.glob('*source-requests.json'):
    for request in json.loads(request_file.read_bytes()):local_sources[request['url'].split('#')[0]]=root/'source-html'/(request['name']+'.html')
def safe_commit(c):
    return dict(sha=c['sha'],url=c['html_url'],message=c['commit']['message'],author={k:c['commit']['author'][k] for k in ['name','date']},committer={k:c['commit']['committer'][k] for k in ['name','date']},files=[{k:f[k] for k in ['filename','status','sha','patch','raw_url'] if k in f} for f in c.get('files',[])])
for row in rows:
    original=row['url'];url=row.get('preserved_url',original);record=dict(url=original,preserved_url=url)
    try:
        key=cache/(hashlib.sha256(url.encode()).hexdigest()+'.json')
        if key.exists():records.append(json.loads(key.read_bytes()));continue
        if 'github.com/' in url and 'raw.githubusercontent.com/' not in url:
            parts=url.split('github.com/',1)[1].split('/');owner,repo,kind=parts[:3]
            if kind=='commit':endpoint='repos/'+owner+'/'+repo+'/commits/'+parts[3]
            else:
                query=dict(sha=parts[3],per_page=100)
                if len(parts)>4:query['path']='/'.join(parts[4:])
                endpoint='repos/'+owner+'/'+repo+'/commits?'+urlencode(query)
            raw=subprocess.check_output(['gh','api',endpoint]);data=json.loads(raw)
            selected=[safe_commit(c) for c in data] if isinstance(data,list) else safe_commit(data)
            content=re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}','[email omitted]',json.dumps(selected,ensure_ascii=False,indent=2))
            record.update(api_source='https://api.github.com/'+endpoint,response_sha256=hashlib.sha256(raw).hexdigest(),kind='Selected public commit fields and diffs' if kind=='commit' else 'Public commit history, first 100 entries',content=content)
        else:
            if 'raw.githubusercontent.com/swccgpc/holotable/3d2c89e5f02cee6c39d70bd023260b638f3c0dc1/' in url:
                url=url.replace('/large/hansolo.gif','/hires/hansolo.png').replace('/large/sonofskywalker.gif','/hires/sonofskywalker.png')
                record['preserved_url']=url;record['correction']='Exact cited commit adds hires PNG; original large GIF citation was broken'
            if 'res.starwarsccg.org/cards/Images-HT/starwars/' in url:
                url=url.replace('/cards/Images-HT/starwars/','/cards/');record['preserved_url']=url;record['correction']='Remove a duplicated repository-path prefix from the published card-image URL; corrected resource retrieved directly'
            localfile=local_sources.get(url.split('#')[0])
            if localfile and localfile.exists():data=localfile.read_bytes();mime='text/html'
            else:
                r=requests.get(url,timeout=90);r.raise_for_status();data=r.content;mime=r.headers.get('content-type','application/octet-stream').split(';')[0]
            assert len(data)>100 and not any(t in data[:2000] for t in [b'Just a moment',b'Attention Required']),url
            record.update(kind='Original published resource bytes',sha256=hashlib.sha256(data).hexdigest(),mime=mime,data=base64.b64encode(data).decode())
        key.write_text(json.dumps(record,ensure_ascii=False),encoding='utf8');records.append(record);print('Retrieved',original,flush=True)
    except Exception as e:errors.append(dict(url=original,error=str(e)));print('Failed',original,str(e),flush=True)
body='<!doctype html><html><meta charset="utf-8"><title>Primary source preservation, Reflections story 381 '+stage+'</title><style>body{font:1rem system-ui;max-width:70rem;margin:2rem auto}pre{white-space:pre-wrap}img{max-width:100%}</style><h1>Card-family primary sources</h1><p>Source preservation for wiki story 381. Resource binaries retain their original bytes; selected public GitHub commit fields and diffs omit email metadata. This is a source-data copy, not a recreation of the original service interface.</p>'
for r in records:
    body+='<section><h2>'+html.escape(r['kind'])+'</h2><p><a href="'+html.escape(r['url'],quote=True)+'">Original citation</a></p>'
    if 'content' in r:body+='<p><a href="'+html.escape(r['api_source'],quote=True)+'">Primary GitHub API response</a>; response SHA256 '+r['response_sha256']+'</p><pre>'+html.escape(r['content'])+'</pre>'
    else:
        body+='<p>Original SHA256 '+r['sha256']+'</p><a download="source-resource" href="data:'+r['mime']+';base64,'+r['data']+'">Unchanged resource bytes</a>'
        if r['mime'].startswith('image/'):body+='<img src="data:'+r['mime']+';base64,'+r['data']+'">'
    body+='</section>'
body+='</html>'
(root/(stage+'-primary-source.html')).write_text(body,encoding='utf8')
(root/(stage+'-primary-manifest.json')).write_text(json.dumps([{k:v for k,v in r.items() if k not in ['data','content']} for r in records],ensure_ascii=False,indent=2),encoding='utf8')
(root/(stage+'-primary-errors.json')).write_text(json.dumps(errors,ensure_ascii=False,indent=2),encoding='utf8')
print(len(records),'retrieved;',len(errors),'failed;',len(body.encode()),'snapshot bytes')
