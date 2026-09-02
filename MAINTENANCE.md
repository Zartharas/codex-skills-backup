# Maintenance record

## 2026-09-02 — currentness and integrity pass

This record distinguishes user-managed instruction packages from runtime
plugins. It is not a claim that every vendor-managed cache directory has been
manually edited.

### Verified skill catalog

- `agents-skills/`: 25 user-managed skills passed the catalog structural audit.
- `agents-skills/durable-project-context`: the one Codex-home skill passed the
  same audit.
- `agents-skills/archify`: added from `tt-a1i/archify` at packaged version
  `2.17`; it produces locally validated standalone technical diagrams. Its
  optional fixed-manifest update reminder can be disabled with
  `ARCHIFY_UPDATE_CHECK_DISABLED=1`.
- The `agent-browser` instructions now require checking the installed version
  and fresh command guidance before relying on newly introduced commands.
- `skill-pack-quality-auditor` now records an explicit maintenance protocol:
  verify upstream sources, preserve provenance and licences, use supported
  plugin update paths, and seek approval before updates that add sign-in,
  egress, hooks, or permissions.

### Runtime and plugin inventory

| Component | Installed / action | Maintenance result |
| --- | --- | --- |
| Codex CLI | `0.147.0` → `0.152.1` | Updated through `codex update`; restart Codex to load the refreshed runtime. |
| Codex local memory | Enabled | Uses Codex's built-in local memory store and per-chat `/memories` controls; configuration is deliberately not copied into this repository. |
| Official bundled plugins | Codex-managed runtime packages | Marketplace upgrade reported no separately selected remote marketplace updates; do not edit cache directories. |
| Ponytail | `4.8.4` → `4.9.0` | Updated through its supported Codex marketplace (`DietrichGebert/ponytail`). |
| agent-browser CLI | `0.33.2` | Installed version verified; its local skill was updated with a fresh-capability check. |
| claude-mem | `13.13.1` installed | Upstream has a newer release, but its installer opens browser authentication and provisions a memory key. It was intentionally not run without a separate approval for that account/credential step. |
| MemPalace | locally cached | No supported marketplace update source was identified; left unchanged. |

### Repeatable validation

Run the dependency-free catalog audit after any package change:

```sh
python3 /Users/zarthras/.agents/skills/skill-pack-quality-auditor/scripts/audit_catalog.py /Users/zarthras/.agents/skills
python3 /Users/zarthras/.agents/skills/skill-pack-quality-auditor/scripts/audit_catalog.py /Users/zarthras/.codex/skills
```

This backup intentionally stores the user-managed skills and third-party
plugin snapshot, not mutable credentials, databases, or vendor-managed cache
trees.
