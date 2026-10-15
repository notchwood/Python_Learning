# registration_clipboard.py

leaderboard = {}

# Constants for output formating
COLUME_WIDTH = 5

print("To quit the program at anytime, type 'exit' and then enter key:")

add_more_racers = True
while add_more_racers:
    racer_name = input("What is your name: ").lower()
    if racer_name == 'exit' or racer_name == "'exit'":
        # break
        escape = False
    
    fastest_speed = int(input("what was your top speed: "))
    # second opportunity to exit
    if racer_name == 'exit' or racer_name == "'exit'":
        break
        # escape = False
    
    # created a str from int-fastest_speed var - to get string length for formating output
    char_speed = str(fastest_speed) # created a str from int-fastest_speed var to get string length for formating output

    leaderboard[racer_name] = fastest_speed

print(leaderboard)

# sorted func. on dict. decending order
speeds = dict(sorted(leaderboard.items(), key = lambda item: item[1], reverse=True))

# format output then print
for racer, speed in speeds.items():
    speed_length = len(char_speed)
    max_str_len = max(len(speed) for speed in speeds)
    dash_line_len = (COLUME_WIDTH - speed_length)
    dashes= "-" * dash_line_len + ">"
    print(f"{speed:>3} mph {dashes} {racer.title()}")    