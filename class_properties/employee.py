class Product:
    def __init__(self,name,price):
        self.name = name
        self._price = price
        # self._quantity = quantity
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if not value:
            raise ValueError("The new price value can not be empty.")
        if value < 0:
            raise ValueError("Negative values are not valid.")
        self._price = value
    
    @price.deleter
    def price(self):
        print(f"The price of {self.name} was removed {self._price}")
        del self._price

    def __str__(self):
        if not hasattr(self,'_price'): 
            return f"Name: {self.name}, Product: 0"
        return f"Name: {self.name}, Product: {self._price}"
    


product = Product('Potato',20)
print(product.price)

product.price = 40
print(product.price)
print(product)

del product.price
print(product)
product.price = 30
print(product)



