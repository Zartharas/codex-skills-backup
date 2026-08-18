# GitHub Actions and CI/CD Security

Use for workflow triggers, token permissions, untrusted input, actions/dependencies, artifacts/caches and runner trust.

## High-value review

1. Map event triggers (`pull_request`, `pull_request_target`, issue/comment, workflow_run, reusable workflows, schedules, dispatch) to the trust level of code and metadata they execute.
2. Trace untrusted PR/issue/branch/commit data into shell, script, expression, path, artifact and deployment operations. Prefer environment/argv-safe passing over interpolating expressions into shell scripts.
3. Minimize `GITHUB_TOKEN` and OIDC permissions per job. Review environment approvals and cloud trust policies, not only YAML permissions.
4. Pin third-party actions to immutable verified commit SHAs when practical; record the human-readable release separately for maintainability. Verify action provenance before changing a pin.
5. Examine checkout of untrusted code combined with secrets/write tokens, especially `pull_request_target` and privileged follow-on workflows.
6. Review artifact/cache poisoning boundaries, reusable workflow inputs/secrets, self-hosted runner persistence, fork behavior and release/deploy jobs.
7. Do not run an untrusted workflow merely to prove it is dangerous.

## Output

For each issue: workflow + lines, attacker-controlled event/input, privilege/secrets available, executable sink, impact, minimal permission/trigger/pinning fix and safe regression check.
