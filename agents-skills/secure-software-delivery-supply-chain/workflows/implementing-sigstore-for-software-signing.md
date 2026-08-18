# Sigstore / Cosign Signing and Verification

Use for Cosign, keyless signing, Fulcio, Rekor, attestations and Sigstore policy.

## Workflow

1. Verify the currently approved Cosign/Sigstore tooling and trust-root guidance from primary Sigstore documentation before giving version-specific commands.
2. Choose keyless or key-based signing based on CI identity, offline needs, policy and recovery requirements; do not default to whichever is easiest.
3. For keyless verification, constrain expected certificate identity and issuer; do not accept "any valid Sigstore identity" as the release policy.
4. Verify the artifact digest, identity/issuer and transparency/timestamp evidence required by current tooling and policy.
5. Protect OIDC workflows from untrusted trigger/context escalation and scope token permissions narrowly.
6. Treat attestations/SLSA-style provenance as claims whose predicate, builder identity and policy must be verified.
7. Roll out verification in audit/dry-run mode before making promotion/release enforcement blocking.

Transparency-log inclusion or a valid signature does not establish that an artifact is safe.
