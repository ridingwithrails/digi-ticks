class Product:
    #P1
    def __init__(self, price, picture, name, inventory):
        self.price = price 
        self.picture = picture
        self.name = name
        self.inventory = inventory
#P2 (in progress)
hotdog    = Product(13, "s3", "HOT Dawg", 10)
milkshake = Product(10, "s3", "Strawberry Milkshake", 20)
snickers  = Product(3, "s3", "Small snicker bar", 10)
slime     = Product(5, "s3", "slime", 20)
pop       = Product(5, "s3", "ring pop", 20)
pencil    = Product(3, "s3", "mechanical pencil", 30)
eraser    = Product(10, "s3", "scented eraser", 15)

#P3
products = [hotdog, milkshake, snickers, slime]
#NaN
for product in products:
    print("Name: ", product.name, "Price: ", product.price )
