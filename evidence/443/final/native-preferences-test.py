from pilotlib import *
code="""from pathlib import Path
import json,requests
exec(Path('/mnt/HC_Volume_107153504/work/memorycore-vader-429-20261114/publisher.py').read_text().split('mode=sys.argv[1]')[0])
KEY='swccg-card-images';s1=s
before=api(action='query',meta='userinfo',uiprop='options',assertuser='Memory Core ChatGPT')['query']['userinfo']['options'].get(KEY,'original')
assert before in ['original','remastered']
proof={}
try:
 result=api(action='options',change=KEY+'=remastered',assertuser='Memory Core ChatGPT',token=token)
 assert result.get('options')=='success',result.get('warnings')
 s2=requests.Session()
 def second(**params):
  r=s2.post(URL,data={'format':'json','formatversion':2,**params},timeout=40);r.raise_for_status();v=r.json();assert'error'not in v,v.get('error',{}).get('code');return v,r.headers.get('Cache-Control','')
 login,_=second(action='query',meta='tokens',type='login');assert second(action='login',lgname='Memory Core ChatGPT',lgpassword=values['p'],lgtoken=login['query']['tokens']['logintoken'])[0]['login']['result']=='Success'
 user,headers=second(action='query',meta='userinfo',uiprop='options',assertuser='Memory Core ChatGPT');assert user['query']['userinfo']['options'].get(KEY)=='remastered'
 anon=requests.get(URL,params={'action':'query','format':'json','formatversion':2,'meta':'userinfo','uiprop':'options'},timeout=40).json()['query']['userinfo'];assert anon.get('anon')is True
 assert anon.get('options',{}).get(KEY,'original')=='original'
 proof={'account':'Own Memory Core ChatGPT bot only','account_saved_default':'remastered','fresh_independent_cookie_session_readback':'remastered','account_sessions_distinct':s1.cookies.get_dict()!=s2.cookies.get_dict(),'authenticated_cache_control':headers,'anonymous_response_is_anon':True,'anonymous_effective_default':'original','guest_browser_storage_touched':False,'other_account_options_recorded':False,'provider_requests':0}
finally:
 s=s1;assert api(action='options',change=KEY+'='+before,assertuser='Memory Core ChatGPT',token=token).get('options')=='success'
 restored=api(action='query',meta='userinfo',uiprop='options',assertuser='Memory Core ChatGPT')['query']['userinfo']['options'].get(KEY,'original');assert restored==before
proof['original_effective_account_preference_restored']=True
print(json.dumps(proof))
"""
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);assert r.returncode==0,r.stderr.decode(errors='replace')[-1600:];save('native-preferences-check.json',json.loads(r.stdout));print(r.stdout.decode())
