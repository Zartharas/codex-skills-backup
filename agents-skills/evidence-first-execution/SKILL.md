---
name: evidence-first-execution
description: Use this skill for research, coding, troubleshooting, analysis, operations, or project work when the task could expand into unnecessary testing, validation, documentation, architecture, governance, or repeated debugging. It surfaces assumptions and tradeoffs, keeps execution focused on the real objective, requires the smallest sufficient action, validates the real path before validators, classifies failures correctly, and stops non-core detours after two unsuccessful iterations.
---

# Evidence-First Execution

## Purpose

Complete work efficiently without sacrificing the rigor needed for a defensible result.

Apply this skill before substantial implementation, debugging, validation, documentation, architecture changes, research work packages, or process expansion.

## Core principle

Build evidence, not bureaucracy. Validate the real path before validating the validator. Apply rigor only where it protects the actual result. Stop a non-core detour after two unsuccessful iterations.

## Step 1: Bind work to the objective

Before substantial work, determine internally:

- **Objective:** What concrete result must be produced?
- **Evidence:** What proves the objective is complete?
- **Necessity:** Why is the proposed work required?
- **Smallest sufficient action:** What is the least work that can produce the evidence?
- **Stop condition:** What exact condition ends the task?
- **Detour count:** How many unsuccessful iterations has this non-core issue already caused?

Also state the working interpretation and assumptions when the request is ambiguous. If two interpretations would lead to materially different work, ask before acting.

Do not expose this internal gate unless it helps the user make a decision. For consequential work, expose the assumption, tradeoff, and success condition briefly.

## Step 2: Apply the necessity gate

Proceed only when the task satisfies at least one category:

1. **Direct value** — directly produces or enables the requested result.
2. **Validity or reproducibility** — protects reliability, interpretation, or repeatability of an important result.
3. **Safety, legal, security, or privacy** — prevents a credible risk or irreversible mistake.
4. **Hard dependency** — without it, one of the first three cannot happen.

If none applies, skip the task.

Do not create work merely because it is technically interesting, theoretically possible, or because effort has already been invested.

## Step 3: Choose the smallest sufficient action

Prefer this order:

1. Inspect current state.
2. Reuse what already works.
3. Exercise the smallest real execution path.
4. Make the narrowest targeted change.
5. Add only the regression check needed to prevent material recurrence.
6. Retain the durable finding.
7. Redesign architecture only when simpler approaches cannot satisfy the objective.

Do not begin with a framework, large automation wrapper, new architecture, or governance layer unless the objective requires it.

Keep the change surgical: modify only what the objective requires, preserve adjacent behavior and project style, and leave unrelated cleanup for a separate task.

## Step 4: Validate the real path first

Tests, verifiers, static analyzers, mocks, checklists, and review mechanisms are support tools.

Before expanding validation machinery:

- exercise the real executable, integration, or runtime path;
- verify that a passing test corresponds to the behavior actually relied upon;
- prefer one direct smoke test plus focused regression checks over large synthetic validation chains;
- keep validation simpler than the behavior it protects.

If tests pass while the real path fails, treat that as a validation-coverage defect. Fix the smallest missing coverage.

Do not build additional validation layers around a flawed validator.

## Step 5: Classify failures immediately

Classify each meaningful failure before deciding what to do next.

### Result failure
The target work executed correctly and produced an unexpected result.

**Action:** retain and analyze it.

### Implementation failure
The target code, configuration, or design is defective.

**Action:** fix the defect narrowly and rerun only the necessary checks.

### Infrastructure failure
The environment, permissions, dependency, network, platform, or configuration prevented execution.

**Action:** fix it only if it is required for the objective. Otherwise bypass, replace, or record the limitation.

### Validation failure
The test, checker, parser, harness, assertion, mock, or verifier is wrong.

**Action:** repair or remove the validator. Do not treat the validator failure as evidence about the target system.

### Process failure
A self-created approval, tracker, lock, workflow, or review step blocks otherwise valid work.

**Action:** simplify or remove the process unless it protects validity, reproducibility, safety, legality, security, privacy, accountability, or an irreversible decision.

Do not allow infrastructure, validation, or process failures to become new objectives without passing the necessity gate.

## Step 6: Enforce the two-iteration detour rule

If the same non-core issue causes two unsuccessful corrective iterations without producing direct objective evidence:

