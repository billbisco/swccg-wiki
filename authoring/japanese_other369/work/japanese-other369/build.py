import hashlib,json,re,sys
from pathlib import Path
import requests
root=Path(__file__).parent
sys.path[:0]=[str(root.parent/'japanese-infobox287'/'vendor'),'work/wiki-tools']
import mwparserfromhell as mw
from style_lint import lint
manifest=json.loads((root/'face-manifest.json').read_bytes())
titles=[r['title'] for r in manifest]+['2-1B (Too-Onebee) (Japanese)']
def api(**kwargs):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(format='json',formatversion=2,**kwargs),timeout=60);response.raise_for_status();j=response.json();assert 'error' not in j,j;return j
pages=api(action='query',titles='|'.join(titles),prop='revisions',rvprop='ids|timestamp|content',rvslots='main')['query']['pages']
heads={p['title']:p for p in pages}
(root/'phase1-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
patches={
 'Death Star (Japanese)':dict(printed_title='<span lang="ja">＊デス・スター</span>',printed_game_text='<span lang="ja">X＝現在位置のパーセク数。パーセク0に配備する。航行速度＝1。「革命」の影響を受けない。ゲーム開始時に出したならライトサイドが先攻。</span><ref name="jp-face" />',translation="'''Title:''' Death Star.\n\n'''Card text:''' X = the parsec number of the current location. Deploy at parsec 0. Hyperspeed = 1. Not affected by Revolution. If put out at the start of the game, the Light Side goes first.",dark_icons='3<ref name="jp-face" />',light_icons='0<ref name="jp-face" />'),
 'Death Star: Conference Room (Japanese)':dict(light_icons='0<ref name="jp-face" />'),
 'Death Star (Japanese Reflections II Foil)':dict(dark_icons='3<ref name="jp-face" />',light_icons='0<ref name="jp-face" />'),
 'Tantive IV (Japanese)':dict(printed_title='<span lang="ja">＊タンティヴィIV</span>',printed_game_text='<span lang="ja">パイロットを3人と、乗客を4人追加できる。ドッキング能力を持つ。能力値2の専属パイロットが搭乗している。どんな星系にでも配備できる（たとえ人員とフォース・アイコンがなくても）。</span><ref name="jp-face" />',printed_lore="''<span lang=\"ja\">オルデラン総督家の外交船。レイア姫が帝国元老員としての職務（そして反乱軍の極秘任務）に使用した。タトゥイーン軌道上でデバステーターに拿捕された。</span>''<ref name=\"jp-face\" />",translation="'''Title:''' Tantive IV.\n\n'''Card text:''' May add 3 pilots and 4 passengers. Has docking capability. A permanent pilot with ability 2 is aboard. May deploy at any system (even without personnel and Force icons).\n\n'''Lore:''' Diplomatic ship of Alderaan's ruling family. Princess Leia used it for her duties as an Imperial senator (and for secret Rebel missions). Captured by Devastator in orbit over Tatooine.",extra_info='<tr><th>Printed subtype</th><td><span lang="ja">大型艦：コルベット</span><ref name="jp-face" /></td></tr>'),
}
for title in ['Leia (Japanese ESB Two-Player)','Leia (Japanese Reflections II Foil)']:
    patches[title]=dict(printed_game_text='<span lang="en">The game-text box is blank.</span><ref name="jp-face" />')
newfile='Japanese-Hoth-2-1B-PSA-175224368.jpg'
patches['2-1B (Too-Onebee) (Japanese)']=dict(title='2-1B (Too-Onebee)',image=newfile,type_display='[[Character]] ([[Droid]])',destiny='1<ref name="jp-face" />',power='0<ref name="jp-face" />',deploy='2<ref name="jp-face" />',forfeit='5<ref name="jp-face" />',uniqueness='Unique<ref name="jp-face" />',printed_title='<span lang="ja">＊2-1B（トゥ・ワンビー）</span>',printed_game_text='<span lang="ja">1ターンに1回、同じ位置か隣接した位置でロストしたドロイド以外のキャラクターを1名、ロストデッキの代わりにユーズドデッキに移せる。バクタ・タンクのXの値から2を引ける（累積可能）。</span><ref name="jp-face">[[:File:'+newfile+'|Original Japanese Hoth printed face]].</ref>',printed_lore="''<span lang=\"ja\">ジーンテック社製。ドロイドとしては非常に強い自我を持つ。いやいや仕えていたフィアロ駐留のモフから、タイリーが逃がしてくれた。以来、同盟軍で働いている。</span>''<ref name=\"jp-face\" />",translation="'''Title:''' 2-1B (Too-Onebee).\n\n'''Card text:''' Once per turn, one non-droid character lost at the same or an adjacent location may be moved to the Used Deck instead of the Lost Deck. May subtract 2 from Bacta Tank's X value (cumulative).\n\n'''Lore:''' Manufactured by Geentech. Has a very strong sense of self for a droid. Tiree helped him escape from the Moff stationed on Firro, whom he had served unwillingly. He has worked for the Alliance ever since.",extra_info='<tr><th>Printed subtype</th><td><span lang="ja">医療用ドロイド</span><ref name="jp-face" /></td></tr>\n<tr><th>Subtype</th><td>[[Droid]]</td></tr>')
rows=[];readings=[]
for title,values in patches.items():
    page=heads[title];rev=page['revisions'][0];old=rev['slots']['main']['content'];code=mw.parse(old)
    template=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    # Preserve full existing source definitions before replacing ref-only placeholders.
    definitions=''.join(re.findall(r'<ref name="jp-face">.*?</ref>',str(template.get('printed_game_text').value),re.S))
    if definitions and not any('<ref name="jp-face">' in str(p.value) for p in template.params if str(p.name).strip()!='printed_game_text'):
        notes=str(template.get('notes').value).replace('<ref name="jp-face" />',definitions,1)
        template.add('notes',notes,preserve_spacing=False)
    for key,value in values.items():template.add(key,value+'\n',preserve_spacing=False)
    if title.startswith('Leia '):
        template.add('translation',str(template.get('translation').value).rstrip()+"\n\n'''Game text:''' None printed.\n",preserve_spacing=False)
    if title.startswith('2-1B'):
        lead=str(template.get('lead').value).replace("'''2-1B (Too-Onebee) (Japanese)'''","'''2-1B (Too-Onebee)'''")
        lead=lead.replace("'''Incomplete article.''' The original Japanese card image has not yet been added here.",'').rstrip()+'\n'
        template.add('lead',lead,preserve_spacing=False)
        assert str(template.get('extra_sections').value).strip()=='<h2>Statistics</h2>\nPrinted statistics, subtype, symbols and uniqueness markers: not yet transcribed.'
        template.remove('extra_sections')
    new=str(code);assert not lint(new,title)[0],(title,lint(new,title))
    rows.append(dict(title=title,text=new,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Complete verified Japanese printed text, translation and statistics from the original face (#369)'))
    readings.append(dict(title=title,source_file='File:'+newfile if title.startswith('2-1B') else next(r['source_file'] for r in manifest if r['title']==title),verified_fields=values,printed_blank_game_text=title.startswith('Leia ')))
# Only the Card list section of the set page changes.
page=json.loads((root/'hoth-set-before.json').read_bytes());rev=page['revisions'][0];old=rev['slots']['main']['content']
needle='| [[2-1B (Too-Onebee) (Japanese)|2-1B (Too-Onebee)]] || Character || Rare1'
replacement='| [[File:'+newfile+'|36px|link=2-1B (Too-Onebee) (Japanese)|alt=Japanese 2-1B]] [[2-1B (Too-Onebee) (Japanese)|2-1B (Too-Onebee)]] || Character || Rare1'
assert old.count(needle)==1
sections=api(action='parse',page=page['title'],prop='sections')['parse']['sections'];index=next(s['index'] for s in sections if s['line']=='Card list')
section=api(action='query',titles=page['title'],prop='revisions',rvprop='content',rvslots='main',rvsection=index)['query']['pages'][0]['revisions'][0]['slots']['main']['content']
assert section.count(needle)==1
new=old.replace(needle,replacement,1);assert not lint(new,page['title'])[0],lint(new,page['title'])
rows.append(dict(title=page['title'],text=new,section=index,section_text=section.replace(needle,replacement,1),before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),summary='Link the verified Japanese Hoth 2-1B original photograph in the card list (#369)'))
(root/'phase1-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
(root/'readings.json').write_text(json.dumps(readings,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'guarded article/set drafts; lint 0')
