# Artifact Code Signing and Verification

Use for generic PKI/platform/enterprise signing outside a Sigstore-specific workflow.

## Workflow

1. Define artifact type, threat model, publisher identity, verifier population and offline/online requirements.
2. Protect signing authority: hardware/service-backed keys where appropriate, least-privilege CI identity, separation from build workers, rotation/revocation and audit.
3. Bind the signature to immutable artifact bytes/digest and relevant metadata; preserve timestamp/identity evidence required by the ecosystem.
4. Verification must fail closed for the policy being enforced and validate certificate/key trust, identity, algorithm/policy, artifact digest and revocation/timestamp semantics as applicable.
5. Do not embed a private key or long-lived signing secret in repository/CI variables merely to simplify automation.
6. Test signing and verification on non-production artifacts before enforcing release blocking.

A valid signature proves only that a trusted signing identity signed specific bytes under the verification policy; it does not prove those bytes are non-malicious or vulnerability-free.
