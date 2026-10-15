# ordinal_numbers

#end = 10


# for ord_num in range(0 , end):
#     if ord_num > 0:
#         print(f{ord_num}"st")
#     elif ord_num < 3:


# nums = [1,2,3,4,5,6]




def counting_num(end_char):
    if end_char == "1":
        print(f"{num}st")
    elif end_char == "2":
        print(f"{num}nd")
    elif end_char == "3":
        print(f"{num}rd")
    else:
        print(f"{num}th")
    #counting_num(end_char)

#first set of ordinals 1st set
for num in range(1, 15): 

    int_to_char = str(num)
    end_char = int_to_char[-1:]
    counting_num(num)

    #for num in range(11, 14):
    if num == 11:
            print("11th")
    if num == 12:
        print("12th")
    if num == 13:
        print("13th")
    else:
        break
    counting_num(num)

