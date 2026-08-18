#!/usr/bin/env python3
import argparse, json, pathlib, sys
from common import TEXT_EXTS, IMAGE_EXTS
from text_hygiene import inspect as inspect_text
from image_meta import parse_png, parse_jpeg_segments, jpeg_label

p = argparse.ArgumentParser()
p.add_argument("path")
a = p.parse_args()
root = pathlib.Path(a.path)
results = []
for path in root.rglob("*"):
    if not path.is_file():
        continue
    ext = path.suffix.lower()
    try:
        if ext in TEXT_EXTS:
            findings = inspect_text(path.read_text(encoding="utf-8"))
            if findings:
                results.append({"file":str(path),"type":"text","findings":findings})
        elif ext == ".png":
            chunks = [c.decode("latin1") for c, _ in parse_png(path.read_bytes())]
            hits = [c for c in chunks if c in {"tEXt","zTXt","iTXt","eXIf","caBX"}]
            if hits:
                results.append({"file":str(path),"type":"PNG","metadata_candidates":hits})
        elif ext in {".jpg", ".jpeg"}:
            labels = [jpeg_label(m, r) for m, r in parse_jpeg_segments(path.read_bytes())]
            hits = [x for x in labels if x.startswith("APP1") or x.startswith("APP11") or x == "COM"]
            if hits:
                results.append({"file":str(path),"type":"JPEG","metadata_candidates":hits})
    except Exception as e:
        results.append({"file":str(path),"error":str(e)})
print(json.dumps({"root":str(root),"result_count":len(results),"results":results}, indent=2))
