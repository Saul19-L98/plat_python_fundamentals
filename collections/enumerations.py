from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 
    SHIPPED = 2
    DELIVERED = 3

def check_order_status(status: OrderStatus):
    #Test the state of the order and return a message
    if status == OrderStatus.PENDING:
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped."
    elif status == OrderStatus.DELIVERD:
        return "Order has been deliverd."

print(check_order_status(OrderStatus.SHIPPED))