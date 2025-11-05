# Simple Casino Payout Calculator

# Ask the player for their bet amount and convert it to a float (to allow decimals)
bet_amount = float(input("Enter your bet amount ($): "))

# Display the payout options to the user
print("\nChoose the game result:")
print("1 - Jackpot (pays 100x)")
print("2 - Big Win (pays 10x)")
print("3 - Small Win (pays 2x)")
print("4 - Lose (pays 0x)")

# Ask the player to choose a result and convert it to an integer
result = int(input("Enter the result number (1-4): "))

# Define payout multipliers for each type of result
# A dictionary maps each result number to its payout multiplier
payout_multipliers = {
    1: 100,  # Jackpot
    2: 10,   # Big Win
    3: 2,    # Small Win
    4: 0     # Lose
}

# Look up the multiplier based on the result entered by the user
# If the input is invalid, default to 0 (lose)
multiplier = payout_multipliers.get(result, 0)

# Calculate the total payout
payout = bet_amount * multiplier

# Display the calculated payout to the player
print(f"\nYour payout is: ${payout:.2f}")

# If the player lost, show a consolation message
if multiplier == 0:
    print("Better luck next time!")
else:
    print("Congratulations! You win!")
