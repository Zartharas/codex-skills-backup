#!/usr/bin/env python3
import argparse, json
from common import read_text
from text_hygiene import inspect

p = argparse.ArgumentParser()
p.add_argument("input")
a = p.parse_args()
findings = inspect(read_text(a.input))
print(json.dumps({"file": a.input, "finding_count": len(findings), "findings": findings}, indent=2, ensure_ascii=False))
