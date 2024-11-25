class Vehicle():
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print ("Beep-Beep")
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def printDetails(self):
        print(f"This car is {self.brand} {self.model}")
    
my_car= Car("Maruti", "Swift")
my_car.printDetails()
my_car.honk()