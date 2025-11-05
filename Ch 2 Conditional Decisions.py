# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements

x = 5
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

    # Conditional flow uses if, elif, and else statements

    # Execute different code based on conditions

    # Conditional statements let you use "a if C else b"
    result = "x is less than y" if x < y else "x is greater than or equal to y"  # This is a shorthand for the above if-else statement
    print(result)


x, y = 10, 100

if x < y:
    print("x is less than y")
elif x == y:
    print("x is the same as y")    
else:
    print("x is greater than y") 

# You can also use multiple conditions in a single line
# You can use "and" & "or" operators to combine conditions
# You can use parentheses to group conditions
# You can use nested conditionals

if (x < y and y < 100):
    print("x is less than y and y is less than 100")
elif (x < y and y >= 100):
    print("x is less than y and y is greater than or equal to 100")
else:
    print("x is greater than or equal to y")
print("This is a nested conditional")

