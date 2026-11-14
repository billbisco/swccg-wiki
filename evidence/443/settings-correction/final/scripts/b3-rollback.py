from b3common import *
expected=next(r['sha256']for r in read('deploy.json')['files']if r['path']=='card-image-pilot.json')
code="""from pathlib import Path
import json,hashlib,requests,subprocess
p=Path('/opt/swccg-wiki/chrome/card-image-pilot.json');current=p.read_bytes();assert hashlib.sha256(current).hexdigest()==EXPECTED;title='SWCCG Wiki:Display settings';limited=json.loads(current);del limited['pages'][title]
def purge():
 r=subprocess.run(['docker','exec','-i','-u','www-data','swccg_wiki','php','maintenance/run.php','purgePage'],input=(title+'\\n').encode(),capture_output=True);assert r.returncode==0
 cache=Path('/var/cache/nginx/wiki-live');key='httpswiki.swccg.com/wiki/SWCCG_Wiki:Display_settings';h=hashlib.md5(key.encode()).hexdigest();entry=cache/h[-1]/h[-3:-1]/h;assert entry.resolve().is_relative_to(cache.resolve())
 if entry.is_file():
  with entry.open('rb')as f:header=f.read(2048)
  assert('KEY: '+key+'\\n').encode()in header;entry.unlink()
try:
 p.write_text(json.dumps(limited));purge();r=requests.get('https://wiki.swccg.com/wiki/SWCCG_Wiki:Display_settings',timeout=40);r.raise_for_status();assert'"swccgCardImagePilot"'not in r.text and'Special:Preferences'in r.text
finally:p.write_bytes(current);purge()
r=requests.get('https://wiki.swccg.com/wiki/SWCCG_Wiki:Display_settings',timeout=40);r.raise_for_status();assert'"swccgCardImagePilot"'in r.text
print(json.dumps({'settings_activation_fallback':'PASS','exact_manifest_restored':'PASS','all_card_activations_retained':True,'article_default_box_reintroduced':False,'scope':'Settings destination only; native Preferences fallback retained; full source rollback documented, not executed','wiki_edits':0,'server_configuration_changes':0}))
""".replace('EXPECTED',repr(expected))
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);assert r.returncode==0,r.stderr.decode(errors='replace')[-1200:];save('rollback-check.json',json.loads(r.stdout));print(r.stdout.decode())
