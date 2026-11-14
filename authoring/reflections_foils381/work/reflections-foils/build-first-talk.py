import json
from pathlib import Path
root=Path(__file__).parent
readings=json.loads((root/'first-readings.json').read_bytes());files=json.loads((root/'first-files-payload.json').read_bytes())
rows=[]
for r,f in zip(readings,files):
    text='== Build notes ==\nThe Reflections foil publication was checked against [[:'+f['title']+'|the original physical foil photograph]] (PSA certification '+r['physical_cert']+'). The full original JPEG and source provenance are retained on the File page. Printed wording and statistics were read from this face; the earlier non-foil article is a comparison, not replacement text. Publication identity is recorded separately from any unverified playable mapping.\n\n'
    if r['title']=='Black 2':text+='The foil prints “May add 1 pilot.” It does not print the additional pilot-aboard requirement on [[Black 2]].\n\n'
    if r['title']=='Biggs Darklighter':text+='The foil prints “anything he pilots” and “When piloting Red 3”; preserve those words separately from [[Biggs Darklighter|the original printing]].\n\n'
    text+='~~~~\n'
    rows.append(dict(title='Talk:'+r['article'],text=text,new=True,signed_note=True,summary='Record physical-foil source verification and printing distinctions (#381)'))
(root/'first-talk-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
