import pandas as pd

alerts = [
    {
        "Alert ID": "001",
        "Type": "Phishing",
        "Priority": "High",
        "MITRE Technique": "T1566",
        "Description": "Suspicious phishing email detected"
    },
    {
        "Alert ID": "002",
        "Type": "Brute-force SSH",
        "Priority": "Medium",
        "MITRE Technique": "T1110",
        "Description": "Multiple failed SSH login attempts"
    },
    {
        "Alert ID": "003",
        "Type": "Log4Shell Exploit",
        "Priority": "Critical",
        "MITRE Technique": "T1190",
        "Description": "Remote code execution attempt detected"
    }
]

df = pd.DataFrame(alerts)

print(df)

df.to_csv("../reports/mock_alerts.csv", index=False)

print("[+] Mock alerts generated")
