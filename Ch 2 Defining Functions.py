# LinkedIn Learning Python course by Joe Marini
# Defining and using functions
# "def" declares a function
#from unicodedata import name


#def my_function():
#    print("Hello from my function!")
# Call the function
#my_function()


# define a basic function

#def hello_func():       # function definition, starts the bock of code so next lines are indented
#    print("hello world!")
#    name = input("What is your name? ")
#    print("Nice to meet you, ", name)

#hello_func()          # function call, executes the block of code inside the function




# Functions can take parameters/arguments

#def hello_func(greeting):    # function definition with a parameter, greeting is the parameter name
#    print("hello world!")
#    name = input("What is your name? ")
#    print(greeting, name)   # using the parameter inside the function
#hello_func("How are you doing?")    # function call with an argument, "How are you doing?" is the argument passed to the function
#hello_func("Hey what's up")         # another function call with a different argument


#def greet_user(username):
#    print("Hello, " + username + "!")

#greet_user(name)

# Function that returns a value

#def cuber(x):       # function definition with a parameter
#    return x*x*x    # return statement to return the cube of x
#
#result = cuber(3)   # function call with argument 3, result will store the returned value
#print(result)       # prints 27



# Function with default value for an parameter

# def hello_func(greeting, name=None):    # function definition with a default parameter
#     print("Hello World!")               # print statement
#     if name == None:                    # check if name is None
#         name = input("What is your name? ")  # if name is None, ask for user input
#     print(greeting, name)               # print greeting and name

# hello_func("Nice to meet you")          # function call with one argument



# Function with variable number of parameters; we don't know how many parameters will be passed

# def multi_add(start, *args):   # function definition with variable number of parameters
#     result = start        # initialize result with start value
#     for x in args:        # iterate over the variable arguments
#         result = result + x # add each argument to result
#     return result  # return the final result
# print(multi_add(5, 10, 20, 30))   # function call with multiple arguments
# prints 65
# 5 + 10 + 20 + 30 = 65


def count_by_parity(which, numbers):
    w = Which.strip().lower()   

    if w == "even":
        return sum(1 for n in numbers if n % 2 == 0) # count even numbers
    elif w == "odd":
        return sum(1 for n in numbers if n % 2 != 0) # count odd numbers
    else:
        return -1  # invalid input
    
#count_by_parity(even, [1, 2, 3, 4, 5, 6])  # returns 3
#count_by_parity(odd, [1, 2, 3, 4, 5, 6])   # returns 3
#count_by_parity(prime, [1, 2, 3, 4, 5, 6]) # returns -1
