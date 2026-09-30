# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko
# Date: sep 30, 2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2d.py


# TO DO 1: copy the required lines from README.md to print version, platform, argv and the length of argv.
# run the script in the terminal using command: python ./lab2d.py

import sys

print(sys.version)
print(sys.platform)
print(sys.argv)
print(len(sys.argv))

# TO DO 2: copy the required lines from README.md to print argv[0], argv[1] and argv[2]
# run the script using the following command: python lab2d.py maija Maija

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(len(sys.argv))