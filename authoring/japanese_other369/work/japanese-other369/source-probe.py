import json,re
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
root=Path(__file__).parent
sources=[('motti-ebay','https://www.ebay.com/itm/175133384414'),('fx7-store','https://www.swccgstore.com/SWCCG-FX-7-Effex-Seven-Jap-p/jap0592.htm'),('anh-store','https://www.swccgstore.com/category-s/205.htm')]
records=[]
for name,url in sources:
    try:
        response=requests.get(url,timeout=40);response.raise_for_status();text=response.text;(root/(name+'.html')).write_text(text,encoding='utf8')
        soup=BeautifulSoup(text,'html.parser');images=[]
        for tag in soup.select('meta[property="og:image"],img'):
            src=tag.get('content') or tag.get('src') or ''
            if ('ebayimg.com' in src or 'JAP' in src.upper()) and not src.endswith('.gif'):images.append(urljoin(url,src))
        records.append(dict(name=name,url=url,status=response.status_code,title=soup.title.get_text() if soup.title else '',images=list(dict.fromkeys(images))))
    except Exception as error:records.append(dict(name=name,url=url,error=str(error)))
(root/'source-probe.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
for row in records:print(row['name'],row.get('title',row.get('error')),len(row.get('images',[])),row.get('images',[])[:2],flush=True)
