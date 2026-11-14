from pathlib import Path
p=Path(__file__).parent;q=Path('work/reflections-foil-tables')
(p/'api-core.py').write_bytes((q/'api-core.py').read_bytes())
s=(q/'publish.py').read_text().replace('Verified foil tables and contribution marker (#430)','Verified foil photograph framing and orientation (#436)')
(p/'publish.py').write_text(s)
s=(q/'store.py').read_text().replace('codex/reflections-foil-tables-430','codex/foil-display-fixes-436').replace('authoring/reflections_foil_tables430/work/reflections-foil-tables/','authoring/foil_display436/work/foil-display-fixes/').replace('evidence/430/','evidence/436/').replace('430-reflections-foil-tables','436-foil-display-fixes').replace('Display Reflections foil tables and scan contribution requests (Refs swccg-guild/work#430)','Correct foil photo framing and inline-symbol sizing (Refs swccg-guild/work#436)')
s=s.replace("if mode=='wiki' and (root/'published-heads.json').exists():","if mode=='wiki':files['wiki/SwccgChrome.php']=(root/'SwccgChrome.php').read_bytes()\nif mode=='wiki' and (root/'published-heads.json').exists():")
(p/'store.py').write_text(s)
