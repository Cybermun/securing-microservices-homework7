# ✅ Submission Checklist – SEAS-8405 Homework 7
**Assignment:** Securing Containerized Microservices  
**Student Name:** Ahmed Humadi  
**GitHub Repo:** [https://github.com/Cybermun/securing-microservices-homework7.git]  
**WSL + Docker Desktop Environment**

## 🗂️ Project Structure
```
homework7/digram.png
├── before/
├── secure_app/
├── deliverables/
│   ├── threat_model.md
│   ├── summary_report.md
│   ├── digram.png
├── docker_security_fixes.py
├── docker-compose.yml
├── Dockerfile
├── .env
├── remediation_walkthrough.mp4
└── README.md
```

## 📋 Checklist of Deliverables

| Item | Description | Status |
|------|-------------|--------|
| ✅ Hardened Flask App | Refactored `app.py` to eliminate insecure code (`eval`, hardcoded secrets, etc.) | ✅ |
| ✅ Docker Hardening | Secure `Dockerfile` using slim base, non-root user, HEALTHCHECK | ✅ |
| ✅ Compose Hardening | `docker-compose.yml` includes `read_only`, `mem_limit`, `security_opt`, port restrictions | ✅ |
| ✅ Threat Model | `deliverables/threat_model.md` includes STRIDE, MITRE ATT&CK, and NIST 800-53 | ✅ |
| ✅ digram | Flow chart | ✅ |
| ✅ Security Diagram | `deliverables/architecture_diagram.png` showing hardened infrastructure | ✅ |
| ✅ Auto-Hardening Script | `docker_security_fixes.py` updates `daemon.json`, Dockerfile, and Compose | ✅ |
| ✅ Screen Recording | `remediation_walkthrough.mp4` includes full narration and steps | ✅ |
| ✅ Summary Report | `deliverables/summary_report.md` describes steps, fixes, and reflections | ✅ |
| ✅ GitHub Repository | Public repo with all code, reports, and assets properly named | ✅ |

## 🛠️ Notes
- Ensure `.env` does **not** include real secrets (use placeholders like `SECRET=changeme123`).
- CI/CD compatibility: verify Docker and Compose files match expected naming conventions (`before`, `secure_app`, etc.).
- Video should show both **before** and **after** states with clear narration or captions.

