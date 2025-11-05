# How to Automate the Boring Stuff with Python Course
# Page 85

def span():
    global eggs
    eggs = 'spam'   # This line modifies the global variable 'eggs'

def bacon():
    eggs = 'bacon'  # This line creates a local variable 'eggs'

def ham():
    print(eggs)     # This line prints the global variable 'eggs' and does not create a local variable

eggs = 'global'    # This line creates a global variable 'eggs'
span()  # Call the function span()
print(eggs)     # This will print 'span' because the global variable was modified by span()


