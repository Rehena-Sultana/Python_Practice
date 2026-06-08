# Multiple child classes inherit from one parent class.

# create a parent class: class 1
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def vehicle_info(self):
        print("Name is: ",self.brand)

# create class2 that inherits class 1
class Car(Vehicle):
    def __init__(self,brand,door):
        super().__init__(brand)
        self.door=door
    def car_info(self):
        print(f"{self.brand} has {self.door} doors")

# create class 3 that also inherits class 1
class Bike(Vehicle):
    def __init__(self,brand,wheels):
        super().__init__(brand)
        self.wheels=wheels
    def bike_info(self):
        print(f"{self.brand} has {self.wheels} wheels")

c= Car ("Toyota", 4)
c.car_info()

b= Bike("A", 2)
b.bike_info()