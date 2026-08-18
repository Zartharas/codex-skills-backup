# Access Control, Authentication, Sessions, and Tenancy

Use when identity or authorization boundaries are in scope.

## Highest-value questions

- Does every sensitive operation authenticate the caller at the server-side trust boundary?
- Does authorization check the **specific object/action/tenant**, not only "logged in" or role existence?
- Can an identifier from route/body/query select another user's or tenant's resource without ownership/tenant scope?
- Are authorization controls enforced at the closest durable boundary (service/data layer) rather than only UI or middleware?
- Are admin/service credentials, impersonation paths, support tooling, background jobs, webhooks, and async workers scoped correctly?
- Are session/token issuer, audience, signature, expiry, revocation/rotation expectations and cookie protections appropriate to the actual architecture?
- For OAuth/OIDC, verify state/nonce/PKCE/redirect handling as applicable using current provider guidance; do not assume one universal flow.

## Database policy systems

For Supabase RLS, Firebase rules, Convex, or similar systems, inspect the actual policy/rule and the client/server credential being used. "RLS enabled" is not proof of correct authorization; "service/admin key present" is not a vulnerability if it is confined to a trusted backend with appropriate controls.

## Tenancy

Trace tenant context through HTTP/RPC handlers, service methods, jobs, queues, caches, object storage, search indexes, exports, and admin paths. A missing tenant condition is reportable only when attacker-controlled selection reaches cross-tenant data/action without another effective boundary.

## Reporting

Prefer BOLA/IDOR or privilege-bypass findings with an explicit user A → resource/user/tenant B path. Do not report missing MFA as a vulnerability by itself unless the product/security requirement or risk context establishes it as a required control.
