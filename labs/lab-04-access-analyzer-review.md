# Lab 04 — IAM Access Analyzer Review

## Objective

Use IAM Access Analyzer as a continuous-review control rather than treating IAM policy creation as a one-time task.

## Review Areas

1. External access findings
2. Unused access findings
3. Policy validation
4. Potential policy refinement based on CloudTrail activity

## Procedure

- Create or identify an Access Analyzer appropriate for the lab scope.
- Review findings.
- Select one finding and document whether it is intended or unintended.
- If unintended, propose the minimum policy change that removes the exposure.
- Validate a customer-managed policy and record any warnings or suggestions.

## Evidence Template

```text
Finding:
Affected resource:
Principal / external entity:
Business justification:
Risk decision:
Remediation:
Validation result:
```

## Enterprise Interpretation

The important skill is not simply opening Access Analyzer. It is being able to classify a finding, explain the trust path, decide whether it is acceptable, and document remediation.
