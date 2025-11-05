# Linkedin Learning Python course by Joe Marini
# Example file for working with dates and times

from datetime import date           # import the date class
from datetime import datetime    # import the datetime class

## Date objects
# get today's date from the simple today() method from the date class

today = date.today()                # get the current date
print("Today's date is ", today)    # print the date


# print out the date's individual components

print("Date components: ", today.day, today.month, today.year)      # print individual date components


# retrieve today's weekday (0=Monday, 6=Sunday)
print("Today's weekday # is: ", today.weekday())                     # print the weekday number


# retrieve today's weekday as a string
print("Today's weekday is: ", today.strftime("%A"))                  # print the weekday name

# Date formatting
# print the date in ISO format
print("Today's date (ISO format) is: ", today.isoformat())            # print date in ISO format

# print the date in a more human friendly format
print("Today's date (formatted) is: ", today.strftime("%B %d, %Y"))     # print date in a human-friendly format

## DateTime objects

# get the current date and time from the datetime class

now = datetime.now()                # get the current date and time 
print("The current date and time is ", now)    # print the date and time


# print out the date's individual components
print("Date components: ", now.day, now.month, now.year)      # print individual


# print out the time's individual components
print("Time components: ", now.hour, now.minute, now.second)   # print individual time components


# retrieve the current time
print("The current time is: ", now.strftime("%H:%M:%S"))        # print the current time


# Date formatting

# print the date and time in ISO format
print("The current date and time (ISO format) is: ", now.isoformat())  # print date and time in ISO format

# print the date and time in a more human friendly format
print("The current date and time (formatted) is: ", now.strftime("%B %d, %Y %H:%M:%S"))  # print date and time in a human-friendly format