
racers = {
    "j" : 11,
    'alice' : 1,
    'bob' : 2,
    'charlie' : 3,
    'david' : 4,
    'eva' : 5,
    "q" : 6,
    "y" : 7,
    "c" : 8,
    "k" : 9,
    "m" : 10,
    
}


# My code 
# def label_position (position, x):
    # for pos in range(0,x):
    #     if pos > 3:
    #         place = f"{position}th"
    #     elif pos > 2:
    #         place = f"{position}rd"
    #     elif pos > 1:
    #         place = f"{position}nd"
    #     else:
    #         place = f"{position}st"

    # return place
# Bing AI code 
# def label_position (pos, x):
#     for pos in range(0, x):
#         if pos % 100 > 3:
#             suffix = "th"
#         elif pos % 10 > 2:
#             suffix = "rd"
#         elif pos % 10 > 1:
#             suffix = "nd"

# My AI companion's code (Gemini AI)     
def label_position (num):
    for num in range(4, 9): # Extended to 21 to see it work
        # Rule 1: Check if the number ends in 11, 12, or 13 first
        if num % 100 in range(4,10):
            suffix = "th"
        # Rule 2: If not, look at the very last digit
        # elif num % 10 == 1:
        #     suffix = "st"
        # elif num % 10 == 2:
        #     suffix = "nd"
        # elif num % 10 == 3:
        #     suffix = "rd"
        # else:
        #     suffix = "th"

        # elif num % 10 < 2:
        #     suffix = "rd"
        # elif num % 10 < 1:
        #     suffix = "nd"
        # elif num % 10 < 0:
        #     suffix = "st"
        # else:
        #     suffix = "th"



    suffix = "th"

        #print(f"{num}{suffix}")
    return suffix
            
# AI where I don't know
# def label_position(n, x):
#     s = ('th', 'st', 'nd', 'rd') + ('th',) * 10
#     v = n % 100
#     if v > 13:
#         v %= 10
#     return f'{n}{s[v]}'

# print(ordinal(1))  # 1st
# print(ordinal(11)) # 11th
# print(ordinal(23)) # 23rd   
def make_pretty(rider):
    total_len = 10 - len(rider)
    spacing = "." * total_len
    return spacing

x = (len(racers)+1)


for rider, position in racers.items():

    spacing = make_pretty(rider)

    # total_len = 10 - len(rider) 
    # spacing = "." * total_len 

    ordinal = label_position(position, x)


    print(f"{rider} {spacing} finished {ordinal}")


# riders = list(racers.keys())
# print(riders)


        





# for rider in racers:
#     riders = rider

# print(riders)
