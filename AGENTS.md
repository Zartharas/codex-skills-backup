# Global Codex Instructions — Installed Skills & Plugins

This machine has several Codex-extended packages installed. Use these
instructions to ensure they activate reliably. Description-matching alone is
not enforceable in Codex, so the explicit notes below take precedence.

## task-observer (skill)

At the start of any substantive, multi-step, tool-using task session, use the
`task-observer` skill. When it is active, read global task-observer memory
from `~/.codex-cc/memories/task-observer` before any project-local memory.
Run applicable AGENTS.md files reported by the skill helper
(`~/.codex-cc/skills/task-observer/scripts/task_observer.py`).
Do not let the observer modify files directly — review and approve its log
entries before applying skill updates.

## MemPalace (plugin + Python CLI)

MemPalace is installed as a Codex plugin at
`~/.codex/plugins/cache/mempalace-local/mempalace/3.7.0/` and the `mempalace`
CLI + MCP server are on PATH (`which mempalace-mcp`). Skills available:
`init`, `mine`, `search`, `status`, `help`, `mempalace`, `mempalace-recall`.
Before answering questions about past work, people, projects, or prior
decisions, run `mempalace search "<query>"` to check the palace. To seed a
project, run `mempalace init <path>` then `mempalace mine <path>`.

## claude-mem (plugin + Bun worker)

claude-mem is installed as a Codex plugin at
`~/.codex/plugins/cache/thedotmack/claude-mem/13.13.1/` with Bun on PATH.
It runs passively via SessionStart/UserPromptSubmit/Stop hooks. Skills
available: `mem-search`, `knowledge-agent`, `learn-codebase`, `how-it-works`,
`make-plan`, `do`, `babysit`, `cloud-sync`, `design-is`, `mode-creator`.
Use `mem-search` when the user asks "did we already solve this?" or references
prior sessions. Memory injection activates on the second session in a project.

## agent-browser (CLI + skill)

The `agent-browser` CLI is installed globally; the matching skill is in
`~/.agents/skills/agent-browser`. For any web-interaction task, prefer
`agent-browser open` -> `agent-browser snapshot -i` -> `click`/`fill` loop
over any built-in browser tooling. Load fresh instructions with
`agent-browser skills get core`.

## Overlap note

MemPalace, claude-mem, and task-observer all touch "memory". To avoid
redundant work: claude-mem captures raw session observations passively (no
action needed); MemPalace is the searchable palace (query it); task-observer
watches for skill-improvement signals specifically (review its logs). Do not
run all three's write paths against the same content in one turn.
