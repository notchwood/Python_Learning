# leaderboard_challenge_rc_2- Copy.py

LAP_MILESTONE = 5

# create dictionary
leaderboard = {
    'Alice': 1,
    'Bob': 5,
    'Charley': 3,
}

def get_ordinal(number):
        
    if number in range(11, 14):
        suffix = "th" # want to see when and how this block gets invoked
        return (number, suffix)
    suffixes = {
        1: "st",
        2: "nd",
        3: "rd"
    }

    suffix = suffixes.get(number % 10, "th")
    return (number, suffix)


# Arthur code to replace space_dots function I wrote.
def space_dots(rider, rider_str_length):
    # Give ourselves a baseline buffer of 3 extra dots so names never touch the text
    padding = 3 
    total_len = (rider_str_length - len(rider)) + padding
    
    return "." * total_len
 # def space_dots(rider, rider_str_length):
#     add_dots = 0 
#     dots = 5
#     if rider_str_length > dots:
#         add_dots = rider_str_length - dots
#     len_rider = len(rider)
#     total_len = dots - len_rider + add_dots + 1

#     spacing = "." * total_len
#     return spacing  

def print_results(results_type, option, rider_str_length):

    for racer, position in (results_type.items()):
        spacing = space_dots(racer, rider_str_length)
        result = get_ordinal(position)
        # print(type(result))
        # print(repr(result))
        number, suffix = result

        print(f"{racer.title():.<{rider_str_length + 3}} finished at position {number}{suffix}")
        # print(f"{racer.title()} {spacing} finished at position {number}{suffix}")

        if option:
            if position % LAP_MILESTONE == 0:
                print(f"   --> 🏁 MILESTONE: {racer.title()} hit a lap milestone position!")

leaderboard.update({'Mike': 13, 'Jack': 22, "Mindy": 88})
str_lens = []

names = dict(sorted(leaderboard.items(), key = lambda item: item[0].lower()))
places = dict(sorted(leaderboard.items(), key=lambda item: (item[1]))) 

names_list = [*names]
# x = 0
# for name in names_list:
#     str_length = len(name)
#     if str_length > x:
#         x = str_length
# rider_str_length = x
rider_str_length = max(len(name) for name in leaderboard)

print("\nOrder by Position:")
option = True
print_results(places, option, rider_str_length)

print("\n")
print("Order by Name:")
option = False
print_results(names, option, rider_str_length)