import re
import math

def entropy(password):
    charset = 0
    if re.search("[a-z]", password): charset += 26
    if re.search("[A-Z]", password): charset += 26
    if re.search("[0-9]", password): charset += 10
    if re.search("[^a-zA-Z0-9]", password): charset += 32
    return round(len(password) * math.log2(charset), 2)

pwd = input("Enter password: ")
score = entropy(pwd)

print("Entropy:", score)

if score < 40:
    print("Strength: Weak ❌")
elif score < 60:
    print("Strength: Medium ⚠️")
else:
    print("Strength: Strong ✅")
