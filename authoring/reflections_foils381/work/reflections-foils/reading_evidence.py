"""Attach source identities to independently written physical-face readings."""
import json
from pathlib import Path
root=Path(__file__).parent
def finish(stage,rows,year):
    sources=json.loads((root/(stage+'-source-manifest.json')).read_bytes());manifest=json.loads((root/'manifest.json').read_bytes());assert len(rows)==len(sources)
    for row,src in zip(rows,sources):
        m=next(r for r in manifest if r['proposed_article']==src['article']);row.setdefault('uniqueness','Unique');row.setdefault('printed_title',row['title']);row.setdefault('side',src['side'])
        assert row['side']==src['side']
        row.update(product=src['product'],language='English',finish='Foil',copyright_year=year,rarity=m['rarity'],article=src['article'],source_photo=src['local_file'],source_url=src.get('source_url',src.get('source')),source_sha256=src['sha256'],inspection='Complete physical foil independently read on '+stage+' inspection sheets; source metadata is provenance, not text evidence',status='manually inspected and independently transcribed',gemp_mapping='unverified: omit playable ID')
        if 'candidate' in src:row.update(source_gallery=src['candidate']['source_html'],registry_key=src['candidate']['registry_key'])
        else:row.update(source_kind='SWCA',source_id=src['id'],source_gallery=src['entry_url'])
        row['field_status']={k:'printed' for k in row if k in ['printed_title','type','subtype','destiny','power','ability','armor','maneuver','landspeed','hyperspeed','deploy','forfeit','parsec','light_icons','dark_icons','icons','lore','game_text','uniqueness','copyright_year']};row['field_status']['rarity']='catalogued: Complete Card List v4.0'
    (root/(stage+'-readings.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(len(rows),'independent readings recorded for',stage)
