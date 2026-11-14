"""Preserve primary source data when GitHub UI/Wayback direct saves fail."""
import base64,hashlib,html,json,re,subprocess
from pathlib import Path
from urllib.parse import urlencode
import requests
root=Path(__file__).parent
latest={r['url']:r for r in map(json.loads,(root/'old-citation-archives.jsonl').read_text().splitlines())}
rows=[r for r in latest.values() if r['status']!='verified'];records=[]
def safe_commit(c):
    return dict(sha=c['sha'],url=c['html_url'],message=c['commit']['message'],author={k:c['commit']['author'][k] for k in ['name','date']},committer={k:c['commit']['committer'][k] for k in ['name','date']},files=[{k:f[k] for k in ['filename','status','sha','patch','raw_url'] if k in f} for f in c.get('files',[])])
for row in rows:
    url=row['url'];record=dict(url=url)
    if 'github.com/' in url:
        parts=url.split('github.com/',1)[1].split('/');owner,repo,kind=parts[:3]
        if kind=='commit':endpoint='repos/'+owner+'/'+repo+'/commits/'+parts[3]
        else:
            query=dict(sha=parts[3],per_page=100)
            if len(parts)>4:query['path']='/'.join(parts[4:])
            endpoint='repos/'+owner+'/'+repo+'/commits?'+urlencode(query)
        raw=subprocess.check_output(['gh','api',endpoint]);data=json.loads(raw)
        selected=[safe_commit(c) for c in data] if isinstance(data,list) else safe_commit(data)
        # Author email fields are intentionally never serialized.
        selected_text=json.dumps(selected,ensure_ascii=False,indent=2)
        selected_text=re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}','[email omitted]',selected_text)
        record.update(api_source='https://api.github.com/'+endpoint,response_sha256=hashlib.sha256(raw).hexdigest(),kind='Public commit fields and diffs' if kind=='commit' else 'Public commit history, first 100 records',content=selected_text)
    else:
        r=requests.get(url,timeout=60);r.raise_for_status();data=r.content
        assert data.startswith(b'\x89PNG') or data.startswith(b'GIF'),url
        record.update(kind='Original published image bytes',sha256=hashlib.sha256(data).hexdigest(),mime='image/png' if data.startswith(b'\x89PNG') else 'image/gif',data=base64.b64encode(data).decode())
    records.append(record)
body='<!doctype html><html><meta charset="utf-8"><title>Primary sources preserved for Reflections foil family navigation repairs</title><style>body{font:1rem system-ui;max-width:70rem;margin:2rem auto}pre{white-space:pre-wrap}img{max-width:100%}</style><h1>Card-version primary sources</h1><p>Preservation copy retrieved for wiki story 381. Public GitHub commit fields/diffs and the first page of history are retained; email metadata is omitted. The image retains its original bytes. This is a source-data preservation copy, not a recreation of GitHub’s interface.</p>'
for r in records:
    body+='<section><h2>'+html.escape(r['kind'])+'</h2><p><a href="'+html.escape(r['url'],quote=True)+'">Original citation</a></p>'
    if 'content' in r:body+='<p><a href="'+html.escape(r['api_source'],quote=True)+'">GitHub primary API source</a>; response SHA256 '+r['response_sha256']+'</p><pre>'+html.escape(r['content'])+'</pre>'
    else:body+='<p>Original SHA256 '+r['sha256']+'</p><img src="data:'+r['mime']+';base64,'+r['data']+'">'
    body+='</section>'
body+='</html>'
(root/'old-primary-source.html').write_text(body,encoding='utf8')
(root/'old-primary-manifest.json').write_text(json.dumps([{k:v for k,v in r.items() if k not in ['data','content']} for r in records],ensure_ascii=False,indent=2),encoding='utf8')
print('Prepared',len(records),'primary-source records;',len(body.encode()),'bytes; email metadata omitted')
