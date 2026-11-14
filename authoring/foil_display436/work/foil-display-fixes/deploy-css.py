import subprocess,hashlib,json,base64
from pathlib import Path
root=Path(__file__).parent
new=(root/'SwccgChrome.php').read_bytes()
code='''
import base64,hashlib,pathlib,subprocess,os,json
p=pathlib.Path('/opt/swccg-wiki/SwccgChrome.php');old=p.read_bytes()
assert hashlib.sha256(old).hexdigest()=='38fb4e321f2a0abe5afc3ebd76b155541348022e06d5f080a9bf057dcd97d924','Concurrent chrome edit'
new=base64.b64decode(PAYLOAD)
check=subprocess.run(['docker','exec','-i','swccg_wiki','php','-l','/dev/stdin'],input=new,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
assert check.returncode==0,check.stdout.decode()
backup=pathlib.Path('/mnt/HC_Volume_107153504/work/memorycore-foil-display-436');backup.mkdir(exist_ok=True)
b=backup/'SwccgChrome.before.php'
assert not b.exists() or b.read_bytes()==old
b.write_bytes(old)
with p.open('wb') as f:f.write(new);f.flush();os.fsync(f.fileno())
assert p.read_bytes()==new
subprocess.run(['docker','exec','swccg_wiki','apachectl','graceful'],check=True)
print(json.dumps(dict(before_sha256=hashlib.sha256(old).hexdigest(),after_sha256=hashlib.sha256(new).hexdigest(),backup=str(b),syntax_check=check.stdout.decode().strip())))
'''
code='PAYLOAD='+repr(base64.b64encode(new).decode())+'\n'+code
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'css-deployment.json').write_bytes(r.stdout);print(r.stdout.decode())
