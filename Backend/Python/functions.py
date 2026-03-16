# Function is a block of code which is used to perform some specific task when it is called.

# Syntax:
# def function_name():
#   Statements

# Parts of Function:
# 1) Function Declaration
# 2) Function Definition
# 3) Function Call

# Function Declaration & Definition
# Function name is commonly declared using camelCase
def sayHello():
    print("Hello Students!")

# Function Call
sayHello()
sayHello()
sayHello()

# Function with Parameters
# fName is a parameter
def greet(fName):
    print(f"Good Morning, {fName}")

# Akshay is a argument and also Regular Argument
greet("Akshay")
greet("Ajay")

def sum(a, b):
    print(f"Sum of {a} and {b}: {a+b}")

sum(10, 20)

# Paramters and Arguments:
# Variables within a paranthesis while defining a function is called as Parameter

# Variables within a paranthesis while calling a function is called as Argument

# functions with Default Parameter
def myInternship(company="ParvaM"):
    print(f"I'm doing my Internship at {company}")

myInternship()
myInternship("VTU")

# Function with Return Value
def square(number):
    return number**2

squareOf5 = square(5)
print(f"Square of 5: {squareOf5}")

# Two types of Functions: 
# Arbitrary Arguments (*args)
# Arbitrary Keyword Arguments (**kwargs)

# *args - If you don't know the number of arguments which may be given by user, in that time  we will use Arbitrary Arguments

# We don't know the limit of registration, so we can use *args
def internshipRegistration(*args):
    print("Completed Students List: ", args)

internshipRegistration("Akshay", "Ajay", "Akash", "Vikas", "Tejas")

internshipRegistration()

# Sum of the given variable number of arguments
def sumOfNumbers(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print("Sum: ", sumOfNumbers())
print("Sum of 2 Numbers: ", sumOfNumbers(2, 3))
print("Sum of 5 Numbers: ", sumOfNumbers(5, 10, 15, 20, 25))
print("Sum of 8 Numbers: ", sumOfNumbers(3, 5, 8, 10, 12, 14, 17, 19))

# Combining Regular Argument with Arbitrary Argument

# domain is normal parameter, *students can accept any number of arguments
def welcomeStudent(domain, *students):
    for std in students:
        print(f"Hello {std}, Welcome to {domain} Internship")

# Python & Java are Regular Arguments, Students Names are arbitrary arguments
welcomeStudent("Python", "Akshay", "Ajay", "Adarsh")
welcomeStudent("Java", "Preetham", "Sai", "Darshan")

# Arbitrary Keyword Arguments - **kwargs
def printLastName(**person):
    print("My Last name is", person["lName"])

# It is same as that of *args, but we need to give the keyword for each arguments
printLastName(fName = "Akshay", lName = "Rao")
printLastName(fName = "Abhishek", lName = "Gowda")

def userDetails(**info):
    print("User Details are as follows:")
    print("Name:", info["name"])
    print("Email:", info["email"])
    print("Phone Number:", info["phone"])

userDetails(name = "Akshay Rao", email = "akshay@gmail.com", phone = "7856235213")
userDetails(name = "Ajay Rao", email = "ajay@gmail.com", phone = "7856235256")

# Combination of Regular Arguments, Arbitrary Arguments (*args) and Arbitrary Keyword Arguments (**kwargs)

def printInfo(title, *args, **kwargs):
    roles = kwargs["roles"]
    depts = kwargs["depts"]

    # zip method is used to map each item respectively
    # name with args, role with roles, dept with depts
    for name, role, dept in zip(args, roles, depts):
        print(f"{title} of {name}:")
        print(f"    Role: {role}")
        print(f"    Department: {dept}")

printInfo("Details", "Akshay", "Ajay", roles = ["Assistant Engineer", "Associate Engineer"], depts = ["Web Development", "QA"])

printInfo("Bio", "Akash", "Vikas", roles = ["Mobile Gamer", "PC Gamer"], depts = ["Mobile Gaming", "PC Gaming"])

def printDetails(title, *args, **kwargs):
    # Enumerate is used to get the index number for the current loop
    for i, name in enumerate(args):
        print(f"{title} of {name}:")
        
        # Dividing the key value pairs to show in new format
        for key, value in kwargs.items():
            print(f"    {key}: {value[i]}")

printDetails("Employee Info", "Abhishek", "Mahesh", Role = ["Software Engineer", "QA Engineer"], Dept = ["Web Development", "QA"], Experience = [3, 1.5])

printDetails("Instagram Bio", "Akshay", "Akash", "Vikas", Bio = ["I love Mobile Gaming", "I love PC Gaming", "I love Console Gaming"], Favorite_Games = ["BGMI", "COD", "Clash of Clans"], Smartphone = ["Samsung", "Asus", "IQOO"])

# Difference b/w zip and enumerate and when to use for loop with key and value

names = ["Akshay", "Abhay", "Vinay"]
ages = [24, 27, 30]
# We will get only the values from normal for loop
for name in names:
    print(name)

# Enumerate is used to get the index number as well as the value from the list
# for index, key in enumerate(list, start=0/1)

for index, name in enumerate(names):
    print(index, name)

for index, name in enumerate(names, start=1):
    print(index, name)

# zip method is used to map each value based on the index position
for name, age in zip(names, ages):
    # print(name, age)
    print(f"{name} is {age} years old")


profile = {
    "name" : "Akshay",
    "age" : 24,
    "tech": "Python Full Stack"
}

print(profile)
print(profile.items())

for key, value in profile.items():
    print(f"{key}={value}")