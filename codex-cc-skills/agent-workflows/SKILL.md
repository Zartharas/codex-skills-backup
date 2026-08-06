---
name: agent-workflows
description: "Planning, execution, and project-monitoring workflows for coding agents. Use when the user asks to make a phased implementation plan and then execute it, babysit/monitor a PR or review cycle, generate standups/weekly digests/timeline reports, design audits, explore a codebase or pathfind, or create custom observation modes. Combines claude-mem's planning and orchestration skills (make-plan, do, babysit, etc.) into one portable bundle. Skill guidance is portable; features requiring the claude-mem Bun worker may be limited without it."
---

# Agent Workflows

Planning + execution + monitoring toolkit consolidated from claude-mem's workflow skills. These compose: `make-plan` produces a phased plan, `do` executes it with subagents, `babysit` keeps watch on a PR until it's clean.

## Sub-skills (loaded on demand from `skills/`)

| Skill | When to use |
|---|---|
| `make-plan` | Create a phased implementation plan before executing (pairs with `do`) |
| `do` | Execute a phased plan as an orchestrator deploying subagents |
| `babysit` | Monitor a PR/review cycle until mergeable; don't stop after one pass |
| `make-plan`→`do` | Two-step plan-then-execute flow |
| `design-is` | Audit a design against Dieter Rams' ten principles → handoff to make-plan |
| `mode-creator` | Create/install custom claude-mem observation modes (needs worker) |
| `smart-explore` | Intelligent codebase exploration with memory-backed suggestions |
| `pathfinder` | Find and validate implementation paths through unfamiliar code |
| `standup` / `weekly-digests` / `timeline-report` | Generate progress summaries from observation history |
| `oh-my-issues` | Triage and track open issues with memory context |
| `what-the` / `wowerpoint` | Explain/visualize recent work or generate presentation decks |
| `version-bump` | Managed version bumping with changelog updates |

## Coordination

`make-plan` and `do` are the core flow: plan first, then execute. `babysit` runs after a PR is up. The reporting skills (`standup`, `weekly-digests`, `timeline-report`) depend on observation history that claude-mem's worker captures; without the worker installed they fall back to manual input. Read `skills/<name>/SKILL.md` for full instructions.

## Source

Consolidated from `github.com/thedotmack/claude-mem` (v13.13.1), Apache-2.0. Skill guidance preserved; plugin-runtime hooks/scripts are not bundled here (install the plugin for live worker features).
