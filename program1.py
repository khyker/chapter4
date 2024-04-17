'''
Katellyn Hyker
Chapter 4 Project 1
Write a script that inputs a line of plaintext and a distance value and outputs an encrypted text using a Caesar cipher.

'''

plaintext = input("Enter a line of plaintext to be encrypted: ")
distvalue = int(input("Enter the distance value: "))
cipherText = ""
for ch in plaintext:
    cipherText += chr(ord(ch)+distvalue)
print(cipherText)