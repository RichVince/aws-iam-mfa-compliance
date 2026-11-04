
import subprocess
import time
from pathlib import Path

import boto3

print("Starting automated AWS IAM MFA scan...")

iam = boto3.client("iam")

# Request a fresh AWS credential report
for attempt in range(12):
    response = iam.generate_credential_report()
    state = response["State"]
    print(f"Report status: {state}")

    if state == "COMPLETE":
        break

    if state == "FAILED":
        raise RuntimeError("AWS report generation failed")

    time.sleep(5)
else:
    raise TimeoutError("AWS report was not ready in time")

# Retrieve and save the live AWS report
report = iam.get_credential_report()
Path("aws_credential_report_live.csv").write_bytes(
    report["Content"]
)

print("Live AWS credential report saved.")

# Run the existing compliance checker
subprocess.run(
    ["python3", "check_mfa.py"],
    cwd=Path(__file__).resolve().parent,
    check=True
)

print("Automated AWS MFA scan completed.")
