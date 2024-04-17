'''
Katellyn Hyker
Chapter 4 Project 2
Write a script that inputs a line of encrypted text and a distance value and outputs plaintext using a Caesar cipher.

'''

encryptedText = input("Enter a line of encrypted text: ")
distValue = int(input('Enter the distance value: '))
decipherText = ""
for ch in encryptedText:
    decipherText += chr(ord(ch)-distValue)
print(decipherText)