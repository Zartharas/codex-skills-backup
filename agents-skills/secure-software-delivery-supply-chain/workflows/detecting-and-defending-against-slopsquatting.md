# Dependency Provenance, Slopsquatting, and Package-Name Risk

Use when an AI/tool/user introduces a dependency name whose existence, identity or provenance is uncertain.

## Workflow

1. Never install the package as the first validation step.
2. Verify the exact name in the authoritative registry for the intended ecosystem. Watch for cross-registry confusion, scope/namespace mistakes, homoglyphs and near-name typos.
3. Verify the expected upstream project/publisher and that registry metadata points to the same project. Check package history, release cadence, repository linkage, maintainer changes and install/build scripts where accessible without executing them.
4. Determine whether the dependency was actually added to manifest/lockfile and whether installation scripts could execute in CI/developer environments.
5. Search the existing dependency graph for a well-established package that already provides the requested capability before adding anything new.
6. If provenance cannot be established, recommend not installing it and use an established alternative or first-party package.
7. For agent-driven development, require a human/controlled policy boundary before package installation or code execution; do not grant package-manager + arbitrary-shell authority from natural-language suggestions alone.

## Output

Package coordinate, registry existence, expected upstream match, provenance confidence, risky install behavior observed, decision: approve / investigate / reject. Avoid transient popularity statistics as security proof.
