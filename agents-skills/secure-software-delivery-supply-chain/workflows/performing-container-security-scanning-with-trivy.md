# Container, Repository, Kubernetes, and IaC Review

Use for authorized Trivy-assisted or equivalent review of images, filesystems, repositories, Kubernetes manifests and infrastructure configuration.

## Workflow

1. Identify the actual target and deployment context: image digest/tag, Dockerfile, filesystem, repo, manifest set, Helm-rendered output, Terraform/IaC, or SBOM.
2. If Trivy is already installed, record its version and database/update state and select only relevant scanners. Do not auto-install or silently download optional components beyond normal authorized scanner operation.
3. Preserve the target digest/revision so findings are reproducible.
4. Vulnerability hits: validate affected package/version, distribution backports, fix availability and runtime relevance.
5. Misconfiguration hits: inspect the rendered/effective configuration and cloud/platform boundary; do not report defaults that are overridden elsewhere.
6. Secret hits: never print the secret. Treat them under the secret-exposure rules.
7. Container hardening: evaluate privilege/capabilities, user, mounts, host namespaces, writable paths, secrets, network exposure, base-image lifecycle and build context based on real deployment.

## Output

Separate confirmed vulnerabilities, configuration risks, secrets, license/policy observations and hardening notes. Scanner severity is input, not final severity.
