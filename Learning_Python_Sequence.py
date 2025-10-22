# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Sequences: Lists and Tuples
# These are sequences of values

mylist = [0, 1, "two", 3.2, False]  #This is a list. Notice you can add different types within the list
print(len(mylist))  #len = length of the variable, in this case the size of the list or the number or items


# To access a member of a sequence type, us []

print(mylist[2])  # *Prints the 3rd value, since it starts with zero for the first value
print(mylist[-1])  # *Prints the first value from the end. Since it is negative
mylist[0] = 10  # ***This is important. It changes the first value (designated by the zero) to 10.
print(mylist)  # Prints the updated list with all values


# Add a list to another list

another_list = [6,7,8]
mylist = mylist + another_list  # This simply adds the new numbers (in this case, 6,7,8) to the end of the previous list
print(mylist)

# Use slices to get parts of a sequence

print(mylist[::2])  # Skips every other one (the first and second value purposely left out). The first value is where to start (e.g., 0). The second value is where to end. 


# You can use slices to reverse a sequence (works for strings as well)

print(mylist[::-1])  # Notice the -1 in the slicer. This reverses it


# TUPLES are like LIST, but they are immutable

mytuple = (0,1,2,"three")
print(mytuple[1])  # It pick the number 1, becuase it is the second number, remember the first number is counted as zero (not to be confused with 0 on the list (just a coincedence))
# Tuples are immutable, they can't be changed
# How does Python know when it is a Tuple versus a list?
    # Tuples use parentheses while List use brackets 
    # Tuple ()
    # List []
    # Set {}


# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 4, "hey"}
print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # This will cause an error
# Only one instance of a particular value


# Test for membership
# You can check to see if there is a number in one of these sets

print(1 in mylist) # True
print(3 in mytuple) # False
print(5 in myset) # False

# Sequences are used in almost every program in Python............



