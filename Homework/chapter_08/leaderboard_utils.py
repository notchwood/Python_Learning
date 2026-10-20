# leaderbard_utils.py

# leaderboard_utils.py

def get_compliant_speed(racer_name):
    """Prompt for speed and enforce that the user types a whole number."""
    while True:
        fastest_speed = input(f"What was your top speed, {racer_name.title()}: ").lower()
        
        if fastest_speed == 'exit':
            return 'exit'
            
        if fastest_speed.isdigit():
            return int(fastest_speed)
        else:
            print("You must enter a numeric whole value.")
