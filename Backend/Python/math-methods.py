# We can use min, max, abs, pow

numbers = [2, 7, 3, 5, 9, 6]
# min
minValue = min(numbers)
# max 
maxValue = max(numbers)

print(f"Min Value: {minValue}, Max Value: {maxValue}")

# abs - Negative value is converted into poistive value
negative = [-5, 3, -7, 4]
for num in negative:
    print(abs(num))

# pow - Power of the number
# pow(number, power)
print(f"2 ^ 5: {pow(2, 5)}")
print(f"5 ^ 6: {pow(5, 6)}")

# Math Module
# Math Module methods: sqrt, sin, cos, tan, ceil, floor, isnan, isqrt, prod, remainder

import math

# math.sqrt()
print(f"Square Root of 25: {math.sqrt(25)}")
print(f"Square Root of 27: {math.sqrt(27)}")

# math.isqrt() - isqrt will round off the decimal value to the nearest integer
print(f"Square Root of 27: {math.isqrt(27)}")

number = 2.01
negativeNumber = -5.2

# math.ceil() will round-off the number to next integer number (try to push for highest integer value)
print(f"Ceil Value of {number}: {math.ceil(number)}")
print(f"Ceil Value with Negative Number {negativeNumber}: {math.ceil(negativeNumber)}")

# math.floor() will round-off the number to same integer number (try to push for lowest integer value)
print(f"Floor Value of {number}: {math.floor(number)}")
print(f"Floor Value with Negative Number {negativeNumber}: {math.floor(negativeNumber)}")

# math constants: math.pi, math.e, math.tau, math.inf, math.nan
print(f"Pi value: {math.pi}")
print(f"e value: {math.e}")
print(f"tau value (2*pi): {math.tau}")
print(f"infinity value: {math.inf}")
print(f"Not a Number: {math.nan}")

# radians and degrees
# Conversion of 180 degree in radian results to pi value
print(f"Radian Value for 180degree: {math.radians(180)}")

# Vice Versa of radian to degree
print(f"Degree Value for pi value: {math.degrees(math.pi)}")

# math.sin(), math.cos(), math.tan() (It will take radian as the input)
print(f"Sine of 180deg: {math.sin(math.pi)}")

# math.remainder() is used to find the remainder to completely divide the number
print(math.remainder(32,7))

# math.isnan is used to check whether the given value is number of not

# NAN - Not a Number
# Try in next class - Remainder, isnan, product

# GCD (Greatest Commion Divisor or HCF)
print(f"GCD of 15, 45: {math.gcd(15, 45)}")
print(f"GCD of 21, 28: {math.gcd(21, 28)}")

# Factorial of a number
print(f"Factorial of 5(5!): {math.factorial(5)}")
print(f"Factorial of 10(10!): {math.factorial(10)}")

# fabs - Floot Absolute Value
print(f"Absolute value of float (-5.3): {math.fabs(-5.3)}")
print(f"Absolute value of float (-5.3): {abs(-5.3)}")

# Product of given numbers in the list
print(f"Product of given numbers: {math.prod([2, 5, 8, 10])}")
print(f"Product of given numbers: {math.prod([2, 4, 8, 16])}")