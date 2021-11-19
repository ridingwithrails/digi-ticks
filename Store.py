from User import User
from Product import Product
from getpass import getpass

data = ''
guest = True
users = User.build()



while guest:
    username = input("Please type in username:\n")
    password = getpass()
    if User.is_user(username, password):
        guest = False
    else:
        print("wrong username or password")
        guest = True



while data != 'E':
    data = input("Store has started.  [L] List Products  [E] Exit\n")
    if data == 'L':
        Product.list()

 