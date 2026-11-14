from pilotlib import *
titles=list(read('source/chrome/card-image-pilot.json')['pages']);expected=sha((P/'source/chrome/card-image-pilot.json').read_bytes())
code="""from pathlib import Path
import requests,subprocess,hashlib,json,datetime
titles=TITLES;manifest=Path('/opt/swccg-wiki/chrome/card-image-pilot.json');payload=manifest.read_bytes();assert hashlib.sha256(payload).hexdigest()==EXPECTED
root=Path('/mnt/HC_Volume_107153504/work/memorycore-443-ovs-pilot-20261114');backup=root/'activation-rollback-manifest.json';backup.write_bytes(payload);assert backup.read_bytes()==payload
def purge():
 r=subprocess.run(['docker','exec','-i','-u','www-data','swccg_wiki','php','maintenance/run.php','purgePage'],input=('\\n'.join(titles)+'\\n').encode(),capture_output=True);assert r.returncode==0,r.stderr.decode()
 cache=Path('/var/cache/nginx/wiki-live')
 for title in titles:
  key='httpswiki.swccg.com/wiki/'+title.replace(' ','_');h=hashlib.md5(key.encode()).hexdigest();entry=cache/h[-1]/h[-3:-1]/h;assert entry.resolve().is_relative_to(cache.resolve())
  if entry.is_file():
   with entry.open('rb')as f:header=f.read(2048)
   assert('KEY: '+key+'\\n').encode()in header;entry.unlink()
url='https://wiki.swccg.com/wiki/SWCCG_Wiki:Samples/Original_Virtual_Darth_Vader_image_viewer';result={}
try:
 manifest.unlink();purge();r=requests.get(url,timeout=40);r.raise_for_status()
 assert'"swccgCardImagePilot"'not in r.text
 assert'Holotable-OVS1-Darth-Vader-v17.gif'in r.text and'Card Text'in r.text
 result['activation_disabled_native_fallback']='PASS'
finally:
 manifest.write_bytes(payload);manifest.chmod(0o644);assert manifest.read_bytes()==payload;purge()
r=requests.get(url,timeout=40);r.raise_for_status();assert'"swccgCardImagePilot"'in r.text and'else (root.RLQ'in r.text
result.update(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),activation_restored='PASS',manifest_sha256=hashlib.sha256(payload).hexdigest(),wiki_content_edits=0,server_configuration_changes=0,provider_requests=0,scope='Four pilot responses only; original files, card content, saved account options and other samples retained')
(root/'rollback-probe.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
""".replace('TITLES',repr(titles)).replace('EXPECTED',repr(expected))
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);assert r.returncode==0,r.stderr.decode(errors='replace')[-1600:];save('rollback-probe.json',json.loads(r.stdout));print(r.stdout.decode())
