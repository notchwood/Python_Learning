# try_3_3_your_list.py
# I wanted to add some complexity to this work problem for fun.

import random as rand # intentionally playing around with aliases
fruits = ["apples", "banana", "mellons", "Peaches", "BLUE berries"]
attributes = ["are good for you", "are yummy", "are sweet", "have vitamins"]
for fruit in fruits: 
    print(f"I like {fruit.lower()}, they {rand.choice(attributes)}.")
    