import json
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup
root=Path(__file__).parent;row=json.loads((root/'redemption-extra-source-requests.json').read_bytes())[0]
soup=BeautifulSoup((root/'source-html'/'swca-45052.html').read_bytes(),'html.parser');row['assets']=[urljoin(row['url'],im.get('src') or im.get('data-src','')) for im in soup.select('.item-media figure img')];assert row['assets'];row['purpose']='Targeted independent foil-face check of a punctuation-sized mark in the PSA photograph'
(root/'swca-probe-redemption.json').write_text(json.dumps([row],ensure_ascii=False,indent=2),encoding='utf8');print(row['assets'])
