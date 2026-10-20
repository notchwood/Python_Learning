# main_runner.py
# 1. Pull your working machine directly from your utility file
from leaderboard_utils import get_compliant_speed

leaderboard = {}
add_more_racers = True

print("To quit the program at anytime, type 'exit':")

# 2. Main Logic Stream
while add_more_racers:
    name_input = input("\nWhat is your name: ").lower()
    
    if name_input == 'exit':
        print("Good bye")
        add_more_racers = False
    else:
        # Activate the imported machine tool!
        returned_speed = get_compliant_speed(name_input)
        
        if returned_speed == 'exit':
            print("Good bye")
            add_more_racers = False
        else:
            leaderboard[name_input] = returned_speed

# 3. Print the raw dictionary data container to check your work
print("\nFinal Compiled Data Storage:")
print(leaderboard)
