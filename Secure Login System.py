# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:57:35 2026

@author: karti
"""

import hashlib

users = {}

# Register
username = input("Create Username: ")
password = input("Create Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

users[username] = hashed_password

print("\nRegistration Successful!")

# Login
print("\n------ Login ------")

login_user = input("Username: ")
login_pass = input("Password: ")

login_hash = hashlib.sha256(login_pass.encode()).hexdigest()

if login_user in users and users[login_user] == login_hash:
    print("Login Successful")
else:
    print("Invalid Username or Password")