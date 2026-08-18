# Input, Database, and Data-Flow Boundaries

Treat all external input as untrusted until the relevant boundary validates it. Trace values to sinks rather than searching for keywords only.

## Review surfaces

- SQL/NoSQL/ORM query construction, including raw fragments, dynamic identifiers, filters, sorting, operators, and bulk update/delete.
- OS commands, subprocess arguments, template engines, expression languages, interpreters, dynamic imports, eval-like APIs.
- Deserialization, YAML/XML/object decoding, archive processing, regular expressions, parsers, and user-controlled schema selection.
- Mass assignment / binding entire request objects into ORM or domain models.
- Path construction, object keys, filenames, cache keys, and tenant/resource selectors.
- Race/TOCTOU where security decisions and sensitive actions occur on mutable state.

## Validation bar

Establish whether the framework/API parameterizes or constrains the specific value. Do not call an ORM query injectable merely because request data reaches `where`; determine whether user-controlled **query structure/operators** are accepted, whether field allowlists exist, and what the ORM semantics are.

For command injection, distinguish shell interpretation from direct argv execution. For ReDoS, prove attacker control and an expression/input combination with meaningful resource impact before reporting.
