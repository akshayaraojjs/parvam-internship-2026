# Open Terminal - Ctrl + Shift + `
# To check output: 
# Run: python file_name.py

# In Python, code is debugged and output is shown using Interpreter

# This is a Single Line Comment

# This is 
# Multi-line
# Comment

# Variables and Datatypes
fName = "Akshay"
lName = 'Rao'
print(fName)
print(lName)
print(fName, lName)

# To check the datatype of any variable, we can use type() method
print(type(fName))

age = 24
print(age, type(age))

height = 150.35
print(height, type(height))

comp = 5 + 3j
print(comp, type(comp))

isIndian = True
print(isIndian, type(isIndian))

# Primitive Datatypes:
# int, float, string, complex, boolean

# Non-Primitive Datatypes:
# list, tuple, set, dictionary

# List - (Similar to Array)
# List is represented by Square Brackets '[]'
fruits = ["Apple", "Banana", "Chikoo", "Dragon Fruit"]
print(fruits, type(fruits))

# Tuple is represented by Paranthesis '()'
cars = ("Toyota Innova", "Tata Punch", "Skoda Rapid", "Mahindra XUV 700", "Kia Sonet")
print(cars, type(cars))

# Set is represented by Flower Braces '{}'
evenNumbers = {2, 4, 6, 8, 10}
print(evenNumbers, type(evenNumbers))

# Dictionary is represented by Key-Value Pairs
profile = {
    # "key" : "value"
    "name" : "Akshay Rao", 
    "age" : 25, 
    "company": "ParvaM",
    "programming-languages": ["C", "C++", "Java", "Python"],
    "frameworks": ("Django", "Laravel", "React", "Spring"),
}

print(profile, type(profile))