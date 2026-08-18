#!/usr/bin/env python3
import argparse, json, pathlib
from image_meta import parse_png, parse_jpeg_segments, jpeg_label

p = argparse.ArgumentParser()
p.add_argument("input")
a = p.parse_args()
data = pathlib.Path(a.input).read_bytes()
if data.startswith(b"\x89PNG\r\n\x1a\n"):
    chunks = [c.decode("latin1") for c, _ in parse_png(data)]
    interesting = [c for c in chunks if c in {"tEXt","zTXt","iTXt","eXIf","caBX"}]
    result = {"format":"PNG","chunks":chunks,"provenance_or_metadata_candidates":interesting}
elif data.startswith(b"\xff\xd8"):
    labels = [jpeg_label(m, r) for m, r in parse_jpeg_segments(data)]
    interesting = [x for x in labels if x.startswith("APP1") or x.startswith("APP11") or x == "COM"]
    result = {"format":"JPEG","segments":labels,"provenance_or_metadata_candidates":interesting}
else:
    raise SystemExit("Unsupported image format: only PNG/JPEG are bundled")
print(json.dumps(result, indent=2))
