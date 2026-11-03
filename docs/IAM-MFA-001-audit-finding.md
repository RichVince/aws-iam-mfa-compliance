
# IAM-MFA-001 — MFA Control Testing

Date: November 3, 2026
Environment: AWS IAM GRC Lab
Finding Type: Simulated Control Failure
Proposed Risk Rating: High
Status: Test Completed

## 1. Control Objective
Ensure AWS IAM users with console password access have MFA enabled to reduce unauthorized access risk.

## 2. Test Procedure
1. Obtained an AWS IAM credential report.
2. Created a separate test CSV.
3. Simulated an IAM user with MFA disabled.
4. Executed a Python compliance validation script.
5. Reviewed the generated exception report.
6. Restored the script to the live credential report.

## 3. Simulated Finding
Account: grc-lab-admin
Password Enabled: True
MFA Enabled: False

The test identified an IAM account with console password access but without MFA.

## 4. Risk
Compromised credentials could allow unauthorized access without an additional authentication factor.

## 5. Test Results
Accounts Tested: 2
Compliant Accounts: 1
Exceptions: 1
Simulated Compliance Rate: 50%

## 6. Recommended Remediation
Require MFA for IAM console users, investigate exceptions, and retest the control after remediation.

## 7. Supporting Evidence
- aws_credential_report_test.csv
- mfa_findings_test_evidence.txt
- check_mfa.py

## 8. Live Verification
Accounts Scanned: 2
Compliant Accounts: 2
Exceptions: 0
Compliance Rate: 100%

The live credential report passed the implemented MFA check. The simulated finding does not represent an actual AWS account misconfiguration.
