import base64,hashlib,json,subprocess
from pathlib import Path
import pymupdf
root=Path(__file__).parent
source=json.loads((root/'pilot378-sources.json').read_bytes())[1]
code='SOURCE='+repr(source)+'\n'+'''
import base64,hashlib,json,urllib.request
with urllib.request.urlopen(SOURCE['url'],timeout=60) as r:data=r.read()
assert hashlib.sha256(data).hexdigest()==SOURCE['sha256']
print(base64.b64encode(data).decode())
'''
p=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
data=base64.b64decode(p.stdout);assert hashlib.sha256(data).hexdigest()==source['sha256']
(root/'checklist.pdf').write_bytes(data)
doc=pymupdf.open(stream=data,filetype='pdf')
text='\n'.join('PAGE '+str(i+1)+'\n'+doc[i].get_text(sort=True) for i in range(27,32))
(root/'checklist-pages29-32.txt').write_text(text,encoding='utf8')
(root/'checklist-preservation.json').write_text(json.dumps(dict(**source,verified=True,replayed_via='VPS direct',pages_read=[28,29,30,31,32]),indent=2),encoding='utf8')
print(text[:6500])
