operand1 = 50
operand2 = 30
 
# Arithemtic Operators: 
# +, -, *, /, //, %, **

sum = operand1 + operand2
difference = operand1 - operand2
product = operand1 * operand2
quotient = operand1 / operand2
floor_division = operand1 // operand2
# Floor Division will round-off the float value and shows only integer part as a Quotient
remainder = operand1 % operand2
# 50^2
square = operand1 ** 2 

print("Sum: ", sum , "Difference: ", difference, "Product: ", product, "Quotient: ", quotient, "Floor Division: ", floor_division , "Remainder: ", remainder, "Square of a Number: ", square)

# Assignment Operators:
# =, +=, -=, *=, /=, %=, **=, //=

# Assigning a value:
number = 20
print("Original Number: ", number)
# number += 5 <=> number = number + 5
number += 5
print("5 is added to the Number: ", number)
number -= 5
print("5 is subtracted from the Number: ", number)
number *= 5
print("5 is multiplied with the Number: ", number)
number /= 5
print("Number is divided by 5: ", number)
number1 = 23
number1 /= 5
print("23 is divided by 5: ", number1)
# Number has been converted to Float, so new number has been taken
number2 = 23
number2 //= 5
print("23 is divided by 5 using Floor Division: ", number2)
new_number = 3
# 3 ^ 5 = 3*3*3*3*3 = 243
new_number **= 5 
print("Number is updated with Power of 5: ", new_number)

# Comparison Operators:
# >, <, >=, <=, ==, !=

n1 = 25
n2 = 35
print("Number 1 is greater than Number 2: ", n1 > n2)
print("Number 1 is lesser than Number 2: ", n1 < n2)
print("Number 1 is greater than or equal to Number 2: ", n1 >= n2)
print("Number 1 is lesser than or equal to Number 2: ", n1 <= n2)
print("Number 1 is equal to Number 2: ", n1 == n2)
print("Number 1 is not equal to Number 2: ", n1 != n2)

# Logical Operators:
# and, or, not

# We will use "and" operator to check multiple conditions together and if both are true, then result is true, if one fails the result will be false

# n1 = 25, n1 > 5 and n1 % 5 == 0
# 25 > 5 - T & 25 % 5 == 0 - T => T & T - T 
print("Number 1 is greater than 5 and multiple of 5: ", n1 > 5 and n1 % 5 == 0)

# n2 = 35, n2 < 50 or n2 % 4 == 0
# 35 < 50 - T or 35 % 4 == 0 - F => T or F - T
print("Number 2 is lesser than 50 or it can divisible by 4: ", n2 < 50 or n2 % 4 == 0)

# 35 < 50 - T and 35 % 4 == 0 - F => T and F - F
print("Number 2 is lesser than 50 and it can divisible by 4: ", n2 < 50 and n2 % 4 == 0)

# not(False) = True
print("Negation of (Number 2 is lesser than 50 and it can divisible by 4): ", not(n2 < 50 and n2 % 4 == 0))

# Identity Operators: 
# "is & is not" - We shall use this in List

# Membership Operators: 
# "in & not in" - We shall use it in List