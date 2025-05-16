## Cybersecurity Architect’s Perspective: Securing the Application

# Summary Report

## Introduction
This report summarizes the process of securing a vulnerable multi-service Flask web application deployed in Docker. The original code exhibited several critical weaknesses—hardcoded secrets, unsafe use of eval(), command injection, and overly permissive container and network settings. Through code remediation, container hardening, threat modeling, and architecture redesign, we achieved a robust, defense-in-depth deployment.

### Environment Setup and Initial Analysis

**Application Review**: Examine `before/app.py`, `Dockerfile`, `docker-compose.yml`, and `Makefile` for vulnerabilities.
**Assets Identified**: Flask app, PostgreSQL database, Docker images, and host system.
**Security Goals**: Ensure confidentiality, integrity, and availability.
**Initial Scans**: Use `make check`, `make scan`, and `make host-security` to identify issues like hardcoded credentials, command injection, and outdated images.

## Steps Taken
1. Environment Setup:
- Installed WSL2 with Ubuntu 22.04 and Docker Desktop on Windows.
- Cloned the homework repository and launched the insecure app via make start.
- Executed initial scans (make check, make scan, make host-security) and recorded all findings.
2. Code Remediation:
- Moved PASSWORD out of code into an .env file (APP_PASSWORD).
- Replaced eval(expr) with ast.literal_eval(expr).
- Added strict regex validation for IP addresses on the /ping endpoint and switched to subprocess.check_output([...], shell=False).
- Bound Flask to 127.0.0.1 instead of 0.0.0.0.
3. Container Hardening:
- Converted the Dockerfile to a multi-stage build.
- Ran the container as a non-root user.
- Added a HEALTHCHECK directive.
4. Compose Configuration:
- Enforced read_only, no-new-privileges, mem_limit, and pids_limit.
- Exposed port only on localhost.
- Loaded secrets from .env.
5. Threat Modeling & Architecture:
- STRIDE analysis and MITRE/NIST mapping.
- Drafted architecture diagram.
6. Verification:
- Re-ran scans to confirm fixes.
- Functional testing of endpoints.

## Vulnerabilities Found and Fixed
- Hardcoded secret (High): Moved to .env and os.getenv
- eval() injection (Critical): Replaced with ast.literal_eval
- Command injection (High): Input validated; shell=False
- Unrestricted bind (High): Changed to 127.0.0.1
- Root container user (High): Added USER nobody
- No healthcheck (Medium): Added HEALTHCHECK
- Resource exhaustion (Medium): Set mem_limit and pids_limit


## Architecture Improvements
- Reduced attack surface and exposure.
- Applied defense-in-depth by hardening each layer.
- Improved compliance with container security best practices.

## Lessons Learned
- Defense in Depth: Security spans multiple layers.
- Principle of Least Privilege: Non-root and resource limits.
- Safe APIs: Avoid eval and shell=True.
- Secure coding, container hygiene, and runtime restrictions are equally important.
- STRIDE helps systematically identify potential flaws.
- Using Python for automation adds repeatability and CI/CD compatibility.


## Conclusion
This exercise demonstrated how layered security—combining safe coding practices, container hardening, orchestration constraints, and structured threat modeling—significantly reduces the attack surface of containerized microservices. The deliverables (secure code, CI/CD-ready pipeline, threat model, architecture diagram, auto-hardening script, and detailed report) provide a comprehensive blueprint for production-grade deployments.
