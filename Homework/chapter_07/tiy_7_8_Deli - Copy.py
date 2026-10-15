sandwich_orders = ["tuna",
    "ham & chez",
    "bolona",
    "egg",
    "spam",
    "peanutbutter and jelly",
    "grilled chez",
    "hamburger",
    "steakandchez"
    ]
pizza_orders = [
    "ham & pineapple",
    "Meat",
    "veggi",
    "mexican",
    "peperonni",
    "sausage",
    "ham chez"
    ]


chez_with = sandwich_orders.count('ham')
print(f"how many chez sandwiches are there, {chez_with}")

#pizza_orders.remove("chez")

pizza_orders.insert(-1,"chez")

finished_sandwiches = []

sandwich_orders.append("tuna-fish")
#sandwich_orders = ["Ham & Chez" ,"tuna"]
temp = list(sandwich_orders)
pizza_orders.extend(sandwich_orders)

print(temp)
print(sandwich_orders)
print(pizza_orders)

b_results = 'ham' in pizza_orders

print(b_results)

length_ofWord = len(pizza_orders)
print(length_ofWord)