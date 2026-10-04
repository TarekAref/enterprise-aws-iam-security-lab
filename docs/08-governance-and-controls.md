# Enterprise Governance and Controls

## Control Layers

Enterprise IAM works best as layered control:

```text
Organization Guardrails
        ↓
Account / Role Boundaries
        ↓
Identity & Resource Policies
        ↓
Session Conditions
        ↓
Monitoring / Review
```

## AWS Organizations

Use multiple AWS accounts to isolate workloads and centralize governance as the environment grows. Organizational Units (OUs) group accounts by control needs and workload purpose.

## Service Control Policies

SCPs define permission guardrails for principals in member accounts. They do **not** grant permissions by themselves.

Example use cases:

- Prevent disabling centralized security logging.
- Restrict use of unapproved AWS Regions.
- Limit high-risk services in regulated environments.
- Protect organization-level security controls.

## Permissions Boundaries

A permissions boundary limits the maximum permissions that an IAM user or role can receive through identity-based policies. This is useful when delegating IAM administration to development teams while preventing privilege escalation beyond an approved ceiling.

## Policy Ownership

Every sensitive policy should have:

- Owner
- Business purpose
- Change history
- Review date
- Scope
- Risk classification
- Rollback plan

## Change Management

For high-impact IAM changes:

1. Propose the change in code.
2. Validate JSON and policy logic.
3. Peer review.
4. Test in non-production.
5. Deploy through controlled change process.
6. Verify effective permissions.
7. Capture evidence.
8. Monitor for unintended effects.
