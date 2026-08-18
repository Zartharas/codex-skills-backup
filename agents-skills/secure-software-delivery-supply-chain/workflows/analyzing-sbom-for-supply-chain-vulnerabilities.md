# SBOM, SCA, and VEX Analysis

Use for CycloneDX/SPDX or equivalent component inventories, dependency graphs, known-vulnerability correlation, VEX, licensing/provenance questions, and component prioritization.

## Workflow

1. Inspect the supplied SBOM format/schema/version and generation metadata. Do not force-convert it merely because another version is newer.
2. Identify components using strong coordinates when available: package URL, ecosystem/name/version, hashes, supplier, and dependency relationships. Flag ambiguous identity separately.
3. Use current vulnerability intelligence from authoritative/ecosystem sources. Prefer OSV/GHSA/vendor/distribution advisories and NVD/CVE information as appropriate; do not require an NVD API key as a prerequisite.
4. For each match, validate that the affected version/range and package identity actually correspond to the deployed component. Account for distro backports and vendor patches.
5. Consider reachability/exposure and VEX only as evidence. A `not_affected` VEX statement needs a reason and trustworthy issuer/context; a scanner match does not prove exploitability.
6. Prioritize by realistic exposure/impact, known exploitation when verified, reachable vulnerable functionality, privilege and network position, data sensitivity, fix availability and operational cost.
7. Check unsupported/EOL components, missing hashes/supplier/source provenance, dependency ambiguity and policy violations separately from exploitable CVEs.

## Output

Produce a concise component-risk table: component, version/identity confidence, advisory, affected status, reachability/exposure evidence, fix/mitigation, confidence. Keep licensing/provenance issues distinct from vulnerability findings.
