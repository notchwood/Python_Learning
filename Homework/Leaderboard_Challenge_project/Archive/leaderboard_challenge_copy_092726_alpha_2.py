
'''NOTE: I intentionally left in TALLY HO and DELTA in the script
as visual aids for me to follow while coding. Plus it's fun to use for now.
This script is still a work in progress'''

LAP_MILESTONE = 5

# create dictionary
leaderboard = {
    'Alice': 1,
    'Bob': 5,
    'Charley': 3,
}

# print(leaderboard.items())

def get_ordinal(number):
    # going to test for position 11- 13, if True, assign var suffix
    # # with string "th" 
    # create dict. with position, and string with 'st', 'nd', 'rd' respective 
    # to int(position) 

    # test = number % LAP_MILESTONE # the suggested 
        
    if number in range(11, 14):
        '''<- to me this line is more self""
            "explainitory than the  IF statement below'''
        #if 11 <= number % LAP_MILESTONE <= 13:
        suffix = "th" # want to see when and how this block gets invoked
        #return str(number)+suffix
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
######################################################################################
leaderboard.update({'Mike': 13, 'Jack': 22, "Mindy": 88})
'''this will append (using .update method)
to the dictionary print(leaderboard)'''

# names = leaderboard.copy()

#names = dict(sorted(names.items(), key=lambda item: item[0]))   
names = dict(sorted(leaderboard.items(), key = lambda item: item[0].lower()))
print(names)
places = dict(sorted(leaderboard.items(), key=lambda item: (item[1]))) 
# places = dict(sorted(leaderboard.items(), key = lambda item: item[0))
  
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

#names = places.copy()

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