item_x = [[5, 0, 8], [7, 4, 0], [0, 9, 4]]
item_y = [(5, 4, 81), (71, 4, 0), [2, 95, 4]]
my_list = ['pc', 'router', 'nas', 'software', 'wifi']
clothings = ['pants', 'shoes', 'shirts', "hat", 'socks']
fruits = ['apple', 'pear', 'peach', 'banana']

fruits[0] = 'orange'
print(fruits)

fruits.append('apple')
print(fruits)


new_fruits = ('apple', 'kiwi', 'pineapple', 'tomato', 'kiwi')
for fruit in new_fruits:
    fruits.append(fruit)
print(fruits)

# use .remove using a value from the list and .pop() 
# an item based on it position
print(fruits)
fruits.remove('pear')
print(fruits)

xouts = ["banana", "apple"]
while 'banana' in fruits:
    fruits.remove('banana')
print(fruits)

fruit_bowl = fruit.count("apple")
print(f"there is {fruit_bowl} apples in the fruits bowl")

# print(fruits)
# fruits.remove('tomato') # <-- this should throw an error, tomato not in list
# print(fruits)

off_the_end = fruits.pop(-2)
print(fruits)
print('got rid of', off_the_end)

off_the_end = fruits.pop()
print(fruits)
print('got rid of', off_the_end)

del fruits[2]
print(fruits)
# del fruits
# print(fruits)

my_list.clear()


a = [3, 1, 2]
a.append(4)           # [3, 1, 2, 4]
a.extend([5, 6])      # [3, 1, 2, 4, 5, 6]
a.insert(0, 0)        # [0, 3, 1, 2, 4, 5, 6]
a.remove(2)           # [0, 3, 1, 4, 5, 6]
last = a.pop()        # 6, list is now [0, 3, 1, 4, 5]
a.sort(reverse=True)  # [5, 4, 3, 1, 0]
a.reverse()           # [0, 1, 3, 4, 5]


item_x = [[5, 0, 8], [7, 4, 0], [0, 9, 4]]
item_y = [(5, 4, 81), (71, 4, 0), [2, 95, 4]]
my_list = ['pc', 'router', 'nas', 'software', 'wifi']
clothings = ['pants', 'shoes', 'shirts', "hat", 'socks']
fruits = ['apple', 'pear', 'peach', 'banana']

my_list = ['pc', 'router', 'nas', 'software', 'wifi']
sort_list = my_list.sort()
print(f"\nThis should be a sorted list\n{sort_list}")
'''The code returns None because the .sort() method is designed 
to sort the list in-place, meaning it modifies the original list 
directly and does not return a new sorted list.  In Python, 
any method that mutates an object (like .sort(), .append(), or .reverse()) 
explicitly returns None to avoid ambiguity regarding whether the 
operation created a new object or changed the existing one. '''

my_list = ['pc', 'router', 'nas', 'software', 'wifi']
my_list.sort()
print(f"\nThis should be a sorted list\n{my_list}")

# you can use the function sorted <-- notice the "ed" suffix.
my_list = ['pc', 'router', 'nas', 'software', 'wifi']
sorted_list = sorted(my_list)
print(f"\nThis should be a sorted list\n{sorted_list}")
