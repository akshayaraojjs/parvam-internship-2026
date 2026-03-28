# Multi-Level Inheritance:
# Derived Class derives a new Derived Class
# Base Class -> Derived Class1 -> Derived Class2
# Base Class(Level 1)-> Base Class(Level 2)-> Derived Class(Level 3)

# Example 1:
class A:
    def printA(self):
        print("Class A")

class B(A):
    def printB(self):
        print("Class B derived from Class A")

class C(B):
    def printC(self):
        print("Class C derived from Class B")

# Object of Class B
b = B()
b.printA()
b.printB()

# Object of Class C
c = C()
# Object of Class C can access all the higher level class methods, can reach up to Base Class (Level 1)
c.printA()
c.printB()
c.printC()

# Example 2:
class Animal:
    def __init__(self, animal):
        self.animal = animal

    def printAnimal(self):
        print(f"\n{self.animal} is an Animal.")

class Habitat(Animal):
    def __init__(self, animal, type):
        super().__init__(animal)
        self.type = type

    def printHabitat(self):
        print(f"This is a {self.type} animal.")

class Food(Habitat):
    def __init__(self, animal, type, food):
        super().__init__(animal, type)
        self.food = food

    def printFood(self):
        print(f"This animal eats {self.food} as a food.\n")

dog = Food("Dog", "domestic", "pedigree")
dog.printAnimal()
dog.printHabitat()
dog.printFood()

tiger = Food("Tiger", "wild", "animal flesh")
tiger.printAnimal()
tiger.printHabitat()
tiger.printFood()

# Example 3: 
class Device:
    def __init__(self, type):
        self.type = type
    
    def print(self):
        print(f"\nThis is {self.type} device.")

# Device -> Type
class Type(Device):
    def __init__(self, type, current):
        # Calling the Constructor method of Device Class
        super().__init__(type)
        self.current = current

    def print(self):
        # Internally Calling (Device Class - print() method using super())
        super().print()
        print(f"It used {self.current} current for Power Supply.")

# Device -> Type -> Gadget
class Gadget(Type):
    def __init__(self, type, current, gadget):
        # Calling the Constructor method of Type Class
        super().__init__(type, current)
        self.gadget = gadget

    def print(self):
        # Call the previous or parent class method (Type Class - print() method)
        super().print()
        print(f"This gadget is used {self.gadget}\n")

mobile = Gadget("Rechargeable", "DC", "as Communication Device")
mobile.print()

mixer = Gadget("Electrical", "AC", "as Kitchen Appliance")
mixer.print()

calculator = Gadget("Calculative", "DC", "for Mathematical Calculations")
calculator.print()