
import csv

total_users = 0
compliant_users = 0
exceptions = 0

from pathlib import Path
   
csv_path = Path(__file__).resolve().parent.parent / "aws_credential_report_live.csv"
with open(csv_path, newline="") as file:
    reader = csv.DictReader(file)

    with open("mfa_findings_auto.txt", "w") as report:
        for user in reader:
            username = user["user"]
            mfa_status = user["mfa_active"].lower()
            password_enabled = user["password_enabled"].lower()

            total_users += 1

            if username == "<root_account>":
                if mfa_status == "true":
                    compliant_users += 1
                    print(f"{username}: COMPLIANT")
                else:
                    exceptions += 1
                    finding = f"{username}: EXCEPTION - Root MFA not enabled"
                    print(finding)
                    report.write(finding + "\n")
            elif password_enabled == "false":
                print(f"{username}: NOT APPLICABLE - No console password")
            elif mfa_status == "true":
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

applicable_users = compliant_users + exceptions
not_applicable_users = total_users - applicable_users

print(f"Not applicable accounts: {not_applicable_users}")

if applicable_users > 0:
    compliance_rate = (compliant_users / applicable_users) * 100
    print(f"Compliance rate: {compliance_rate:.1f}%")

