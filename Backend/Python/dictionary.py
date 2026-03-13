# dictionary is represented by key-value pairs

# Dictionary Properties:
# Ordered, Mutable (Changeable), Duplicate Values not allowed

student = {
    "name" : "Akshay Rao",
    "college": "ABC College",
    "degree": "B.E",
    "branch": "ISE",
    "sem": 8,
    "hobbies": ["Singing", "Playing", "Gaming", "Learning"]
}

print(student)

print(type(student))

print("Student Name:", student["name"])
print("Student Hobbies:", student["hobbies"])

# Dictionary Methods:
# keys, values, items, get, pop, popitem, update, copy, clear

# Keys method is used to get all the keys in a list format
print(student.keys())

# Values method is used to get all the values in a list format
print(student.values())

# Items method is used to get all the key-value pairs in tuple format
# We will get all the items in List format but each pair is formatted in tuple format (Outer part is list, Inner part or each key value pair is in tuple)
print(student.items())

# Get method is used to get the individual key-value pair using its key
# print(student["college"])
print(student.get("college"))

# Update method is used to add a new key-value pair or update the existing key-value pair
# Adding new key-value pair (new item)
student.update({"skills": ("HTML", "CSS", "Bootstrap", "JavaScript")})
print(student)

# Update the existing key-value pair
# dict.update({key: value})
student.update({"college": "ParvaM"})
print(student)

# Pop method is used to remove the specific item from the dictionary
# dict.pop("key")
student.pop("sem")
print("Student Details (sem has been removed):", student)

# Pop Item method is used to remove the last inserted key-value paid
student.popitem()
print("Student Details:", student)

# Copy method is used to copy the key-value pairs from one dictionary to another
new_student = student.copy()
print(new_student)

# Clear method is used to clear all the key-value pairs from the dictionary
new_student.clear()
print(new_student)