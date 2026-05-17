from datetime import datetime

incident = f"""
================ INCIDENT TICKET ================

Title: [Critical] Ransomware Detected on Server-X

Timestamp: {datetime.now()}

Indicators:
- File: crypto_locker.exe
- IP: 192.168.1.50
- MITRE: T1486

Priority: Critical

Actions:
1. Isolate endpoint
2. Collect evidence
3. Block attacker IP

=================================================
"""

with open("../reports/incident_ticket.txt", "w") as f:
    f.write(incident)

print(incident)
