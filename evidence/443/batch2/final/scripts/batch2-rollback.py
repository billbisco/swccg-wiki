from b2common import *
expected=read('deploy.json')['sha256'];title=read('inventory.json')[1]['canonical']
code="""from pathlib import Path
import requests,subprocess,hashlib,json,datetime,urllib.parse
root=Path('/mnt/HC_Volume_107153504/work/memorycore-443-ovs1-batch2-20261114');target=Path('/opt/swccg-wiki/chrome/card-image-pilot.json');current=target.read_bytes();old=(root/'before-batch2-manifest.json').read_bytes();assert hashlib.sha256(current).hexdigest()==EXPECTED;title=TITLE
def purge():
 r=subprocess.run(['docker','exec','-i','-u','www-data','swccg_wiki','php','maintenance/run.php','purgePage'],input=(title+'\\n').encode(),capture_output=True);assert r.returncode==0,r.stderr.decode()
 cache=Path('/var/cache/nginx/wiki-live');path='/wiki/'+title.replace(' ','_')
 for path in{path,urllib.parse.quote(path,safe=\"/():\"),urllib.parse.quote(path,safe=\"/():'\")}:
  key='httpswiki.swccg.com'+path;digest=hashlib.md5(key.encode()).hexdigest();entry=cache/digest[-1]/digest[-3:-1]/digest;assert entry.resolve().is_relative_to(cache.resolve())
  if entry.is_file():
   with entry.open('rb')as f:header=f.read(2048)
   assert('KEY: '+key+'\\n').encode()in header;entry.unlink()
url='https://wiki.swccg.com/wiki/'+title.replace(' ','_');result={}
try:
 target.write_bytes(old);purge();r=requests.get(url,timeout=45);r.raise_for_status();assert'"swccgCardImagePilot"'not in r.text and'Holotable-OVS1-Fusion-Generator-Supply-Tanks-Light-v17.gif'in r.text and'Card Text'in r.text;result['prior_cohort_native_fallback']='PASS'
finally:
 target.write_bytes(current);assert target.read_bytes()==current;purge()
r=requests.get(url,timeout=45);r.raise_for_status();assert'"swccgCardImagePilot"'in r.text and'else (root.RLQ'in r.text
result.update(activation_restored='PASS',at=datetime.datetime.now(datetime.timezone.utc).isoformat(),manifest_sha256=hashlib.sha256(current).hexdigest(),wiki_edits=0,server_configuration_changes=0,scope='Prior four-page cohort restored briefly, one new article response verified, exact twelve-card manifest restored in finally; existing sources and uploads retained')
print(json.dumps(result))
""".replace('EXPECTED',repr(expected)).replace('TITLE',repr(title))
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);assert r.returncode==0,r.stderr.decode(errors='replace')[-1600:];save('rollback-probe.json',json.loads(r.stdout));print(r.stdout.decode())
