---
name: memory-system
description: "Persistent cross-session memory and searchable recall for coding agents. Use when the user asks to remember past work, recall previous decisions or sessions, search prior conversations/projects, check 'did we already solve this?', mine a project into a knowledge base, or build a queryable memory palace. Combines MemPalace (searchable palace backed by ChromaDB) and claude-mem (passive session observation/compression). Requires the mempalace-mcp server and claude-mem Bun worker when used with the full plugin; the skill guidance itself is portable."
---

# Memory System

Combines two complementary memory packages so the agent has both **passive capture** and **active search**:

- **claude-mem** captures session observations passively (via hooks) and compresses them for later injection. No action needed during normal work.
- **MemPalace** is the searchable palace — query it before answering questions about past work, people, projects, or prior decisions.

## When to use

- "Did we already solve this?" / "How did we do X last time?" → `mem-search` / `mempalace search`
- "What did we decide about …" / "Who is … in this project" → invoke `mempalace-recall`
- Starting work in a repo with prior history → check the palace first, then seed if empty (`mempalace init` / `mempalace mine`)
- "Learn this codebase" → `learn-codebase` front-loads the whole repo into memory
- "Build a knowledge base about topic X" → `knowledge-agent`

## Sub-skills (loaded on demand from `skills/`)

| Skill | Purpose |
|---|---|
| `mem-search` | Search claude-mem's persistent cross-session memory |
| `mempalace` / `mempalace-recall` | Search the palace before answering about past work |
| `init` / `mine` / `search` / `status` / `help` | MemPalace CLI workflows |
| `learn-codebase` | Prime a codebase by reading every source file |
| `knowledge-agent` | Build focused "brains" from observation history |
| `how-it-works` | Explain how claude-mem captures/inserts memory |
| `cloud-sync` | Optional cmem.ai Pro cloud backup |

## Coordination rule

claude-mem writes observations passively; MemPalace is the query layer. Do not run both write paths against the same content in one turn — claude-mem captures, MemPalace retrieves. Read the individual `skills/<name>/SKILL.md` for full instructions before running CLI commands that require a backend (`mempalace-mcp`, Bun worker).

## Source

Installed on this machine from `github.com/MemPalace/mempalace` (v3.6.0 CLI, v3.7.0 plugin) and `github.com/thedotmack/claude-mem` (v13.13.1). This bundle preserves upstream attribution and licensing (MemPalace MIT; claude-mem Apache-2.0).
