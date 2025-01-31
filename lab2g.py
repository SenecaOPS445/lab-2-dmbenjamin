#!/usr/bin/env python3

# Darian Benjamin
# dmbenjamin
# 2001/06/11

import sys

# Determine timer value based on command-line arguments
if len(sys.argv) == 2:
    try:
        timer = int(sys.argv[1])
        if timer <= 0:
            raise ValueError
    except ValueError:
        print("Error: Please provide a positive integer as an argument.")
        sys.exit(1)
else:
    timer = 3  # Default value when no argument is provided

# While loop that counts down to 0
while timer > 0:
    print(timer)
    timer -= 1

# Print final message
print("blast off!")