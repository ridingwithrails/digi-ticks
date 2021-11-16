from User import User
from Product import Product
from getpass import getpass


data = ''
guest = True

while guest:
    username = input("Please type in username:\n")
    password = getpass()
    print(password)

    users = User.build()
    print(users)

    guest = False




while data != 'E':
    data = input("Store has started.  [L] List Products  [E] Exit\n")
    if data == 'L':
        Product.list()
