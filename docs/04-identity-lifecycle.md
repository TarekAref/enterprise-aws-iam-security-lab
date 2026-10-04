# Identity Lifecycle Governance

## Objective

Enterprise IAM is a lifecycle process, not a one-time account-creation task.

```text
Join -> Provision -> Grant -> Review -> Change -> Revoke -> Audit
```

## Joiner

When a person joins:

- Identity is created in the authoritative directory.
- Group or role assignments are based on job function.
- MFA is enrolled.
- Access is approved by an accountable owner.
- Initial access is scoped to the minimum required privileges.

## Mover

When responsibilities change:

- Existing access is reviewed before adding new access.
- Incompatible privileges are removed.
- Elevated access is time-bounded when possible.
- Production access requires separate approval from routine development access.

## Leaver

When a user leaves:

- Disable the authoritative identity promptly.
- Revoke active sessions where supported.
- Deactivate or delete remaining access keys.
- Remove role/group assignments.
- Reassign owned resources if required.
- Review recent CloudTrail activity for unusual behavior.

## Periodic Access Review

Review:

- Dormant users and roles
- Unused permissions
- Old access keys
- External and cross-account trust
- Broad wildcard permissions
- Privileged roles
- Exceptions and break-glass access

## Evidence

An enterprise-ready IAM process should produce evidence of:

- Who approved access
- What permission was granted
- Why it was required
- When it was granted
- When it expires or is reviewed
- When it was revoked
