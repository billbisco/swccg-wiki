"""Record the representative captures inspected by the current editor."""
import json,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;stage=sys.argv[1];seen=sys.argv[2:]
assert seen and all((root/f).is_file() for f in seen)
file=root/(stage+'-publication-verification.json');row=json.loads(file.read_bytes());assert row['publication_verified']
row.update(visual_inspection='inspected and accepted by MemoryCoreChatGPT',inspected_files=seen)
file.write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf8')
for script in ['update-inventory-progress.py','update-publication-report.py']:subprocess.run([sys.executable,str(root/script)],check=True)
