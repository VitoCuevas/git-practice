# LinkedIn Learning Python course by Joe Marini
# Read and write files using the built-in Python file methods
#


# Open the file and read the contents
# 

sample_file = open("textfile.txt", "r")

if sample_file.mode == 'r':

# Use the read() function to read the entire contents of the file
    contents = sample_file.read()
    print(contents) 

    file_lines = sample_file.readlines()  # Read all lines into a list
    for line in file_lines:                # Iterate over the list and print each line
        print(line)                     # Print each line

sample_file.close()  # Close the file when done