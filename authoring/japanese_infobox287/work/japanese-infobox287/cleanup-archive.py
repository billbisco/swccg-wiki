import json
from pathlib import Path
import subprocess

root=Path(__file__).parent
code='''
import gzip,hashlib,json,urllib.parse,urllib.request
url='https://boardgamegeek.com/filepage/33565/star-wars-ccg-complete-card-list-42'
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'SWCCG Wiki preservation check'}),timeout=45) as response:data=response.read()
    return gzip.decompress(data) if data[:2]==b'\\x1f\\x8b' else data
query='https://web.archive.org/cdx/search/cdx?'+urllib.parse.urlencode(dict(url=url,output='json',filter='statuscode:200',fl='timestamp,original,length',collapse='digest'))
try:
    captures=json.loads(fetch(query))
    print(json.dumps(dict(kind='cdx',rows=captures)),flush=True)
    for stamp,original,length in reversed(captures[1:]):
        capture='https://web.archive.org/web/'+stamp+'id_/'+original
        try:
            data=fetch(capture);text=data.decode('utf8','replace')
            valid='33565' in text and ('Complete Card List' in text or 'complete card list' in text or 'complete-card-list' in text) and 'cf-browser-verification' not in text and '<title>Just a moment' not in text
            print(json.dumps(dict(kind='replay',capture=capture.replace('id_/','/'),verified=valid,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),sample=text[:180])),flush=True)
            if valid:break
        except Exception as error:print(json.dumps(dict(kind='replay',capture=capture,error=str(error))),flush=True)
except Exception as error:print(json.dumps(dict(kind='cdx',error=str(error))),flush=True)
'''
result=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'cleanup-archive.jsonl').write_bytes(result.stdout)
for row in map(json.loads,result.stdout.splitlines()):
    if row.get('kind')=='cdx':print('CDX',len(row.get('rows',[])),row.get('error',''))
    else:print(row)
