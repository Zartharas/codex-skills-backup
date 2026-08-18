# Application-Level LLM Integration

Use this reference for ordinary applications that call an LLM but are not primarily an agent/RAG/MCP security assessment. Route deep agent/RAG/MCP work to `ai-agent-rag-mcp-security-suite`.

## Boundaries

- Provider/API credentials remain server-side or in an appropriate secret store.
- Model output is untrusted content before HTML rendering, code execution, database queries, URLs, file paths, or other security-sensitive sinks.
- Tool/function arguments returned by a model must pass schema validation **and independent authorization**. Schema validity does not grant authority.
- System/user message separation can improve instruction hierarchy but does not solve prompt injection.
- Do not rely on "sanitize the prompt" as a complete prompt-injection control. Minimize privileges, separate untrusted data from authority, constrain tools, validate outputs/actions, and require human approval for consequential operations where appropriate.
- Treat cached model/retrieval output as tainted when its provenance or tenant boundary is not trustworthy.

## Reportability

A jailbreak or undesired text response is not automatically a security vulnerability. Establish a protected asset or policy boundary and a concrete confidentiality/integrity/availability/financial consequence.
