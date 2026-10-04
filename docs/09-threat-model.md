# IAM Threat Model

## Objective

This document identifies common identity-related threats and the controls used to reduce risk.

| Threat | Example | Primary Controls |
|---|---|---|
| Credential theft | Stolen password or access key | MFA, federation, temporary credentials, monitoring |
| Excess privilege | Developer has account-wide admin | Least privilege, permission sets, boundaries, review |
| Privilege escalation | User can create/attach stronger policies | Permissions boundaries, separation of duties, SCPs |
| Confused deputy | Third party misuses cross-account trust | External ID, narrow trust policy, monitoring |
| Dormant access | Old role/user still active | Access review, unused-access analysis, deprovisioning |
| Public/external exposure | Resource policy trusts unintended principal | Access Analyzer, resource-policy review |
| Security-log tampering | Attacker disables logging | SCP guardrails, separate log archive account |
| Secret in source code | Access key committed to Git | Roles, secret scanning, credential revocation process |

## Example Attack Path

```text
Developer credential compromised
        ↓
Attacker authenticates
        ↓
Overly broad IAM policy permits iam:PassRole
        ↓
Attacker launches workload with privileged role
        ↓
Privilege escalation
```

## Defensive Design

Reduce this risk by:

- Limiting `iam:PassRole` to approved roles.
- Restricting role creation and policy attachment.
- Using permissions boundaries for delegated role creation.
- Monitoring IAM modifications.
- Separating security administration from application development.
- Reviewing effective permissions rather than only attached policy names.
