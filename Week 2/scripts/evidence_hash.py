import hashlib
import os

folder = "../evidence"

os.makedirs(folder, exist_ok=True)

sample = os.path.join(folder, "memory_dump.bin")

with open(sample, "wb") as f:
    f.write(b"Sample forensic dump")

sha256 = hashlib.sha256()

with open(sample, "rb") as f:
    while chunk := f.read(4096):
        sha256.update(chunk)

hash_value = sha256.hexdigest()

report = f"""
Evidence Report

Item: Memory Dump
SHA256: {hash_value}
"""

with open("../reports/evidence_report.txt", "w") as f:
    f.write(report)

print(report)
