

sandwich_orders = [
    "tuna",
    "hamchez",
    "bolona",
    "egg",
    "spam",
    "peanutbutter",
    "hez",
    "hamburger",
    "steak"
    ] 

done_sandwiches = []
make_sandwiches = True

while make_sandwiches:
   
    # sandwich in sandwich_orders:
    sandwich = sandwich_orders.pop()
    done_sandwiches.append(sandwich)
    print(f"I've done making your {sandwich}")
    if len(sandwich_orders) < 1:
        make_sandwiches = False
print(f"\nThere are these order left: \n{sandwich_orders}")
print(f"\nThis are the made sandwiches: \n{done_sandwiches}")