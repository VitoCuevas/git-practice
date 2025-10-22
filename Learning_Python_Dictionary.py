# Learning Python
# Dictionary Data Types

# Key is like a dictionary word
# Dictionaries are indexed by a set of unique key-values

# Dictionary: a key-value data structure

mydict = {          # {} used to defind the dictionary
    "one" : 1,      # : used to seperate the key from the value
    "two" : 2,
    3 : "three",    # Can mix types
    4.5 : ["four", "point", "five"]     # Can have lists 
}

print(mydict)

# Each key has to be unique in the dictionary

# Dictionaries are access via keys

print(mydict["one"]) # Prints the value of the key "one", should be "1"
print(mydict[3])     # Prints the value of the key "3", should result in "three"

# You can also set dictionary data by creating a new key

mydict["seven"] = 7
print(mydict)


# Trying to access a nonexistent key will produce an error

# Example: print(mydict[Big])  // This will error our as Big is not part of the dictionary


# To avoid this, you can use the "in" operator to see if a key exists

print("two" in mydict)  # Results in True as two is part of the dictionary
print("big" in mydict)  # Results in False as Big is NOT part of the dictionary


# You can retrieve all of the keys and values from a dictionary

print(mydict.keys())    # This results in all the keys to be displayed from the mydict dictionary
print(mydict.values())  # This results in all the values to be displayed from the my dict dictionary


# You can also iterate over all the items in a dictionary

for key, val in mydict.items():
    print(key, val)
    