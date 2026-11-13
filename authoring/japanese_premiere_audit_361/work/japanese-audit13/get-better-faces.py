import base64
import json
from pathlib import Path
import re
import subprocess

root=Path('work/japanese-audit13')
source=Path('work/japanese-complete/swca-service-fetch.py').read_text(encoding='utf8')
source=re.sub(r'sources = \{.*?\n\}',"sources = {'12508':'duncan-images/1GAMES/GA06478.JPG','12548':'duncan-images/1GAMES/GA06523.JPG'}",source,count=1,flags=re.S)
process=subprocess.run(['ssh','-o','BatchMode=yes','gemp','docker','exec','-i','-w','/app','flaresolverr','python','-'],input=source.encode(),stdout=subprocess.PIPE,check=True)
manifest=[]
for row in map(json.loads,process.stdout.splitlines()):
    data=row.pop('data',None)
    row.pop('rendered_png',None)
    if data:
        file=root/('original-'+row['id']+'.jpg')
        file.write_bytes(base64.b64decode(data))
        row['local_path']=str(file)
    manifest.append(row)
    print(row)
(root/'better-faces.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
