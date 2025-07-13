#Q.1)WAP: to find area of Circle, Square, Triangle using OOPs, and use Abstraction
"""""
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length= length
        self.breadth= breadth
    def area(self):
        return self.length * self.breadth
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height)/2
shapes = [Circle(5), Rectangle(2, 2), Triangle(24, 56)] 
for shape in shapes:
    area = shape.area()
    print(f"Area of {type(shape).__name__} is {area}")
#obj1 = Circle(2)
"""
#Q.2)WAP: for Banking System Deposits and withdraw but use OOPs encapsulation by creating private variables
"""""
class Bank():
    def __init__(self, balance = 0):
        #self.balance = balance #Public Variable
        #self._balance = balance  #Protected Vaiable
        self.__balance = balance #Private Variable
        
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f"Your {amount} is Deposit Successfull Current Balance{self.__balance}")
    def withdraw(self, amount):
#        self.__balance = self.__balance + amount
#        print(f"Your {amount} is Deposit Successfull Current Balance{self.__balance}")
         if self.__balance < amount:
             print("Not Enough Amount in Bank")
         else:
             self.__balance = self.__balance + amount
             print(f"Your {amount} is withdraw Successfull Current Balance{self.__balance}")
    def balance(self):
        print(f"Your Current Balance{self.__balance}") 

obj = Bank()
obj.balance()
obj.deposit(1000)
#obj.balance()
obj.withdraw(500)
#print(obj.__balance)
#obj.balance = 1000
#print(obj.balance)"
"""
#Q.3)WAP: for Vehicle Hierarchy for Cars & Bikes use OOPs inheritance
class Vehicles():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def showdetails(self):
        print(f"Vehicle Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class Car(Vehicles):
    def __init__(self, brand, model, year, seats):
        super().__init__(brand, model, year)  
        self.seats = seats

    def showdetails(self):
        super().showdetails()
        print(f"Car Seats: {self.seats}")

class Bike(Vehicles):
    def __init__(self, brand, model, year, mileage):
        super().__init__(brand, model, year)  
        self.mileage = mileage

    def showdetails(self):
        super().showdetails()
        print(f"Bike Mileage: {self.mileage} km/l")

carobj = Car("Audi", "A15", 2024, 4)
bikeobj = Bike("Royal Enfield", "Bullet", 2024, 25)
carobj.showdetails()
bikeobj.showdetails()
