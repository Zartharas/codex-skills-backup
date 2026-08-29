# model-efficiency-router

## When this workflow applies

Use before suggesting or starting a distinct task or phase when the user wants
efficient model usage. Perform the bounded context preflight below, then
recommend a host-available model and reasoning effort only when a change is
useful. Do not claim to change the active model, raise native intelligence,
monitor in the background, or rely on unavailable model names.

## Purpose

Recommend the least costly host-available reasoning/model configuration that is still appropriate for the **next distinct task**. This is advisory. A skill cannot increase native intelligence, change the active model, or monitor work in the background unless the host exposes and the user uses those controls.

## Bounded context preflight

Run this before proposing or beginning the next distinct task or phase. Reuse context already read; do not repeat scans.

1. Identify the next task, expected artifact, consequence of error,
   reversibility, ambiguity, verification burden, and the user's actual
   cost/latency preference.
2. Classify the session:
   - **Chat-only:** no project/repository is in scope. Use the current conversation and the smallest available session-memory summary or registry entry. Do not scan unrelated files.
   - **Project:** a repository, workspace, or project files are in scope. Read applicable agent instructions first, then inspect only the most relevant status/index material such as `README`, `docs`, plan/spec, task notes, current diff, and matching memory entries. Prefer search and targeted sections; normally stop after the memory summary plus three relevant documents.
3. Treat memory as routing context, not proof. Verify drift-prone or consequential facts against current project files.
4. Stop scanning when the next task's complexity, risk, and validation needs are clear. If evidence remains thin, state the assumption instead of widening the scan automatically.

## Minimize non-model token use first

Before selecting a stronger model or effort, reduce the work the model must do:

1. Reuse the current summary and previously verified facts; do not re-read a
   repository or long document merely for reassurance.
2. Ask for or state one narrow assumption when it resolves a branching scope.
3. Use targeted search and batched read-only commands instead of broad scans.
4. Prefer a direct real-path check over multiple synthetic validators.
5. Request compact output by default; expand only for artifacts, decisions, or
   evidence that the user needs to inspect.
6. Keep stable multi-turn work on the same capable model when the host retains
   useful context; switch only when the expected gain exceeds that cost.

## Select by capability tier, then map to the host

Classify the task before naming a model. Map the chosen tier only to models and
efforts actually exposed by the host.

| Tier | Typical work | Default effort | Escalate when |
|---|---|---|---|
| 0 — lightweight | lookup, classification, formatting, known command with an obvious check | none or low | tool use, ambiguity, or a multi-step decision is needed |
| 1 — routine | small reversible edit, focused triage, narrow test or review | low | the task has several dependent steps or the lower-effort attempt leaves material uncertainty |
| 2 — balanced | ordinary feature work, bounded debugging, document synthesis, review with several constraints | medium | direct validation shows the lower tier missed constraints or cannot form a safe plan |
| 3 — advanced | ambiguous architecture, security-sensitive design, difficult root cause, cross-domain synthesis | high | the outcome is high impact and bounded evaluation cannot reduce the remaining uncertainty |
| 4 — exceptional | hard quality-first evaluation, consequential irreversible decision, or unusually difficult long-horizon task | xhigh or max, if available | only after Tier 3 plus clear evaluation criteria show a real need |

Choose the lowest available model that meets the tier. For hosts that expose
cost-oriented, balanced, and flagship labels, use the cost-oriented model for
Tiers 0–1, the balanced model for Tier 2, and the flagship model for Tiers 3–4
unless direct evidence supports a different choice. Do not encode a provider's
current marketing names as permanent requirements.

## Daybreak and specialist cybersecurity models

Treat specialist cybersecurity models as a separate fit decision, not as a
stronger default tier.

1. Confirm the work is authorized defensive cybersecurity work and that the
   specialist model is provisioned on the host.
2. Use a safeguarded general-purpose defensive-cyber model, such as Daybreak
   Blue when it is available, for consequential defensive architecture, code
   review, threat modeling, or validation where cyber-specific safeguards or
   handling materially improve the outcome. Compare it with the ordinary
   flagship tier at the same effort; do not assume it saves tokens.
3. Use an advanced cyber-research model, such as Daybreak Red or GPT-5.6 Cyber
   when it is available, only for approved advanced vulnerability research,
   exploit validation, or security testing that requires its specialist
   capability. Its higher cost and separate provisioning mean it is not a
   replacement for routine secure coding, linting, dependency review, or
   ordinary threat-model documentation.
4. A specialist model does not broaden authorization. Keep the same scope,
   evidence, safety, approval, and disclosure requirements.

## Escalation and de-escalation

1. Start one effort level lower when the task is reversible and a focused check
   can detect failure.
2. Raise effort or model tier only after an observable trigger: unresolved
   constraints, failed direct validation, a security or irreversibility risk
   that cannot be bounded, or an evaluation that demonstrates a quality gain.
3. Do not use a higher tier merely because a project is important, a task is
   lengthy, or previous work used a stronger model.
4. After the hard boundary is designed or reviewed, return to the lowest tier
   that can implement and validate the next bounded slice.
5. Reserve any quality-first or pro-style mode for a measured marginal gain on
   difficult work; it increases latency and token use.

## Routing decision record

For each distinct task, record internally:

- selected tier and host mapping;
- selected effort and why lower effort is insufficient or sufficient;
- smallest evidence and tool plan;
- one escalation trigger and one de-escalation boundary; and
- residual uncertainty that the user, test, or review must resolve.

Do not over-document this record for simple Tier 0–1 work.

## Output

Use one compact advance notice only when a change is useful:

`Model routing: <host model or tier>, <effort> for <next task> — <one-sentence reason>. Switch back to <lower setting> after <boundary>.`

If the current setting is already sufficient, say nothing about routing and continue.

## Completion gate

- Recommendation is based on the next task, not the prestige of the project.
- The bounded preflight used available memory and, for project work, the smallest relevant documentation set.
- The named control actually exists or is clearly labeled as a generic category.
- Necessary validation is never removed to save tokens or cost.
- No background monitoring or automatic switching is implied.
- The route names a stronger model only when host availability and an observable
  escalation trigger support it.
- A Daybreak or other specialist-cyber recommendation confirms authorized scope
  and provisioned availability, and states why a general tier is insufficient.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: model-efficiency-router. Consolidated from the validated source; executable examples and platform-specific artifacts were intentionally omitted._
