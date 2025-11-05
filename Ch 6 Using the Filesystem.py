# Linkedin Learning Course by Joe Marini
# Example file for working with the filesystem shell methods
#

# Make a duplicate of an existing file


    # Get the path to the file in the current directory


import os   # import the os module

def file_info():    # Function to get total size of .txt files in a folder
    totalbytes = 0  # Initialize total byte counter
    folder = 'Python_test'    # Specify the target folder
    
# --- Fix: Check if the directory exists first ---
    if not os.path.isdir(folder):           # Check if the folder exists
        print(f"Error: Directory '{folder}' not found.")        # Print error message
        return 0 # Return 0 if the folder is missing    
 
 # Get a list of all items in the directory
    dirlist = os.listdir(folder)                                # List all entries in the folder
    
    for entry in dirlist:                # Iterate over each entry in the directory 
# --- Fix: Use os.path.join to safely build the path ---
        full_path = os.path.join(folder, entry)         # Create full path to the entry

# Make sure it's a file and ends with .py
        if os.path.isfile(full_path) and entry.endswith(".py"):    # Check if it's a file and ends with .py
 # Add the file size to the total
            filesize = os.path.getsize(full_path)   # Get the size of the file
            totalbytes += filesize  # Add to total byte counter

    print(f"Total size of .py files: {totalbytes} bytes") # Print the total size of .txt files
    #print(f"The function returned: {size}")   # Print the size returned by the function



 # --- Fix: The return statement MUST be indented ---
    return totalbytes # Return the total size in bytes   

file_info()  # Call the function to execute it




