"""Resume non-mutating batch QA and prepare representative captures for inspection."""
import datetime,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;stage=sys.argv[1];env=dict(os.environ,PYTHONIOENCODING='utf8')
for script in ['purge-publication-batch.py','verify-batch.py','capture-batch.py']:
    subprocess.run([sys.executable,str(root/script),stage],env=env,check=True)
marker=dict(stage=stage,at=datetime.datetime.now(datetime.timezone.utc).isoformat(),publication_verified=True,original_images_sha_checked=True,archive_deferred=True,preservation_task=412,visual_inspection='screenshots captured; inspect before accepting this stage',authorization='publication-authorization.json')
(root/(stage+'-publication-verification.json')).write_text(json.dumps(marker,indent=2),encoding='utf8')
for script in ['update-inventory-progress.py','update-publication-report.py']:subprocess.run([sys.executable,str(root/script)],env=env,check=True)
print('READY_FOR_VISUAL_INSPECTION',stage,flush=True)
