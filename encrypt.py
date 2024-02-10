from cryptography.fernet import Fernet

with open("mykey.key", "rb") as mykey:
    key = mykey.read()

f = Fernet(key)

with open("hot.zip", "rb") as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open("hot_enc.zip", "wb") as encrypted_file:
    encrypted_file.write(encrypted)
