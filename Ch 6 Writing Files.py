# LinkedIn Learning Pythong course by Joe Marini
# Write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist

sample_file = open("textfile.txt", "w+")    # Open for read/write, create if doesn't exist

sample_file.write("This is some sample text in our sample file.") # Write a line of text to the file

sample_file.close()    # Close the file when done

# This creates a new file or overwrites an existing file



# Open the file for appending text to the end

sample_file = open("textfile.txt", "a+")   # Open for read/write, create if doesn't exist; see the 'a' mode

# Write some lines of data to the file

sample_file.write("\nThis is some more sample text appended to the file.")  # Append a line of text to the file
sample_file.write("\nHere is even more sample text appended to the file.")  # Append another line of text to the file

# Close the file when done

sample_file.close()     # Close the file when done


