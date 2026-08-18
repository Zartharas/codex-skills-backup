# Secret Scanning and Exposure Review

Use for authorized current-tree or Git-history secret review and Gitleaks configuration/tuning.

## Rules

- Never reveal secret values in terminal excerpts, chat, reports, SARIF summaries or patches.
- Prefer the already-installed scanner. Do not install Gitleaks automatically.
- Verify current Gitleaks syntax before giving exact commands. Current releases use target modes such as `git`, `dir`, and `stdin`; avoid assuming legacy command names remain supported.
- Use full redaction in user-visible output when supported.

## Workflow

1. Define scope: working tree, tracked files, Git history, generated artifacts, build logs, or CI.
2. Verify scanner version/config/rules if Gitleaks is available. Otherwise perform a limited static review and state the reduced coverage.
3. Scan with redacted output. Exclude vendored/binary/generated paths only with a documented reason.
4. Triage each hit: plausible credential vs fixture/example/test vector; provider/type; whether it was committed/shared/built into a public artifact; whether access is still active if the user can verify safely.
5. For credible exposure: recommend revoke/rotate first, then remove source/history exposure as needed and review provider usage/audit logs.
6. Tune allowlists by stable path/rule/fingerprint or explicit safe fixture—not by broad regexes that hide future real leaks.
7. CI enforcement should fail safely without echoing the secret.

## Output

Location, credential class, confidence, exposure surface, rotation priority and remediation. Value always `[REDACTED]`.
