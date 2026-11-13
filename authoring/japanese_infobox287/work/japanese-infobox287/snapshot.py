import subprocess
code='''
import subprocess
from pathlib import Path
root=Path('/mnt/HC_Volume_107153504/work/memorycorechatgpt-infobox287-20261113')
subprocess.run(['python3','/opt/swccg-ops/repos/swccg-wiki/authoring/make_snapshot.py',str(root/'bgg.html'),'--url','https://boardgamegeek.com/filepage/33565/star-wars-ccg-complete-card-list-43','-o',str(root/'bgg-snapshot.html')],check=True)
'''
subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),check=True)
