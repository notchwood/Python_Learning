
# initialize
my_list = []

# create with assignment
my_list = ['pc', 'router', 'nas', 'software']

new_list = my_list.copy()
print(f"The following is a copy of an array my_list\n",
       "with a new list that has't own\n"
       "mem address, also called a shallow copy")
print(new_list)

ref_list = new_list
print(f"The re_list is an alias list of new_list\n",
      "also called a referrence assignment")

# using a constructor 'list' from a  tuple or string
using_list_con = list('aeiou')
print(using_list_con)

from_list_func = list((1, 10, 11, 20, 31))
print(f"List created from tuple,\n{from_list_func}"
      )
nums = list(range(5))
print(nums)

# replication
zeros = [0] * 5
print(zeros)

grid = [[0] * 3 for _ in range(3)] # 3x3 matrix
print(grid) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
item2 = grid[2]
print(item2)


item_x = [[5, 0, 8], [7, 4, 0], [0, 9, 4]]
print(item_x)

# not mix of tuples and list
item_y = [(5, 0, 8), (7, 4, 0), [0, 9, 4]]
print(item_y)