# Lab 03 — Cross-Account Role Assumption

## Objective

Demonstrate temporary, read-only cross-account access without creating a duplicate IAM user in the destination account.

## Accounts

- Source account: `111122223333`
- Destination account: `444455556666`

Use placeholders or lab accounts only.

## Flow

```text
Source principal
     |
     | sts:AssumeRole
     v
Destination role
     |
     | temporary credentials
     v
Approved resource
```

## Trust Policy

Use [`../policies/trust/cross-account-role.json`](../policies/trust/cross-account-role.json) and narrow the principal before use.

## Validation

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::444455556666:role/ProjectDataReadRole \
  --role-session-name iam-portfolio-lab
```

Never commit returned credentials.

Verify the temporary session can perform only the intended actions.

## Enterprise Interpretation

Cross-account access should be explicit, temporary, auditable, and removable without distributing long-lived credentials in the destination account.
