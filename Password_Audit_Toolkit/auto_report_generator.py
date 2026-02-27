import math
import datetime

def entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(not c.isalnum() for c in password): charset += 32
    return round(len(password) * math.log2(charset), 2)

# READ ACTUAL TESTED PASSWORDS
with open("wordlist.txt", "r") as f:
    tested_passwords = [line.strip() for line in f.readlines()]

report = []
weak_passwords = []

report.append("PASSWORD SECURITY AUDIT REPORT\n")
report.append("Date: " + str(datetime.datetime.now()) + "\n")
report.append("=" * 45 + "\n\n")

for pwd in tested_passwords:
    ent = entropy(pwd)

    if ent < 40:
        strength = "WEAK"
        weak_passwords.append(pwd)
    elif ent < 60:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    report.append(f"Password Tested: {pwd}\n")
    report.append(f"Entropy Score: {ent}\n")
    report.append(f"Strength Level: {strength}\n")
    report.append("-" * 30 + "\n")

report.append("\nSUMMARY\n")
report.append(f"Total Passwords Tested: {len(tested_passwords)}\n")
report.append(f"Weak Passwords Found: {len(weak_passwords)}\n\n")

report.append("WEAK PASSWORD LIST\n")
for wp in weak_passwords:
    report.append("- " + wp + "\n")

report.append("\nSECURITY RECOMMENDATIONS\n")
report.append("- Minimum password length: 12 characters\n")
report.append("- Use upper, lower, digits, symbols\n")
report.append("- Avoid names, DOB, usernames\n")
report.append("- Implement account lockout policies\n")

with open("audit_report.txt", "w") as f:
    f.writelines(report)

print("[+] Audit report generated using ACTUAL tested passwords!")
