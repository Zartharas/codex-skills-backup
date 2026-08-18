# OPA / Rego / Gatekeeper Policy-as-Code

Use for authorization policy, admission control, policy bundles and CI/promotion gates.

## Workflow

1. Define the policy input contract, trust source, enforcement point and fail-open/fail-closed requirement.
2. Inspect existing Rego/Gatekeeper version/schema and current semantics before proposing syntax; do not assume an old policy example still compiles or behaves identically.
3. Keep sensitive input out of decision logs unless explicitly required and protected.
4. Write small test cases for allowed, denied, malformed, missing and boundary inputs before enabling enforcement.
5. Verify bundle/source authenticity and update behavior; a compromised policy distribution path can reverse the intended control.
6. Stage potentially disruptive deny policies in audit/warn mode first where the platform supports it.
7. Separate compliance labels from tested technical behavior; passing a policy does not prove overall compliance.
