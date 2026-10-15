

def counting_num(num):
    if 10 < num % 100 < 14:
        suffix = "th"
    else:
        suffix = {
            1: "st",
            2: "nd",
            3: "rd",
        }.get(num % 10, "th")

    print(f"{num}{suffix}")


for num in range(1, 14):
    counting_num(num)