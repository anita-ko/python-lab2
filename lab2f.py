# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko
# Date: sep 30, 2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file

import sys

if len(sys.argv) < 3:
    print("The script requires at least 2 arguments.")
elif len(sys.argv) >= 3:
    name = sys.argv[1]
    age = sys.argv[2]
    print("Hi " + name + ", you are " + age + " years old and the script received " + str(len(sys.argv) - 1) + " arguments.")