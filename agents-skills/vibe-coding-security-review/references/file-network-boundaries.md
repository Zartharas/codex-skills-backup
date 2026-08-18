# File, Parser, and Outbound Network Boundaries

## File uploads

Check size/resource limits, storage path construction, authorization, content handling, active-content formats, server-side parsing, image/document conversion, archive extraction, decompression limits, filename trust, and serving headers/origin. Extension or MIME mismatch alone is not proof; determine what parser or browser actually consumes the bytes.

## Path traversal / archives

Normalize and confine writes/reads to an intended root and verify symlink behavior. For archives, validate each extracted path and resource limits; consider symlink/hardlink entries and decompression bombs when supported by the archive format/library.

## SSRF

A safe SSRF review must consider the complete connection path:

- attacker influence over URL/host/port/scheme
- DNS resolution and rebinding/TOCTOU
- IPv4/IPv6 and alternate address representations
- loopback, link-local, private, carrier-grade and cloud metadata ranges as applicable
- redirects, including revalidation at every hop
- proxy behavior and environment proxy variables
- credential forwarding and response exposure
- protocol restrictions and URL parser ambiguity

Do not recommend the flawed pattern "resolve once, then fetch the hostname and follow redirects" as a complete fix. Prefer an explicit destination allowlist or an egress component/library that validates the **actual connected destination** and every redirect.

## Dynamic proof

Use local/synthetic endpoints for validation. Do not probe cloud metadata or internal production services merely to demonstrate an SSRF candidate.
