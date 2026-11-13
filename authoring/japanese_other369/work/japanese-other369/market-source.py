import json,subprocess
from pathlib import Path
root=Path(__file__).parent
code='''
import json,urllib.request
from bs4 import BeautifulSoup
from pathlib import Path
url='https://www.ebay.com/itm/175133384414'
req=urllib.request.Request('http://127.0.0.1:8191/v1',json.dumps(dict(cmd='request.get',url=url,maxTimeout=60000)).encode(),{'Content-Type':'application/json'})
with urllib.request.urlopen(req,timeout=90) as response:result=json.load(response)
solution=result.get('solution',{});html=solution.get('response','')
folder=Path('/mnt/HC_Volume_107153504/work/memorycorechatgpt-japanese369-20261113');folder.mkdir(exist_ok=True,parents=True)
(folder/'README.txt').write_text('MemoryCoreChatGPT #369 Japanese card source research, 13 November 2026. Public-source HTML only.')
(folder/'motti-ebay.html').write_text(html,encoding='utf8')
soup=BeautifulSoup(html,'html.parser')
images=list(dict.fromkeys((x.get('content') or x.get('src') or '') for x in soup.select('meta[property="og:image"],img') if 'ebayimg.com' in str(x)))
print(json.dumps(dict(url=url,status=result.get('status'),http_status=solution.get('status'),title=soup.title.get_text() if soup.title else '',images=images,path=str(folder/'motti-ebay.html'))),flush=True)
'''
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'market-source.json').write_bytes(r.stdout);print(r.stdout.decode())
