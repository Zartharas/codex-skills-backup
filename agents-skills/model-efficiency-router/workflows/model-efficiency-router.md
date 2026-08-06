# model-efficiency-router

## When this workflow applies

Use before suggesting or starting a distinct task or phase when the user wants efficient model usage. Perform the bounded context preflight below, then recommend a host-available model and reasoning effort only when a change is useful. Do not claim to change the active model, raise native intelligence, monitor in the background, or rely on unavailable model names.

## Purpose

Recommend the least costly host-available reasoning/model configuration that is still appropriate for the **next distinct task**. This is advisory. A skill cannot increase native intelligence, change the active model, or monitor work in the background unless the host exposes and the user uses those controls.

## Bounded context preflight

Run this before proposing or beginning the next distinct task or phase. Reuse context already read; do not repeat scans.

1. Identify the next task, expected artifact, consequence of error, reversibility, ambiguity, and verification burden.
2. Classify the session:
   - **Chat-only:** no project/repository is in scope. Use the current conversation and the smallest available session-memory summary or registry entry. Do not scan unrelated files.
   - **Project:** a repository, workspace, or project files are in scope. Read applicable agent instructions first, then inspect only the most relevant status/index material such as `README`, `docs`, plan/spec, task notes, current diff, and matching memory entries. Prefer search and targeted sections; normally stop after the memory summary plus three relevant documents.
3. Treat memory as routing context, not proof. Verify drift-prone or consequential facts against current project files.
4. Stop scanning when the next task's complexity, risk, and validation needs are clear. If evidence remains thin, state the assumption instead of widening the scan automatically.

## Lowest-sufficient routing

Use only model names and effort controls actually exposed by the host. Otherwise describe a generic tier.

- **Default model, low effort:** straightforward lookup, formatting, small reversible edit, or known command with an obvious check.
- **Default model, medium effort:** ordinary implementation, bounded debugging, document synthesis, or several dependent steps.
- **Stronger available model, high effort:** ambiguous architecture, difficult root-cause analysis, security-sensitive or irreversible work, cross-domain synthesis, or many interacting constraints.
- **Strongest available model, maximum supported effort:** reserve for exceptionally consequential work where failure is costly and independent validation cannot adequately reduce uncertainty.

Prefer better tools, narrower context, and a concrete validation check before escalating the model. Never reduce safety checks, evidence requirements, or user approvals to save tokens.

Recommend stepping back down at the next boundary once the complex portion is complete.

## Output

Use one compact advance notice only when a change is useful:

`Model routing: <model/tier>, <effort> for <next task> — <one-sentence reason>. Switch back to <lower setting> after <boundary>.`

If the current setting is already sufficient, say nothing about routing and continue.

## Completion gate

- Recommendation is based on the next task, not the prestige of the project.
- The bounded preflight used available memory and, for project work, the smallest relevant documentation set.
- The named control actually exists or is clearly labeled as a generic category.
- Necessary validation is never removed to save tokens or cost.
- No background monitoring or automatic switching is implied.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: model-efficiency-router. Consolidated from the validated source; executable examples and platform-specific artifacts were intentionally omitted._
