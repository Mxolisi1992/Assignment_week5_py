
class Car:
    color = "Green" 

    def drive(self):
        print("The car is driving ")

my_car = Car()
print(my_car.color)
my_car.drive()

class Car:
    def __init__(self, color, model):
        self.color = color    
        self.model = model  

car = Car("Green", "Golf7")
print(car.color) 

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(1)
print(car.wheels) 