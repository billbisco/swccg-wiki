from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'batch2-publish.py').read_text(encoding='utf-8').replace('from b2common import *','from b3common import *').replace('memorycore-443-ovs1-batch2-20261114','memorycore-443-settings-correction-20261114').replace('Story443: audited Original/Remastered images and direct historical source provenance','Story443: move saved image default to dedicated Display settings page')
(P/'b3-publish.py').write_bytes(s.encode())
