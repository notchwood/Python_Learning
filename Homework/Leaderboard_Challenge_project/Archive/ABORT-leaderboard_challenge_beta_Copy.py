

LAP_MILESTONE = 5
racers_name_len = [0]



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

def names_length(rider, racers_name_len):
    rider_length = len(rider)
    racers_name_len.append(rider_length)
    x = len(racers_name_len)
    for racers_name_len in range(0, x):
        if rider_length > racers_name_len(x):
            greatest_num = rider_length
    return greatest_num

def space_dots(rider, racers_name_len):
    rider_length = len(rider)
    total_len = 10 - rider_length
    spacing = "." * total_len
    return spacing  

# def space_dots(rider):
#     rider_length = len(rider)
#     total_len = 10 - rider_length
#     spacing = "." * total_len
#     return spacing 

# def longest_name_length(rider):
#     rider_length = len(rider)
#     if rider_length > greatest_len

leaderboard.update({'Mike': 13, 'Jack': 22, "Mindy": 88})

names = dict(sorted(leaderboard.items(), key = lambda item: item[0].lower()))
places = dict(sorted(leaderboard.items(), key=lambda item: (item[1]))) 
  
print("\nOrder by Position:")

for racer, position in (places.items()):
    racers_name_len = names_length(racer, racers_name_len)
    spacing = space_dots(racer, racers_name_len)
    result = get_ordinal(position)
    number, suffix = result
    print(f"{racer.title()} {spacing} finished at position {number}{suffix}")

    if position % LAP_MILESTONE == 0:
        print(f"   --> 🏁 MILESTONE: {racer.title()} hit a lap milestone position!")

print("\n")
print("Order by Name:")

for racer, position in (names.items()):
    spacing = space_dots(racer, racers_name_len)
    result = get_ordinal(position)
    # print(type(result))
    # print(repr(result))
    number, suffix = result
    #number, suffix = get_ordinal(position, ending)
    print(f"{racer.title()} {spacing} finished at position {number}{suffix}")

print("\n")
print(racers_name_len)
print(f"this is dict. places \n{places}")
print(f"this is dict. names \n{names}")
print(f"this is dict. leaderboards \n{leaderboard}")