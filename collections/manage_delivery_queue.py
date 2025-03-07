from collections import deque

def manage_delivery_queue() -> deque:
    # Create a queue to manage products delivery.
    delivery_queue = deque(["order_1","order_2","order_3"])
    delivery_queue.append("order_4") # Add it at the end of the queue
    delivery_queue.appendleft("order_0") # Add it at the beginning
    delivery_queue.pop() # Delete the last element
    delivery_queue.popleft() # Delete the first element
    return delivery_queue

queue = manage_delivery_queue()
print(queue)