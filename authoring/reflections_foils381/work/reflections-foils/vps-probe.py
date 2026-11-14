import base64,json,subprocess,sys
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/sys.argv[1]).read_bytes()) if len(sys.argv)>1 else [r for r in json.loads((root/'source-probe.json').read_bytes()) if r.get('error')]
code='ROWS='+repr(rows)+'\n'+'''
import base64,json,re,urllib.request
from pathlib import Path
root=Path('/mnt/HC_Volume_107153504/work/memorycorechatgpt-reflections381-20261113');root.mkdir(exist_ok=True)
for row in ROWS:
    url=row['url']
    try:
        try:
            with urllib.request.urlopen(url,timeout=30) as r:html=r.read().decode();route='VPS direct'
        except Exception:
            body=json.dumps(dict(cmd='request.get',url=url,maxTimeout=90000)).encode()
            req=urllib.request.Request('http://127.0.0.1:8191/v1',data=body,headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req,timeout=130) as r:result=json.load(r)
            assert result.get('status')=='ok',result.get('message')
            html=result['solution']['response'];route='VPS no-session FlareSolverr'
        assert 'Just a moment' not in html[:2000]
        (root/(row['name']+'.html')).write_text(html,encoding='utf8')
        print(json.dumps(dict(name=row['name'],url=url,route=route,html=base64.b64encode(html.encode()).decode())),flush=True)
    except Exception as e:print(json.dumps(dict(name=row['name'],url=url,error=str(e))),flush=True)
'''
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
p.stdin.write(code.encode());p.stdin.close();out=[]
for line in p.stdout:
    r=json.loads(line)
    if 'html' in r:
        html=base64.b64decode(r.pop('html'));(root/'source-html'/(r['name']+'.html')).write_bytes(html);r['bytes']=len(html)
    out.append(r);print(r,flush=True)
(root/('vps-probe-'+(Path(sys.argv[1]).stem if len(sys.argv)>1 else 'initial')+'.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
raise SystemExit(p.wait())
