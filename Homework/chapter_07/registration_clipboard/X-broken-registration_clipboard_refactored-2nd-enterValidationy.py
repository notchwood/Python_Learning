# registration_clipboard.py

leaderboard = {}

# Constants for output formating
COLUME_WIDTH = 5

print("To quit the program at anytime, type 'exit' and then enter key:")

add_more_racers = True

while add_more_racers:
    
    racer_name = input("What is your name: ").lower()
    
    if racer_name == 'exit' or racer_name == "'exit'":
        print("Good bye")
        add_more_racers = False
        
    else:
        isAlpha = False
        while not isAlpha:
            fastest_speed = input("what was your top speed: ").lower()
            
            if fastest_speed == 'exit' or fastest_speed == "'exit'":
                print("Good bye too")
                add_more_racers = False
                isAlpha = True
            elif not isAlpha:
                isAlpha = fastest_speed.isalpha()
                if isAlpha:
                    print(fastest_speed.isalpha())
                    print("msg only numbers or exit")
                    isAlpha = False
                else:
                    isAlpha = True
                    print("flag issue")
       
            else:
                leaderboard[racer_name] = int(fastest_speed) # changed to int so it could be sorted by int value

        # sorted func. on dict. decending order then created dictionary speeds from list
        speeds = dict(sorted(leaderboard.items(), key = lambda item: item[1], reverse=True))

print("\n--- Final Results ---")
# format output then print
for racer, speed in speeds.items():
    
    speed_length: str = len(str(speed))
    max_str_len = max(len(speed) for speed in speeds)

    dash_line_len = (COLUME_WIDTH - speed_length)
    dashes= "-" * dash_line_len + ">"

    print(f"{speed:>3} mph {dashes} {racer.title()}") 

    # note: I have still not looked at your code. But I had to resort to my
    # referrance material for syntax and internet for f string right alignment of 
    # speed output.  