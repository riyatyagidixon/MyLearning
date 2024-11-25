class Person:
    def __init__(self, id, name):
        self.id = id
        self.name= name
class Employee(Person):
    def __init__(self,id, name, salary):
        super().__init__(id, name)
        self.salary = salary

    def printDetails(self):
        print(self.id)
        print(self.name)
        print(self.salary)

e = Employee(101, "Riya", 500000)
e.printDetails()