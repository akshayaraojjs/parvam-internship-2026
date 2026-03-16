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

number = 2.45

# math.ceil() will round-off the number to next integer number
print(f"Ceil Value of {number}: {math.ceil(number)}")

# math.floor() will round-off the number to same integer number
print(f"Floor Value of {number}: {math.floor(number)}")

# math.sin(), math.cos(), math.tan()
print(f"Sine of 90: {math.sin(90)}")

# math.remainder() is used to find the remainder to completely divide the number
print(math.remainder(32,7))

# math.isnan is used to check whether the given value is number of not

# NAN - Not a Number
# Try in next class - Remainder, isnan, product