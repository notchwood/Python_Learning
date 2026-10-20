# leaderboard_functions.py

leaderboard = {}
add_more_racers = True

def get_compliant_speed(racer_name):
    while True:
        # Using .title() preserves your clean dictionary output formatting lookup
        fastest_speed = input(f"What was your top speed, {racer_name.title()}: ").lower()
        
        if fastest_speed == 'exit':
            print("Good bye")
            return 'exit'
            
        if fastest_speed.isdigit():
            # Return it as a clean math-ready integer right out of the gate!
            return int(fastest_speed)
        else:
            print("❌ You must enter a numeric whole value.")
        
def display_leaderboard(speeds_dict, column_width=3):
    print('\n- Speed ---- Name -')
    print('-------------------')
    for racer, speed in speeds_dict.items():
        # Clean string layout conversion
        speed_str = str(speed)
        speed_length = len(speed_str)
        
        # Mirroring the f-string padding exactly (column_width matches >3)
        dash_line_len = (column_width - speed_length) + 4
        dashes = "-" * dash_line_len + ">"
        
        print(f"{speed:>3} mph {dashes} {racer.title()}")     

# =====================================================================
# MAIN APPLICATION ENGINE RUNNER
# =====================================================================

print("To quit the program at anytime, type 'exit' and hit enter:")

while add_more_racers:
    name_input = input("\nWhat is your name: ").lower()
    
    if name_input == 'exit':
        print("Good bye")
        add_more_racers = False
    else:
        # This code block ONLY triggers if name_input is a valid name asset
        returned_speed_results = get_compliant_speed(name_input)
        
        if returned_speed_results == 'exit':
            add_more_racers = False
        else:
            # Both variables are guaranteed to exist safely here!
            leaderboard[name_input] = returned_speed_results
            
            # Perform sorting right inside the update pass block
            sorted_speeds = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

# Only call the formatting printer if your data structure isn't empty
if leaderboard:
    display_leaderboard(sorted_speeds)
