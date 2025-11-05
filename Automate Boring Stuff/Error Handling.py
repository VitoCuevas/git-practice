# How to Automate the Boring Stuff with Python Course
# Try clauses

# def spam(divide_by):
#     try: # Any code in this block that causes an error will jump to the except block
#       return 42 / divide_by
#     except ZeroDivisionError:   # If ZeroDivisionError occurs, this block will run
#         print('Error: Invalid argument.')

# print(spam(2))  # Outputs: 21.0
# print(spam(12)) # Outputs: 3.5
# print(spam(0))  # Outputs: Error: Invalid argument.
# print(spam(1))  # Outputs: 42.0

# def collate():
#     import random
#     try:
#         num = random.randint(1, 100)
#         if num > 50:
#             return [1, 2, 3]
#         else:
#             return 'Not a list'
#     except TypeError:
#         return None
# print(collate())  # Outputs either [1, 2, 3] or None depending on random number


# def collatz(number):    # Implements the Collatz conjecture with error handling
#     try:                # Try block to catch errors
#         if number % 2 == 0: # Check if the number is even
#             return number // 2  # If even, return half the number
#         else:   # If odd
#             return 3 * number + 1 # Return 3 times the number plus 1
#     except TypeError:   # Catch TypeError if input is not an integer
#         print('Error: Input must be an integer.')   # Print error message


# print(collatz(10))  # Outputs: 5
# print(collatz(7))   # Outputs: 22   
# print(collatz('a')) # Outputs: Error: Input must be an integer.
# print(collatz(3.5)) # Outputs: Error: Input must be an integer.

z = 3 - int(3.2)  
a = int(6 / 10) - bool("python") + 1  # Outputs: 0
b = bool(1) * int(4.2) + 1  # Outputs: 
c = True * 2 - False * 5  # Outputs: 2

print(z)
print(a)
print(b)
print(c)

*/ZeroDivisionError
//ZeroDivisionError