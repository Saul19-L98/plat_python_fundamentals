class Vehicle:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"The vehicle {self.brand}, has been sold.")
        else:
            print(f"The vehicle {self.brand}, is not available.")

    def check_available(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("This method should be implemented by the subclass")
 
    def stop_engine(self):
        raise NotImplementedError("This method should be implemented by the subclass")


class Car(Vehicle): 
    def start_engine(self):
        if not self.is_available:
            return f"The car's engine {self.brand} is running."
        else:
            return f"The car {self.brand} was not available."
 
    def stop_engine(self):
        if self.is_available:
            return f"The car's  engine {self.brand} was turned off."
        else:
            return f"The car {self.brand} is not available."

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The bicycle {self.brand} is running."
        else:
            return f"The bicycle {self.brand} was not available."
 
    def stop_engine(self):
        if self.is_available:
            return f"The car's  engine {self.brand} was turned off."
        else:
            return f"The car {self.brand} is not available."

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The truck's engine {self.brand} is running."
        else:
            return f"The truck {self.brand} was not available."
 
    def stop_engine(self):
        if self.is_available:
            return f"The truck's  engine {self.brand} was turned off."
        else:
            return f"The truck {self.brand} is not available."

class Customer:
    def __init__(self,name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self,vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Sorry, {vehicle.brand} was not available")

    def inquire_vehicle(self,vehicle:Vehicle):
            if vehicle.check_available():
                availability = "available"
            else: 
                availability = "not available"
            print(f"Vehicle {vehicle.brand} is '{availability}' and has a price of '{vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self,vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"The vehicle {vehicle.brand} was added to storage.")

    def register_customer(self,customer: Customer):
        self.customer.append(customer)
        print(f"The customer {customer.name} was added.")

    def show_available_vehicle(self):
        print("--Available vehicles at the store--")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"--{vehicle.brand} by $ {vehicle.get_price()}--")
        

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo","FH16",80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)


dealership.show_available_vehicle()

customer1.inquire_vehicle(car1)

customer1.buy_vehicle(car1)

dealership.show_available_vehicle()

