# ----------------------------------------------------------------------
# Project: Race Leaderboard Tracking System
# Core Concepts: Dictionaries, Loops, Modulo Operator (%), User Input
# ----------------------------------------------------------------------

def display_menu():
    """Prints the main navigation menu for the user."""
    print("\n=== RACE LEADERBOARD MENU ===")
    print("1. Add/Update Racer Finish Position")
    print("2. View Current Leaderboard")
    print("3. Print Podium Winners (Top 3)")
    print("4. Clear Leaderboard")
    print("5. Exit Application")


def main():
    # Core tracking dictionary: {racer_name: finish_position}
    leaderboard = {
        'alice' : 1,
        'bob' : 2,
        'charlie' : 3,
        'david' : 4,
        'eva' : 5,
    }
    
    # Target value for the modulo operator demonstration.
    # Used to trigger a specific milestone notification or lap check.
    LAP_MILESTONE = 5 

    print("Welcome to the Race Tracking System, Mike!")

    while True:
        display_menu()
        
        choice = input("\nSelect an option (1-5): ").strip()

        for position in leaderboard:
            if position in leaderboard:
                position %5 == 0
                print("yes")

        
################################################################################
        
        if choice == '1':
            # ----------------------------------------------------------
            # OPTION 1: Add or Update a Racer
            # ----------------------------------------------------------
            name = input("Enter racer name: ").strip().title()
            
            # Input validation for positioning
            try:
                position = int(input(f"Enter finish position for {name}: "))
                if position <= 0:
                    print("Position must be a positive integer starting at 1.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number for the position.")
                continue
            
            # Save data directly into the tracking dictionary
            leaderboard[name] = position
            print(f"Successfully recorded: {name} finished at Position {position}.")

            # --- MODULO OPERATOR (%) CHALLENGE INTEGRATION ---
            # TODO: Use the modulo operator here to check if the racer's 
            # position is a multiple of LAP_MILESTONE (e.g., position 5, 10, 15).
            # If it matches cleanly with a remainder of 0, print a special award 
            # or milestone announcement to the screen.





#########################################################################################

        elif choice == '2':
            # ----------------------------------------------------------
            # OPTION 2: View Entire Leaderboard
            # ----------------------------------------------------------
            if not leaderboard:
                print("\nThe leaderboard is currently empty. No racers registered.")
            else:
                print("\n--- CURRENT RACER POSITIONS ---")
                # TODO: Sort the dictionary by its values (positions) so it reads 
                # chronologically from 1st place downwards before printing.
                
                for name, position in leaderboard.items():
                    sorted(leaderboard, key=leaderboard.get) # pb 102 pcc
                    print(f"Position {position}: {name}")

        elif choice == '3':
            # ----------------------------------------------------------
            # OPTION 3: Print Podium Winners
            # ----------------------------------------------------------
            print("\n--- 🏎️ THE PODIUM (TOP 3 WINNERS) 🏎️ ---")
            # TODO: Loop through the leaderboard dataset and isolate positions 1, 2, and 3.
            # Print unique, formatted congratulatory announcements for each podium finisher.
            pass

        elif choice == '4':
            # ----------------------------------------------------------
            # OPTION 4: Reset Leaderboard Data
            # ----------------------------------------------------------
            confirm = input("Are you sure you want to clear all data? (yes/no): ").lower().strip()
            if confirm == 'yes':
                leaderboard.clear()
                print("Leaderboard successfully cleared.")
            else:
                print("Clear operation canceled.")

        elif choice == '5':
            # ----------------------------------------------------------
            # OPTION 5: Graceful Exit
            # ----------------------------------------------------------
            print("\nExiting Race Leaderboard Tracking. Great coding session, Mike!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 5.")


# Standard conditional check ensuring script runs cleanly from VS Code terminal
if __name__ == "__main__":
    main()
