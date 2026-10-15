# # for creation
my_lists = []

car_models = ['edge', 'jeep', 'corvette', 'neon']

fruits = ['apple', 'pear', 'peach', 'banana']


# a shallow copy using .copy method
words1 = fruits.copy()
print(f"this is the list that is being copied to words1\n{fruits}")
print(f"this is a .copy of \n{words1}\n")

# create a list from a iterating over items that are maluble 
'''`list()` works on **any iterable**. Tuples, sets, dicts, ranges, generators, 
ile objects — all work:'''
vowels = list('abcdef')
print("this list is created from a string - vowels = list('abcdef')\n",vowels)

# # print(car_models)

# accessing a list
# fruits = ['apple', 'pear', 'peach', 'banana']
print('\nthis should be a peach -->' + fruits[2]) # peach
print('this should be the last item of the list banana -->' + fruits[-1])

# tuple, tuple, tuple!
words = ('car', 'door', 'pants') # <-- this is a tuple
misc_words = words # I think this is what is condidered assignment copy
# the pointer address don't change.
print(f"\nthis is the list words that is being copied from,\n{words}")
print(f"this is the assignment copy to new tuple misc_words =\n{misc_words}\n")

print([*words], ', print([*words] - unpacking usint the * asterisk' ) #!! unpacking usint the * asterisk

print([word for word in words], ', - using comprehention : [word for word in words]') # using comprehention - loop


list_of_words = []
print("\nitetation over a tuple to create a list")
for word in words:
    list_of_words.append(word)
print(f"From a tuple created ths list itterating w/ for loop to create list\n{list_of_words}\n")

# to check if an item is in a list
# use the "in" for a IF statement.
# car_models = ['edge', 'jeep', 'corvette', 'neon']
print(f"Is the car 'edge' in\n {car_models}")
is_in_car_models = 'edge' in car_models
print(is_in_car_models)

print(f"Is the car 'toyota' in\n {car_models}")
is_in_car_models = 'toyota' in car_models
print(is_in_car_models)

# # get the length of a list
print(f"\n{car_models}")
car_length = len(car_models)
print(f"The length of the list is: {car_length}\n")

# print(car_models)

# # add to the end of list using append method
car_models.append('toyota')
print('added toyota to the list of car models.\n',car_models)

car_models.append('jeep')
print('addedjeep to the list of car models.\n',car_models)

print(f"\ncount the number of time a key jeep appears in list")
times_appears = car_models.count('jeep')
print('number of times "jeep" appears in list :',times_appears)

# car_models = 'toyota'
# print(car_models)

# insert a car model into list 'car_models'

print('\ninsert using position and item\n', car_models)
car_models.insert(1, 'chevy')
print(f"after inserting chevy at position 1\n{car_models}\n")

# # combine two list
# list_combined = fruit.extend(words)
# print(f"combining two list fruit and words {list_combined}")

# concanate two lists using the unpacking operator * and the + sign operator
# to do the concanate of two lists, we unpack the tuple into a list using * and then add it to the other list
tuple_unpacked = [*words]
list_combined = car_models + tuple_unpacked
print(f"combining two list 'car_models' and 'words'\n: {list_combined}\n")

# Finding a list item's index
index = [] 
for  'jeep' in list_combined:
    index = list_combined.index('jeep')
indexs = list_combined.index('jeep')
print(f"\nthe index for jeep is: {index}")
item = 'jeep'
index = list_combined.index(item) if item in list_combined else None
print(f"the index for {item} is: {index}")