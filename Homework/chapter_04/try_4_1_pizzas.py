import random
pizzas = ["meat lovers pizza", "hawiian pizza", "cheese pizza", "mushroom pizza"] 
stmts = ["clasic - I like", "is tasty", "is yummy", "is mmm, mmm, good!"]
for pizza in pizzas:
    print(f"{pizza} {random.choice(stmts)}")
print(f"This is were I suppose to be creative and\ntell you how much I love {pizzas[1]}.\nSo here I am, waiting for\nan x-large, {pizzas[1]} ")

