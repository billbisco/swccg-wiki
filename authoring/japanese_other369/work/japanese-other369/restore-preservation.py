import base64,json,subprocess
from pathlib import Path
root=Path(__file__).parent
failed=root/'recovered-preservation.json'
if failed.exists():(root/'recovered-preservation-v2-attempt.json').write_bytes(failed.read_bytes())
result=json.loads(subprocess.check_output(['gh','api','repos/swccg-guild/work/contents/evidence/369/recovered-preservation.json?ref=f71c3949cb5deb89170638d96ce318e13dee6e9c']))
data=base64.b64decode(result['content']);record=json.loads(data)
assert record['verified'] and record['sha256']=='74179307dcfa46d75f95250bfb3dcb26b1f9511c27426323af0bb88fcc6c5b18'
(root/'recovered-preservation-v1.json').write_bytes(data);failed.write_bytes(data)
print('Restored byte-verified original-photo preservation receipt from shared evidence')
