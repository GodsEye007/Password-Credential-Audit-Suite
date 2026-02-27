# Password Cracking & Credential Attack Suite

## Project Overview

The Password Cracking & Credential Attack Suite is a cybersecurity project that demonstrates how weak passwords can be exploited and how security professionals analyze password security.

This toolkit simulates password auditing techniques used in cybersecurity assessments. It includes modules for dictionary generation, password hashing demonstration, brute-force simulation, and password strength analysis.

This project was developed and tested in a **Kali Linux lab environment** for educational and internship purposes.

---

## Features

* Dictionary generator for password testing
* Password hash generation demonstration
* Brute-force password cracking simulation
* Password strength analyzer using entropy calculation
* Security audit report generation

---

## Project Modules

### Dictionary Generator

Generates custom password wordlists based on common patterns such as names, years, and symbol combinations. This simulates how attackers build targeted password dictionaries.

### Hash Extraction Demo

Demonstrates how passwords are converted into hashes using hashing algorithms. Instead of storing plain text passwords, systems store **cryptographic hashes**.

### Brute Force Simulator

Simulates a brute-force attack by generating combinations of characters until the correct password is found. It shows the number of attempts and time taken to crack a password.

### Password Strength Analyzer

Analyzes password security based on length, character complexity, and entropy. Passwords are categorized as **Weak, Medium, or Strong**.

---

## Tools & Technologies

Operating System: Kali Linux
Programming Language: Python

Python Libraries Used:

* hashlib
* re
* itertools
* math
* time

---

## Project Structure

Password-Credential-Audit-Suite

dictionary_generator.py
hash_extractor_demo.py
brute_force_simulator.py
password_strength_analyzer.py
audit_report.txt
README.md

---

## How to Run the Project

Run the following scripts in Kali Linux terminal:

Dictionary Generator
python3 dictionary_generator.py

Hash Extraction Demo
python3 hash_extractor_demo.py

Brute Force Simulator
python3 brute_force_simulator.py

Password Strength Analyzer
python3 password_strength_analyzer.py

---

## Expected Output

The toolkit produces:

* Generated password wordlists
* Password hash outputs
* Brute-force simulation results
* Password strength evaluation
* Security audit findings

---

## Learning Outcomes

This project demonstrates:

* How password authentication works
* How password hashes are generated
* How attackers attempt to crack weak passwords
* How security professionals analyze password strength
* Red Team vs Blue Team password security concepts

---

## Ethical Disclaimer

This project is created strictly for **educational and cybersecurity research purposes**.
All demonstrations are performed in a **controlled lab environment using dummy data**.

This project must **not be used against real systems without proper authorization**.

---

## Author

Akash Kachare
Cybersecurity Intern
