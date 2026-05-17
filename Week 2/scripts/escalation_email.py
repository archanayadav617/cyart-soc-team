email = """
Subject: Critical Alert Escalation

Dear Tier 2 Team,

Critical ransomware activity detected on Server-X.

Indicators:
- crypto_locker.exe
- IP: 192.168.1.50

Containment initiated.

Regards,
SOC Analyst
"""

with open("../docs/escalation_email.txt", "w") as f:
    f.write(email)

print(email)
