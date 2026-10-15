item_x = [[5, 0, 8], [7, 4, 0], [0, 9, 4]]
print(item_x)

# not mix of tuples and list
item_y = [(5, 4, 81), (71, 4, 0), [2, 95, 4]]
print(item_y)

# create with assignment
my_list = ['pc', 'router', 'nas', 'software']

# from_list_func = list((1, 10, 11, 20, 31))
# print(f"List created from tuple,\n{from_list_func}")

# access a specific item by its element position
my_list = ['pc', 'router', 'nas', 'software']
print(f"this should return 'router', the second position\n{my_list[1]}")

# getting tricky here:
# access the third posistion
print(item_y[2]) # [2, 95, 4]
# access the third posistion's item and the second item of the nested list
print(item_y[2] [1]) # 95

print(item_y[0] [2]) # 81

print(item_y[-1] [-2]) # 95

# Access & Slicing
a = [10, 20, 30, 40, 50]

print(a[0])      # 10  (first)

print(a[-1])     # 50  (last)

print(a[1:3])    # [20, 30]  (start:end, end exclusive)

print(a[::2])    # [10, 30, 50]  (every 2nd)

print(a[-1::4])   # [50, 40, 30, 20, 10]  (reversed copy)

my_list = ['pc', 'router', 'nas', 'software']
