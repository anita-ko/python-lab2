# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko
# Date: sep 30, 2026
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

# TO DO 1: 
# Import the `math` module.
# Define a variable named num. Prompt the user to input a number and assign it to the variable num.
# Convert the user input to a floating-point number and assign it to num.

# TO DO 2: 
# Create an infinite loop using while True. Inside the loop:
# Check if num is negative:
# If it is, print "Invalid number." and continue to the next iteration of the loop.

# TO DO 3: 
# Check if num is zero:
# If it is, print "Exiting..." and break out of the loop.

# TO DO 4: 
#Calculate the square root of num using the math.sqrt function.

# TO DO 1: Import the `math` module.

import math

num = float(input("Enter a number: "))

# TO DO 2: Create an infinite loop using while True.

while True:
    if num < 0:
        print("Invalid number.")
        num = float(input("Enter a number: "))
        continue

# TO DO 3: Check if num is zero:

    if num == 0:
        print("Exiting...")
        break

# TO DO 4: Calculate the square root of num using the math.sqrt function.

    print("Square root:", math.sqrt(num))
    num = float(input("Enter a number: "))