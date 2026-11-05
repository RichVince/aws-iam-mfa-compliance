# HISTORICAL TEST ONLY — NOT THE CURRENT MFA CONTROL IMPLEMENTATION
# This early simulation checks mfa_active for every CSV record and does not
# exclude IAM users without console password access. Its compliance percentage
# must not be used as the current console MFA compliance metric.
# For current control testing, use scripts/check_mfa.py and scripts/run_aws_scan.py.

import csv

total_users = 0
compliant_users = 0
exceptions = 0

with open("aws_credential_report_test.csv", newline="") as file:
    reader = csv.DictReader(file)

    with open("mfa_findings_test.txt", "w") as report:
        for user in reader:
            username = user["user"]
            mfa_status = user["mfa_active"].lower()

            total_users += 1

            if mfa_status == "true":
                compliant_users += 1
                print(f"{username}: COMPLIANT")
            else:
                exceptions += 1
                finding = f"{username}: EXCEPTION - MFA not enabled"
                print(finding)
                report.write(finding + "\n")

print("\n===== AWS MFA COMPLIANCE SUMMARY =====")
print(f"Total accounts scanned: {total_users}")
print(f"Compliant accounts: {compliant_users}")
print(f"MFA exceptions: {exceptions}")

if total_users > 0:
    compliance_rate = (compliant_users / total_users) * 100
    print(f"Compliance rate: {compliance_rate:.1f}%")
