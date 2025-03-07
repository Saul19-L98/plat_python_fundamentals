from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    #Create a dictionary with a default value 0
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] += 1
    return product_count

orders = ['laptop','smarthphone','laptop','tablet']
count = count_products(orders)
print(count)