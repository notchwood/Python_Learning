# registration_clipboard.py


unregistered_racers = {}
leaderboard = {}
# Constants for output formating
PADDING = 3
COLUME_WIDTH = 15
#def format_layout ():
      
exit = False
while not exit:
    racer_name = input("What is your name: ")
    if racer_name == 'exit':
            break
    fastest_speed = input("what was your top speed: ")
    
    
    # leaderboard.update({racer_name: fastest_speed})
    #leaderboard = {racer_name: fastest_speed}
    leaderboard[racer_name] = fastest_speed


#for reg_racer in leaderboard:

print(leaderboard)

for racer, speed in leaderboard.items():

    name_length = len(racer)
    max_str_len = max(len(tracer_name) for tracer_name in leaderboard)
    PADDING = 3
    COLUME_WIDTH = 15

    dash_line_len = (COLUME_WIDTH - name_length) + PADDING
    dashes= "-" * dash_line_len + ">"

      
    print(f"{racer.title()} {dashes} {speed}")
print()

# racer = dict(sorted(leaderboard.items(), key = lambda item: item[0].lower()))
# speed = dict(sorted(leaderboard.items(), key=lambda item: (item[1])))