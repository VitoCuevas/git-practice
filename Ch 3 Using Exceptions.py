# LinkedIn Learning Pythong course by Joe Marini
# Example file for working with exceptions
#

# Errors can happen in programs, and we need a clean way to handle them

# This code will cause an error because of division by zero

# x = 10 / 0 -- uncomment to see the error ZeroDivisionError

# Simple try/except block to catch exceptions

# try:
#     x = 10 / 0
# except ZeroDivisionError:       # catch the specific error by name ZeroDivisionError
#     print("Error: Division by zero is not allowed.")    # handle the error gracefully



# You can also catch specific exceptions

try:
    answer = input("Enter a number to divide 10 by: ")
    num = int(answer)
    print(10 / num)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")    # handle division by zero error
    print(e)    # print out the exception details   
except ValueError as e:
    print("Error: Invalid input. Please enter a valid number.")   # handle invalid input error
    print(e)    # print out the exception details
finally:
    print("This is part of the 'finally' block.")    # this block always executes