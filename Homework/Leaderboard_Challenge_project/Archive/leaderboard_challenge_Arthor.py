
LAP_MILESTONE = 5
''' I'm not sure where this constant fits in? if I set
this to 5, and it return the wrong suffix fo position 88'''

# create dictionary
leaderboard = {
    'Alice': 1,
    'Bob': 5,
    'Charle': 3,
}

print(leaderboard.items())

def get_ordinal(number):
    # going to test for position 11- 13, if True, assign var suffix
    # # with string "th" 
    # create dict. with position, and string with 'st', 'nd', 'rd' respective 
    # to int(position) 

    test = number % LAP_MILESTONE # the suggested 
    
    
    if number in range(11, 14): # <- to me this line is more self explainitory than the
        # IF statement below
    #if 11 <= number % LAP_MILESTONE <= 13:
        suffix = "th -TANGO-" # want to see when and how this block gets invoked
        return str(number)+suffix
    suffixes = {
        1: "st",
        2: "nd",
        3: "rd"
    } # standard created dictionary

    # the string DELTA shows me when the 2nd arg get 
    suffix = suffixes.get(number % 10, "th -DELTA-")
    # the .get method - looks for a matching key in the dctionary 
    # suffixes - if not found, then the second "get" argument is evaluated
    #print(suffix)
    
    print(f"this the mod remainder of {number} % 5 = {test}")
    print(f"this is the mod remainder of {number} % 10 -> {number % 10}")
    print(f"this is the mod remainder of {number} % 100 -> {number % 100}")

    return str(number)+suffix
    

# I want to test the 11 thru 13 positions, also the 21 thru 23 positions, plus 88 position
leaderboard.update({'Mike': 13, 'jack': 22, "mindy": 88}) # this will append (using .update method)
# to the dictionary

# tryed to figure out if I could sort order printed by values accending
for racer, position in (leaderboard.items()):
    place = get_ordinal(position)
    
    #places = sorted(leaderboard.items(), key=lambda item: item[1])
    print(f"{racer.title()} finished at position {place}\n")


# arranged = sorted(leaderboard.items(), key=lambda item: item[1])
# print(arranged)