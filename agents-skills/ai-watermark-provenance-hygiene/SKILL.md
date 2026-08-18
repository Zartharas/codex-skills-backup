---
name: ai-watermark-provenance-hygiene
description: >
  Inspect and clean user-owned or otherwise authorized text and files for invisible
  Unicode watermarks, privacy-sensitive metadata, EXIF/XMP, selected C2PA/JUMBF
  provenance containers, and related content-hygiene issues. Use for privacy cleanup,
  provenance research, metadata inspection, or preparing authorized content for sharing.
---

# AI Watermark & Provenance Hygiene

Use this skill only on content the user owns or is authorized to modify.

## Goals

1. Inspect before modifying.
2. Distinguish deterministic removals from best-effort or unsupported watermark classes.
3. Preserve content semantics and visual fidelity whenever possible.
4. Never claim that cleanup proves content is human-authored or guarantees detector evasion.

## Capability classes

### Portable deterministic core

Use the bundled Python scripts for:

- invisible Unicode and bidi/tag-character inspection and cleanup;
- optional normalization of exotic spacing;
- PNG metadata inspection/removal for text metadata, EXIF, and `caBX` provenance chunks;
- JPEG metadata inspection/removal for EXIF/XMP APP1 and JUMBF/C2PA-oriented APP11 segments;
- recursive directory inspection for supported text/image files.

### Best-effort / external-tool class

Statistical or token-sampling watermarks, embedded pixel-domain watermarks, PDF/DOCX/ODT
container provenance, and vendor-specific schemes may require specialized tooling or a
rewrite step. Report these as unsupported/best-effort unless the runtime exposes a verified
backend. Do not pretend they were removed.

## Standard workflow

1. Identify the file type and requested outcome.
2. Run inspection first.
3. Explain what was detected and which classes are deterministic vs uncertain.
4. Run the smallest sufficient cleanup operation.
5. Re-run inspection on the cleaned output.
6. Report exactly what changed, what remains, and any fidelity tradeoffs.

## Commands

### Text

```bash
python3 scripts/inspect_text.py input.txt
python3 scripts/clean_text.py input.txt -o cleaned.txt
```

Add `--normalize-spaces` only when the user explicitly wants exotic spaces normalized.

### PNG/JPEG

```bash
python3 scripts/inspect_image.py image.png
python3 scripts/clean_image.py image.png -o image.cleaned.png
```

For JPEG, default cleanup removes EXIF/XMP APP1 and APP11 JUMBF-style provenance segments.
Use `--strict-privacy` only when the user also wants comments and ICC/application metadata
removed, because that can affect rendering or downstream workflows.

### Directory audit

```bash
python3 scripts/audit_dir.py ./content
```

## Output rules

Always separate findings into:

- **Verified removed** — deterministic classes actually removed by the script.
- **Not detected** — classes checked but absent.
- **Unsupported / uncertain** — classes that require another backend or cannot be proven.

If a cleanup would materially alter content or color fidelity, explain the tradeoff before
using an aggressive option.

## Responsible-use boundary

Appropriate uses include privacy cleanup, engineering hygiene, provenance research, removal
of invisible control characters, and sanitizing authorized files for publication or sharing.
Do not use this skill to facilitate academic fraud, unlawful disclosure avoidance, or false
claims that AI-generated content is human-authored.
