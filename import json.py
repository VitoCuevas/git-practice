import json     # For saving and loading global play statistics
import os   # For checking if stats file exists
import random  # For generating random numbers
from datetime import datetime   # For timestamping audit log entries

STATS_FILE = "egm_stats.json"       # File to store global play statistics
AUDIT_FILE = "egm_audit_log.txt"    # File to store audit logs
FORCE_WIN_EVERY = 50  # Force a win on every 50th global play


def load_stats():    #"""Load global play statistics from a JSON file."""
    if not os.path.exists(STATS_FILE):  # Check if the stats file exists
        return {"global_play_count": 0} # Return default stats if file doesn't exist
    try:                                # Try to read and parse the stats file
        with open(STATS_FILE, "r", encoding="utf-8") as f:  # Open the file
            return json.load(f) # Load and return the JSON data
    except Exception: # If there's an error, return default stats
        return {"global_play_count": 0}  # Return default stats


def save_stats(stats):  #"""Save global play statistics to a JSON file."""
    with open(STATS_FILE, "w", encoding="utf-8") as f:  # Open the file for writing
        json.dump(stats, f) # Write the stats as JSON


def log_play(play_number, user_number, machine_number, result, credits_left):   # Append an entry to the audit log with a timestamp.
    """Append an entry to the audit log with a timestamp."""                    # Append an entry to the audit log with a timestamp.    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    # Get current timestamp
    entry = (                                                   # Format the log entry
        f"[{timestamp}] Play #{play_number}: "                  # Format the log entry
        f"User={user_number}, Machine={machine_number}, "     # Format the log entry
        f"Result={result}, Credits Left={credits_left}\n"   # Format the log entry
    )
    with open(AUDIT_FILE, "a", encoding="utf-8") as f:  # Open the audit log file in append mode
        f.write(entry)  # Write the log entry


def should_force_win(global_play_count):    # Determine if the current play should be a forced win based on global play count. 
    return global_play_count % FORCE_WIN_EVERY == 0 # Return True if it's time to force a win


def main(): # Main game loop
    stats = load_stats()    # Load global play statistics
    credits = int(input("Enter the number of credits you want to play with: ")) # Get initial credits from user

    while credits > 0:  # While the player has credits
        print(f"\nYou have {credits} credits left.")    # Display current credits
        user_number = int(input("Enter a number between 1 and 10: "))   # Get user's number choice
        credits -= 1    # Deduct one credit for the play

        stats["global_play_count"] += 1 # Increment global play count
        save_stats(stats)   # Save updated stats

        machine_number = random.randint(1, 10)      
        forced_win = False  # Flag to indicate if this play is a forced win

        if should_force_win(stats["global_play_count"]):    # Check if we should force a win
            machine_number = user_number                # Set machine number to user's number
            forced_win = True   # Mark this play as a forced win    
            print("(Global pity win triggered)")         # Notify the player of the forced win       

        print("The machine picked:", machine_number)    # Display the machine's number

        if user_number == machine_number:   # Compare the two numbers
            print("You Win!!! 🎉 You earn 20 credits.")  # Notify the player of their win
            credits += 20   # Award 20 credits for a win    
            result = "WIN"      # Set result to WIN
        else:                       # If the numbers don't match
            print("You lose, try again.")  # Notify the player of their loss
            result = "LOSE"   # Log the play details

        # Add audit log entry
        log_play(               # Log the play details
            stats["global_play_count"],         # Play number
            user_number,        # User's chosen number
            machine_number,  # Machine's chosen number
            f"{result}{' (Forced)' if forced_win else ''}", # Result with forced win note
            credits_left=credits, # Credits left after the play
        )

    print("\nGame over! You are out of credits.")  # Notify the player that the game is over
    print(f"Global plays so far: {stats['global_play_count']}") # Display total global plays
    print(f"Audit log saved to {AUDIT_FILE}") # Notify where the audit log is saved


if __name__ == "__main__":      # Run the main game loop
    main()      # 
