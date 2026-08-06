#!/usr/bin/env bash
# Re-stage Codex skills/config/plugin caches into this repo, commit changes, and push.
# Safe to run repeatedly. Exits 0 with "up to date" when nothing changed.
# Run from inside the cloned repo (the directory containing this script).
set -euo pipefail

if [ ! -d .git ]; then
  echo "Run this from the repo root (the dir containing update-backup.sh)." >&2
  exit 1
fi

BACKUP_ROOT="$(pwd -P)"

echo "Re-staging from live directories..."

# 1. Codex Desktop + CLI skills -> codex-cc-skills/
rm -rf codex-cc-skills
cp -R "$HOME/.codex-cc/skills" codex-cc-skills

# 2. Community suite -> agents-skills/
rm -rf agents-skills
cp -R "$HOME/.agents/skills" agents-skills

# 3. Global AGENTS.md (both surfaces; CLI copy is a symlink to the Desktop one)
cp "$HOME/.codex-cc/AGENTS.md" AGENTS.md
[ -f "$HOME/.codex/AGENTS.md" ] && cp "$HOME/.codex/AGENTS.md" codex-cli-AGENTS.md || true

# 4. Sanitized config.toml (strip ephemeral per-session temp-dir trust entries)
python3 - <<'PY'
import re, pathlib, shutil
src = pathlib.Path.home() / ".codex-cc" / "config.toml"
if src.exists():
    txt = src.read_text()
    txt = re.sub(
        r'\n\[projects\."/private/var/folders/[^"]*codex-(?:cc|nvidia)-executor[^"]*"\]\ntrust_level = "trusted"\n',
        '\n', txt)
    pathlib.Path("config.toml").write_text(txt)
PY

# 5. Live plugin caches (only the ones we installed)
rm -rf codex-plugins-cache
mkdir -p codex-plugins-cache
[ -d "$HOME/.codex/plugins/cache/mempalace-local" ] && cp -R "$HOME/.codex/plugins/cache/mempalace-local" codex-plugins-cache/
[ -d "$HOME/.codex/plugins/cache/thedotmack" ] && cp -R "$HOME/.codex/plugins/cache/thedotmack" codex-plugins-cache/

echo "Staged. Checking for changes..."
git add -A

if git diff --cached --quiet; then
  echo "Up to date. Nothing to commit."
  exit 0
fi

# Commit with a timestamp
TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
git commit -q -m "Update Codex skills/config/plugin backup ${TIMESTAMP}"
echo "Committed: $(git log -1 --oneline)"

# Push
if git rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1; then
  git push -q origin HEAD
  echo "Pushed to origin."
else
  git push -q -u origin HEAD
  echo "Pushed (set upstream)."
fi

echo "Done."
