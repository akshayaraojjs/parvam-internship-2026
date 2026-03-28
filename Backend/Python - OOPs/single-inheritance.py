# Single Inheritance: 
# "Base Class" Derives a "Derived Class"
# "Derived Class" is derived by a "Base Class"

# Example 1
# A -> B
# Base Class
class A:
    def show(self):
        print("Class A\n")

# Derived Class
class B(A):
    def display(self):
        print("Class B is derived from Class A\n")

# Object of Base Class
a = A()
a.show()

# Object of Derived Class
b = B()
# b object can call or access the methods of "base class A"
b.show()
b.display()

# Example 2:
# Vehicle -> Car
# Base Class
class Vehicle:
    def showVehicleInfo(self):
        print("Vehicle Started!")

# Derived Class
class Car(Vehicle):
    def showCarInfo(self):
        print("Car Started!")

car1 = Car()
# Directly I can access the Base Class methods
car1.showVehicleInfo()
car1.showCarInfo()

# Example 3:
class Computer:
    def __init__(self, processor, ram, rom):
        self.processor = processor
        self.ram = ram
        self.rom = rom

    def displayBasicInfo(self):
        print(f"Device is built with {self.processor} processor with {self.ram} RAM & {self.rom}")

class Laptop(Computer):
    def __init__(self, processor, ram, rom, brand, model, price):
        # Calling the constructor method of Base Class from Derived Class 
        super().__init__(processor, ram, rom)
        self.brand = brand
        self.model = model
        self.price = price
    
    def displayInfo(self):
        print(f"\nLaptop Brand: {self.brand} \nModel: {self.model} \nPrice: Rs.{self.price}/-")

# We can pass the details of Base Class to constructor
lap1 = Laptop("Intel i5 10th gen", "16gb", "512gb", "Asus", "TUF", 50000)
lap1.displayInfo()
lap1.displayBasicInfo()

lap2 = Laptop("Intel i7 13th gen", "16gb", "1Tb", "MSI", "Katana", 70000)
lap2.displayInfo()
lap2.displayBasicInfo()