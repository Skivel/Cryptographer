from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('mykey1.key', 'wb') as mykey:
    mykey.write(key)
