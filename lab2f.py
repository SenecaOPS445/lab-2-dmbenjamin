#!/usr/bin/env python3

# Darian Benjamin
# dmbenjamin
# 2001/06/11

import sys

# Ensure an argument is provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <starting_number>")
    sys.exit(1)

# Assign command-line argument to timer variable
try:
    timer = int(sys.argv[1])
    if timer <= 0:
        raise ValueError
except ValueError:
    print("Error: Please provide a positive integer as an argument.")
    sys.exit(1)

# While loop that counts down to 0
while timer > 0:
    print(timer)
    timer -= 1

# Print final message
print("blast off!")