import base64,hashlib,json,subprocess
from pathlib import Path
import requests
p=Path(__file__).parent;raw=(p/'preview.html').read_bytes().replace(b'\r\n',b'\n').rstrip()+b'\n';(p/'preview.html').write_bytes(raw)
prior=json.loads((p/'preview-deployment.json').read_bytes())['sha256'] if (p/'preview-deployment.json').exists() else None
code='DATA='+repr(base64.b64encode(raw).decode())+'\nPRIOR='+repr(prior)+'\n'+'''import pathlib,base64,hashlib,json
root=pathlib.Path('/opt/swccg-res/snapshots');assert root.is_dir()
target=root/'review/story-435-set-symbols.html';target.parent.mkdir(exist_ok=True);assert target.resolve().is_relative_to(root.resolve())
data=base64.b64decode(DATA);assert not target.exists() or target.read_bytes()==data or hashlib.sha256(target.read_bytes()).hexdigest()==PRIOR,'Existing different review file; do not overwrite'
target.write_bytes(data);target.chmod(0o644)
print(json.dumps(dict(path=str(target),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))))
'''
deployment=json.loads(subprocess.check_output(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode()))
url='https://swccg.com/snapshots/review/story-435-set-symbols.html';r=requests.get(url,timeout=60);r.raise_for_status();assert r.content==raw and r.headers.get('Content-Type','').startswith('text/html')
deployment.update(url=url,public_exact_readback=True,source_backup_commit=(p/'wiki-commit.txt').read_text().strip(),source_backup_path='authoring/set_symbols435/preview.html')
(p/'preview-deployment.json').write_text(json.dumps(deployment,indent=2),encoding='utf8');print(url,'exact public HTML bytes verified')
