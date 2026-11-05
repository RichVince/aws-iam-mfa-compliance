
# AWS IAM MFA Compliance Automation

## Project Overview
This project demonstrates automated identity and access management (IAM) compliance testing using AWS, Python, Boto3, and AWS CloudShell.

The solution evaluates MFA enrollment for AWS IAM users, identifies potential control exceptions, and generates evidence to support IT audits and GRC assessments.

## Objectives
- Automate AWS IAM credential report retrieval.
- Evaluate MFA compliance for IAM users.
- Identify and document control exceptions.
- Calculate compliance metrics.
- Validate detection logic using simulated test data.
- Produce reproducible audit evidence.

## Technologies
- AWS IAM
- AWS CloudShell
- Python 3
- Boto3
- CSV
- Linux Bash

## Control Framework Alignment
- NIST SP 800-53 IA-2: Identification and Authentication
- NIST CSF 2.0 PR.AA: Identity Management, Authentication, and Access Control
- CIS AWS Foundations Benchmark: MFA-related controls

## Project Structure
```text
aws-iam-mfa-compliance/
├── README.md
├── scripts/
│   ├── check_mfa.py
│   ├── check_mfa_test.py
│   └── run_aws_scan.py
├── docs/
│   └── IAM-MFA-001-audit-finding.md
└── evidence/
    └── mfa_findings_test_evidence.txt
```

## Testing Results

### Live AWS Assessment
- Accounts scanned: 2
- Compliant accounts: 2
- Exceptions: 0
- Compliance rate: 100%

### Simulated Exception Test
- Accounts scanned: 2
- Compliant accounts: 1
- Exceptions: 1
- Compliance rate: 50%

The simulated exception confirmed that the script detects an IAM user with a console password enabled but MFA disabled.

The simulated finding does not represent an actual misconfiguration in the live AWS environment.

## Audit Evidence
The project includes:
- Python compliance-checking scripts.
- Automated AWS credential report retrieval.
- A simulated MFA exception.
- A documented audit finding.
- Supporting test evidence.

## Security Considerations
The project uses read-only IAM reporting operations and does not disable MFA or modify user permissions.

IAM credential reports may contain sensitive account metadata and should not be published in public repositories.

## Future Improvements
- Export structured CSV or JSON findings.
- Add automated scheduling.
- Implement AWS CloudWatch monitoring.
- Integrate AWS Security Hub.
- Expand IAM compliance checks to access key rotation and unused credentials.

## Skills Demonstrated
AWS IAM | Python Automation | Boto3 | GRC Engineering | IAM Compliance | Control Testing | Audit Evidence | Risk Assessment

## Additional Control Validation

### Simulated MFA Exception — Updated Test
- Accounts scanned: 3
- Compliant accounts: 2
- MFA exceptions: 1
- Not applicable accounts: 0
- Compliance rate: 66.7%
- Result: PASS

The checker successfully detected a simulated IAM console
user with MFA disabled.

### Simulated Non-Console Account Test
- Accounts scanned: 3
- Compliant accounts: 2
- MFA exceptions: 0
- Not applicable accounts: 1
- Compliance rate: 100%
- Result: PASS

The checker correctly excluded an account without console
password access from the console MFA compliance denominator.

### Validation Scope
All simulated accounts were created in local CSV test data.
No AWS IAM accounts or MFA configurations were modified.

The live AWS assessment identified 2 compliant accounts
and 0 MFA exceptions.

The compliance percentage measures the implemented
console MFA control only. It does not represent overall
AWS account security or regulatory compliance.
