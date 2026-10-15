
'''NOTE: I intentionally left in TALLY HO and DELTA in the script
as visual aids for me to follow while coding. Plus it's fun to use for now.
This script is still a work in progress'''

LAP_MILESTONE = 5

leaderboard = {
    'Alice': 1,
    'Bob': 5,
    'Charley': 3,
}

def get_ordinal(number):
        
    if number in range(11, 14):
        suffix = "th" 
        return (number, suffix)
    suffixes = {
        1: "st",
        2: "nd",
        3: "rd"
    }
    suffix = suffixes.get(number % 10, "th")
    return (number, suffix)

def space_dots(rider):
    total_len = 10 - len(rider)
    spacing = "." * total_len
    return spacing  

leaderboard.update({'Mike': 13, 'Jack': 22, "Mindy": 88})

names = dict(sorted(leaderboard.items(), key = lambda item: item[0].lower()))
places = dict(sorted(leaderboard.items(), key=lambda item: (item[1]))) 
  
print("\nOrder by Position:")
for racer, position in (places.items()):
    spacing = space_dots(racer)
    result = get_ordinal(position)
    # print(type(result))
    # print(repr(result))
    number, suffix = result
    #number, suffix = get_ordinal(position, ending)
    print(f"{racer.title()} {spacing} finished at position {number}{suffix}")

    if position % LAP_MILESTONE == 0:
        print(f"   --> 🏁 MILESTONE: {racer.title()} hit a lap milestone position!")

print("\n")
print("Order by Name:")
for racer, position in (names.items()):
    spacing = space_dots(racer)
    result = get_ordinal(position)
    # print(type(result))
    # print(repr(result))
    number, suffix = result
    #number, suffix = get_ordinal(position, ending)
    print(f"{racer.title()} {spacing} finished at position {number}{suffix}")

print("\n")
print(f"this is dict. places \n{places}")
print(f"this is dict. names \n{names}")
print(f"this is dict. leaderboards \n{leaderboard}")