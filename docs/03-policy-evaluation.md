# IAM Policy Evaluation

## Why Policy Evaluation Matters

Enterprise IAM troubleshooting requires understanding *effective permissions*, not merely reading one attached policy.

A request can be affected by several policy layers:

```text
Identity-based policy
Resource-based policy
Permissions boundary
Session policy
SCP / RCP
        |
        v
Effective authorization decision
```

## Baseline Rules

1. Requests are implicitly denied by default.
2. A valid Allow is required where the evaluation model requires it.
3. An applicable explicit Deny overrides an Allow.
4. Permissions boundaries define a maximum permission set for the IAM user or role to which they are attached.
5. SCPs and RCPs are organization-level guardrails; they do not independently grant task permissions.

## Example

Assume a developer role has this identity policy:

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::example-project-data/*"
}
```

If an applicable SCP explicitly denies `s3:GetObject`, the request is denied even though the role policy allows it.

## Troubleshooting Workflow

When access is unexpectedly denied:

1. Identify the principal ARN or role session.
2. Identify the exact API action.
3. Identify the exact resource ARN.
4. Review identity policies.
5. Review resource policies.
6. Review permissions boundary.
7. Review session policies.
8. Review applicable SCPs/RCPs.
9. Check policy conditions and request context.
10. Review CloudTrail for the event and error context.

## Enterprise Skill Demonstrated

The goal is to explain *why* AWS made an authorization decision rather than simply adding broader permissions until the error disappears.
