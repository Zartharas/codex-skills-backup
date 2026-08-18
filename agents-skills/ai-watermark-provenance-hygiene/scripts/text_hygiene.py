from __future__ import annotations

import unicodedata

ZERO_WIDTH = {
    0x200B: "ZERO WIDTH SPACE",
    0x200C: "ZERO WIDTH NON-JOINER",
    0x200D: "ZERO WIDTH JOINER",
    0x2060: "WORD JOINER",
    0xFEFF: "ZERO WIDTH NO-BREAK SPACE/BOM",
}
BIDI = set(range(0x202A, 0x202F)) | set(range(0x2066, 0x206A))
TAG_RANGE = range(0xE0000, 0xE0080)
SPACE_MAP = {
    "\u00a0": " ", "\u1680": " ", "\u2000": " ", "\u2001": " ", "\u2002": " ",
    "\u2003": " ", "\u2004": " ", "\u2005": " ", "\u2006": " ", "\u2007": " ",
    "\u2008": " ", "\u2009": " ", "\u200a": " ", "\u202f": " ", "\u205f": " ", "\u3000": " ",
}


def classify(ch: str):
    cp = ord(ch)
    if cp in ZERO_WIDTH:
        return "zero_width", ZERO_WIDTH[cp]
    if cp in BIDI:
        return "bidi_control", unicodedata.name(ch, f"U+{cp:04X}")
    if cp in TAG_RANGE:
        return "tag_character", unicodedata.name(ch, f"U+{cp:04X}")
    if ch in SPACE_MAP:
        return "exotic_space", unicodedata.name(ch, f"U+{cp:04X}")
    return None


def inspect(text: str):
    findings = []
    for i, ch in enumerate(text):
        item = classify(ch)
        if item:
            kind, name = item
            findings.append({"index": i, "codepoint": f"U+{ord(ch):04X}", "kind": kind, "name": name})
    return findings


def clean(text: str, normalize_spaces: bool = False):
    removed = []
    out = []
    for i, ch in enumerate(text):
        cp = ord(ch)
        if cp in ZERO_WIDTH or cp in BIDI or cp in TAG_RANGE:
            removed.append({"index": i, "codepoint": f"U+{cp:04X}", "kind": classify(ch)[0]})
            continue
        if normalize_spaces and ch in SPACE_MAP:
            removed.append({"index": i, "codepoint": f"U+{cp:04X}", "kind": "normalized_space"})
            ch = SPACE_MAP[ch]
        out.append(ch)
    return "".join(out), removed
