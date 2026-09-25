import json
import hashlib
from pathlib import Path

root = Path(r'd:\2_K4_Vinuni\Lab8\K4-L2-Day08-DoanTanPhat-2A202602152-AI-Assisted-Annotation-Student')
d = root / 'data' / 'test' / 'labels'
js = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(d.glob('*.txt'))}
(root / 'data' / 'test' / 'label_hashes.json').write_text(json.dumps(js, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'updated {len(js)} hashes')
