# Browser, Client, CORS, CSRF, XSS, and WebSockets

## Client trust

Anything shipped to a browser or mobile bundle is observable and modifiable by the user. Never rely on client-only price, role, subscription, entitlement, feature flag, or authorization enforcement for a sensitive server action.

## XSS and unsafe rendering

Trace attacker-controlled content to HTML/DOM/script/URL/style sinks and account for framework auto-escaping, sanitizers, trusted-type systems, template contexts, Markdown renderers, and URL-scheme validation. `dangerouslySetInnerHTML` or equivalent is a candidate, not proof.

## CSRF

Assess only endpoints authenticated in a way that browsers attach automatically and that perform meaningful state changes. Account for SameSite cookie mode, CSRF tokens, origin checks, custom headers, CORS, and framework protections.

## CORS

CORS is a browser read-control mechanism, not server authentication. Wildcard origins are not automatically vulnerabilities. Report when a concrete origin/credentials configuration enables unauthorized browser access to sensitive responses or actions.

## WebSockets / realtime

Check authentication at connection and authorization for each sensitive subscription/action. Validate Origin where browser cross-site connection risk applies. Re-authorize mutable permissions where long-lived sessions can outlive privilege changes.

## Headers

Treat CSP, HSTS, frame controls, Referrer-Policy and similar headers as context-dependent controls. Missing defense-in-depth belongs under hardening unless it creates or materially enables an exploit path. Do not prescribe HSTS/includeSubDomains without understanding deployment ownership and HTTPS coverage.
