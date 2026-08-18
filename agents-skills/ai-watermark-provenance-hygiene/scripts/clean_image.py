#!/usr/bin/env python3
import argparse, json, pathlib
from image_meta import clean_png, clean_jpeg

p = argparse.ArgumentParser()
p.add_argument("input")
p.add_argument("-o", "--output")
p.add_argument("--strict-privacy", action="store_true")
a = p.parse_args()
src = pathlib.Path(a.input)
out = pathlib.Path(a.output) if a.output else src.with_name(src.stem + ".cleaned" + src.suffix)
data = src.read_bytes()
if data.startswith(b"\x89PNG\r\n\x1a\n"):
    cleaned, removed = clean_png(data)
    fmt = "PNG"
elif data.startswith(b"\xff\xd8"):
    cleaned, removed = clean_jpeg(data, a.strict_privacy)
    fmt = "JPEG"
else:
    raise SystemExit("Unsupported image format: only PNG/JPEG are bundled")
out.write_bytes(cleaned)
print(json.dumps({"format":fmt,"input":str(src),"output":str(out),"removed":removed}, indent=2))
