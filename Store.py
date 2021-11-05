from User import User
from Product import Product

data = ''
while data != 'E':
    data = input("Store has started.  [L] List Products  [E] Exit\n")
    if data == 'L':
        Product.list()
