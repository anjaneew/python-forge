import random
import string

# chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#Encription
plain_text = input("Enter a message to encript: ")
ciper_text = ""

for letter in plain_text:
    # ciper_text.append(chars[letter.index()])
    index = chars.index(letter)
    ciper_text += key[index]
  
print("************************")
print(f"Original message: {plain_text}")
print(f"Encypted message: {ciper_text}")
print("************************")

#Decription
ciper_text = input("Enter a message to decript: ")
plain_text = ""

for letter in ciper_text:
    # ciper_text.append(chars[letter.index()])
    index = key.index(letter)
    plain_text += chars[index]
  
print("************************")
print(f"Original message: {ciper_text}")
print(f"Decrypted message: {plain_text}")
print("************************")