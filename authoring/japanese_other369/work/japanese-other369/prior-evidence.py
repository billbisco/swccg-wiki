import base64,json,subprocess
from pathlib import Path
root=Path(__file__).parent
for file in ['named-source-gaps.md','HANDOFF.md','hoth-video-frames.json','expanded-collector-source-index.json','indexed-face-coverage.csv','vehicle-icons-verified.json']:
    response=json.loads(subprocess.check_output(['gh','api','repos/swccg-guild/work/contents/evidence/226/'+file]))
    data=base64.b64decode(response['content']);(root/('prior-'+file)).write_bytes(data)
    if file=='named-source-gaps.md':print(data.decode()[:3500])
    else:print(file,len(data),'bytes')
