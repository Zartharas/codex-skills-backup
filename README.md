# codex-skills-backup

Private backup of this machine's Codex CLI + Codex Desktop skills, config, and
live plugin caches. Use this to restore the setup on a new device.

## What's here

| Path | Contents |
|---|---|
| `codex-cc-skills/` | Codex Desktop + CLI skills: `superpowers`, `memory-system`, `agent-workflows`, `task-observer` (each with `SKILL.md` + `skills/` sub-skills) |
| `agents-skills/` | Community suite under `~/.agents/skills/`: 22 validated skills (security assessment, academic, AI/RAG/MCP, application security, provenance hygiene, caveman, ponytail, agent-browser, etc.) |
| `config.toml` | `~/.codex-cc/config.toml` with **ephemeral temp-dir trust entries removed**. Provider uses a local-loop OmniRoute endpoint — no real secrets. |
| `AGENTS.md` | Global activation instructions read by Codex Desktop (`~/.codex-cc/AGENTS.md`). The CLI's `~/.codex/AGENTS.md` symlinks to this. |
| `codex-cli-AGENTS.md` | The Codex CLI copy of the same file. |
| `codex-plugins-cache/` | Live plugin caches for **MemPalace** (`mempalace-local/mempalace/3.7.0/`) and **claude-mem** (`thedotmack/claude-mem/13.13.1/`), including skills, hooks, MCP/server scripts. |

## Restore on a new device

### 1. Codex skills

```bash
# Desktop + CLI skills -> ~/.codex-cc/skills/
mkdir -p ~/.codex-cc/skills
cp -R codex-cc-skills/* ~/.codex-cc/skills/

# Community suite -> ~/.agents/skills/
mkdir -p ~/.agents/skills
cp -R agents-skills/* ~/.agents/skills/
```

### 2. Global AGENTS.md

```bash
cp AGENTS.md ~/.codex-cc/AGENTS.md
# Codex CLI reads ~/.codex/AGENTS.md; symlink to keep both in sync:
ln -sf ~/.codex-cc/AGENTS.md ~/.codex/AGENTS.md
```

### 3. Config

```bash
cp config.toml ~/.codex-cc/config.toml
```
Adjust the `model` / `model_provider.omniroute` `base_url` if the new device's
OmniRoute endpoint differs (default here: `http://127.0.0.1:20128/v1`, no auth).

### 4. Plugin caches (MemPalace + claude-mem)

```bash
mkdir -p ~/.codex/plugins/cache
cp -R codex-plugins-cache/mempalace-local ~/.codex/plugins/cache/
cp -R codex-plugins-cache/thedotmack ~/.codex/plugins/cache/
```

Then restore the **runtime dependencies** the plugin hooks call out to:

- **MemPalace CLI + MCP server** (provides `mempalace`, `mempalace-mcp` on PATH):
  ```bash
  uv tool install mempalace   # Python 3.9+; uv recommended
  ```
- **claude-mem worker** (Bun runtime, the hooks invoke `bun-runner.js`):
  ```bash
  curl -fsSL https://bun.sh/install | bash
  # restart your shell so ~/.bun/bin is on PATH
  ```
- **agent-browser CLI + Chrome** (the `agent-browser` skill drives this):
  ```bash
  npm i -g agent-browser && agent-browser install
  ```

### 5. Superpowers (optional, via Codex marketplace)

Superpowers is also available as an official Codex plugin. In Codex Desktop:
Plugins sidebar → search `superpowers` → `+`. In Codex CLI: `/plugins` →
search `superpowers` → Install. The marketplace version may lag the local copy
in this backup.

## Notes

- `config.toml` had per-session temp-dir trust entries (`/private/var/folders/.../codex-cc-executor.*`) stripped — those are ephemeral and not portable.
- The plugin caches contain minified JS with long identifiers; not real secrets.
- claude-mem's hooks do runtime path discovery, so the cache layout (`<source>/<name>/<version>/`) must be preserved exactly as staged here.
