message = "Hello Folks!"
print(message)
#Variables reference a certain value, they can be like a label - not a box. 
variables="Variables reference a certain value"
print (variables)

#Changing Case with a METHOD; the METHOD here is TITLE
name = "robert cuevas"
print(name.title())

print(name.upper())
print(name.lower())

#variables in strings. Also F-STRINGS 
first_name = "Robert"
last_name = "Cuevas"
full_name = f"{first_name} {last_name}"
print(full_name) #combines the first and last name variables into the full name variable
print("      ")
print(f"Get to work, {full_name.upper()}!") #uses f-string and upper case method
print("     ") #inserts a blank line

message =f"Get to work, {full_name.upper()}!"
print ("\nThis is a new line\n") #shortcut for new line
print ("\tThis is a tab.\n") #shortcut for tab
print (message)
print("     ")

#lstrip rstrip strip

import webbrowser 
webbrowser.open('http://robert-cuevas.com') 
