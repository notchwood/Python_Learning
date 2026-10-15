sandwich_orders = [
    "tuna",
    "pastrami",
    "hamchez",
    "bolona",
    "egg",
    "spam",
    "peanutbutter",
    "pastrami",
    "hez",
    "hamburger",
    "steak",
    "pastrami"
    ] 

print("\nWe are all out of pastrami - 86")

b_weGot = "pastrami" in sandwich_orders
print(f"\nthis is before removing Pastrami sandwiches, {sandwich_orders}")
while b_weGot:
    
    sandwich_orders.remove("pastrami")
    b_weGot = "pastrami" in sandwich_orders

print(f"\nthis is the list after we 86-ed the pastrami\n{sandwich_orders}")





# done_sandwiches = []
# make_sandwiches = True

# while make_sandwiches:
   
#     # sandwich in sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     done_sandwiches.append(sandwich)
#     print(f"I've done making your {sandwich}")
#     if len(sandwich_orders) < 1:
#         make_sandwiches = False
# print(f"\nThere are these order left: \n{sandwich_orders}")
# print(f"\nThis are the made sandwiches: \n{done_sandwiches}")