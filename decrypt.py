from cryptography.fernet import Fernet

with open("mykey.key", "rb") as mykey:
    key = mykey.read()

f = Fernet(key)

with open("hot_enc.zip", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open("hot.zip", "wb") as decrypted_file:
    decrypted_file.write(decrypted)