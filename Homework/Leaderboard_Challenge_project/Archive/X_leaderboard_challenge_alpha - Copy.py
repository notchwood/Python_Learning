
'''NOTE: I intentionally left in TALLY HO and DELTA in the script
as visual aids for me to follow while coding. Plus it's fun to use for now.
This script is still a work in progress'''

LAP_MILESTONE = 5
''' I'm not sure where this constant fits in? Further I think the hint that 
was given threw me off a bit'''

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

    # test = number % LAP_MILESTONE # the suggested 
        
    if number in range(11, 14):
        '''<- to me this line is more self""
            "explainitory than the  IF statement below'''
        #if 11 <= number % LAP_MILESTONE <= 13:
        suffix = "th -TALLY HO-" # want to see when and how this block gets invoked
        return str(number)+suffix
    suffixes = {
        1: "st",
        2: "nd",
        3: "rd"
    }

    # the string DELTA shows me when the 2nd arg get 
    suffix = suffixes.get(number % 10, "th -DELTA-")
    # the .get method - looks for a matching key in the dctionary 
    # suffixes - if not found, then the second "get" argument is evaluated
    
    #print(suffix)
    # print(f"this the mod remainder of {number} % 5 = {test}")
    # print(f"this is the mod remainder of {number} % 10 -> {number % 10}")
    # print(f"this is the mod remainder of {number} % 100 -> {number % 100}")

    return str(number)+suffix
    
######################################################################################
# I want to test the 11 thru 13 positions, also the 21 thru 23 positions, plus 88 position
leaderboard.update({'Mike': 13, 'jack': 22, "mindy": 88}) # this will append (using .update method)
# to the dictionary

places = dict(sorted(leaderboard.items(), key = lambda item: item[1]))
'''In all honesty, I had to do a lot of research on sorting a dictionaries. I tried to
follow the example online/my books and using the debugger. This part is hard to 
follow: "key = lambda item: item[1]" 
I learned that lambda is an anonymous function, I'm guessing like a pointer 
to a memory address? The "item[1]" looks like the second sub of a list pair? The "item:" 
maybe referring to the dictionary leaderboard. The "item[1]" is the value that is
getting sorted on? When the “places” var is printed, with out the dict() function, its printing a list not a dictionary.
I'm going to assume the dict() function takes the list as an argument and converts
the list back into a dictionary. I finally got the sorting kinda to work without the suffix. This effort
to get it work took a good amount of trial BY error and debugging. The mechanics are
still a bit fuzzy for me '''
# ordinal_results = []
print("\n")
for racer, position in (leaderboard.items()):
    ordinal_results = (get_ordinal(position))
    
    # for ordinal in ordinal_results:
    
    # for ordinal in ordinal_results:
    print(f"{racer.title()} finished at position {ordinal_results}")
    print(ordinal_results)

print("\n")
# I can't figure out how to add the suffix to the sort order
for name, number in places.items():
    print(f"{name} finished {ordinal_results}")
