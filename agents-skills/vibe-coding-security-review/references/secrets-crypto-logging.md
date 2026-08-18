# Secrets, Passwords, Cryptography, and Logging

## Secrets

Detect exposure without echoing values. Distinguish real credentials from examples/fixtures/placeholders. Review current files, generated bundles, configuration, logs, and—when routed to the supply-chain specialist—Git history.

If credible exposure occurred, remediation normally includes revocation/rotation and usage-log review; removing the literal from a file does not invalidate an already exposed credential.

## Password storage

Do not turn one fixed bcrypt work factor into a universal pass/fail rule. Prefer the current OWASP/vendor guidance and the application's platform constraints. For new systems, memory-hard password hashing such as Argon2id is commonly preferred; legacy bcrypt/scrypt/PBKDF configurations require parameter and deployment-context assessment. General-purpose fast hashes are unsuitable for password storage.

## Encryption

Assess the construction, not algorithm names in isolation: authenticated encryption/integrity, key source and separation, nonce/IV uniqueness requirements, randomness, rotation/versioning, associated data, error handling, and protocol/library semantics. Do not label every AES-CBC occurrence vulnerable without proving the absence of authentication or another relevant defect.

## Tokens/signatures

Use constant-time primitives where secret comparison timing is security-relevant. Validate signatures using the protocol/library's supported verifier rather than hand-rolled comparisons.

## Logging

Sensitive values should not enter logs, traces, analytics, crash reports, or client errors. Preserve enough audit information for incident investigation without storing secrets or unnecessary personal data.
