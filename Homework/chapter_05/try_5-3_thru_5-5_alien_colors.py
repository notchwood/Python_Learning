# try_5-3_thru_5-5_alien_colors
import random

alien_colors = ["green", "red", "yellow", "no color"]

# sanitize the list by removing whitespace for each string
clean_colors = [color.replace(" ", "") for color in alien_colors]
# print both lists to verify that the spaces have been removed
print(clean_colors)
print(alien_colors)
point = 0
i = 0
while i <= 5:
    i += 1
    color = random.choice(clean_colors)
    if (color == 'green'):
        hit_points = 5
        point = point + hit_points
        the_alien = "green"
    elif (color == "red"):
        hit_points = 15
        point = point + hit_points
        the_alien = "red"
    elif (color == "yellow"):
        hit_points = 10
        point = point + hit_points
        the_alien = "yellow"
    else:
        hit_points = 0
        point = point + hit_points
        the_alien = "no color"

    if the_alien != "no color":
        print(f"You've just earned {hit_points} points for shooting a {the_alien} alien" )
    else:
        print(f"You've just earned {hit_points} points, for shooting at a {the_alien}ed alien")
print(f'you have earned a total of {point} points')
