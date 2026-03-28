# Multiple Inheritance will have 2 or more Parent with 1 child
# 2 or more Base Class derives a Derived Class
#  A     B
#     C

# Example 1:
class A:
    def displayA(self):
        print("Class A is a base Class")

class B:
    def displayB(self):
        print("Class B is also a base Class")

class C(A, B):
    def displayC(self):
        print("Class C is derived from both Clas A & B - Base Classes")

# Object of Class A
a = A()
a.displayA()

# Object of Class B
b = B()
b.displayB()

# Object of Class C
c = C()
# c object can refer or call both the methods of Class A & B
c.displayA()
c.displayB()
c.displayC()

# Example 2:
class Father:
    def displayInfo(self):
        print("\nHe is a Father to some children.")

class Husband:
    def displayDetails(self):
        print("He is also a Husband for his wife.")

class Person(Father, Husband):
    def display(self):
        print("He is a person.")

person = Person()
person.display()
person.displayDetails()
person.displayInfo()

# Example 3:
class Camera:
    def print(self):
        print("It can capture the pictures.")

class Communication:
    def print(self):
        print("It can be used for calling someone to convey the message.")

class Smartphone(Camera, Communication):
    def print(self):
        print("\nThis is a Smartphone Device, which can act as both Camera & Communication Device.")
        # Calling both the class methods by using the class name itself
        Camera.print(self)
        Communication.print(self)

mob = Smartphone()
mob.print()