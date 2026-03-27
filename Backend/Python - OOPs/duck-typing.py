# It is a type of Polymorphism in Python
# "If it looks like a duck and quacks like a duck, it is a duck"

class Dog:
    def eat(self):
        print("Dog eats Biscuit")

    def makeSound(self):
        print("Dog barks")

    def sleep(self):
        print("Dog sleeps in the hut")

class Cat:
    def eat(self):
        print("Cat eats Cat Food")

    def makeSound(self):
        print("Cat meows")

    def sleep(self):
        print("Cat sleeps in the hut")

class Duck:
    def eat(self):
        print("Duck eats fishes")

    def makeSound(self):
        print("Duck quacks")

    def sleep(self):
        print("Duck sleeps in the water")

d1 = Dog()

d1.eat()
d1.makeSound()
d1.sleep()

c1 = Cat()

c1.eat()
c1.makeSound()
c1.sleep()

duck1 = Duck()

duck1.eat()
duck1.makeSound()
duck1.sleep()

# Example 2

class Item:
    def fly(self, item):
        print(f"{item} flies in the sky")

    def lives(self, item, type):
        print(f"{item} is a {type} object\n")

# Object
aeroplane = Item()
aeroplane.fly("Aeroplane")
aeroplane.lives("Aeroplane", "Non-Living")

# Object
bird = Item()
bird.fly("Bird")
aeroplane.lives("Bird", "Living")

# Object
kite = Item()
kite.fly("Kite")
kite.lives("Kite", "Non-Living")

# Example 3:
class CreditCard:
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Credit Card")

class UPI:
    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI")

class NetBanking:
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Net Banking")

class Cash:
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Cash")

def make_payment(method, amount):
    method.pay(amount)

# Objects
c = CreditCard()
u = UPI()
n = NetBanking()
cash = Cash()

make_payment(c, 500)
make_payment(u, 1000)
make_payment(n, 800)
make_payment(cash, 1200)

# Example 4:
class Email:
    def sendMessage(self):
        print(f"Message sent through the E-mail")

class WhatsApp:
    def sendMessage(self):
        print(f"Message sent through the WhatsApp")

class Telegram:
    def sendMessage(self):
        print(f"Message sent through the Telegram")

class Letter:
    def sendMessage(self):
        print(f"Message sent through the Letter")

def notify(mode):
    mode.sendMessage()

e = Email()
w = WhatsApp()
t = Telegram()
l = Letter()

print("\n")
notify(e)
notify(w)
notify(t)
notify(l)