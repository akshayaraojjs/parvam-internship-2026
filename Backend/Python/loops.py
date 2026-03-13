# while loop
# syntax:
# while condition:
#       print Statement

i = 0
while i < 10:
    print(f"{i}")
    # In python, increment(++) and decrement(--) operator, we should use += or -=
    # i += 1 <=> i = i + 1
    i += 1 

print("Even numbers from 10 to 20")
while i <= 20:
    if i % 2 == 0:
        print(i) 
    i += 1

print("Odd numbers from 20 to 30")
while i <= 30:
    if i % 2 != 0:
        print(i) 
    i += 1

# While Loop problems
# Work on Sum of Natural Numbers, Sum of Digits, Sum of Even Digits, Sum of Odd Digits, Count Even and Odd Digits, Reverse a Number, Palidrome or Not

# For Loop
# Syntax:
# range limit is exclusive
# for key in range(limit):
#       Print Staments
x = 1
# Print from 1 to 9, because 10 is exclusive
for x in range(11):
    print(x)

# print multiples of 3
for x in range(20):
    if x % 3 == 0:
        print(x)

# range(start, end)
# Printing the multiples of 3 from 10 to 30
print("Multiples of 3 from 10 to 30:")
for x in range(10, 30):
    if x % 3 == 0:
        print(x)

# range(start, end, step)
print("Multiple of 5:")
for x in range(0, 21, 5):
    print(x)

# For Loop with List, Tuple:
# List
milkProducts = ["Milk", "Curd", "Ghee", "Butter", "Paneer", "Cheese"]
print(milkProducts)

# for item in list:
#   print(item)

# for loop with list
for item in milkProducts:
    print(item)

# Tuple
movies = ("KGF", "KD", "Toxic", "Hebbuli", "Kantara")
print(movies)

# for loop with tuple
for movie in movies:
    print(movie)

# Nested For Loop
languages = ["Kannada", "Tamil", "Marathi", "Malayalam"]
states = ["Karnataka", "Tamil Nadu", "Maharashtra", "Kerala"]

for state in states:
    for lang in languages:
        print(f"({state}, {lang})")

# Monday Topics:
# Functions, Math Methods and Date Methods, "Regular Expressions"