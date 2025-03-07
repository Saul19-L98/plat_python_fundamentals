class OrderStatic:

    @staticmethod
    def calculate_tax(amount,tax_rate):
        return amount * (tax_rate / 100)

print(OrderStatic.calculate_tax(1000,18))


class Order:
    global_discount = 10

    def __init__(self,amount):
        self.amount = amount
    
    @classmethod
    def update_global_discount(cls,new_discount):
        cls.global_discount = new_discount

Order.update_global_discount(15)
print(Order.global_discount)


#Exercise
class OrderExercise:
    discount = 0.10

    @staticmethod
    def calculate_price(amount):
        if amount < 20:
            raise ValueError("Low price, not authorized.")
        return f"Order authorized, amount to pay: ${ amount - (amount * OrderExercise.discount)}"

    @classmethod
    def update_global_discount (cls,new_discount):
        cls.discount = new_discount

#print(OrderExercise.calculate_price(19.99))
print(OrderExercise.calculate_price(30))
OrderExercise.update_global_discount(0.15)
print(OrderExercise.calculate_price(30))


