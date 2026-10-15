# ordinal_numbers

# print ordinal numbers 1 - 9
for num in range(1 , 10): 
    if num > 3:
        print(f"{num}th")
    elif num > 2:
        print(f"{num}rd")
    elif num > 1:
        print(f"{num}nd")
    else: #num > 0:
       print(f"{num}st")