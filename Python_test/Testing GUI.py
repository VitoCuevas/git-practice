# Testing UI

import tkinter as tk

def say_hello():            # Function to be called when button is clicked
    print("Hello, World!")  # Print message to console

# Create the main window
window = tk.Tk()
window.title("My First GUI")    # Set window title

# Window size
window.geometry("300x200+100+100")      # Set window size to 300x200 and position at (100,100)
window.resizable(True, True)    # Allow window to be resizable

# Create a button and attach the say_hello function

hello_button = tk.Button(window, text="Click Me!", command=say_hello)   # Create a button and attach the say_hello function

button = tk.Button(window, text="Click Me!", command=say_hello) # Create a button and attach the say_hello function
button.pack(pady=50)        # Add some vertical padding

# Run the application
window.mainloop()   # Start the GUI event loop
