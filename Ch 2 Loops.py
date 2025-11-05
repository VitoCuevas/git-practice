# LinkedIn Learning Python course by Joe Marini
# Example file for working with Loops
# Used to execute code multiple times


x = 0


# Define a WHILE loop

while x < 5:
    print(x)
    x = x + 1

# Another example
# Common example for when you want to read data untile there is no more data to read, but you don't know how many times you'll need to loop

answer = input("Should I stop?:")
while answer != "yes":
    print(answer)
    answer = input("Should I stop?:")   

# Define a FOR loop

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    print(d)


# Use a For loop over a collection
for i in range(len(days)):
    print(days[i])

# Use the BREAK and CONTINUE statements

for d in days:
    if (d == "Wed"):
        break
    print(d)

# Continue example. This will skip printing "Thu". Think of it like a "skip" command!

for d in days:
    if (d == "Thu"):
        continue
    print(d)


# Using the enumerate() function with loops

for i, d in enumerate(days):    # Get index and value
    print(i, d)                 # Print the index and day


# Import the random module to generate random numbers


# Initialize a counter variablecountercounter = 0   