import difflib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0,'work/wiki-tools')
from style_lint import lint
root=Path(__file__).parent
heads=json.loads((root/'heads-before.json').read_bytes())
old=heads['Template:Card']['revisions'][0]['slots']['main']['content']
text=old
def arg(name,default=''):return '{{{'+name+'|'+default+'}}}'
def choose(name,yes,no=''):return '{{#if:'+arg(name)+'|'+yes+'|'+no+'}}'
def replace(before,after):
    global text
    assert text.count(before)==1,before[:100]
    text=text.replace(before,after,1)
nav=re.search(r'<div class="card-nav">(.*?)</div>',text)[1]
replace('<div class="card-nav">'+nav+'</div>','<div class="card-nav">'+choose('navigation',arg('navigation'),nav)+'</div>')
for label,key in [('Type','type'),('GEMP ID','gemp_id'),('Dark Side Icons','dark_icons'),('Light Side Icons','light_icons'),('Icons','icons'),('Landspeed','landspeed'),('Versions','versions')]:
    replace('<th>'+label+'</th>','<th>'+arg('label_'+key,label)+'</th>')
for label,param in [('Type','type_display'),('Set','set_display')]:
    if label=='Type':pattern=r'(<tr><th>\{\{\{label_type\|Type\}\}\}</th><td>)(.*?)(</td></tr>)'
    else:pattern=r'(<tr><th>Set</th><td>)(.*?)(</td></tr>)'
    m=re.search(pattern,text)
    assert m,label
    replace(m[0],m[1]+choose(param,arg(param),m[2])+m[3])
rarity=re.search(r'(<tr><th>Rarity</th><td>)(.*?)(</td></tr>)',text)
replace(rarity[0],rarity[1]+choose('rarity_display',arg('rarity_display'),rarity[2])+rarity[3])
language=arg('language_display','{{#language:'+arg('language','en')+'|en}}')
newrows=choose('language','<tr><th>'+arg('label_language','Printed language')+'</th><td>'+language+'</td></tr>')
for name,label in [('edition','Edition'),('border_finish','Border / finish'),('release','Release'),('size','Size'),('year','Year')]:
    newrows+=choose(name,'<tr><th>'+label+'</th><td>'+arg(name)+'</td></tr>')
replace('<tr><th>Set icon</th>',choose('language',newrows)+'<tr><th>Set icon</th>')
replace('</table>',choose('extra_info',arg('extra_info'))+'</table>')
replace('<table class="wikitable mw-collapsible card-infobox">',choose('image_note','<div class="card-image-note">'+arg('image_note')+'</div>')+'<table class="wikitable mw-collapsible card-infobox">')
lead=re.search(r"'''\{\{\{title\}\}\}''' is a .*?\]\]\.",text)[0]
replace(lead,choose('lead',arg('lead'),lead))
game_start='{{#if:{{{game_text|}}}|<h2>Card Text</h2>'
native_title=choose('printed_title','<nowiki />\n<h2>Title</h2>\n<div lang="'+arg('language','en')+'">\n'+arg('printed_title')+'\n</div>')
replace(game_start,native_title+'{{#if:'+arg('printed_game_text',arg('game_text'))+'|<h2>Card Text</h2>')
replace('{{{game_text}}}',choose('printed_game_text','<div lang="'+arg('language','en')+'">\n'+arg('printed_game_text')+'\n</div>','{{{game_text}}}'))
replace('{{#if:{{{lore|}}}|<h2>Lore</h2>\n\'\'{{{lore}}}\'\'}}','{{#if:'+arg('printed_lore',arg('lore'))+'|<h2>Lore</h2>\n'+choose('printed_lore','<div lang="'+arg('language','en')+'">\n'+arg('printed_lore')+'\n</div>',"''{{{lore}}}''")+'}}')
translation=choose('translation','<nowiki />\n<h2>Translation of Japanese Text</h2>\n'+arg('translation'))
translation+=choose('translation_note','<nowiki />\n<h2>Comparison with the English printing</h2>\n'+arg('translation_note'))
replace('{{#if:{{{errata_history|}}}|',translation+'{{#if:{{{errata_history|}}}|')
replace('{{#if:{{{see_also|}}}|',choose('extra_sections',arg('extra_sections'))+'{{#if:{{{see_also|}}}|')
replace('<h2>See Also</h2>','<h2>'+arg('see_also_heading','See Also')+'</h2>')
# Oversized promo has no set category; retain its original four categories with an explicit override.
category_block='[[Category:Cards]][[Category:{{{set}}}]][[Category:{{{side}}}]][[Category:{{{type}}}]]'
replace(category_block,choose('category_override',arg('category_override'),category_block))
assert not lint(text,'Template:Card')[0],lint(text,'Template:Card')[0]
(root/'template-draft.wiki').write_text(text,encoding='utf8')
(root/'template.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile='Template:Card before',tofile='Template:Card after')),encoding='utf8')
print('Optional language and conservation fields prepared; original branches retained as defaults')
