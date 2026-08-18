# Supported formats

## Deterministic bundled support

| Format | Inspect | Clean | Notes |
|---|---:|---:|---|
| UTF-8 text / Markdown / HTML source | Yes | Yes | Unicode controls and optional space normalization only |
| PNG | Yes | Yes | Removes tEXt/zTXt/iTXt, eXIf, and caBX chunks by default |
| JPEG | Yes | Yes | Removes EXIF/XMP APP1 and APP11 JUMBF-style segments by default |

## Not bundled in the portable core

PDF, DOCX, ODT, SVG binary provenance, pixel-domain watermark removal, and statistical
language-model watermark removal require specialized tooling or model-assisted rewrite.
The skill must report these as unsupported unless a verified external backend is available.
