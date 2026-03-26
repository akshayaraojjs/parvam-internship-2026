# Built-In Polymorphism

name = "Akshay Rao"
hobbies = ["Playing", "Learning", "Teaching", "Coding"]
skills = ("Python", "PHP", "Java", "Django", "Laravel", "Spring")

# len() - method can be used with all kind of datatypes, same method can be used
print("Length of name:",len(name))
print("Number of hobbies:",len(hobbies))
print("Number of skills:",len(skills))

# type() - method can be used to check the datatype of any variable
print(type(name))
print(type(hobbies))
print(type(skills))

# sum() - method can be used with multiple datatype
print(sum([1,2,3,4])) # Sum method with List
print(sum((1,2,3,4))) # Sum method with Tuple
print(sum({1,2,3,4})) # Sum method with Set

# Custom Method
def display(value):
    print(f"Given Value: {value}, It is of type {type(value)}")

display("Akshay")
display(50)
display(50.5)
display([1, 5, 8, 15])

# Custom Method
def findArea(sides, side1, side2 = None, side3 = None):
    if sides == 1:
        shape = "Square"
        print(f"Shape: '{shape}', Area of {shape}: {side1 * side1}")
    elif sides == 2:
        shape = "Rectangle"
        print(f"Shape: '{shape}', Area of {shape}: {side1 * side2}")
    elif sides == 3:
        shape = "Cube"
        print(f"Cube: '{shape}', Area of {shape}: {side1 * side2 * side3}")

findArea(1, 5)
findArea(2, 5, 10)
findArea(3, 20, 10, 5)