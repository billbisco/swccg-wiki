"""Documented scoped MediaWiki maintenance purge; no content or configuration changes."""
import json,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;stage=sys.argv[1];titles=set()
for kind in ['new','family-final','shared-nav','set','talk','correction']:
    path=root/(stage+'-'+kind+'-packet.json')
    if path.exists():titles.update(r['title'] for r in json.loads(path.read_bytes()))
packet=root/(stage+'-packet.json')
if packet.exists():titles.update(r['title'] for r in json.loads(packet.read_bytes()))
files=root/(stage+'-files-payload.json')
if files.exists():titles.update(r['title'] for r in json.loads(files.read_bytes()))
assert titles,'No approved packet titles supplied'
code='TITLES='+repr(sorted(titles))+'\n'+'''import subprocess
result=subprocess.run(['docker','exec','-i','-u','www-data','swccg_wiki','php','maintenance/run.php','purgePage'],input=('\\n'.join(TITLES)+'\\n').encode(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
print(result.stdout.decode());raise SystemExit(result.returncode)
'''
result=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/(stage+'-maintenance-purge.txt')).write_bytes(result.stdout)
print(len(titles),'approved batch titles purged as www-data; content/reviews/configuration unchanged')
