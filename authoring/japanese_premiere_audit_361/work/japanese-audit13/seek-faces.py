import json
from pathlib import Path
import subprocess

root=Path('work/japanese-audit13')
code='''
import json,urllib.request
for item in ['12508','12548']:
    url='https://theswca.com/index.php?action=disp_item&item_id='+item
    payload=json.dumps(dict(cmd='request.get',url=url,maxTimeout=55000)).encode()
    request=urllib.request.Request('http://127.0.0.1:8191/v1',payload,{'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(request,timeout=100) as response: result=json.load(response)
        print(json.dumps(dict(item=item,status=result.get('status'),solution=result.get('solution'),message=result.get('message'))),flush=True)
    except Exception as error:
        print(json.dumps(dict(item=item,error=str(error))),flush=True)
'''
result=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'better-scan-search.jsonl').write_bytes(result.stdout)
for row in map(json.loads,result.stdout.splitlines()):
    html=(row.get('solution') or {}).get('response','')
    (root/('swca-'+row['item']+'.html')).write_text(html,encoding='utf8')
    print(row['item'],row.get('status',row.get('error')),len(html))
