# Indentation needs to maintained in Python for all the conditional statements

# If Statement
number = 20
if (number > 10):
    print("The given number is greater than 10")

if (number % 2 == 0):
    # f-string is used to pass the value within a single line
    print(f"{number} is even number")

# If-Else
if(number % 2 == 0 and number % 5 == 0):
    print(f"{number} is divisible by both 2 & 5")
else:
    print(f"{number} is not divisible by either 2 or 5")

# Elif is used to check multiple conditions
num1 = 25
num2 = 35

if(num1 > num2):
    print(f"{num1} is greater than {num2}")
elif(num2 > num1):
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is equal to {num2}")

# Shorthand If and If-else
if num1 > num2 : print(f"{num1} is greater than {num2}")

# true statement | if condition | else | False Statement
print(f"{num1} is greater than {num2}") if num1 > num2 else print(f"{num2} is greater than {num1}")

# Nested If 
num3 = 45
if (num1 > num2):
    if(num1 > num3):
        print(f"{num1} is greatest")
    else:
        print(f"{num3} is greatest")
else:
    if(num2 > num3):
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")

# Match Statement
month = 5
match month:
    case 1: 
        print("January")
    case 2: 
        print("Febraury")
    case 3: 
        print("March")
    case 4: 
        print("April")
    case 5: 
        print("May")
    case 6: 
        print("June")
    case 7: 
        print("July")
    case 8: 
        print("August")
    case 9: 
        print("September")
    case 10: 
        print("October")
    case 11: 
        print("November")
    case 12: 
        print("December")