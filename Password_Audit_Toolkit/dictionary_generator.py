names = ["akash", "admin", "user", "sahil"]
years = ["2000", "2001", "123"]
specials = ["@", "!", ""]

wordlist = []

for name in names:
    for year in years:
        for sp in specials:
            wordlist.append(name + year + sp)

with open("wordlist.txt", "w") as f:
    for word in wordlist:
        f.write(word + "\n")

print("[+] Wordlist generated successfully!")
print("[+] Total passwords:", len(wordlist))
