# leaderboard_functions.py

leaderboard = {}
add_more_racers = True

def get_compliant_speed(racer_name):
    while True:
        fastest_speed = input(f"what was your top speed {racer_name}: ").lower()
            # second opportunity to exit
        if fastest_speed == 'exit' :
                print("Good bye")
                return 'exit'
        if fastest_speed.isdigit():
             return fastest_speed
        else:
             print("You must enter a numeric value")
        
def display_leaderboard(speeds_dict, column_width=5):
    print('\n- Speed ---- Name -')
    print('-------------------')
    for racer, speed in speeds_dict.items():
        speed_str = str(speed)
        speed_length = len(speed_str)
        dash_line_len = ( 5 - speed_length) +2
        dashes= "-" * dash_line_len + ">"
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
        returned_speed_results = get_compliant_speed(name_input)
        if returned_speed_results == 'exit':
            add_more_racers = False
    if name_input != "exit" and returned_speed_results != "exit":
        leaderboard[name_input] = int(returned_speed_results)
    print(leaderboard)
    sorted_speeds = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

display_leaderboard(sorted_speeds)