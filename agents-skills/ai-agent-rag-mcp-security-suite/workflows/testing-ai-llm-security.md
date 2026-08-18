# Broad Authorized AI/LLM Security Assessment

Use when the request spans multiple AI security surfaces rather than a single RAG/MCP/tool issue.

## Build a small system model

Identify model/provider, system/developer/user inputs, retrieval/memory, tools, output consumers, identities, secrets, tenant boundaries, external actions, moderation/policy controls and logging/feedback loops.

## Prioritize security surfaces

- sensitive data/context disclosure
- prompt/goal injection with authority impact
- insecure model-to-tool/action paths
- agent excessive privilege / confused deputy
- tenant/retrieval/memory isolation
- unsafe code/HTML/query/URL execution from model output
- denial-of-wallet/resource exhaustion when a realistic attacker can trigger material cost/availability impact
- model/provider credential exposure
- training/fine-tuning/data provenance only when actually part of the system

Use the current OWASP GenAI LLM and Agentic guidance as a mapping aid when requested; verify the current taxonomy instead of treating a year label in this package as permanently current.

## Testing

Prefer deterministic test cases that assert the protected boundary, not a collection of novelty jailbreak prompts. Optional frameworks such as garak, promptfoo or PyRIT can broaden coverage if already available, but their pass/fail output requires semantic triage.

## Output

Validated security findings, robustness observations, test limitations and mitigations tied to real control points.
