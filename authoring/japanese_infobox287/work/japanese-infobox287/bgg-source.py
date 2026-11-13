import base64,json,subprocess
from pathlib import Path
root=Path(__file__).parent
code='''
import base64,json,re,urllib.request
from pathlib import Path
root=Path('/mnt/HC_Volume_107153504/work/memorycorechatgpt-infobox287-20261113')
root.mkdir(parents=True,exist_ok=True)
(root/'README.txt').write_text('MemoryCoreChatGPT; #287/#366 Japanese infobox migration; 13 November 2026. Public-source preservation scratch.')
url='https://boardgamegeek.com/filepage/33565/star-wars-ccg-complete-card-list-42'
payload=json.dumps(dict(cmd='request.get',url=url,maxTimeout=90000,returnScreenshot=True)).encode()
request=urllib.request.Request('http://127.0.0.1:8191/v1',payload,{'Content-Type':'application/json'})
with urllib.request.urlopen(request,timeout=135) as response:result=json.load(response)
solution=result.get('solution') or {}
html=solution.get('response','')
(root/'bgg.html').write_text(html,encoding='utf8')
title=re.search('<title>(.*?)</title>',html,re.S)
record=dict(status=result.get('status'),http_status=solution.get('status'),url=solution.get('url'),title=title[1] if title else '',bytes=len(html),has_card_list='card list' in html.lower(),has_id='33565' in html,path=str(root/'bgg.html'))
if solution.get('screenshot'):record['screenshot']=solution['screenshot']
print(json.dumps(record),flush=True)
'''
result=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
record=json.loads(result.stdout)
shot=record.pop('screenshot',None)
if shot:(root/'bgg-source.png').write_bytes(base64.b64decode(shot))
(root/'bgg-source.json').write_text(json.dumps(record,indent=2),encoding='utf8')
print(record)
