def add(a,b,c):
    return a + b + c

values = (1,2,3)
print(add(*values)) 

def show_info(name,age):
    print(f"Name: {name}, Age: {age}")

data = {"name":"Ana", "age": 28}

show_info(**data)

#exercise 1:
print("-------exercise-------")

products = [
    {
        "name": "Coffe",
        "price": 22.25
    },
    {
        "name": "Water",
        "price": 5.25,
    },
    {
        "name": "Bread",
        "price": 10.75
    }
]


def calculate_total (*args,**kwargs):
    if kwargs.get("discount", False):
        add = sum(args)
        return add - ( add * 0.15)
    else:
        return sum(args) 

def iterate_products (products):
    prices = []
    for product in products:
        prices.append(product['price'])
    return prices

getPrices = iterate_products(products)
print(getPrices)
getTotal = calculate_total(*getPrices, discount=False)
getTotalDiscount = calculate_total(*getPrices, discount=True)
print(getTotal)
print(getTotalDiscount)