racers = {
    'alice' : 1,
    'bob' : 2,
    'charlie' : 3,
    'david' : 4,
    'eva' : 5,
}

def label_position (pos, n):
    for pos in range(0,n):
        if pos > 3:
            place = f"{position}th"
        elif pos > 2:
            place = f"{position}rd"
        elif pos > 1:
            place = f"{position}nd"
        else:
            place = f"{position}st"
    return position

def make_pretty(rider):
    total_len = 10 - len(rider)
    spacing = "." * total_len
    return spacing

for rider, position in racers.items():
    spacing = make_pretty(rider)
    ordinal = label_position(position, 6)
    print(f"{rider} {spacing} finished {ordinal}")
