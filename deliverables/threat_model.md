# Threat Model (STRIDE + MITRE + NIST)

## STRIDE Analysis


Conduct threat modeling using STRIDE and MITRE ATT&CK for Containers to identify risks and map controls.

#### STRIDE Analysis

| Threat Category       | Example                        | Impact                  | Mitigation            |
|-----------------------|--------------------------------|-------------------------|-----------------------|
| Spoofing              | No auth on `/calculate`        | Unauthorized access     | Add authentication    |
| Tampering             | Unsafe IP input to `ping`      | Command injection       | Input validation      |
| Repudiation           | No logging                     | Untraceable actions     | Implement logging     |
| Information Disclosure| Hardcoded passwords            | Credential exposure     | Use environment vars  |
| Denial of Service     | Unrestricted `ping` or `eval`  | Resource exhaustion     | Rate limiting         |
| Elevation of Privilege| Runs as root (potential)       | System compromise       | Non-root user         |

#### MITRE ATT&CK Mapping

| Tactic                | Technique ID | Technique Name                  | Relevance                  |
|-----------------------|--------------|---------------------------------|----------------------------|
| Initial Access        | T1190        | Exploit Public-Facing App       | Command injection in `/ping` |
| Execution             | T1059        | Command and Scripting Interpreter | Unsafe `eval()`          |
| Persistence           | T1525        | Implant Container Image         | No image validation       |
| Privilege Escalation  | T1611        | Escape to Host                  | Root user risks           |
| Defense Evasion       | T1211        | Exploitation for Defense Evasion | Poor isolation           |

#### Controls Mapping

| Issue                | Control                  | Framework Reference       |
|----------------------|--------------------------|---------------------------|
| Hardcoded secrets    | Use environment variables| NIST 800-53: SC-12, SC-28 |
| Root user            | Non-root user            | NIST 800-53: AC-6, CM-6   |
| Network exposure     | Restrict with networks   | NIST 800-53: SC-7         |
| Missing health check | Add `HEALTHCHECK`        | CIS Docker Benchmark      |
| Unvalidated inputs   | Strict validation        | OWASP Top 10: A1-Injection|

