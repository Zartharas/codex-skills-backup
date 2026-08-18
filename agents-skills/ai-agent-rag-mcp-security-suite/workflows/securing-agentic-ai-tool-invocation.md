# Secure Agent Tool Invocation

Use to design or assess agents that can read/change external systems.

## Architecture questions

- Whose identity does the agent act as: user, shared service account, delegated/OAuth identity, workload identity?
- Where is authorization evaluated: before model call, at tool gateway, inside downstream service, or nowhere?
- Can untrusted content select a tool, widen scope, change recipient/resource, or bypass approval?
- Are read/write/delete/execute/send/purchase/admin capabilities separated?
- Are resource identifiers and tenant context independently bound to the authenticated user/task?
- Are credentials scoped, short-lived and audience-bound where practical?
- What actions require explicit user confirmation based on **actual resolved parameters**, not the model's summary?

## Control pattern

`model proposal → strict schema → semantic/policy validation → identity/authorization → approval when consequential → constrained tool execution → output validation → audit/recovery`

Schema validation alone is insufficient: `delete_account(account_id=other_user)` can be syntactically valid but unauthorized.

## Testing

Use synthetic adversarial instructions in messages, retrieved documents and tool output to try to redirect actions, recipients, paths or destinations. Validate in a sandbox/test account and stop before real external impact.

## Output

Trust-boundary diagram in prose, capability matrix if useful, validated privilege/approval failures, and minimal control changes.
