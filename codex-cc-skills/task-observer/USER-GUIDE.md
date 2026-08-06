# Codex User Guide: task-observer

This guide covers the Codex adaptation of "One Skill to Rule Them All".

## Purpose

`task-observer` helps Codex remember how skills and workflows should improve.
It is useful when you do repeated technical work, maintain several skills, or
want corrections from real sessions to become durable guidance.

The observer should stay quiet during normal work. It logs only reusable,
sanitized observations and surfaces them when you ask or when skill maintenance
is the task.

## Global memory

The global memory directory is:

```text
${CODEX_HOME:-$HOME/.codex}/memories/task-observer
```

Install the skill under `${CODEX_HOME:-$HOME/.codex}/skills/task-observer`.
The helper examples assume that exact directory name.

It contains:

- `log.md` for open/actioned/declined observations
- `cross-cutting-principles.md` for rules that apply across many skills
- `last-review-date.txt` for review cadence tracking
- `skill-updates/` for staged skill updates

Codex must read this global directory before project-local observer memory, even
when launched inside a repository that has its own memories.

## AGENTS.md

Use `AGENTS.md` or `agents.md` for durable Codex activation instructions. A
practical global instruction is:

```markdown
At the start of substantive task-oriented Codex sessions, use $task-observer.
When $task-observer is active, run its context helper and read the reported
AGENTS.md files plus global observer memory before project-local memory.
```

The helper command is:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/task-observer/scripts/task_observer.py" context --cwd "$PWD"
```

## Normal workflow

1. Work normally.
2. Let the observer silently capture generalizable improvements.
3. Near the end of a session, ask: `Any observations logged?`
4. Review open observations.
5. Ask Codex to stage skill updates when you want to apply them.
6. Install staged skill updates only after review.

## Safety rules

Do not put sensitive details into observation logs. Generalize:

- secrets and tokens
- patient, customer, payment, or health data
- private URLs or credentials
- proprietary snippets
- client names unless explicitly internal and necessary

If an observation needs sensitive details to be useful, skip it.

## Helper examples

Initialize memory:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/task-observer/scripts/task_observer.py" init
```

Show required context files:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/task-observer/scripts/task_observer.py" context --cwd "$PWD"
```

Append a sanitized observation:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/task-observer/scripts/task_observer.py" log \
  --title "Skill needs a validation step" \
  --skill "example-skill" \
  --kind "improvement" \
  --scope "internal" \
  --issue "A documented rule was missed during output." \
  --suggestion "Add a preflight checklist before final response." \
  --principle "Skills with strict output rules need explicit self-checks." \
  --evidence "Sanitized post-task feedback."
```

Show status counts:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/task-observer/scripts/task_observer.py" status
```
