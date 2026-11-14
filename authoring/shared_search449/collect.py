import json,re,hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
p=Path(__file__).parent
cards=['Seeking An Audience','Seeking An Audience (Reflections III Foil)','Shmi Skywalker','You Will Go To The Dagobah System','Rendezvous Point On Tatooine','Presence Of The Force','Shistavanen Wolfman','Reserve Pilot','Trade Federation Droid Control Ship','Luke Skywalker','Darth Vader','Admiral Ackbar','Bacta Tank','Captain Han Solo','Imperial Artillery','Admiral Ozzel','The Emperor','Imperial Command',"Twi'lek Advisor"]
cards+=['Officer Evax','Rebel Barrier','Houjix','Ghhhk']
decks=['2026 Retro GEMPC Timo Dusel DS Ralltiir Operations','2026 Retro GEMPC Timo Dusel LS Hidden Base','2026 Worlds Top 8 Brian Fred DS ISB','2026 Worlds Top 8 Brian Fred LS Diplo']
def fetch(ts):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(ts),prop='revisions',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
heads={h['title']:h for h in fetch(cards+decks)}
(p/'source-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
for title,h in heads.items():
    if not h.get('revisions'):print('MISSING',title);continue
    text=h['revisions'][0]['slots']['main']['content']
    if title in cards:
        fields={k:(re.search(r'^\|\s*'+k+r'\s*=([^\n]*)',text,re.M).group(1) if re.search(r'^\|\s*'+k+r'\s*=([^\n]*)',text,re.M) else '') for k in ['card_uid','gemp_id','set','set_icon','uniqueness','image','game_text']}
        print(title,fields)
    else:print('DECK',title,text[:650].replace('\n',' '),'MEDIA',re.findall(r'(?:Media:|File:)([^\]|]+\.txt)',text))
