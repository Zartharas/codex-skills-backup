# Provenance and watermark classes

1. **Invisible Unicode / formatting controls** — deterministic inspection and cleanup.
2. **Container metadata** — EXIF/XMP/text chunks and selected C2PA/JUMBF container segments.
3. **Statistical text watermarks** — not deterministically removable by the bundled core.
4. **Pixel-domain watermarks** — not handled by the bundled core.
5. **Cryptographic provenance** — metadata can sometimes be removed, but removal does not
   alter historical copies or prove anything about content origin.
