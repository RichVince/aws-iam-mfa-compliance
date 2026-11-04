
import csv

total_users = 0
compliant_users = 0
exceptions = 0

with open("../aws_credential_report_live.csv", newline="") as file:
    reader = csv.DictReader(file)

    with open("mfa_findings_auto.txt", "w") as report:
        for user in reader:
            username = user["user"]
            mfa_status = user["mfa_active"].lower()
            password_enabled = user["password_enabled"].lower()

            total_users += 1

            if password_enabled == "false" or mfa_status == "true":
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
