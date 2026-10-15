import Homework.chapter_04.septor as septor ; import random

sept_line = septor.prnt_ln(45, "%")

'''I created functions so if I reused a variable in w/ the name,
they would be local to the function only.
~no variable is global to avoid cross
contamination, between my practice problems.
 <- is there a technical term for this?'''

def pizza():
    # try_4_1_pizzas.py
    print(sept_line)
    pizzas = [
        f"meat lovers pizza", "hawiian pizza",
        f"cheese pizza", "mushroom pizza"
        ] 
    stmts = ["clasic - I like", "is tasty", "is yummy", "is mmm, mmm, good!"]
    for pizza in pizzas:
        print(f"{pizza} {random.choice(stmts)}")
    print(
        f"This is were I suppose to be creative and"
        f"\ntell you how much I love {pizzas[1]}.\n"
        f"So here I am, waiting for\nan x-large, {pizzas[1]}"
        )
    print(sept_line)

def cats_animals():
    # try_4_2_animals.py
    animals = ["domestic cat", "linx", "bobcat"]
    for a in animals:
        print(f"A {a} is a natural hunter")
    print("They are all color blind, I thing.")
    print(sept_line)

def counting_to_twenty():
    # try_4_3_counting_to_twenty.py
    for x in range(1, 21):
        print(x)
    print(sept_line)

''' try_4_4_one_million.py
create a list of 1 - one million
remember in the range the first number
is inclusive and the last number is non_inclusive'''
def one_million():
    numbers = list(range(1, 1000001))
    # print(numbers)
    for num in numbers:
        print(f"{num}")
    print(sept_line)

def summing_a_million():
    # try_4_5_summing_a_million.py
    numbers = list(range(1, 100000001))
    print(min(numbers))
    print(max(numbers))
    the_total = (sum(numbers))
    print(type(the_total))
    print(f'{the_total:,}')
    print(sept_line)

'''try_4_6_odd_numbers.py
print odd number from 1 to 20. 
The number 20 won't be included by designg'''
def odd_numbers():
    odd_nums = list(range(1, 20, 2))
    print(odd_nums)
    print(sept_line)

def threes():
    products = []
    for factor in range(1, 11):
        products.append(factor * 3)
    print(f"here are the multiples of 3:\n{products}")  
    print(sept_line)

def cubes():
    cubes = []
    for num in range(1, 11):
        cubes.append(num ** 3)
    print(cubes)
    print(sept_line)

def cubes_comprehension(): 
    print(f"{[num** 3 for num in range(1, 11)]}")
    print(sept_line)

def lynx_lineage():
    # try_4_10_cats.py
    cats = [
        f"canadian lynx", "fisher cat", "bobcat",
        f"ocelot", "serval", "caracel"
        ]
    print(
        f"These three cats are in the"
        f"\nbeginning of the list 'cats':\n{cats[:3]}\n"
        )
    print(f"These three cats are in the \n"
          f"middle of the list 'cats':\n{cats[2:5]}\n"
          )
    print(f"These last three cats are \nin the list 'cats':\n{cats[-3:]}\n")
    print(sept_line)

def friends_pizza():
    # try_4_11_friends_pizza.py
    my_pizzas = [
        f"hawiian pizza", "cheese pizza", "mushroom pizza", "nacho pizza",
        ] 
    friends = my_pizzas[:] 
    my_pizzas.append("green eggs & spam pizza ")
    friends.insert(0, "baloney & chez pizza")
    print(f"My favorite pizza list:\n{my_pizzas}\n")
    print(f"My friend's favorite pizza list:\n{friends}\n")
    print ("My favorite pizzas are")
    for pizza in my_pizzas:
        print(pizza)
    print(sept_line)
    print ("My friends favorite pizzas are")
    for pizza in friends:
        print(pizza)
    print(sept_line)


def food():

    print("\nThis is our current MENU!")
    menus = ("Steak", "Lobster", "Clams", "Chicken")
    for m in menus:
        print(m)
    new_foods = ("salad", "vegtables")
    keep_foods = ("steak", "clams")
    new_menus = new_foods + keep_foods
    print("\nThe following is the new MENU!")
    for x in new_menus:
        print(x)
    print(sept_line)

pizza()
cats_animals()
counting_to_twenty()
one_million()
summing_a_million()
odd_numbers()
threes()
cubes()
cubes_comprehension()
lynx_lineage()
friends_pizza()
food()