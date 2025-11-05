# LinkedIn Learning Python course by Joe Marini

#  print("Hello from VS Code!")
#  print("This is difficult")
#  name = input("What is your name? ")
#  print("Nice to meet you", name)

myint = 10 # An integer is a number without a decimal
myfloat = 13.2576 #A float is a number with a decimal
mystr = "This is a string" 
mybool = True #This is a boolean, True or False

print(myint)
print(mystr)

#Operators are used to perform operations on variables

print(myint + myfloat)
print(myint * myfloat)
print(myint / myfloat)
print(myint % 3)  #  Modulus, this is prints out the remainder of the first value divided by the second number

another_str = "This is another string"

print(mystr + another_str)
print("nah " * 3)


#  Logical and comparison operators: True or False

print(myint == 10)  # Does it equal
print(myfloat != 20)  # Does not equal
print(myint > 20)  # Greater than
print(myfloat < 10)  # Less than

print(myint < 5 or myfloat < 25.0)  # using OR
print(myint > 5 and myfloat < 25.0)  # using AND

print(not (myint < 5 or myfloat < 25))  # Using the NOT, almost like times -1

#  re-declaring a variable works
#  Can change the value of a variable later in the program
