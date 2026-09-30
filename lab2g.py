# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko
# Date: sep 30, 2026
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

single_limit = 32000
married_limit = 64000
tax_rate1 = 0.10
tax_rate2 = 0.25

income = float(input("Enter your taxable income: "))
status = input("Enter your marital status (single or married): ")

if status == "single":
    if income <= single_limit:
        tax = income * tax_rate1
    else:
        tax = 3200 + (income - single_limit) * tax_rate2

elif status == "married":
    if income <= married_limit:
        tax = income * tax_rate1
    else:
        tax = 6400 + (income - married_limit) * tax_rate2

else:
    print("Invalid marital status.")
    tax = 0

print("Tax:", tax)