---
name: durable-project-context
description: "Establish or improve concise, repository-native project memory for coding agents. Use when a project lacks a clear durable context index, progress tracker, decision record, or bug-resolution record; do not use for ordinary feature implementation."
---

# Durable Project Context

Create a small, reviewable memory system that helps humans and coding agents
resume work without relying on an opaque local database or a long chat history.

## Outcome

Establish a concise context index that points to the authoritative project
records. It must not become a duplicate issue tracker, evidence archive, or
architecture specification.

## Before changing files

1. Read applicable `AGENTS.md` files and inspect the repository's existing
   README, development status/roadmap material, and issue/PR conventions.
2. Confirm whether the repository already has equivalent files. Reuse and link
   them instead of creating competing trackers.
3. Identify the smallest useful gap. Normally this is one short
   `docs/development/agent-context.md` file and, if needed, one concise link
   from `AGENTS.md`.
4. Keep secrets, tokens, personal data, customer data, raw datasets, evidence
   archives, local logs, and private legal material out of the repository.
5. Follow the repository's branching and review rules. Do not modify a protected
   or sealed baseline branch.

## Recommended durable records

Use existing equivalents where present. Create only records that are missing
and useful for the project.

| Need | Preferred authority |
|---|---|
| Agent operating rules and prohibited actions | `AGENTS.md` |
| Current phase, active work, and next decision | short project-status document plus the issue tracker |
| Phase order and exit conditions | roadmap or implementation plan |
| Verified defects, root causes, fixes, and regressions | resolution ledger or issue/PR links |
| Architecture and security decisions | ADRs and threat reviews |
| Completed implementation evidence | merged commits and pull requests |

## Context-index content

Keep the index short. Include only:

- product or repository maturity boundary and prohibitions that affect current
  work;
- current integration branch and a verified commit only when those are stable
  and useful;
- where to find active scope, blockers, reviews, architecture, threat reviews,
  and defect history;
- the repository-defined development and validation commands; and
- an update rule that prevents copied history from going stale.

Do not copy large specifications, enumerate every completed task, or promise
that an unmounted/internal boundary authorizes release, deployment, or external
behavior.

## Validation and handoff

1. Confirm every referenced repository path exists.
2. Run the lightest relevant documentation, policy, or architecture check.
3. Review the diff for duplicate trackers, accidental sensitive content, and
   misleading authority claims.
4. Report the files changed, validation performed, and any remaining project
   decision that needs user approval.

## Optional search tools

Search tools such as MemPalace or session memory may speed up discovery, but
they are not authoritative. If a search index is unavailable, use the
repository's versioned records and report the limitation. Do not rebuild or
re-index a healthy memory store merely because a sandbox blocks SQLite lock or
temporary-file writes.
