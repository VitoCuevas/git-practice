import random

credits = int(input("Enter the number of credits you want to play with: "))
tries = 0   # count how many times the player has tried without winning

while credits > 0:
    print(f"\nYou have {credits} credits left.")
    user_number = int(input("Enter a number between 1 and 10: "))

    credits -= 1
    tries += 1

    # Generate random number
    machine_number = random.randint(1, 10)

    # Force a win after 20 failed attempts
    if tries == 20:
        machine_number = user_number
        print("(Lucky break! The machine is feeling generous...)")

    print("The machine picked:", machine_number)

    if user_number == machine_number:
        print("You Win!!! You earn 20 credits.")
        credits += 20
        tries = 0   # reset the try counter after a win
    else:
        print("You lose, try again.")

print("\nGame over! You’re out of credits.")

