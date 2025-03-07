class Car:
    def __init__(self,car_id,name,price):
        self.car_id = car_id
        self.name = name
        self.price = price
        self.available = True

    def car_purchased(self):
        if self.available:
            self.available = False
            print(f"The car {self.name} has been purchaed successfuly.")
        else:
            print(f"The car {self.name} was sold out.")

class User:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name
        self.owned_cars = []

    def purchase(self,car):
        if car.available:
            car.car_purchased()
            self.owned_cars.append(car)
            print(f"The car {car.name} has been purchased succefuly by {self.name}")
            return
        getCarFromStorage = [ item for item in self.owned_cars if item.car_id == car.car_id ]
        if len(getCarFromStorage) > 0:
            print(f"You already adquired this car, {getCarFromStorage[0].name}")
        else:
            print(f"This car, {car.name} is not loger available.")

class Company:
    def __init__(self):
        self.cars = []
        self.users = []


    def register_users(self,user):
        self.users.append(user)
        print(f"--> New user added with the name: {user.name}")

    def add_cars(self,car):
        self.cars.append(car)
        print(f"--> New car added with the name: {car.name}")

    def show_available_cars(self):
        getAvailableCarsFromStorage = [ item for item in self.cars if item.available == True ]
        if len(getAvailableCarsFromStorage) == 0:
            print("Currently there is not available cars to sell. =(.")
            return
        print("--Avaible cars--")
        for item in getAvailableCarsFromStorage:
            print(f"id:{item.car_id},name: {item.name},price: $ {item.price}")

car1 = Car("1","Toyota",10000)
car2 = Car("2","Nissan",15000)

user1 = User("1","Sam")

company1 = Company()
company1.register_users(user1)
company1.add_cars(car1)
company1.add_cars(car2)
            
company1.show_available_cars()
user1.purchase(car1)
company1.show_available_cars()
user1.purchase(car1)

        
        

