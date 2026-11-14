import subprocess
from pathlib import Path
code='''
import pathlib,re,datetime,json,os,subprocess
p=pathlib.Path('/opt/swccg-wiki/extra-settings.php');old=p.read_bytes();s=old.decode();matches=re.findall(r"^\\$wgCacheEpoch = '[0-9]{14}';$",s,re.M);assert len(matches)==1
newvalue=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S');newline="$wgCacheEpoch = '"+newvalue+"';"
backup=pathlib.Path('/mnt/HC_Volume_107153504/work/memorycore-foil-display-436/extra-settings.before.php');assert not backup.exists();backup.write_bytes(old)
new=s.replace(matches[0],newline).encode()
check=subprocess.run(['docker','exec','-i','swccg_wiki','php','-l','/dev/stdin'],input=new,stdout=subprocess.PIPE);assert check.returncode==0
assert p.read_bytes()==old
with p.open('wb') as f:f.write(new);f.flush();os.fsync(f.fileno())
subprocess.run(['docker','exec','swccg_wiki','apachectl','graceful'],check=True)
print(json.dumps(dict(before=matches[0],after=newline,only_cache_epoch_changed=True,backup=str(backup))))
'''
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
Path(__file__).with_name('cache-epoch-deployment.json').write_bytes(r.stdout);print(r.stdout.decode())
