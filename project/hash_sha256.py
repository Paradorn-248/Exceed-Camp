import hashlib

password = input("password: ")
encryp = hashlib.sha256(password.encode())
print(encryp.hexdigest())
print(hashlib.sha256(password.encode()).hexdigest())