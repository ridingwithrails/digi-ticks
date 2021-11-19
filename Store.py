from User import User
from Product import Product
from getpass import getpass

data = ''
guest = True
users = User.build()

while guest:
    username = input("Please type in username:\n")
    password = getpass()
    user = User.fetch(username, password)
    if user: 
        guest = False
    else:
        print("wrong username or password")
        guest = True

while data != 'E':
    print("Hello " + user.name + "!")
    data = input("Store has started.  [L] List Products  [E] Exit\n")
    if data == 'L':
        Product.list()

 