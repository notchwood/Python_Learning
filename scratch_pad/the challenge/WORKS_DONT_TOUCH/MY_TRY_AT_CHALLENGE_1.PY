racers = {
    'alice' : 1,
    'bob' : 2,
    'charlie' : 3,
    'david' : 4,
    'eva' : 5,
}



def display_menu():
    """Prints the main navigation menu for the user."""
    print("\n=== RACE LEADERBOARD MENU ===")
    print("1. Add/Update Racer Finish Position")
    print("2. View Current Leaderboard")
    print("3. Print Podium Winners (Top 3)")
    print("4. Clear Leaderboard")
    print("5. Exit Application")



def main():


    print("Welcome")


# 1)  Show imput menu to choose a fucnction to perform

    choice = input("input 1  5") 
    if choice == 1







for racer, finish_position in racers.items():
    if finish_position > 10 and finish_position < 14:
        suffix = "th"
    elif finish_position % 100  == 1: # 1 / 100 = .01 therefore 
        remainder = 1 / 100 # the remainder should end w/ an 2 digit int .01
        print(f"{remainder} remainder")
        suffix = 'st'
    elif finish_position % 10  == 2:
        suffix = 'nd'
    elif finish_position % 10  == 3:
        suffix = 'rd'
    else:
        suffix = "th_"

    print(f"{racer} {finish_position}{suffix}")