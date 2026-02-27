import itertools
import time

password = "ab1"
charset = "abc123"

start = time.time()
attempts = 0

for length in range(1, 5):
    for guess in itertools.product(charset, repeat=length):
        attempts += 1
        if "".join(guess) == password:
            end = time.time()
            print("[+] Password cracked:", password)
            print("[+] Attempts:", attempts)
            print("[+] Time taken:", round(end - start, 2), "seconds")
            exit()
