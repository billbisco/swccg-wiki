import subprocess
code='''
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.request,gzip
path=Path('/mnt/HC_Volume_107153504/work/memorycorechatgpt-infobox287-20261113/bgg.html')
for name,data in [('live',path.read_bytes()),('archive',urllib.request.urlopen('https://web.archive.org/web/20261026191455id_/https://boardgamegeek.com/filepage/33565/star-wars-ccg-complete-card-list-43',timeout=45).read())]:
    if data[:2]==b'\\x1f\\x8b':data=gzip.decompress(data)
    soup=BeautifulSoup(data.decode('utf8','replace'),'html.parser')
    for tag in soup.select('script,style'):tag.decompose()
    print(name,soup.get_text(' ',strip=True)[:6500])
'''
subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),check=True)
