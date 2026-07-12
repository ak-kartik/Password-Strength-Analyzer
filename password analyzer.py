# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:08:40 2026

@author: karti
"""

import re
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS password_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password TEXT
)
""")

conn.commit()

# ---------------- PASSWORD INPUT ----------------
password = input("Enter Password: ")

score = 0
suggestions = []

# ---------------- LENGTH CHECK ----------------
if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

# ---------------- UPPERCASE ----------------
if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")

# ---------------- LOWERCASE ----------------
if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")

# ---------------- NUMBER ----------------
if re.search(r"\d", password):
    score += 1
else:
    suggestions.append("Add at least one number.")

# ---------------- SPECIAL CHARACTER ----------------
if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;<>,.?/]", password):
    score += 1
else:
    suggestions.append("Add at least one special character.")

# ---------------- COMMON PASSWORD CHECK ----------------
common_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "abc123",
    "12345678"
]

if password.lower() in common_passwords:
    print("\n Very Weak Password")
    print("Reason: Common password.")
    exit()

# ---------------- DATABASE CHECK ----------------
cursor.execute("SELECT * FROM password_history WHERE password=?", (password,))
result = cursor.fetchone()

if result:
    print("\n Password has already been used before.")
    print("Please choose another password.")
    exit()

# ---------------- STRENGTH ----------------
if score <= 3:
    strength = "Weak"
elif score <= 5:
    strength = "Medium"
else:
    strength = "Strong"

# ---------------- OUTPUT ----------------
print("\n========== PASSWORD REPORT ==========")
print("Password Length :", len(password))
print("Score           :", score, "/6")
print("Strength        :", strength)

if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)
else:
    print("\nExcellent Password!")

# ---------------- SAVE PASSWORD ----------------
cursor.execute(
    "INSERT INTO password_history(password) VALUES(?)",
    (password,)
)
conn.commit()

print("\nPassword saved successfully.")

conn.close()



