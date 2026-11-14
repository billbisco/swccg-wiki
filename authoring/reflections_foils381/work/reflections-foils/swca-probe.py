"""Fetch missing-face leads through one owned browser session; always destroy it."""
import base64,json,subprocess,sys
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup
root=Path(__file__).parent;start=int(sys.argv[1]) if len(sys.argv)>1 else 0;count=int(sys.argv[2]) if len(sys.argv)>2 else 40
rows=[r for r in json.loads((root/'swca-requests.json').read_bytes()) if not (root/'source-html'/(r['name']+'.html')).exists()][start:start+count]
code='ROWS='+repr(rows)+'\n'+'''
import base64,json,re,urllib.request,uuid
from pathlib import Path
root=Path('/mnt/HC_Volume_107153504/work/memorycorechatgpt-reflections381-20261113');root.mkdir(exist_ok=True)
def solver(cmd,**fields):
    req=urllib.request.Request('http://127.0.0.1:8191/v1',data=json.dumps(dict(cmd=cmd,**fields)).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=100) as r:return json.load(r)
session='memorycore-reflections381-'+uuid.uuid4().hex
assert solver('sessions.create',session=session).get('status')=='ok'
try:
    for row in ROWS:
        try:
            path=root/(row['name']+'.html')
            if path.exists():html=path.read_text(encoding='utf8')
            else:
                result=solver('request.get',url=row['url'],session=session,maxTimeout=60000)
                assert result.get('status')=='ok',result.get('message')
                html=result['solution']['response']
                assert 'Just a moment' not in html[:3000] and 'disp_item' in html
                path.write_text(html,encoding='utf8')
            print(json.dumps(dict(row,html=base64.b64encode(html.encode()).decode())),flush=True)
        except Exception as e:print(json.dumps(dict(row,error=str(e))),flush=True)
finally:
    destroyed=solver('sessions.destroy',session=session)
    print(json.dumps(dict(owned_session_destroyed=destroyed.get('status')=='ok')),flush=True)
'''
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close();out=[]
for line in p.stdout:
    row=json.loads(line)
    if 'html' in row:
        data=base64.b64decode(row.pop('html'));(root/'source-html'/(row['name']+'.html')).write_bytes(data)
        soup=BeautifulSoup(data,'html.parser');row['title']=soup.title.get_text() if soup.title else '';row['bytes']=len(data)
        row['assets']=[urljoin(row['url'],im.get('src') or im.get('data-src','')) for im in soup.select('.item-media figure img')]
        row['no_photo']='No photograph of this item yet' in soup.get_text(' ',strip=True)
    out.append(row);print({k:v for k,v in row.items() if k!='assets'},'assets='+str(len(row.get('assets',[]))),flush=True)
(root/f'swca-probe-{start}-{count}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
raise SystemExit(p.wait())
