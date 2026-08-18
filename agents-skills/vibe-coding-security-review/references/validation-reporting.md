# Validation, Severity, and Reporting

## Candidate lifecycle

`candidate → validate/falsify → attack path → severity → fix → targeted regression`

A static pattern or scanner hit is not a finding until enough of the source/control/sink/precondition/impact path is established.

## Confidence

- **High** — direct code/config evidence plus clear reachability; ideally a safe focused reproduction when material.
- **Medium** — strong source/control/sink evidence but one deployment/runtime assumption remains.
- **Low** — plausible pattern with meaningful proof gaps. Usually report as `needs-validation`, not as a confirmed vulnerability.

## Severity

Use realistic likelihood + concrete impact and existing controls. Prioritize boundary defeats: unauthenticated or cross-tenant data access, privilege escalation, arbitrary code/command execution, meaningful injection, credential compromise, financially meaningful business-logic bypass, or reliable service compromise.

Do not rate a defense-in-depth gap as Critical/High solely because the associated vulnerability class can be severe.

## Dynamic validation

Use the smallest safe method that can change the decision: existing test, unit/integration test, minimal harness, controlled local request, parser input, or sandbox PoC. Preserve proof artifacts outside the target tree where practical.

## Falsification

Actively look for counterevidence: upstream middleware actually mounted, authorization in a shared data layer, framework escaping, database RLS, gateway controls, fixed library behavior, unreachable code, trusted-only input, or deployment constraints.

## Report hygiene

- exact lines, but never literal secrets
- no sensational language
- separate findings from hardening
- state what was not tested
- do not imply compliance certification
- do not claim "vulnerability-free"
