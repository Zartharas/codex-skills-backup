# Mapping to the Current OWASP Top 10 for Agentic Applications

Use when the user asks for an OWASP Agentic crosswalk, coverage map or control review.

The OWASP GenAI Security Project released a Top 10 for Agentic Applications in late 2025 for autonomous/agentic risk. Exact category names, identifiers and companion guidance can evolve; verify the current primary OWASP publication before producing a formal mapping.

## Mapping method

For each current OWASP Agentic risk:

1. Quote or paraphrase the current official category name/intent from the primary source.
2. Identify the system component/trust boundary that corresponds to it.
3. Cite repository/configuration/runtime evidence for existing controls.
4. Record a concrete gap only when the architecture actually exposes that risk.
5. Distinguish `covered`, `partial`, `not-evidenced`, and `not-applicable`.
6. Do not equate "not evidenced in the supplied artifacts" with "control absent".

Use least agency, independent authorization, trusted identity, memory/data provenance, constrained inter-agent communication, bounded execution and recovery as recurring control lenses, but let the current official taxonomy control formal labels.

A crosswalk is not a certification and does not replace adversarial validation.
