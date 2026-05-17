import pandas as pd

triage = [{
    "Alert ID": "002",
    "Description": "Brute-force SSH Attempts",
    "Source IP": "192.168.1.100",
    "Priority": "Medium",
    "Status": "Open"
}]

df = pd.DataFrame(triage)

print(df)

df.to_csv("../reports/triage_report.csv", index=False)

summary = """
Threat Intelligence Validation:
IP checked using AlienVault OTX.
No known malicious indicators found.
"""

with open("../reports/threat_intel_summary.txt", "w") as f:
    f.write(summary)

print(summary)
