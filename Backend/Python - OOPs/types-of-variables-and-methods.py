# In Python OOPs, we have 2 types of variables:
# Instance Variables & Class Variables

class Internship:
    # class variables, It is common for all class members or objects
    company = "ParvaM"
    duration = "15 weeks"

    def __init__(self, name, college, branch, internship):
        # instance variables - It is unique or different for by each object
        self.name = name
        self.college = college
        self.branch = branch
        self.internship = internship
    
    def enroll(self):
        # For accessing the Class variables, we need to refer to the class itself, 
        # ex: Internship.company & Internship.duration

        # For accessing the Instance variables, we need to refer the object,
        # ex: self.name, self.internship
        print(f"{self.name}, Thank You for enrolling with {Internship.company} for {self.internship} Internship for the duration of {Internship.duration}")

    def joinClass(self):
        print("You can join the session and learn about the concepts.")

    def practice(self):
        print("Practice on the concepts learned in the session and implement it through the tasks.")

    def interview(self):
        print("Participate in Mock Interviews and feel confident to attend the Industry Interviews and secure the job.\n")

# Object Creation or Initialization of the Objects:

std1 = Internship(name = "Sai Sanket", college="Acharya", branch="CSE", internship="Python Full Stack")

std2 = Internship(name = "Anushka", college="SMVCE", branch="CSE", internship="Machine Learning")

Internship.company = "VTU"

# Internship.enroll(std1)

# Self is automatically assigned as the Object itself (Behind the Scenes)
std1.enroll()
std1.joinClass()
std1.practice()
std1.interview()

std2.enroll()
std2.joinClass()
std2.practice()
std2.interview()

# Example 2
class Car:
    # class variables
    mode_of_transport = "Road"
    no_of_wheels = 4

    def __init__(self, brand, model, fuel_type, color, price, mileage):
        # instance variables
        # We can change the variable names
        self.carBrand = brand
        self.carModel = model
        self.fuelType = fuel_type
        self.carColor = color
        self.price = price
        self.mileage = mileage

    def demo(self):
        print(f"This is a car from {self.carBrand} brand, and it is a new model car named {self.carModel} and it is in {self.carColor} color, and it runs using {self.fuelType} as a fuel on the {Car.mode_of_transport} with {Car.no_of_wheels} wheels and costs around Rs.{self.price}L/- and it can give mileage upto {self.mileage} kmpl")

    def driveCar(self):
        print(f"{self.carModel} started driving and reached 2km distance, so it can drive upto {self.mileage - 2} Kms")

    def refillFuel(self):
        print(f"{self.fuelType} Fuel has been recharged, it can run upto {self.mileage} Kms")

    def parkCar(self):
        print(f"{self.carModel} has been parked successfully \n")

# Car Objects

car1 = Car(brand="Tata", model="Punch", fuel_type="Petrol", color = "Red", price=8.35, mileage=26.5)
car2 = Car(brand="Mahindra", model="XUV 700", fuel_type="Petrol", color = "Navy Blue", price=28.5, mileage=23.5)

car1.demo()
car1.driveCar()
car1.refillFuel()
car1.parkCar()

car2.demo()
car2.driveCar()
car2.refillFuel()
car2.parkCar()

# In OOPs, we have 3 types of methods:
# Instance Methods, Class Methods and Static Methods

class Bank:
    # class variables
    bank_name = "SBI"
    branch = "Hesaraghatta Road"
    no_of_accounts = 0
    interest_rate = 7.3

    def __init__(self, name, email, phone, address, type_of_account):
        self.custName = name
        self.custEmail = email
        self.custPhone = phone
        self.custAddress = address
        self.typeOfAc = type_of_account
        self.balance = 0

    # Instance methods: createAccount, deposit, withdraw, checkBalance
    # Default Parameter for instance method is "self"
    def createAccount(self):
        # random package is used to generate random numbers 
        import random
        print(f"Thank you for creating the account in {Bank.bank_name} bank, Check your account details given below: \n")
        ac_num = random.randint(1000000000, 9999999999)
        print(f"Name: {self.custName}\nEmail: {self.custEmail} \nPhone Number: {self.custPhone} \nAddress: {self.custAddress} \nBranch: {Bank.branch} \nA/C No.: {ac_num} \nInterest Rate: {Bank.interest_rate}%\n")
        Bank.no_of_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} deposited successfully, Your Current Balance: {self.balance}/-")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Rs.{amount} withdrawn successfully, Your Current Balance: {self.balance}/-")

    def checkBalance(self):
        print(f"Current Balance: Rs.{self.balance}/-\n")

    # class methods
    # decorator is a special symbol used for some purpose
    @classmethod
    # Default Parameter for class method is "cls"
    # cls refers to class itself
    def number_of_accounts(cls):
        print(f"Number of Account Holders: {Bank.no_of_accounts}\n")

    @classmethod
    def calculateInterest(cls, amount, duration):
        print(f"Principal Amount: {amount}, Duration: {duration} yrs, Rate of Interest: {Bank.interest_rate}\n")
        SimpleInterest = (amount*duration*Bank.interest_rate)/100
        print(f"Total Amount after Interest: Rs.{amount + SimpleInterest}/-\n")

    # static methods
    # Static Methods does not require any default paramter, if given it accepts any parameter
    @staticmethod
    def enquiry():
        print(f"Bank Name: {Bank.bank_name} \nBranch: {Bank.branch} \nInterest Rate: {Bank.interest_rate}\n")

# New Account - Object Creation
cust1 = Bank(name="Akshay Rao", email="akshay@gmail.com", phone="8218445125", address="Chikkabanavara", type_of_account="savings")

cust2 = Bank(name="Ajay Rao", email="ajay@gmail.com", phone="7028445125", address="Udupi", type_of_account="current")

cust1.createAccount()
cust1.deposit(5000)
cust1.deposit(10000)
cust1.withdraw(7000)
cust1.checkBalance()

print("\n")

cust2.createAccount()
cust2.deposit(25000)
cust2.deposit(5000)
cust2.withdraw(12000)
cust2.checkBalance()

Bank.enquiry()

Bank.number_of_accounts()
Bank.calculateInterest(50000, 2)

# Employee
# name, dob, email, phone, education, skills[list]

# registration - generate id for employee and add to some dept

# assign some work

# employee work on that and mentions the time taken for work