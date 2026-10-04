# Credential and MFA Strategy

## Human Access

Preferred enterprise model:

```text
Enterprise identity -> Federation / IAM Identity Center -> Role -> Temporary credentials
```

MFA should protect human sign-in, especially privileged access.

## Workload Access

Preferred workload model:

```text
AWS workload -> IAM role -> Temporary credentials
```

Avoid hard-coding access keys in source code, container images, scripts, or configuration files.

## Long-Term Access Keys

Some use cases may still require IAM-user access keys, but they should be treated as exceptions. Controls should include:

- Documented business justification
- Least-privilege permissions
- Secure storage
- Usage monitoring
- Deactivation when unused
- Rotation based on organization policy and risk
- Immediate revocation on suspected exposure

## MFA

MFA combines more than one authentication factor. For AWS workforce access, it reduces the impact of password compromise.

## Root User

Root credentials require exceptional protection and should not be used for routine administration. In multi-account Organizations environments, use the available root-access management capabilities and follow AWS root-user guidance.

## Break-Glass Access

An emergency-access process should be:

- Rarely used
- Strongly authenticated
- Closely monitored
- Documented
- Tested periodically
- Reviewed after every use
