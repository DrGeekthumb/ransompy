#!/usr/bin/env python3

# Based on original concept by Network Chuck


import os
from cryptography.fernet import fernet


files = []

for file in os.listdir():
	if file =="cryptor.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)
