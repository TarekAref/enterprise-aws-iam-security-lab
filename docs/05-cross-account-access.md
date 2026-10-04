# Cross-Account Access

## Business Scenario

A development team in **Account A** needs read-only access to a controlled S3 dataset in **Account B**. Creating duplicate long-term users in Account B is avoided.

## Design

```text
Account A principal
      |
      | sts:AssumeRole
      v
Account B: DataReadRole
      |
      | temporary role session
      v
Approved S3 bucket/prefix
```

Two permission relationships must be considered:

1. The caller needs permission to call `sts:AssumeRole` on the target role.
2. The target role trust policy must trust the approved principal/account.

The assumed role then needs task permissions for the destination resource.

## Security Controls

- Scope trusted principals as narrowly as practical.
- Avoid trusting an entire external account when a specific role can be trusted.
- Use conditions where appropriate.
- Use an external ID when granting role access to a third party to mitigate confused-deputy risk.
- Keep session duration appropriate to the task.
- Log role assumptions through CloudTrail.
- Review cross-account access with IAM Access Analyzer.

## Failure Modes

- Trust policy is too broad.
- Caller can assume a role with more privilege than required.
- Resource policy independently grants unintended access.
- Role chain creates unexpected operational limitations.
- External access is never reviewed after the project ends.
