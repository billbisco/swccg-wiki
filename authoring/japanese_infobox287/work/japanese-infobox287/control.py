import gzip,json,requests
from pathlib import Path
from bs4 import BeautifulSoup,Comment
root=Path(__file__).parent
heads=json.loads((root/'heads-before.json').read_bytes())
title=json.loads((root/'english-sample.json').read_bytes())[0]
text=heads[title]['revisions'][0]['slots']['main']['content']
result=requests.post('https://wiki.swccg.com/api.php',data=dict(format='json',formatversion=2,action='parse',title=title,text=text,prop='text')).json()['parse']['text']
old=json.load(gzip.open(root/'before-renders.json.gz','rt',encoding='utf8'))[title]['text']
new=json.load(gzip.open(root/'english-sandbox-renders.json.gz','rt',encoding='utf8'))[title]['text']
def clean(text):
    soup=BeautifulSoup(text,'html.parser')
    for comment in soup.find_all(string=lambda x:isinstance(x,Comment)):comment.extract()
    return str(soup)
print(title,'oldid versus fresh original',clean(old)==clean(result),'fresh original versus sandbox',clean(result)==clean(new))
(root/'english-fresh-control.json').write_text(json.dumps(dict(title=title,oldid_vs_fresh=clean(old)==clean(result),fresh_vs_sandbox=clean(result)==clean(new))),encoding='utf8')
