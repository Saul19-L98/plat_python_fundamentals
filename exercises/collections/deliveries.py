import random
from enum import Enum
from collections import defaultdict

class OrderStatus(Enum):
    PENDING = 1 
    SHIPPED = 2
    DELIVERED = 3

def createOrderList(products: list[str], size: int) -> list[str]:
    newList = []
    for i in range(0,size):
        getRandomItem = products[random.randint(0,len(products) - 1)]
        newList.append(getRandomItem)
    return newList

def count_products(orders: list[str]) -> defaultdict:
    #Create a dictionary with a default value 0
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] += 1
    return product_count

def check_order_status(status: OrderStatus) -> str:
    #Test the state of the order and return a message
    if status == OrderStatus.PENDING:
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "Order has been deliverd."

products = ["pc","tablet","laptop","smartphone"]

ordersList = createOrderList(products,10)

order = count_products(ordersList)
print("--> Orders Collection.")
print(order)

ordersWithStatus = [
    {'name': name, 'count': count, 'status': OrderStatus(random.randint(1, 3))} 
    for name, count in order.items()
]
print("--> Orders transformed into a list.")
print(ordersWithStatus)

for order in ordersWithStatus:
    print(f"-----Verifying Prdouct {order['name']} Status-----")
    print(f"--> Status: {check_order_status(order['status'])}")
