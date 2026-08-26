# Basic Encryption Program

import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# Encrypt
ptext = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in ptext:
    index = chars.index(letter)
    cipher_text += key[index]

print("Encrypted:", cipher_text)

# Decrypt
cipher_text = input("Enter a message to decrypt: ")
ptext = ""

for letter in cipher_text:
    index = key.index(letter)
    ptext += chars[index]   # FIX: use chars, not key

print("Decrypted:", ptext)

