import json
from pathlib import Path
p=Path(__file__).parent;rows=json.loads((p/'main-packet.json').read_bytes())
names=['Rebel Leadership (Reflections III Foil)','Coruscant: Jedi Council Chamber (Reflections III Foil)','Cloud City: Guest Quarters (Reflections Foil)',"Dagobah: Yoda's Hut (Reflections Foil)",'Death Star: Trench (Reflections Foil)','Rendezvous Point (Reflections Foil)','Luke Skywalker (Reflections Foil)','Gold Squadron 1 (Reflections II Foil)','Death Star II (Dark) (Reflections II Foil)','Battle Deployment (Reflections III Foil)','Yavin 4: Massassi Throne Room (Reflections II Foil)','Executor (Reflections Foil)']
assert set(names)<=set(r['title'] for r in rows)
for stage,selected in [('pilot',[r for r in rows if r['title'].startswith('Template:') or r['title'] in names]),('remaining',[r for r in rows if not r['title'].startswith('Template:') and r['title'] not in names])]:
    (p/(stage+'-packet.json')).write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf8')
    print(stage,len(selected))
