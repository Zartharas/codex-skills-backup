#!/usr/bin/env python3
import argparse, json, pathlib
from common import read_text, write_text
from text_hygiene import clean, inspect

p = argparse.ArgumentParser()
p.add_argument("input")
p.add_argument("-o", "--output")
p.add_argument("--normalize-spaces", action="store_true")
a = p.parse_args()
out = a.output or str(pathlib.Path(a.input).with_suffix(pathlib.Path(a.input).suffix + ".cleaned"))
cleaned, removed = clean(read_text(a.input), a.normalize_spaces)
write_text(out, cleaned)
print(json.dumps({"input": a.input, "output": out, "removed_count": len(removed), "remaining_findings": inspect(cleaned)}, indent=2))
