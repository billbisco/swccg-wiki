from pathlib import Path
from PIL import Image,ImageDraw
root=Path(__file__).parent
for name in ['2-1b','fx7','creature']:
    canvas=Image.new('RGB',(1100,900),'white');draw=ImageDraw.Draw(canvas)
    for x,stage in [(0,'before'),(550,'live')]:
        im=Image.open(root/(stage+'-'+name+'.webp')).convert('RGB');im.thumbnail((540,860))
        canvas.paste(im,(x,35));draw.text((x+10,10),('Before (saved revision)' if stage=='before' else 'After (verified public revision)'),fill='black')
    canvas.save(root/('comparison-'+name+'.webp'),quality=80,method=6)
(root/'visual-review.md').write_text('''# Visual review — 13 November 2026

Twelve final public captures pass: 2-1B, FX-7, R3-T6, Brainiac, Y-wing Assault Squadron, Arcona, Wampa, both Hoth Echo Command Centers, Hoth checklist, and two 390px mobile views. All images load, there are no Cite errors, and the rotated location face fits its 280px container on desktop/mobile.

Viewed final FX-7, Dark Echo Command, mobile Light Echo Command and squadron captures directly: native glyphs render, original photo detail is retained, the location lies upright, metadata and body remain readable, and repeated squadron icons remain distinct. Saved old-revision captures for 2-1B, FX-7 and Wampa provide before/after pairs. Comparisons are layout aids, not pixel-equality tests: content additions intentionally change heights. The 50 English controls compare parsed DOM exactly and all remain identical.

- [2-1B before/after](comparison-2-1b.webp)
- [FX-7 before/after](comparison-fx7.webp)
- [Wampa before/after](comparison-creature.webp)
- [Public capture manifest](live-visual.json)
- [Old-revision manifest](before-visual.json)
- [English controls](rotation-english-report.json)

No separate wiki Test server exists. Phase-three orientation was first checked with four sandbox/browser examples and all English controls; the opt-in then went live and was checked in the public pages. Earlier batches have saved parse previews and exact source/review receipts. No additional reviewer was requested or required.
''',encoding='utf8')
print('Three comparison artifacts saved')
