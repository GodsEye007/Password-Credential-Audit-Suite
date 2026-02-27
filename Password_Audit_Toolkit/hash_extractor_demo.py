import hashlib

passwords = ["akash2000", "admin123"]

print("Username : Hash")

for pwd in passwords:
    hash_val = hashlib.sha256(pwd.encode()).hexdigest()
    print("user :", hash_val)
