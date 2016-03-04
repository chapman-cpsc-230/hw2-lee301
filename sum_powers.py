"""
File: sum_powers

Copyright (c) 2016 Krystal

License: MIT

<Sum of b^0 to b^n>

"""

user_input = raw_input("Enter a float number: ")
b = float(user_input)

while b == 1:
    user_input = raw_input ("Value cannot be 1. Enter value for b: ")
    b = float (user_input)

user_input = raw_input("Enter a value: ")
n = int(user_input)

i = 0
total = 0

while i < n:
    total += b**i
    i += 1

print total
print (b**(n+1)-1)/(b-1)
