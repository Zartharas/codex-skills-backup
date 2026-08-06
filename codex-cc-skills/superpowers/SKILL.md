---
name: superpowers
description: "An agentic software-development methodology: brainstorm ideas into designs, write and execute plans, practice TDD and systematic debugging, run subagent-driven development, request/receive code review, dispatch parallel agents, use git worktrees, verify before completion, and finish development branches. Use when starting any build/feature/bugfix conversation so the right process skill is invoked first. Combines all 14 Superpowers skills into one bundle."
---

# Superpowers

A complete development methodology that runs on top of any coding agent. The entry skill `using-superpowers` establishes the core rule: **invoke relevant skills before any response or action, including clarifying questions.** Then process skills (brainstorming, systematic-debugging) set the approach before implementation skills carry it out.

## When to use (routing)

| Trigger | Skill |
|---|---|
| "Let's build X" / new feature / creative work | `brainstorming` first |
| "Fix this bug" / test failure / unexpected behavior | `systematic-debugging` first |
| Have a spec, need a plan | `writing-plans` |
| Executing a written plan | `executing-plans` (separate session) or `subagent-driven-development` (same session) |
| Implementing a feature/bugfix | `test-driven-development` |
| 2+ independent tasks, no shared state | `dispatching-parallel-agents` |
| Need isolation from current workspace | `using-git-worktrees` |
| Tasks complete, ready to verify | `requesting-code-review` |
| Received review feedback | `receiving-code-review` |
| About to claim work complete | `verification-before-completion` |
| Implementation done, integrating | `finishing-a-development-branch` |
| Creating/editing skills | `writing-skills` |

## Sub-skills

All 14 skills live under `skills/<name>/` with their full reference files and scripts preserved:

`brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `test-driven-development`, `systematic-debugging`, `dispatching-parallel-agents`, `using-git-worktrees`, `requesting-code-review`, `receiving-code-review`, `verification-before-completion`, `finishing-a-development-branch`, `writing-skills`, `using-superpowers`.

Always read `skills/using-superpowers/SKILL.md` first — it defines the invocation discipline all the others rely on.

## Platform adaptation

`using-superpowers` reads platform-specific references (e.g. `references/codex-tools.md` for Codex). If your harness isn't listed, the core methodology still applies; just adapt the tool names.

## Source

From `github.com/obra/superpowers` (v6.2.0 upstream; v5.1.3 in the official Codex marketplace). MIT. Full `.codex-plugin/plugin.json` is included at `.codex-plugin/plugin.json` for Codex install.
