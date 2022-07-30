#!/usr/bin/env python3

# Based on original concept by Network Chuck


import os
from cryptography.fernet import Fernet

# Iterate through each file except encrypter and decryption key

files = []

for file in os.listdir():
	if file =="cryptor.py" or file == "decrypt.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()



with open("decrypt.key", "rb") as key
	ransomkey = key.read()

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(ransomkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)
