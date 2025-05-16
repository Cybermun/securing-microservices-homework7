# Summary Report

## Steps Taken
1. Cloned the vulnerable app and reviewed its architecture.
2. Identified issues: use of eval, hardcoded secrets, root container, unrestricted input.
3. Rewrote the app using ast.literal_eval and input validation.
4. Refactored Dockerfile with a non-root user, healthcheck, and minimal image.
5. Hardened docker-compose with read_only, mem_limit, pids_limit, and local port binding.
6. Created a STRIDE-based threat model and mapped MITRE/NIST controls.
7. Drafted an architecture diagram and Python hardening script.
8. Performed re-scans and verified remediation effectiveness.

## Vulnerabilities Found and Fixed
- Replaced eval with safe literal evaluation.
- Removed hardcoded secrets, used `.env` file.
- Switched container from root to non-root user.
- Limited container memory and process limits.

## Architecture Improvements
- Reduced attack surface and exposure.
- Applied defense-in-depth by hardening each layer.
- Improved compliance with container security best practices.

## Lessons Learned
- Secure coding, container hygiene, and runtime restrictions are equally important.
- STRIDE helps systematically identify potential flaws.
- Using Python for automation adds repeatability and CI/CD compatibility.
