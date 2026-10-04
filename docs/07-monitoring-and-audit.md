# Monitoring and Audit

## Objective

Access control is incomplete without visibility into how identities are used.

## AWS CloudTrail

CloudTrail provides an audit trail of AWS API activity. IAM investigations commonly ask:

- Which principal made the request?
- Which API action was called?
- From which source IP or service context?
- Which role was assumed?
- Was MFA context present where applicable?
- Which resource was targeted?
- Was the request allowed or denied?

## IAM Access Analyzer

Use IAM Access Analyzer to:

- Identify resources shared externally.
- Review internal access paths where supported.
- Identify unused access.
- Validate IAM policies.
- Generate/refine policies using observed access activity.

## Review Cadence Example

| Review | Purpose |
|---|---|
| Daily / alert-driven | Investigate anomalous privileged actions |
| Weekly | Review high-risk IAM changes and external sharing |
| Monthly | Review unused credentials and stale roles |
| Quarterly | Formal privileged-access and cross-account review |

The exact cadence should be risk-based rather than copied mechanically.

## High-Value IAM Events to Monitor

Examples include:

- New access keys
- Policy attachment or modification
- Trust-policy changes
- New privileged roles
- MFA changes
- Root-user activity
- `AssumeRole` events from unexpected principals
- CloudTrail configuration changes
- Access Analyzer findings
