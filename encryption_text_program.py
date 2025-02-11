#Encryption program

import random
import string #by using this module, we can import all the characters below 
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

chars= string.punctuation + string.digits + string.ascii_letters + " " # " " is a space which we will also use
chars = list(chars) # since earlier, we had one long string of characters, we need to convert that into a list that separates every character into its own element separately
key = chars.copy()  #we copy the list into the variable of key so we will have two identical lists  

random.shuffle(key) #shuffles the elements in the lists of keys
 
#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:   #for every letter in the plain_text
    index = chars.index(letter) #(index means position) find the position of the letter correspondong to the position of that letter in the chars set
    cipher_text += key[index]   #return the index(letter from the cooresponding postion) and add it to cipher_text accordin to their position respectively

print(f"Original message {plain_text}")
print(f"Encrypted message {cipher_text}")


#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message {plain_text}")
print(f"Original message {cipher_text}")
