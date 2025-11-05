# Number Guessing Game

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)  # Generate a random secret number
attempts = 0    # Initialize attempt count

while True:                                 # Start of the guessing loop
    guess = input("Enter your guess: ")     # Prompt user for a guess
    try:                                    # Convert input to integer
        guess = int(guess)                   # Handle invalid input
    except ValueError as e: 
        print("Invalid input. Please enter a valid number.")
        print(e)
        continue    

    attempts += 1   # Increment attempt count

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break