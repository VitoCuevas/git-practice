# LinkedIn Learning Python Course by Joe Marini
# Workking with modules of code

# Importing built-in modules
# Import the math module, which contains features for working with mathematical operations
# Can go to the python website to see the full list of built-in modules and functions

import math     # Import the math module

print("The square root of 16 is:", math.sqrt(16))  # Use the sqrt function from the math module


# Import a specific part of the module so you can refer to it more easily

from math import pi    # Import only the pi constant from the math module
print("PI is", pi)   # Use the pi constant directly


# Import a module and give it a different name

import random as r  # Import the random module with an alias 'r'
print(r.randint(100, 200))  # Use the randint function from the random module



# Use the 3rd party tabulate module to print tabulated data

from tabulate import tabulate  # Import the tabulate function from the tabulate module

    # Sample data to be tabulated

data = [
    ["Product", "Price", "Stock"],
    ["Laptop", 999.99, 45],
    ["Mouse", 24.99, 128],
    ["Keyboard", 59.99, 89]
]

# Create a formatted table using the tabulate function
print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))