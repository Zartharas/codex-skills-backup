# Payments, Mobile, and Platform-Specific Trust

## Payments

- Prices, discounts, product identifiers with security meaning, subscription entitlements, and refund/transfer amounts must be derived or validated server-side.
- Verify webhook/event authenticity with the provider's documented verification primitive and replay/idempotency controls where relevant.
- Treat asynchronous payment status as a state machine; test stale, duplicated, reordered, forged, and partially failed events.
- Do not reproduce provider secrets in findings.

A client-supplied amount is not automatically exploitable if the server maps it to an allowlisted price or provider-side product.

## Mobile

Assume application bundles and local storage can be inspected on a user-controlled device. Public client identifiers/configuration may legitimately be present; secret credentials must not depend on bundle confidentiality.

Review deep/universal links, exported components/intents, WebViews, certificate/network assumptions, secure-storage use, backend authorization, and local data sensitivity. Do not promise that device-side storage protects against a fully compromised device.
