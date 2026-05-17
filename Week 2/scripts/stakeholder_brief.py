brief = """
A ransomware-related incident was detected and contained successfully.

The affected system was isolated immediately.
No evidence of lateral movement identified.

Further forensic investigation is ongoing.
"""

with open("../reports/stakeholder_brief.txt", "w") as f:
    f.write(brief)

print(brief)
