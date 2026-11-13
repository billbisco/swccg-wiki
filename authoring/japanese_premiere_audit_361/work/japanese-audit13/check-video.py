import json
from pathlib import Path
import subprocess

code='''
import gzip,hashlib,json,urllib.request
url='https://web.archive.org/web/20261106164955id_/https://www.youtube.com/watch?v=qqdS5JpNPiE'
with urllib.request.urlopen(url,timeout=45) as response:
    raw=response.read()
data=gzip.decompress(raw) if raw[:2]==b'\\x1f\\x8b' else raw
text=data.decode('utf8')
assert all(x in text for x in ['qqdS5JpNPiE','Star Wars CCG Japanese Premiere Complete Set','swccgBoosterBreaks'])
print(json.dumps(dict(kind='video_page',capture=url.replace('id_/','/'),verified=True,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),compressed=raw!=data)))
'''
result=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
Path('work/japanese-audit13/video-capture.json').write_bytes(result.stdout)
print(result.stdout.decode())
