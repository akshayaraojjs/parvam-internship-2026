# 1 Parent with multiple Children
# A Base Class derives multiple 'Derived Class'

# Example 1:
class A:
    def printA(self):
        print("Class A is a Base Class")

# A -> B
class B(A):
    def print(self):
        print("Class B is derived from Base Class A\n")

# A -> C
class C(A):
    def print(self):
        print("Class C is also derived from Base Class A\n")

# A -> D
class D(A):
    def print(self):
        print("Class D is also derived from Base Class A\n")

# Object of Class B can access the methods of Class A
b = B()
b.printA()
b.print()

# Object of Class C can access the methods of Class A
c = C()
c.printA()
c.print()

# Object of Class D can access the methods of Class A
d = D()
d.printA()
d.print()

# Example 2:
class Animal:
    def display(self):
        print("This is an Animal.")

# Animal -> Dog
class Dog(Animal):
    def sound(self):
        super().display()
        print("Dog barks!\n")    

# Animal -> Cat
class Cat(Animal):
    def sound(self):
        super().display()
        print("Cat meows!")    

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

# Example 3:
class Vehicle:
    def __init__(self, no_of_wheels):
        self.wheels = no_of_wheels

    def display(self):
        print(f"This vehicle consists of {self.wheels} wheels.")

class Bike(Vehicle):
    def __init__(self, model, wheels):
        super().__init__(wheels)
        self.model = model

    def drive(self):
        print(f"{self.model} vehicle started driving.")

    def park(self):
        print(f"{self.model} vehicle has been parked.")

class Car(Vehicle):
    def __init__(self, model, wheels):
        super().__init__(wheels)
        self.model = model

    def drive(self):
        print(f"{self.model} vehicle started driving.")

    def park(self):
        print(f"{self.model} vehicle has been parked.\n")

bike1 = Bike("Pulsar - NS125", 2)
bike1.display()
bike1.drive()
bike1.park()

bike2 = Bike("Royal Enfield - GT Continental", 2)
bike2.display()
bike2.drive()
bike2.park()

car1 = Car("Mahindra - XUV700", 4)
car1.display()
car1.drive()
car1.park()

car2 = Car("Skoda - Rapid", 4)
car2.display()
car2.drive()
car2.park()