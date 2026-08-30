#!/usr/bin/env python3
"""Dependency-free checks for a directory of Agent Skills."""
from pathlib import Path
import re
import sys

def audit(root: Path) -> int:
    errors = []
    seen = {}
    files = sorted(root.glob("*/SKILL.md"))
    for path in files:
        text = path.read_text(errors="replace")
        if not text.startswith("---\n"):
            errors.append(f"{path}: missing YAML frontmatter")
        name = re.search(r"^name:\s*[\"']?([^\"'\n]+)", text, re.M)
        if not name:
            errors.append(f"{path}: missing name")
        else:
            value = name.group(1).strip()
            if value in seen:
                errors.append(f"duplicate name {value}: {seen[value]} and {path}")
            seen[value] = path
        if not re.search(r"^description:", text, re.M):
            errors.append(f"{path}: missing description")
        for ref in re.findall(r"\[[^]]+\]\(([^)#]+)", text):
            if not ref.startswith(("http://", "https://")) and not (path.parent / ref).exists():
                errors.append(f"{path}: missing reference {ref}")
    print(f"audited {len(files)} skills")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: audit_catalog.py SKILLS_DIRECTORY")
    raise SystemExit(audit(Path(sys.argv[1])))
