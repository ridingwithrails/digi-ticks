from User import User
from Product import Product
from getpass import getpass

data = ''
guest = True
users = User.build()

def is_user(username, password):
     print(username)
     print(password)
     if username in users:
            user = users(username)
            return user.password == password
     else:
        return True

while guest:
    username = input("Please type in username:\n")
    password = getpass()
    if is_user(username, password):
        guest = False
    else:
        guest = True



while data != 'E':
    data = input("Store has started.  [L] List Products  [E] Exit\n")
    if data == 'L':
        Product.list()

 