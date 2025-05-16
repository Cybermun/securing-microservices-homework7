# Threat Model (STRIDE + MITRE + NIST)

## STRIDE Analysis

| Threat       | Description                                      | Mitigation                            |
|--------------|--------------------------------------------------|----------------------------------------|
| Spoofing     | Fake IP input to ping                            | Input validation on IP addresses       |
| Tampering    | Command injection via eval or shell              | Replaced eval, restricted ping command |
| Repudiation  | No logging for actions                           | Add logging middleware                 |
| Information Disclosure | Error stack traces exposed            | Return user-friendly error messages    |
| Denial of Service | Large requests or CPU-intensive eval       | Add input size limits, use ast         |
| Elevation of Privilege | App runs as root                      | Run container as non-root user         |

## MITRE ATT&CK for Containers

- **T1609**: Container Administration Command
- **T1611**: Escape to Host
- **T1203**: Exploitation for Privilege Escalation

## Mapped NIST 800-53 Controls

| Vulnerability        | Control     | Description                      |
|----------------------|-------------|----------------------------------|
| Hardcoded secrets    | SC-12       | Cryptographic Key Management     |
| eval usage           | SA-11       | Developer Security Guidelines    |
| Container runs as root | AC-6      | Least Privilege                  |