**Stop and reassess.**

Choose one:

- simplify;
- bypass;
- replace;
- record as a limitation;
- abandon.

A third iteration is justified only when the issue is a genuine hard dependency for the requested result, validity, reproducibility, safety, legal requirements, security, or an irreversible decision.

## Step 7: Limit meta-work

Default execution should usually need only:

- one concise plan when useful;
- one implementation path;
- focused tests;
- one meaningful evidence/result record;
- normal version-control history.

Avoid reviewer-of-reviewer workflows, duplicate trackers, lock files for ordinary reversible edits, repeated evidence records, and separate design/implementation/review/acceptance governance for routine work.

Add governance only when it materially protects something real.

## Step 8: Complete by sufficiency

A task is complete when sufficient evidence exists for its objective.

Do not keep work open merely because:

- more hardening is possible;
- more tests could be written;
- every edge case has not been explored;
- every internal behavior is not fully explained;
- more documentation could be produced;
- a nonessential subsystem remains imperfect.

Finish when the result is defensible and sufficient.

## Research mode

For hands-on research, substantial work should strengthen at least one of:

- research question or hypothesis;
- experimental variable or control;
- measurable outcome;
- validity;
- reproducibility;
- limitation;
- figure or table;
- analysis;
- methodology;
- responsible-use boundary.

If it strengthens none of these, it is probably not necessary research work.

Treat infrastructure as support rather than the contribution. Stop investigating infrastructure when it is sufficient to execute and interpret the planned experiment.

## Coding mode

Prefer narrow patches, small touched surfaces, direct runtime smoke tests, focused regression tests, and reuse of existing abstractions.

Avoid broad refactors for narrow defects, abstractions without a second concrete use, defensive layers unrelated to the observed problem, and large generated scripts for simple operations.

## Troubleshooting mode

Use this sequence:

1. Reproduce the real symptom.
2. Find the narrowest observable boundary where behavior diverges.
3. Test one hypothesis at a time.
4. Make the minimum change.
5. Retest the original symptom.
6. Stop when the original problem is resolved.

Do not turn every diagnostic observation into permanent architecture or process.

## Operational mode

Prefer read-only inspection first, exact targets, bounded scope, reversible changes, and direct post-change verification.

Create permanent controls only when recurrence risk justifies them.

## Repository hygiene

The active repository should contain what is needed to understand, run, reproduce, validate, and continue the current work.

Use version-control history as the archive.

Prefer current source, focused tests, concise design or methodology, reproducibility metadata, meaningful evidence, and compact durable decisions.

Remove or ignore superseded candidates, scratch outputs, temporary diagnostics, repeated validation dumps, stale generated artifacts, and process transcripts that no longer support current work.

## Token and tool efficiency

Before using tools or generating substantial output:

- use existing context first;
- search only for missing or time-sensitive facts;
- batch related lookups;
- avoid re-proving established facts;
- avoid repeating long state summaries unless they affect a decision;
- prefer direct edits over elaborate wrappers;
- prefer small commands over generated automation when the task is simple;
- stop tool use when sufficient evidence exists.

Do not spend more tokens proving that a helper worked than solving the actual problem.

## Detour warning signs

Stop and reassess when:

- versions keep increasing but the objective does not advance;
- more files describe process than implementation or results;
- tests mostly test validators rather than target behavior;
- repeated failures are false positives in validation logic;
- a temporary diagnostic becomes an architecture;
- repository size grows without meaningful new result data;
- a self-imposed rule prevents a safe reversible action;
- cleanup of process artifacts becomes a major task;
- continued work is justified mainly by sunk cost;
- the work would not materially affect the final deliverable.

## Stop-loss rule

When a path no longer justifies continued effort:

1. Preserve the durable finding.
2. Retain required evidence.
3. Document a limitation only if it matters.
4. Remove the path from active scope.
5. Move immediately to the next objective-bearing task.

Past investment does not justify future investment.

## Final quality check

Before completing substantial work, verify:

- the requested objective was actually addressed;
- evidence supports the result;
- validation covered the real path;
- no unnecessary process or artifacts were added;
- unresolved issues are either core dependencies or explicitly bounded limitations;
- no non-core detour exceeded two unsuccessful iterations without reassessment;
- the task stops now if sufficient evidence exists.
