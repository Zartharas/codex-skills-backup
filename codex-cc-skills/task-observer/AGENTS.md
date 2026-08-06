# AGENTS.md

These instructions apply when Codex works in this repository.

- Treat `SKILL.md` as the installable Codex skill source.
- Keep the skill Codex-native. Do not reintroduce Claude/Cowork-only runtime
  assumptions such as `CLAUDE.md`, `.claude/skills`, `present_files`, or Claude
  scheduled-task tools unless they are clearly marked as external compatibility
  notes outside the skill body.
- Preserve upstream attribution to Eoghan Henn / rebelytics.com and the CC BY
  4.0 license.
- Keep `SKILL.md` concise enough for runtime loading. Put deterministic
  filesystem behavior in `scripts/task_observer.py`.
- When validating changes, run:

  ```bash
  if [ -f "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" ]; then
    python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
  else
    echo "quick_validate.py not found; skip Codex skill structural validation"
  fi
  python3 scripts/task_observer.py init
  python3 scripts/task_observer.py context --cwd "$PWD"
  ```

  Run these commands from the repository root.

- The Codex adaptation must always preserve this rule: global observer memory in
  `${CODEX_HOME:-$HOME/.codex}/memories/task-observer` is read before any
  project-local memory, even when a project has its own memory files.
