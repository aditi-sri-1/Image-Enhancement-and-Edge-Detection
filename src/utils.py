import os
import json

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_summary(outdir, data):
    with open(os.path.join(outdir, 'summary.json'), 'w') as f:
        json.dump(data, f, indent=2)
