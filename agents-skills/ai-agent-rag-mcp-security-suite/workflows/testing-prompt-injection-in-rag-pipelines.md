# Authorized RAG Prompt-Injection and Retrieval-Poisoning Test

## Scope first

Define corpus/vector store, retriever/reranker, model, prompt assembly, tools/actions, test identities/tenants, data classification, environment and stop conditions. Use synthetic or explicitly approved documents.

## Test families

1. **Direct injection** — user text tries to override task/security constraints.
2. **Indirect injection** — retrieved content carries instructions targeting the model/agent.
3. **Retrieval poisoning** — malicious/incorrect content is indexed to influence future responses/actions.
4. **Instruction/data confusion** — document markup, metadata, citations or delimiters promote data into authority.
5. **Cross-tenant retrieval** — one tenant/user's content becomes retrievable by another.
6. **Unsafe downstream action** — retrieved content causes a tool call, URL fetch, message send, data query or other consequence.
7. **Output rendering/exfiltration** — model output leaks protected context or is interpreted unsafely downstream.

## Evidence bar

A prompt that changes prose is usually robustness. A security finding requires a protected asset or authority boundary: unauthorized retrieval, secret/context disclosure, cross-tenant access, dangerous tool use, policy bypass, or material integrity impact.

## Mitigation lens

Fix authorization and retrieval ACLs at the data/tool boundary; separate untrusted content from policy; minimize tool privileges; validate actions; require parameter-aware approval for consequential actions; sanitize/encode output for its sink; support poisoned-content removal and reindexing.

Optional red-team tools are allowed only when already available/authorized. Manual synthetic cases are sufficient when they directly test the boundary.
